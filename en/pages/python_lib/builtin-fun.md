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

## range()

- range(*stop*)
- range(*start*, *stop*[, *step*])

Rather than being a function, [`range`](https://docs.python.org/3/library/stdtypes.html#range) is actually an immutable sequence type, as documented in [Ranges](https://docs.python.org/3/library/stdtypes.html#typesseq-range) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).

[start, stop)，start默认为0。

```python
list(range(5))  # [0, 1, 2, 3, 4]
list(range(4, -1, -1))  # [4, 3, 2, 1, 0]
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
```

## print()

print(*objects*, *sep=' '*, *end='\n'*, *file=sys.stdout*, *flush=False*)

Print *objects* to the text stream *file*, separated by *sep* and followed by *end*. *sep*, *end* and *file*, if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like [`str()`](https://docs.python.org/3/library/stdtypes.html#str) does and written to the stream, separated by *sep* and followed by *end*. Both *sep* and *end* must be strings; they can also be `None`, which means to use the default values. If no *objects* are given, [`print()`](https://docs.python.org/3/library/functions.html#print) will just write *end*.

The *file* argument must be an object with a `write(string)` method; if it is not present or `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout) will be used. Since printed arguments are converted to text strings, [`print()`](https://docs.python.org/3/library/functions.html#print) cannot be used with binary mode file objects. For these, use `file.write(...)` instead.

Whether output is buffered is usually determined by *file*, but if the *flush* keyword argument is true, the stream is forcibly flushed.

Changed in version 3.3: Added the *flush* keyword argument.

```python
print("Hello, world.")  # Hello, world.
print(s, end='')  # 末尾不要回车
print(s, file=f)  # 输出到文件f
print(1, 2, 3)  # 1 2 3
print(1, 2, 3, sep=',')  # 1,2,3
```

## len(s)

Return the **length** (the number of items) of an object. The argument may be a **sequence** (such as a string, bytes, tuple, list, or range) or a **collection** (such as a dictionary, set, or frozen set).

返回长度或个数。

```python
len("abcd")  # 4, string
len([1, 2, 3, 4])  # 4, list
len((1, 2))  # 2, tuple
len(set([1, 2, 3, 1]))  # 3, set
```

## open()

------

## list()

## dict()

## set()

## tuple()

------

## sum()

## max()

## min()

## pow()

## round()

## abs(x)

Return the **absolute value** of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.

取绝对值，针对整型、浮点及复数都可用。如果是复数，则返回它的模。

```python
abs(3)  # 3, integer
abs(-3)  # 3
abs(1.2)  # 1.2, floating point
abs(-1.2)  # 1.2
abs(3 + 4j)  # 5.0, complex number
```

## divmod(a, b)

Take two (non complex) numbers as arguments and return a pair of numbers consisting of their **quotient** and **remainder** when using **integer division**. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as `(a // b, a % b)`. For floating point numbers the result is `(q, a % b)`, where *q* is usually `math.floor(a / b)` but may be 1 less than that. In any case `q * b + a % b` is very close to *a*, if `a % b` is non-zero it has the same sign as *b*, and `0 <= abs(a % b) < abs(b)`.

返回整数除法的商及余数，余数的符号与除数b相同。

```python
a = 9
b = 4
divmod(a, b)  # (2, 1)
b = -4
divmod(a, b)  # (-3, -3), q * b + a % b = a, -3 * (-4) + (-3) = 9
```

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