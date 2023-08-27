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

在 `Python.h` 中，所有用户可见的标识符，都有前缀 `Py` 或 `PY`，只有在标准库中定义的变量是例外。这是由于它们（标准库中的这些标识符）被Python解释器大量地使用，`Python.h` 包含的一些标准库的文件比如：`<stdio.h>`， `<string.h>`， `<errno.h>` 和 `<stdlib.h>`。如果这些头文件在系统中不存在，那么它就会直接声明函数 `malloc()`, `free()` 和 `realloc()`。

接下来，要给我们的模块文件加入一个C函数，这个函数在Python解释器执行到 `spam.system(string)` 语句的时候被调用到（稍后我们会看到它是如何被调用的）,

```cpp
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}
```

这里从Python参数列表到传入C函数的参数列表，是一个直观的转换，比如这里的参数 `ls -l`。按照约定俗成，这里的C函数的两个参数名称分别是 `self` 和 `args`。

`self` 指针参数指向的是模块对象，为的是访问模块层级的函数；对于一个Python method，它指向的是一个对象实例。

`args` 指针参数指向的是包含有参数的Python元组（tuple）。这个元组中的每一项对应的就是调用参数列表中的一个参数。因为参数是Python对象，为了在我们的C函数中使用，就需要将其转换为C的值。Python API中的函数 [`PyArg_ParseTuple()`](file:///D:/procs/python-3.11.4-docs-html/c-api/arg.html#c.PyArg_ParseTuple) 就是用来检查参数类型，并将其转换为C值。它使用一个字符串模板来决定所需的参数类型，以及用来存储转换后的C值的C变量。

如果所有参数的类型正确，并且其对应的C值存入到了传入的地址（对应的内存）中，函数 [`PyArg_ParseTuple()`](file:///D:/procs/python-3.11.4-docs-html/c-api/arg.html#c.PyArg_ParseTuple) 返回 `true` （非零）。如果传入的是一个不正确的参数列表，那么函数 [`PyArg_ParseTuple()`](file:///D:/procs/python-3.11.4-docs-html/c-api/arg.html#c.PyArg_ParseTuple) 返回 `false` （零）。在后者的情况中，它同时会抛出一个合适的异常，据此调用它的函数就能立即返回 `NULL`。

### 1.2. Intermezzo: Errors and Exceptions

贯穿于Python解释器中一个约定是，当一个函数执行失败时，它应该设置一个异常条件，并且返回一个错误值（通常是 `-1` 或 `NULL` 指针）。异常信息则被存储在了Python解释器的三个线程安全的变量中。当没有异常的时候，它们都是 `NULL`。当存在异常的时候，它们是和 [`sys.exc_info()`](file:///D:/procs/python-3.11.4-docs-html/library/sys.html#sys.exc_info) 返回的Python元组对应的三个C变量。了解它们对于理解错误（信息）是如何传递的很重要。

Python API定义了一系列的函数，用来设定各种类型的异常。

最常用的函数是 is [`PyErr_SetString()`](file:///D:/procs/python-3.11.4-docs-html/c-api/exceptions.html#c.PyErr_SetString)。它的参数一个异常对象和一个C字符串。这个异常对象通常是预定义的对象，比如 `PyExc_ZeroDivisionError`。这C字符串描述了错误发生的原因，并且它会被转换为Python字符串对象，然后存储在和异常关联的值上。

另一个有用的函数是 [`PyErr_SetFromErrno()`](../c-api/exceptions.html#c.PyErr_SetFromErrno "PyErr_SetFromErrno")，它只接收一个异常参数，然后根据这个查询一个全局变量 `errno` 来构造对应的关联值。最一般化的函数是 [`PyErr_SetObject()`](../c-api/exceptions.html#c.PyErr_SetObject "PyErr_SetObject")，它接收两个对象参数，一个异常，一个和这个异常关联的值。你不需要对传入这些函数的对象调用 [`Py_INCREF()`](../c-api/refcounting.html#c.Py_INCREF "Py_INCREF")。

你可以通过非侵入式的测试，来检查一个异常是否由 [`PyErr_Occurred()`](../c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred") 设定。它返回当前的异常对象，当没有异常时则返回 `NULL`。一般情况下，你不需要通过调用[`PyErr_Occurred()`](../c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred") 来确定在函数调用中是否发生了错误，因为你能够从函数的返回值中就可以得知。

当一个函数 $f$ 调用另一个函数 $g$，并且后者失败了，那么函数 $f$ 本身就应该返回一个错误值（通常是 `NULL` 或 `-1`）。它**不应该**调用那些 `PyErr_*` 函数，因为这些函数通常已经在 $g$ 中被调用过了。同样的，调用 $f$ 的函数也不需要调用那些 `PyErr_*` 函数，它也只需返回一个错误指示给调用它的函数，以此类推，因为关于错误最详细的发生原因，已经由第一个检测到它的函数报告过了。一旦这个错误到达Python解释器的主循环，它就会中断执行当前的Python代码，然后试图找到一个由Python编程者指定的异常处理机制。

（确实有一些情况下，模块实际上可以通过调用些 `PyErr_*` 函数来给出关于错误的更详细的信息， 那么在这种情况下，这样做是合适的。然而，按照一般原则，这不是必需的，而且有可能造成关于错误信息丢失的情况，因为大部分操作有可能因为各种各样的问题而失败）

为了忽略一个由函数调用失败引起的异常，那么异常条件就必须显式地使用 [`PyErr_Clear()`](../c-api/exceptions.html#c.PyErr_Clear "PyErr_Clear") 来清除掉。在C代码中，显式调用 [`PyErr_Clear()`](../c-api/exceptions.html#c.PyErr_Clear "PyErr_Clear") 的唯一情况是，它不想把这个错误传递给Python解释器，而是想独自完全处理它（比如很可能尝试其他操作，或者装作无事发生）。

每次调用 `malloc()` 就必须抛异常，当直接调用 `malloc()` 或 `realloc()` 失败时必须调用 [`PyErr_NoMemory()`](../c-api/exceptions.html#c.PyErr_NoMemory "PyErr_NoMemory")，然后返回一个错误指示。所有创建了对象的函数（比如 [`PyLong_FromLong()`](../c-api/long.html#c.PyLong_FromLong "PyLong_FromLong")）已经做了这样的事情，所以这是给那些直接调用 `malloc()` 相关的代码的提示。

同样要注意，除了 [`PyArg_ParseTuple()`](../c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple") 这个重要的例外，对于返回一个整型值表示状态的函数，应该返回一个正值或 `0` 表示成功，`-1`表示失败，就像Unix系统调用一样。

最后，当返回一个错误指示的时候，如果要清理“垃圾”时要小心，比如对已经创建的对象调用[`Py_XDECREF()`](../c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF") 或 [`Py_DECREF()`](../c-api/refcounting.html#c.Py_DECREF "Py_DECREF")。

选择抛出什么样的异常完全由调用者自己决定。对于Python内置的异常，都有对应的预定义好的C对象，比如 `PyExc_ZeroDivisionError`，而这些是可以直接使用的。当然，应该合理地选择要抛出的异常，比如，如果要表示一个文件无法打开，就不应该使用 `PyExc_TypeError`，而应该使用 `PyExc_OSError`。如果有参数列表错误，函数 [`PyArg_ParseTuple()`](../c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple") 通常抛出异常 `PyExc_TypeError`。如果有一个参数的值不符合想要的范围，或没有满足某些条件，那么抛出异常 `PyExc_ValueError` 是合适的。

当然也可以在模块中定义一个新的异常，这个异常就是对这个模块独有的。为了定义这个异常，通常在（模块）文件的开始声明一个 `static` 静态变量（指针）：

```cpp
static PyObject *SpamError;
```

然后在该模块的初始化函数（本文的例子里就是 `PyInit_spam()`）里去初始化它：

```cpp
PyMODINIT_FUNC
PyInit_spam(void)
{
    PyObject *m;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    SpamError = PyErr_NewException("spam.error", NULL, NULL);
    Py_XINCREF(SpamError);
    if (PyModule_AddObject(m, "error", SpamError) < 0) {
        Py_XDECREF(SpamError);
        Py_CLEAR(SpamError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
```

注意，这里给出的异常名称，在Python中是 `spam.error`。函数 [`PyErr_NewException()`](../c-api/exceptions.html#c.PyErr_NewException "PyErr_NewException") 创建的class的基类是 [`Exception`](../library/exceptions.html#Exception "Exception")（除法传入的参数不是 `NULL` 而是其他class），它在中 [Built-in Exceptions](../library/exceptions.html#bltin-exceptions) 有描述。

还要注意，`SpamError` 变量保留了一个指向新创建的异常类的引用，而这是故意如此！因为这个异常可以被该模块以外的代码删除，所以为了防止 `SpamError` 变成一个dangling指针，一个指向这个类的owned reference就应该被保留。如果它变成了一个dangling指针，那么要抛出这个异常的C代码就可能产生core dump，或者其他非预期的副作用。

关于 `PyMODINIT_FUNC` 被当做一个函数返回值来使用的细节，我们后面再讨论。

这个定义好的 `spam.error` 异常，就可以在扩展模块中使用 [`PyErr_SetString()`](../c-api/exceptions.html#c.PyErr_SetString "PyErr_SetString") 函数来抛出，如下：

```cpp
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(SpamError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}
```



