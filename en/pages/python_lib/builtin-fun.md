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

## min()

## pow()

## round()

## abs(x)

```python
abs(x)
```

例子：

```python
abs(3)  # 3, integer
abs(-3)  # 3
abs(1.2)  # 1.2, floating point
abs(-1.2)  # 1.2
abs(3 + 4j)  # 5.0, complex number
```

Return the **absolute value** of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.

取绝对值，针对整型、浮点及复数都可用。如果是复数，则返回它的模。

## divmod(a, b)

```python
divmod(a, b)
```

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

返回整数除法的商及余数，余数的符号与除数b相同。

------

## str()

## int()

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