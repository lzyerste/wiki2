# 2. [Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-functions)

## 内置函数一览

| 1                                        | 2                                        | 3                                        | 4                                        | 5                                        |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| [abs()](https://docs.python.org/3/library/functions.html#abs) | [dict()](https://docs.python.org/3/library/functions.html#func-dict) | [help()](https://docs.python.org/3/library/functions.html#help) | [min()](https://docs.python.org/3/library/functions.html#min) | [setattr()](https://docs.python.org/3/library/functions.html#setattr) |
| [all()](https://docs.python.org/3/library/functions.html#all) | [dir()](https://docs.python.org/3/library/functions.html#dir) | [hex()](https://docs.python.org/3/library/functions.html#hex) | [next()](https://docs.python.org/3/library/functions.html#next) | [slice()](https://docs.python.org/3/library/functions.html#slice) |
| [any()](https://docs.python.org/3/library/functions.html#any) | [divmod()](https://docs.python.org/3/library/functions.html#divmod) | [id()](https://docs.python.org/3/library/functions.html#id) | [object()](https://docs.python.org/3/library/functions.html#object) | [sorted()](https://docs.python.org/3/library/functions.html#sorted) |
| [ascii()](https://docs.python.org/3/library/functions.html#ascii) | [enumerate()](https://docs.python.org/3/library/functions.html#enumerate) | [input()](https://docs.python.org/3/library/functions.html#input) | [oct()](https://docs.python.org/3/library/functions.html#oct) | [staticmethod()](https://docs.python.org/3/library/functions.html#staticmethod) |
| [bin()](https://docs.python.org/3/library/functions.html#bin) | [eval()](https://docs.python.org/3/library/functions.html#eval) | [int()](https://docs.python.org/3/library/functions.html#int) | [open()](https://docs.python.org/3/library/functions.html#open) | [str()](https://docs.python.org/3/library/functions.html#func-str) |
| [bool()](https://docs.python.org/3/library/functions.html#bool) | [exec()](https://docs.python.org/3/library/functions.html#exec) | [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) | [ord()](https://docs.python.org/3/library/functions.html#ord) | [sum()](https://docs.python.org/3/library/functions.html#sum) |
| [bytearray()](https://docs.python.org/3/library/functions.html#bytearray) | [filter()](https://docs.python.org/3/library/functions.html#filter) | [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) | [pow()](https://docs.python.org/3/library/functions.html#pow) | [super()](https://docs.python.org/3/library/functions.html#super) |
| [bytes()](https://docs.python.org/3/library/functions.html#bytes) | [float()](https://docs.python.org/3/library/functions.html#float) | [iter()](https://docs.python.org/3/library/functions.html#iter) | [print()](https://docs.python.org/3/library/functions.html#print) | [tuple()](https://docs.python.org/3/library/functions.html#func-tuple) |
| [callable()](https://docs.python.org/3/library/functions.html#callable) | [format()](https://docs.python.org/3/library/functions.html#format) | [len()](https://docs.python.org/3/library/functions.html#len) | [property()](https://docs.python.org/3/library/functions.html#property) | [type()](https://docs.python.org/3/library/functions.html#type) |
| [chr()](https://docs.python.org/3/library/functions.html#chr) | [frozenset()](https://docs.python.org/3/library/functions.html#func-frozenset) | [list()](https://docs.python.org/3/library/functions.html#func-list) | [range()](https://docs.python.org/3/library/functions.html#func-range) | [vars()](https://docs.python.org/3/library/functions.html#vars) |
| [classmethod()](https://docs.python.org/3/library/functions.html#classmethod) | [getattr()](https://docs.python.org/3/library/functions.html#getattr) | [locals()](https://docs.python.org/3/library/functions.html#locals) | [repr()](https://docs.python.org/3/library/functions.html#repr) | [zip()](https://docs.python.org/3/library/functions.html#zip) |
| [compile()](https://docs.python.org/3/library/functions.html#compile) | [globals()](https://docs.python.org/3/library/functions.html#globals) | [map()](https://docs.python.org/3/library/functions.html#map) | [reversed()](https://docs.python.org/3/library/functions.html#reversed) | [\_\_import\_\_()](https://docs.python.org/3/library/functions.html#__import__) |
| [complex()](https://docs.python.org/3/library/functions.html#complex) | [hasattr()](https://docs.python.org/3/library/functions.html#hasattr) | [max()](https://docs.python.org/3/library/functions.html#max) | [round()](https://docs.python.org/3/library/functions.html#round) |                                          |
| [delattr()](https://docs.python.org/3/library/functions.html#delattr) | [hash()](https://docs.python.org/3/library/functions.html#hash) | [memoryview()](https://docs.python.org/3/library/functions.html#func-memoryview) | [set()](https://docs.python.org/3/library/functions.html#func-set) |                                          |

## range(start, stop[, step])

```python
range(stop)
range(start, stop[, step])
```

例子：
```python
list(range(5))  # [0, 1, 2, 3, 4]
list(range(4, -1, -1))  # [4, 3, 2, 1, 0]
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
```

Rather than being a function, [`range`](https://docs.python.org/3/library/stdtypes.html#range) is actually an immutable sequence type, as documented in [Ranges](https://docs.python.org/3/library/stdtypes.html#typesseq-range) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).

[start, stop)，start默认为0。

## print(s)

```python
print(objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

例子：

```python
print("Hello, world.")  # Hello, world.
print("Number %d" % (1))  # Number 1
print(s, end='')  # 末尾不要回车
print(s, file=f)  # 输出到文件f
print(1, 2, 3)  # 1 2 3   空格分开
print(1, 2, 3, sep=',')  # 1,2,3   以sep分开
```

Print *objects* to the text stream *file*, separated by *sep* and followed by *end*. *sep*, *end* and *file*, if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like [`str()`](https://docs.python.org/3/library/stdtypes.html#str) does and written to the stream, separated by *sep* and followed by *end*. Both *sep* and *end* must be strings; they can also be `None`, which means to use the default values. If no *objects* are given, [`print()`](https://docs.python.org/3/library/functions.html#print) will just write *end*.

The *file* argument must be an object with a `write(string)` method; if it is not present or `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout) will be used. Since printed arguments are converted to text strings, [`print()`](https://docs.python.org/3/library/functions.html#print) cannot be used with binary mode file objects. For these, use `file.write(...)` instead.

Whether output is buffered is usually determined by *file*, but if the *flush* keyword argument is true, the stream is forcibly flushed.

Changed in version 3.3: Added the *flush* keyword argument.

## len(s)

例子：

```python
len("abcd")  # 4, string
len([1, 2, 3, 4])  # 4, list
len((1, 2))  # 2, tuple
len(set([1, 2, 3, 1]))  # 3, set
```

Return the **length** (the number of items) of an object. The argument may be a **sequence** (such as a string, bytes, tuple, list, or range) or a **collection** (such as a dictionary, set, or frozen set).

返回长度或个数。

## open(file, mode, encoding)

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

例子（文本模式）：

```python
fin = open("in.txt", encoding='utf8')  # read text mode
fout = open("out.txt", 'w', encoding='utf8')  # write text mode
# fout.write(fin.read())
for line in fin:
    print(line, file=fout, end='')  # easy to control format
fin.close()
fout.close()
```

文件的常见操作有：

* **read()**：默认读取文件全部，也可以传入size参数指定读取字符个数。针对小文件，可以先一次性全部读取（返回字符串），然后再对返回的字符串进行操作，比如正则表达式处理或简单分行split()。
* **readlines()**：默认读取所有行（每行的换行符原汁原味存在），返回一个字符串链表。跟f.read().split()类似。也可以指定要读取的行数。
* **write()**：与read()对应的写操作，返回结果为写成功的字符个数。
* **writelines()**：与readlines()对应。

系统的标准输入输出为sys.stdin与sys.stdout，可以类似操作。

Open *file* and return a corresponding [file object](https://docs.python.org/3/glossary.html#term-file-object). If the file cannot be opened, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError) is raised.

***file*** is a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) giving the pathname (absolute or relative to the current working directory) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed, unless *closefd* is set to `False`.)

file一般使用文件路径字符串。

***mode*** is an optional string that specifies the mode in which the file is opened. It **defaults** to `'r'` which means open for **reading** in **text mode**. Other common values are `'w'`for **writing** (truncating the file if it already exists), `'x'` for exclusive creation and `'a'` for **appending** (which on *some* Unix systems, means that *all* writes append to the end of the file regardless of the current seek position). In text mode, if ***encoding*** is not specified, the encoding used is platform dependent:`locale.getpreferredencoding(False)` is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave *encoding* unspecified.) The available modes are:

| Character | Meaning                                  |
| --------- | ---------------------------------------- |
| `'r'`     | open for reading (default)               |
| `'w'`     | open for writing, **truncating the file first** |
| `'x'`     | open for exclusive creation, failing if the file already exists |
| `'a'`     | open for writing, appending to the end of the file if it exists |
| `'b'`     | **binary mode**                          |
| `'t'`     | text mode (default)                      |
| `'+'`     | open a disk file for updating (reading and writing) |
| `'U'`     | [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines) mode (deprecated) |

The default mode is `'r'` (open for reading text, synonym of `'rt'`). For binary read-write access, the mode `'w+b'` opens and truncates the file to 0 bytes. `'r+b'` opens the file without truncation.

As mentioned in the [Overview](https://docs.python.org/3/library/io.html#io-overview), Python distinguishes between binary and text I/O. Files opened in **binary mode** (including `'b'` in the *mode* argument) return contents as [`bytes`](https://docs.python.org/3/library/functions.html#bytes) objects without any decoding. In **text mode** (the default, or when `'t'` is included in the *mode* argument), the contents of the file are returned as [`str`](https://docs.python.org/3/library/stdtypes.html#str), the bytes having been first decoded using a platform-dependent encoding or using the specified ***encoding*** if given.

***encoding*** is the name of the encoding used to decode or encode the file. This should only be used in text mode. The default encoding is platform dependent (whatever [`locale.getpreferredencoding()`](https://docs.python.org/3/library/locale.html#locale.getpreferredencoding) returns), but any [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding) supported by Python can be used. See the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs) module for the list of supported encodings.

------

## list([iterable])

```python
class list([iterable])
```

例子：

```python
list()  # []
[]  # []
[1, 'a']  # [1, 'a']
list(range(5))  # [0, 1, 2, 3, 4]
list((1, 2))  # [1, 2], tuple, list(1, 2) is wrong
list({3, 5, 5})  # [3, 5], set
[i ** 2 for i in range(5)]  # [0, 1, 4, 9, 16]
[i for i in range(5) if i & 1]  # [1, 3], odd numbers
```

Rather than being a function, [`list`](https://docs.python.org/3/library/stdtypes.html#list) is actually a mutable sequence type, as documented in [Lists](https://docs.python.org/3/library/stdtypes.html#typesseq-list) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).

## dict(**kwarg)

```python
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
```

例子：

```python
dict()  # {}
{}  # {}
{1: 'a', 2: 'b'}  # {1: 'a', 2: 'b'}
```

Create a new dictionary. The [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) object is the dictionary class. See [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) and [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#typesmapping) for documentation about this class.

For other containers see the built-in [`list`](https://docs.python.org/3/library/stdtypes.html#list), [`set`](https://docs.python.org/3/library/stdtypes.html#set), and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple) classes, as well as the [`collections`](https://docs.python.org/3/library/collections.html#module-collections) module.

## set([iterable])

```python
class set([iterable])
```

例子：

```python
set()  # set()
{1, 2, 2}  # {1, 2}
# {} is an empty dict.
set([1, 2, 3, 3])  # {1, 2, 3}
```

Return a new [`set`](https://docs.python.org/3/library/stdtypes.html#set) object, optionally with elements taken from *iterable*. `set` is a built-in class. See [`set`](https://docs.python.org/3/library/stdtypes.html#set) and [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#types-set) for documentation about this class.

For other containers see the built-in [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset), [`list`](https://docs.python.org/3/library/stdtypes.html#list), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple), and [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) classes, as well as the [`collections`](https://docs.python.org/3/library/collections.html#module-collections) module.

## tuple([iterable])

```python
tuple([iterable])
```

tuple元组不可改。

例子：

```python
tuple()  # an empty tuple
()  # an empty tuple
tuple([1, 2])  # (1, 2)
(1, 2)  # (1, 2)
1, 2  # (1, 2)
a, b = b, a  # swap two elements
```

Rather than being a function, [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple) is actually an **immutable** sequence type, as documented in [Tuples](https://docs.python.org/3/library/stdtypes.html#typesseq-tuple) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).

------

## sum()

```python
sum(iterable[, start])
```

sum一般用于将iterable里的元素进行累加（对数字来说是求和，对链表则是连接），起始元素start可选，默认为0。

字符串的连接建议使用`''.join(sequence)`，即先将字符串碎片都存到一个链表，而不要一直使用`+`操作。

例子：

```python
sum([1, 2, 3])  # 6
sum([[1], [2], [3]], [])  # [1, 2, 3]，没必要，使用itertools.chain()
list(itertools.chain(*[[1], [2], [3]]))  # [1, 2, 3]
```

Sums *start* and the items of an *iterable* from left to right and returns the total. *start* defaults to `0`. The *iterable*‘s items are normally numbers, and the start value is not allowed to be a string.

For some use cases, there are good alternatives to [`sum()`](https://docs.python.org/3/library/functions.html#sum). The preferred, fast way to concatenate a sequence of strings is by calling `''.join(sequence)`. To add floating point values with extended precision, see [`math.fsum()`](https://docs.python.org/3/library/math.html#math.fsum). To concatenate a series of iterables, consider using [`itertools.chain()`](https://docs.python.org/3/library/itertools.html#itertools.chain).

## max()

```python
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
```

返回最大值，有两种调用方式。第一种传入iterable数据结构，如list，只占用一个positional argument，如`max([1, 2, 3])`；第二种方式直接传入要处理数据，至少要提供两个数据，如`max(1, 2)`因为如果只传入一个那么会被视为第一种调用方式。因此，`max(1)`的调用方式是错误的，因为`TypeError: 'int' object is not iterable`。

第一种调用方式有个default可选参数，这是因为传入的iterable可能是空的，那么返回default，如果default也没指定，那么就会报`ValueError`错误。

两种调用方式都提供了key可选参数，这与`list.sort()`是类似的，即可以指定比较方式。如果数据里有多个相同的最大值，那么返回第一个最大值，类似稳定排序。

例子：

```python
max([1, 2, -5])  # 2
max(1, 2, -5)  # 2
max([], default=0)  # 0
max([1, 2, -5], key=lambda x: abs(x))  # -5
```

Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, it should be an [iterable](https://docs.python.org/3/glossary.html#term-iterable). The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.

There are two optional keyword-only arguments. The *key* argument specifies a one-argument ordering function like that used for [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort). The *default* argument specifies an object to return if the provided iterable is empty. If the iterable is empty and *default* is not provided, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError) is raised.

If multiple items are maximal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as `sorted(iterable,key=keyfunc, reverse=True)[0]` and `heapq.nlargest(1, iterable, key=keyfunc)`.

## min()

```python
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
```

最小值函数，参考`max()`。

例子：

```python
min([1, 2, -5])  # -5
min(1, 2, -5)  # -5
min([], default=0)  # 0
min([1, 2, -5], key=lambda x: abs(x))  # 1
```

## pow()

```python
pow(x, y[, z])
```

指数函数，返回x的y次方。如果提供了第三个参数z，那么结果为x的y次方模z（比`pow(x, y) % z`要高效）。如果z参数是有效的，那么x跟y必须是整数，且y非负。

当然，`pow(x, y)`跟`x ** y`是等价的。

例子：

```python
pow(2, 4)  # 16
pow(2, 4, 7)  # 2
pow(2, 0.5)  # 1.414...
```

Return *x* to the power *y*; if *z* is present, return *x* to the power *y*, modulo *z* (computed more efficiently than `pow(x, y) % z`). The two-argument form `pow(x, y)` is equivalent to using the power operator: `x**y`.

The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. For [`int`](https://docs.python.org/3/library/functions.html#int) operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, `10**2` returns `100`, but `10**-2` returns `0.01`. If the second argument is negative, the third argument must be omitted. If *z* is present, *x* and *y* must be of integer types, and *y* must be non-negative.

## round()

```python
round(number[, ndigits])
```

四舍五入，保留ndigits位小数精度，默认则返回整数。

例子：

```python
round(1.5)  # 2
round(2.5)  # 2，因为倾向于偶数结果
round(-0.5)  # 0
round(-1.5)  # -2
round(3.1415926, 2)  # 3.14
round(3.1415926, 4)  # 3.1416
round(2.675, 2)  # 2.67，注意
```

Return *number* rounded to *ndigits* precision after the decimal point. If *ndigits* is omitted or is `None`, it returns the nearest integer to its input.

For the built-in types supporting [`round()`](https://docs.python.org/3/library/functions.html#round), values are rounded to the closest multiple of 10 to the power minus *ndigits*; if two multiples are equally close, rounding is done toward the even choice (so, for example, both `round(0.5)` and `round(-0.5)` are `0`, and `round(1.5)` is `2`). Any integer value is valid for *ndigits* (positive, zero, or negative). The return value is an integer if called with one argument, otherwise of the same type as *number*.

For a general Python object `number`, `round(number, ndigits)` delegates to `number.__round__(ndigits)`. 

> **Note:** The behavior of [`round()`](https://docs.python.org/3/library/functions.html#round) for floats can be surprising: for example, `round(2.675, 2)` gives `2.67` instead of the expected `2.68`. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues) for more information.

## abs(x)

```python
abs(x)
```

取绝对值，针对整型、浮点及复数都可用。如果是复数，则返回它的模。

例子：

```python
abs(3)  # 3, integer
abs(-3)  # 3
abs(1.2)  # 1.2, floating point
abs(-1.2)  # 1.2
abs(3 + 4j)  # 5.0, complex number
```

Return the **absolute value** of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.

## divmod(a, b)

```python
divmod(a, b)
```

返回整数除法的商及余数，余数的符号与除数b相同。

例子：

```python
a = 9
b = 4
divmod(a, b)  # (2, 1)
b = -4
divmod(a, b)  # (-3, -3), q * b + a % b = a, -3 * (-4) + (-3) = 9
divmod(1234, 10)  # (123, 4)
```

Take two (non complex) numbers as arguments and return a pair of numbers consisting of their **quotient** and **remainder** when using **integer division**. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as `(a // b, a % b)`. For floating point numbers the result is `(q, a % b)`, where *q* is usually `math.floor(a / b)` but may be 1 less than that. In any case `q * b + a % b` is very close to *a*, if `a % b` is non-zero it has the same sign as *b*, and `0 <= abs(a % b) < abs(b)`.

------

## str()

```python
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
```

常用的转字符串函数，返回字符串`str`类型。

例子：

```python
str(1)  # '1'
str([1, 2])  # '[1, 2]'
```

Return a [`str`](https://docs.python.org/3/library/stdtypes.html#str) version of *object*. See [`str()`](https://docs.python.org/3/library/stdtypes.html#str) for details.

`str` is the built-in string [class](https://docs.python.org/3/glossary.html#term-class). For general information about strings, see [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#textseq).

## int()

```python
class int(x=0)
class int(x, base=10)
```

转整型。传入为字符串时，可以指定转换进制。如果传入为浮点数，那么相当于把小数部分去除，只保留整数部分，也就是向0靠拢。

例子：

```python
int('101')  # 101，默认10进制
int('101', 2)  # 5，2进制
int('101', 8)  # 65，8进制

int('101', 0)  # 101
# int('0101', 0)  # invalid literal，0x，0o，0b
int('0x101', 0)  # 257，0x指定为16进制，base=0
int('0o101', 0)  # 65，8进制
int('0b101', 0)  # 5，2进制

int(1.2)  # 1
int(-1.2)  # -1
```

Return an integer object constructed from a number or string *x*, or return `0` if no arguments are given. If *x* is a number, return [`x.__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__). For floating point numbers, this truncates towards zero.

If *x* is not a number or if *base* is given, then *x* must be a string, [`bytes`](https://docs.python.org/3/library/functions.html#bytes), or [`bytearray`](https://docs.python.org/3/library/functions.html#bytearray) instance representing an [integer literal](https://docs.python.org/3/reference/lexical_analysis.html#integers) in radix *base*. Optionally, the literal can be preceded by `+` or `-` (with no space in between) and surrounded by whitespace. A base-n literal consists of the digits 0 to n-1, with `a` to `z` (or `A` to `Z`) having values 10 to 35. The default *base* is 10. The allowed values are 0 and 2–36. Base-2, -8, and -16 literals can be optionally prefixed with `0b`/`0B`, `0o`/`0O`, or `0x`/`0X`, as with integer literals in code. Base 0 means to interpret exactly as a code literal, so that the actual base is 2, 8, 10, or 16, and so that `int('010', 0)` is not legal, while `int('010')` is, as well as `int('010', 8)`.

The integer type is described in [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#typesnumeric).

## float()

------

## bin()

## hex()

## oct()

## chr()

## ord()

------

## sorted()

## reversed()

## map()

## zip()