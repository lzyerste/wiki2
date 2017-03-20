# 链表list

## PyListObject

文件：Include/listobject.h，Objects/listobject.c

对应的类型type为PyList_Type，名字为“list”。

```c
PyTypeObject PyList_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    "list",
    sizeof(PyListObject),
    ...
}
```

先看listobject.h的开头注释：

```c
/*
Another generally useful object type is a list of object pointers.
This is a mutable type: the list items can be changed, and items can be
added or removed.  Out-of-range indices or non-list objects are ignored.

*** WARNING *** PyList_SetItem does not increment the new item's reference
count, but does decrement the reference count of the item it replaces,
if not nil.  It does *decrement* the reference count if it is *not*
inserted in the list.  Similarly, PyList_GetItem does not increment the
returned item's reference count.
*/
```

List是mutable的，即可以随意增删元素。

PyList_SetItem相当于替换，所以新元素的引用并不需要更改，但被替换的引用得减1，因为它被移出了链表，所以这里是替换，而不是原地更新，类似lst[3] = a。如果最终没有成功放入链表，那么它的引用计数得减1。

类似地，PyList_GetItem也不会增加引用计数，因为本身已经在链表中了。

```c
typedef struct {
    PyObject_VAR_HEAD
    /* Vector of pointers to list elements.  list[0] is ob_item[0], etc. */
    PyObject **ob_item;

    /* ob_item contains space for 'allocated' elements.  The number
     * currently in use is ob_size.
     * Invariants:
     *     0 <= ob_size <= allocated
     *     len(list) == ob_size
     *     ob_item == NULL implies ob_size == allocated == 0
     * list.sort() temporarily sets allocated to -1 to detect mutations.
     *
     * Items must normally not be NULL, except during construction when
     * the list is not yet visible outside the function that builds it.
     */
    Py_ssize_t allocated;
} PyListObject;
```

这是PyListObject的定义，因为它是可变长的，所以在头部插入`PyObject_VAR_HEAD`，如此PyListObject指针可以直接转换为PyVarObject指针，PyVarObject里有成员记录当前实际使用中的元素个数，即当前长度。`allocated`成员当然是为了记录链表当前的容量，最大可容纳个数，所以自然有`0 <= ob_size <= allocated`。`ob_item`是实际的数据存储，申请数量由allocated控制，它的类型是PyObject的二级指针，可视为一维向量或数组，成员的类型是`PyObject *`。因此，Python中一切皆对象。

## Methods

方法一开始都要检查是否为list类型，因为传进来的参数类型是PyObject *。

```c
#define PyList_GET_ITEM(op, i) (((PyListObject *)(op))->ob_item[i])
#define PyList_SET_ITEM(op, i, v) (((PyListObject *)(op))->ob_item[i] = (v))
#define PyList_GET_SIZE(op)    Py_SIZE(op)
#define _PyList_ITEMS(op)      (((PyListObject *)(op))->ob_item)
```

一些快速操作（get，set，size），但要确保安全。

```c
PyAPI_FUNC(PyObject *) PyList_New(Py_ssize_t size);
PyAPI_FUNC(Py_ssize_t) PyList_Size(PyObject *);
PyAPI_FUNC(PyObject *) PyList_GetItem(PyObject *, Py_ssize_t);
PyAPI_FUNC(int) PyList_SetItem(PyObject *, Py_ssize_t, PyObject *);
PyAPI_FUNC(int) PyList_Insert(PyObject *, Py_ssize_t, PyObject *);
PyAPI_FUNC(int) PyList_Append(PyObject *, PyObject *);
PyAPI_FUNC(PyObject *) PyList_GetSlice(PyObject *, Py_ssize_t, Py_ssize_t);
PyAPI_FUNC(int) PyList_SetSlice(PyObject *, Py_ssize_t, Py_ssize_t, PyObject *);
PyAPI_FUNC(int) PyList_Sort(PyObject *);
PyAPI_FUNC(int) PyList_Reverse(PyObject *);
PyAPI_FUNC(PyObject *) PyList_AsTuple(PyObject *);
#ifndef Py_LIMITED_API
PyAPI_FUNC(PyObject *) _PyList_Extend(PyListObject *, PyObject *);

PyAPI_FUNC(int) PyList_ClearFreeList(void);
PyAPI_FUNC(void) _PyList_DebugMallocStats(FILE *out);
#endif
```

### PyList_New

### PyList_Size, O(1)

这个实现很简单，检查下是否为list类型，是的话直接调用Py_SIZE返回。

时间复杂度为O(1)。

```c
Py_ssize_t
PyList_Size(PyObject *op)
{
    if (!PyList_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    else
        return Py_SIZE(op);
}
```

### PyList_GetItem, O(1)

```c
PyObject *
PyList_GetItem(PyObject *op, Py_ssize_t i)
{
    if (!PyList_Check(op)) {
        PyErr_BadInternalCall();
        return NULL;
    }
    if (i < 0 || i >= Py_SIZE(op)) {
        if (indexerr == NULL) {
            indexerr = PyUnicode_FromString(
                "list index out of range");
            if (indexerr == NULL)
                return NULL;
        }
        PyErr_SetObject(PyExc_IndexError, indexerr);
        return NULL;
    }
    return ((PyListObject *)op) -> ob_item[i];
}
```

检查是否越界，如果区间合法则直接从ob_item中索引，最后也可以调用`PyList_GET_ITEM`宏。

时间复杂度为O(1)。

### PyList_SetItem, O(1)

```c
int
PyList_SetItem(PyObject *op, Py_ssize_t i,
               PyObject *newitem)
{
    PyObject **p;
    // check range
    ...
    p = ((PyListObject *)op) -> ob_item + i;
    Py_XSETREF(*p, newitem);
    return 0;
}
```

p = list[i]，PyXSETREF的作用是使p指向newitem，同时让原来p指向的对象引用计数减1（Py_XDECREF）。如果引用计数到0了，那么可以回收。

时间复杂度为O(1)。

### PyList_Insert, O(N)

调用内部函数`ins1`。

```c
int
PyList_Insert(PyObject *op, Py_ssize_t where, PyObject *newitem)
{
    if (!PyList_Check(op)) {
        PyErr_BadInternalCall();
        return -1;
    }
    return ins1((PyListObject *)op, where, newitem);
}
```

```c
static int
ins1(PyListObject *self, Py_ssize_t where, PyObject *v)
{
    Py_ssize_t i, n = Py_SIZE(self);
    PyObject **items;
    if (v == NULL) {
        PyErr_BadInternalCall();
        return -1;
    }
    if (n == PY_SSIZE_T_MAX) {
        PyErr_SetString(PyExc_OverflowError,
            "cannot add more objects to list");
        return -1;
    }

    if (list_resize(self, n+1) < 0)
        return -1;

    if (where < 0) {
        where += n;
        if (where < 0)
            where = 0;
    }
    if (where > n)
        where = n;
    items = self->ob_item;
    for (i = n; --i >= where; )
        items[i+1] = items[i];
    Py_INCREF(v);
    items[where] = v;
    return 0;
}
```

链表的容量是有最大限制的，即能索引范围，等于`PY_SSIZE_T_MAX`。

接下来调用`list_resize()`检测是否能够容纳n+1个元素，不行的话，需要进行扩容。

对where插入位置进行调整，list是支持负数索引的，所以如果where为负数的话，需要给它加上当前大小n。加了n以后还是负数，那就不管了，直接赋值为0，插入到链表头部。

如果where为正数且超出了n（>n），那么，直接将where置为n，也就是插入到链表尾部（注意索引是从0开始的，所以当前list[n]位置是不可见的，但经过上面的list_resize调整之后，空间是足够的），那么效果类似于append。

位置计算好之后，接下来一个循环就是数据挪位了，从原链表的where位置开始（包括where），后面的元素都要向后移一位。注意for循环的写法及自减--的使用。

搬运结束之后，链表中的where位置腾出来了，可以放置新元素，注意增加新元素的引用计数（Py_INCREF）。

链表插入的时间复杂度平均为O(n)，插入链表头的代价最大，所有元素都要后移，O(n)；插入链表尾部的代价最小，O(1)。

PyList_Append

### PyList_GetSlice

### PyList_SetSlice

### PyList_Sort

### PyList_Reverse

### PyList_AsTuple

### _PyList_Extend

### PyList_ClearFreeList

### list_resize