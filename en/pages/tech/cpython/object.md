## PyObject

文件：Include/object.h

```c
/* Nothing is actually declared to be a PyObject, but every pointer to
 * a Python object can be cast to a PyObject*.  This is inheritance built
 * by hand.  Similarly every pointer to a variable-size Python object can,
 * in addition, be cast to PyVarObject*.
 */
typedef struct _object {
    _PyObject_HEAD_EXTRA  // 用于debug & trace，组成双向链表
    Py_ssize_t ob_refcnt;  // 引用计数
    struct _typeobject *ob_type;  // 类型信息
} PyObject;
```

一般来说，是将PyObject嵌入具体的object，而且放在第一位置，所以其他object可方便地直接转换为PyObject指针，然后可以获取它的type信息（ob_type）。

```c
#ifdef Py_TRACE_REFS
/* Define pointers to support a doubly-linked list of all live heap objects. */
#define _PyObject_HEAD_EXTRA            \
    struct _object *_ob_next;           \
    struct _object *_ob_prev;

#define _PyObject_EXTRA_INIT 0, 0,
```

0、0表示初始化时将`_ob_next`与`_ob_prev`置为NULL。

```c
/* PyObject_HEAD defines the initial segment of every PyObject. */
#define PyObject_HEAD                   PyObject ob_base;

#define PyObject_HEAD_INIT(type)        \
    { _PyObject_EXTRA_INIT              \
    1, type },
```

用来初始化PyObject，将引用计数初始化为1。如果其他数据结构需要在头部放置一个PyObject，那么可以直接塞入一个PyObject_HEAD宏即可。

## PyVarObject

文件：Include/object.h

```c
typedef struct {
    PyObject ob_base;
    Py_ssize_t ob_size; /* Number of items in variable part */
} PyVarObject;
```

可变长的数据结构一般嵌套一个PyVarObject，它本身内部也包含一个PyObject（置于头部），此外，另一个成员ob_size用来记录可变长数据结构的当前可见大小（比如链表的长度），而不是实际可容纳大小（比如链表数据结构有另一个成员allocated来记录）。

因为首地址相同，所以可通过指针直接转换数据类型，比如PyListObject指针可以直接转换为PyVarObject指针，然后再取它的ob_size成员，即可得到长度。这也就是Py_SIZE的实现方式。

```c
#define PyVarObject_HEAD_INIT(type, size)       \
    { PyObject_HEAD_INIT(type) size },

/* PyObject_VAR_HEAD defines the initial segment of all variable-size
 * container objects.  These end with a declaration of an array with 1
 * element, but enough space is malloc'ed so that the array actually
 * has room for ob_size elements.  Note that ob_size is an element count,
 * not necessarily a byte count.
 */
#define PyObject_VAR_HEAD      PyVarObject ob_base;
```

与PyObject的初始化类似。

注释中说的array with 1 element是说其他可变长数据结构包含PyVarObject之后，一般会有一个指针变量（array with 1 element，比如PyListObject中的二级指针ob_item），用来申请及存储元素，比如存放ob_size个元素。

## Methods

```c
#define Py_REFCNT(ob)           (((PyObject*)(ob))->ob_refcnt)
#define Py_TYPE(ob)             (((PyObject*)(ob))->ob_type)
#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)
```

这几个宏的含义很直观。

## TOOD

struct _typeobject，即PyTypeObject（Include/object.h）。