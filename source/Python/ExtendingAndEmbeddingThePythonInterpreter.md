# Extending and Embedding the Python Interpreter

本文档主要描述，如何通过C/C+-来创建新的Rython模块（module），从而扩展Python解释器（的使用）。这些Python module不仅可以定义新函数，而且还能定义新的对象类型（class）和对应的（类）方法。

本文档同样也描述了，如果把Python解释器嵌入另外一个程序，从而当做一个扩展语言使用。

最后，文档也展示了，当操作系统支持的时候，如何编译并链接这些扩展模块，以便在（程序）运行时，它们能够被解释器动态地加载。

本文档假定读者具备Python的基本知识。关于Python这门语言的非正式的介绍，可以查看[The python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)，而[The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index)给出了Python更正式的定义[The Python Standard Library](https://docs.python.org/3/library/index.html#library-index)描述了现有的对象类型（object types)，函数（functions)和模块 (modules)，它们都是使用Python编写，并且内置的，它们都有着广泛的应用范围关开完整的Python/C API接体文档，可以查看单独的[Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html#c-api-index)

### 推荐的第三方工具

本指南只介绍了在此版本的CPython下，利用其提供的基本工具，创建扩展模块。其他第三方程序，如 [Cython](https://cython.org/), [cffi](https://cffi.readthedocs.io/), [SWIG](https://www.swig.org/) 以及 [Numba](https://numba.pydata.org/) 都提供了更简单便捷和更复杂功能多样的方法，用来创建Python的C和C++的扩展。

[Python Packaging User Guide: Binary Extensions](https://packaging.python.org/guides/packaging-binary-extensions/) 不仅介绍了几种可用工具，它们使得创建二进制扩展更加便捷，而且还讨论了为什么创建一个扩展模块或许是首要考虑的各种原因。

### 不使用第三方工具来创建扩展

这一节主要讲述，在不使用第三方工具的情况下，如何创建出C/C++的扩展模块，这主要是为了这些第三方工具的作者使用，并不是鼓励使用这种办法创建自己的C/C++的扩展模块。

-   [1. Extending Python with C or C++](https://docs.python.org/3/extending/extending.html)
    -   [1.1. A Simple Example](https://docs.python.org/3/extending/extending.html#a-simple-example)
    -   [1.2. Intermezzo: Errors and Exceptions](https://docs.python.org/3/extending/extending.html#intermezzo-errors-and-exceptions)
    -   [1.3. Back to the Example](https://docs.python.org/3/extending/extending.html#back-to-the-example)
    -   [1.4. The Module’s Method Table and Initialization Function](https://docs.python.org/3/extending/extending.html#the-module-s-method-table-and-initialization-function)
    -   [1.5. Compilation and Linkage](https://docs.python.org/3/extending/extending.html#compilation-and-linkage)
    -   [1.6. Calling Python Functions from C](https://docs.python.org/3/extending/extending.html#calling-python-functions-from-c)
    -   [1.7. Extracting Parameters in Extension Functions](https://docs.python.org/3/extending/extending.html#extracting-parameters-in-extension-functions)
    -   [1.8. Keyword Parameters for Extension Functions](https://docs.python.org/3/extending/extending.html#keyword-parameters-for-extension-functions)
    -   [1.9. Building Arbitrary Values](https://docs.python.org/3/extending/extending.html#building-arbitrary-values)
    -   [1.10. Reference Counts](https://docs.python.org/3/extending/extending.html#reference-counts)
    -   [1.11. Writing Extensions in C++](https://docs.python.org/3/extending/extending.html#writing-extensions-in-c)
    -   [1.12. Providing a C API for an Extension Module](https://docs.python.org/3/extending/extending.html#providing-a-c-api-for-an-extension-module)
-   [2. Defining Extension Types: Tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html)
    -   [2.1. The Basics](https://docs.python.org/3/extending/newtypes_tutorial.html#the-basics)
    -   [2.2. Adding data and methods to the Basic example](https://docs.python.org/3/extending/newtypes_tutorial.html#adding-data-and-methods-to-the-basic-example)
    -   [2.3. Providing finer control over data attributes](https://docs.python.org/3/extending/newtypes_tutorial.html#providing-finer-control-over-data-attributes)
    -   [2.4. Supporting cyclic garbage collection](https://docs.python.org/3/extending/newtypes_tutorial.html#supporting-cyclic-garbage-collection)
    -   [2.5. Subclassing other types](https://docs.python.org/3/extending/newtypes_tutorial.html#subclassing-other-types)
-   [3. Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html)
    -   [3.1. Finalization and De-allocation](https://docs.python.org/3/extending/newtypes.html#finalization-and-de-allocation)
    -   [3.2. Object Presentation](https://docs.python.org/3/extending/newtypes.html#object-presentation)
    -   [3.3. Attribute Management](https://docs.python.org/3/extending/newtypes.html#attribute-management)
    -   [3.4. Object Comparison](https://docs.python.org/3/extending/newtypes.html#object-comparison)
    -   [3.5. Abstract Protocol Support](https://docs.python.org/3/extending/newtypes.html#abstract-protocol-support)
    -   [3.6. Weak Reference Support](https://docs.python.org/3/extending/newtypes.html#weak-reference-support)
    -   [3.7. More Suggestions](https://docs.python.org/3/extending/newtypes.html#more-suggestions)
-   [4. Building C and C++ Extensions](https://docs.python.org/3/extending/building.html)
    -   [4.1. Building C and C++ Extensions with distutils](https://docs.python.org/3/extending/building.html#building-c-and-c-extensions-with-distutils)
    -   [4.2. Distributing your extension modules](https://docs.python.org/3/extending/building.html#distributing-your-extension-modules)
-   [5. Building C and C++ Extensions on Windows](https://docs.python.org/3/extending/windows.html)
    -   [5.1. A Cookbook Approach](https://docs.python.org/3/extending/windows.html#a-cookbook-approach)
    -   [5.2. Differences Between Unix and Windows](https://docs.python.org/3/extending/windows.html#differences-between-unix-and-windows)
    -   [5.3. Using DLLs in Practice](https://docs.python.org/3/extending/windows.html#using-dlls-in-practice)


### 把CPython runtime嵌入更大的应用中


相比于创建一个运行于Python解释器当中的扩展当做主应用程序，有时候，更希望把CPython runtime嵌入到一个更大的应用程序中。这部分讲述了成功达成这个目的的一些细节。

-   [1. Embedding Python in Another Application](https://docs.python.org/3/extending/embedding.html)
    -   [1.1. Very High Level Embedding](https://docs.python.org/3/extending/embedding.html#very-high-level-embedding)
    -   [1.2. Beyond Very High Level Embedding: An overview](https://docs.python.org/3/extending/embedding.html#beyond-very-high-level-embedding-an-overview)
    -   [1.3. Pure Embedding](https://docs.python.org/3/extending/embedding.html#pure-embedding)
    -   [1.4. Extending Embedded Python](https://docs.python.org/3/extending/embedding.html#extending-embedded-python)
    -   [1.5. Embedding Python in C++](https://docs.python.org/3/extending/embedding.html#embedding-python-in-c)
    -   [1.6. Compiling and Linking under Unix-like systems](https://docs.python.org/3/extending/embedding.html#compiling-and-linking-under-unix-like-systems)



## 1. [Extending Python with C or C++](https://docs.python.org/3/extending/extending.html)

如果懂得如何使用C语言编程，那么很容易在Python中添加新的内置模块（built-in module）。这种扩展模块可以做到在Python中做不到的两件事（1）它们可以实现新的内置对象类型（built-in object type）（2）它们可以调用C的库函数和系统调用。

为了支持这样的扩展模块，Python应用程序接口（API，Application Programmers Interface）定义了一系列的函数、宏以及变量，它们被用来访问Python运行系统的各个方面。Python的这些API在C源文件中以`include "Python.h"`的方式被包含进来。

一个扩展模块的编译，不仅依赖于它的用途，而且也依赖于系统设置，后面的章节会给出更多的细节。

注意：C的扩展接口（函数）是CPython特有的，这样的扩展模块在其他实现方式的Python上是不工作的。在大多数情况下，可以避免撰写C的扩展，并且可以保留对其他实现方式的Python的可移植性。比如，如果使用场景是调用C的库函数或者调用系统函数，那么就可以考虑使用 `ctype` 这个Python模块，或者 `cffi` library，而不是编写自己的C代码。这些模块能够使你通过写Python代码的方式和（对应的）C代码打交道，并且在各个不同的Python实现上，比起自己撰写C代码和编译，更具有移植特性。

### 1.1. [A Simple Example](https://docs.python.org/3/extending/extending.html#a-simple-example)

下面举例，创建一个叫做 `spam` 的扩展模块，并假设要生成一个Python的接口，用来调用C的库函数 `system()`。这个函数接受一个以 `\0` 结尾的字符串作为参数，并且返回一个整型值。假设如下在Python中调用这个函数。

```python
import spam
status = spam.system("ls -l")
```

我们以创建一个叫做 `spammodule.c` 的文件开始。

根据历史约定俗成，如果一个模块叫做 `spam`，那么包含它的实现的C文件就命名为 `spammodule.c`；如果模块的名字很长，比如 `spammify`，那么模块（文件的）名字就可以直接叫做 `spammify.c`。

这个C文件开始的两行是，

```cpp
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```

这样就拉取了 `Python.h` 中包含的Python API，当然可以加入一些注释，用来说明该模块的作用，以及一些版权信息。

注意，由于Python定义了一些预编译的宏，它们可能在某些系统上影响标准库的头文件，所以（保险起见），必须在包含其他标准库头文件之前，首先包含该头文件，即 `#include <Python.h>`。

同时，也建议在  `#include <Python.h>` 之前，总是定义宏 `PY_SSIZE_T_CLEAN`，关于该宏的描述，参考 [Extracting Parameters in Extension Functions](https://docs.python.org/3/extending/extending.html#extracting-parameters-in-extension-functions)。

在 `Python.h` 中，所有用户可见的标识符，都有前缀 `Py` 或 `PY`，只有在标准库中定义的变量是例外。这是由于它们（标准库中的这些标识符）被Python解释器大量地使用，`Python.h` 包含的一些标准库的文件比如：`<stdio.h>`， `<string.h>`， `<errno.h>` 和 `<stdlib.h>`。

