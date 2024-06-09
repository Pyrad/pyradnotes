# Extending and Embedding the Python Interpreter

本文档主要描述，如何通过C/C+-来创建新的Python模块（module），从而扩展Python解释器（的使用）。这些Python module不仅可以定义新函数，而且还能定义新的对象类型（class）和对应的（类）方法。

本文档同样也描述了，如果把Python解释器嵌入另外一个程序，从而当做一个扩展语言使用。

最后，文档也展示了，当操作系统支持的时候，如何编译并链接这些扩展模块，以便在（程序）运行时，它们能够被解释器动态地加载。

本文档假定读者具备Python的基本知识。关于Python这门语言的非正式的介绍，可以查看[The python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)，而[The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index)给出了Python更正式的定义[The Python Standard Library](https://docs.python.org/3/library/index.html#library-index)描述了现有的对象类型（object types)，函数（functions)和模块 (modules)，它们都是使用Python编写，并且内置的，它们都有着广泛的应用范围关开完整的Python/C API接体文档，可以查看单独的[Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html#c-api-index)


## Words

exercise caution 谨慎行事

boilerplate /ˈbɔɪləpleɪt/ 

assorted 各种各样，混杂的

## Links

[Python 3.x.x documentation](https://docs.python.org/3/index.html)

[Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)

[The Python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)

[浅谈Python C扩展](https://blog.csdn.net/fitzzhang/article/details/79212411)


### 编译Python export 模块

- [C++ CMake 使用 Python3](https://www.cnblogs.com/mxnote/p/16743186.html)
- [浅析 C++ 调用 Python 模块](https://www.cnblogs.com/findumars/p/6142330.html)
- [FindPython3 - 3.27.4](https://cmake.org/cmake/help/latest/module/FindPython3.html)






## 推荐的第三方工具

本指南只介绍了在此版本的CPython下，利用其提供的基本工具，创建扩展模块。其他第三方程序，如 [Cython](https://cython.org/), [cffi](https://cffi.readthedocs.io/), [SWIG](https://www.swig.org/) 以及 [Numba](https://numba.pydata.org/) 都提供了更简单便捷和更复杂功能多样的方法，用来创建Python的C和C++的扩展。

[Python Packaging User Guide: Binary Extensions](https://packaging.python.org/guides/packaging-binary-extensions/) 不仅介绍了几种可用工具，它们使得创建二进制扩展更加便捷，而且还讨论了为什么创建一个扩展模块或许是首要考虑的各种原因。

## 不使用第三方工具来创建扩展

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


## 把CPython runtime嵌入更大的应用中


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

下面举例，创建一个叫做 `spam` 的扩展模块，并假设要生成一个Python的接口，用来调用C的库函数 `system()` 【1】。这个函数接受一个以 `\0` 结尾的字符串作为参数，并且返回一个整型值。假设如下在Python中调用这个函数。

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

`args` 指针参数指向的是包含有参数的Python元组（tuple）。这个元组中的每一项对应的就是调用参数列表中的一个参数。因为参数是Python对象，为了在我们的C函数中使用，就需要将其转换为C的值。Python API中的函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 就是用来检查参数类型，并将其转换为C值。它使用一个字符串模板来决定所需的参数类型，以及用来存储转换后的C值的C变量。

如果所有参数的类型正确，并且其对应的C值存入到了传入的地址（对应的内存）中，函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 返回 `false` （零）。在后者的情况中，它同时会抛出一个合适的异常，据此调用它的函数就能立即返回 `NULL`。

### 1.2. Intermezzo: Errors and Exceptions

贯穿于Python解释器中一个约定是，当一个函数执行失败时，它应该设置一个异常条件，并且返回一个错误值（通常是 `-1` 或 `NULL` 指针）。异常信息则被存储在了Python解释器的三个线程安全的变量中。当没有异常的时候，它们都是 `NULL`。当存在异常的时候，它们是和 [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info) 返回的Python元组对应的三个C变量。了解它们对于理解错误（信息）是如何传递的很重要。

Python API定义了一系列的函数，用来设定各种类型的异常。

最常用的函数是 is [`PyErr_SetString()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString)。它的参数一个异常对象和一个C字符串。这个异常对象通常是预定义的对象，比如 `PyExc_ZeroDivisionError`。这C字符串描述了错误发生的原因，并且它会被转换为Python字符串对象，然后存储在和异常关联的值上。

另一个有用的函数是 [`PyErr_SetFromErrno()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrno)，它只接收一个异常参数，然后根据这个查询一个全局变量 `errno` 来构造对应的关联值。最一般化的函数是 [`PyErr_SetObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetObject)，它接收两个对象参数，一个异常，一个和这个异常关联的值。你不需要对传入这些函数的对象调用 [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF)。

你可以通过非侵入式的测试，来检查一个异常是否由 [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred) 设定。它返回当前的异常对象，当没有异常时则返回 `NULL`。一般情况下，你不需要通过调用[`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred) 来确定在函数调用中是否发生了错误，因为你能够从函数的返回值中就可以得知。

当一个函数 $f$ 调用另一个函数 $g$，并且后者失败了，那么函数 $f$ 本身就应该返回一个错误值（通常是 `NULL` 或 `-1`）。它**不应该**调用那些 `PyErr_*` 函数，因为这些函数通常已经在 $g$ 中被调用过了。同样的，调用 $f$ 的函数也不需要调用那些 `PyErr_*` 函数，它也只需返回一个错误指示给调用它的函数，以此类推，因为关于错误最详细的发生原因，已经由第一个检测到它的函数报告过了。一旦这个错误到达Python解释器的主循环，它就会中断执行当前的Python代码，然后试图找到一个由Python编程者指定的异常处理机制。

（确实有一些情况下，模块实际上可以通过调用些 `PyErr_*` 函数来给出关于错误的更详细的信息， 那么在这种情况下，这样做是合适的。然而，按照一般原则，这不是必需的，而且有可能造成关于错误信息丢失的情况，因为大部分操作有可能因为各种各样的问题而失败）

为了忽略一个由函数调用失败引起的异常，那么异常条件就必须显式地使用 [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear) 来清除掉。在C代码中，显式调用 [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear) 的唯一情况是，它不想把这个错误传递给Python解释器，而是想独自完全处理它（比如很可能尝试其他操作，或者装作无事发生）。

每次调用 `malloc()` 就必须抛异常，当直接调用 `malloc()` 或 `realloc()` 失败时必须调用 [`PyErr_NoMemory()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NoMemory)，然后返回一个错误指示。所有创建了对象的函数（比如 [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong)）已经做了这样的事情，所以这是给那些直接调用 `malloc()` 相关的代码的提示。

同样要注意，除了 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple") 这个重要的例外，对于返回一个整型值表示状态的函数，应该返回一个正值或 `0` 表示成功，`-1`表示失败，就像Unix系统调用一样。

最后，当返回一个错误指示的时候，如果要清理“垃圾”时要小心，比如对已经创建的对象调用[`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF) 或 [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF)。

选择抛出什么样的异常完全由调用者自己决定。对于Python内置的异常，都有对应的预定义好的C对象，比如 `PyExc_ZeroDivisionError`，而这些是可以直接使用的。当然，应该合理地选择要抛出的异常，比如，如果要表示一个文件无法打开，就不应该使用 `PyExc_TypeError`，而应该使用 `PyExc_OSError`。如果有参数列表错误，函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple") 通常抛出异常 `PyExc_TypeError`。如果有一个参数的值不符合想要的范围，或没有满足某些条件，那么抛出异常 `PyExc_ValueError` 是合适的。

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

注意，这里给出的异常名称，在Python中是 `spam.error`。函数 [`PyErr_NewException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewException) 创建的class的基类是 [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)（除法传入的参数不是 `NULL` 而是其他class），它在中 [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) 有描述。

还要注意，`SpamError` 变量保留了一个指向新创建的异常类的引用，而这是故意如此！因为这个异常可以被该模块以外的代码删除，所以为了防止 `SpamError` 变成一个dangling指针，一个指向这个类的owned reference就应该被保留。如果它变成了一个dangling指针，那么要抛出这个异常的C代码就可能产生core dump，或者其他非预期的副作用。

关于 `PyMODINIT_FUNC` 被当做一个函数返回值来使用的细节，我们后面再讨论。

这个定义好的 `spam.error` 异常，就可以在扩展模块中使用 [`PyErr_SetString()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString) 函数来抛出，如下：

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


### 1.3. Back to the Example

现在回到我们之前的例子，现在应该就能理解下面的语句：

```cpp
if (!PyArg_ParseTuple(args, "s", &command))
    return NULL;
```

当检测到参数列表中有错误出现时，它就会返回 `NULL`。这个错误是根据 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 内部的异常所设置的，这里的 `NULL` 是错误指示器，用在那些返回值是对象指针的函数里。如果参数列表正常，字符串里的值就被拷贝到局部变量 `command` 中去。这是一个指针赋值，而且不应该修改这个指针指向的字符串（因此在标准C中，变量 `command` 应该被声明为 `const char *command`，这样更合适）。

下面的语句就是调用Unix函数 `system()`，把从  [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 得到的字符串作为参数传入：

```cpp
sts = system(command);
```

因为我们的 `spanm.system()` 必须将 `sts` 以Python对象的形式返回，所以使用函数 [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong) 然后返回：

```cpp
return PyLong_FromLong(sts);
```

这种情况下，函数返回一个整型对象（是的，在Python里面，整型数实际上也是位于堆上的对象！）。

如果你的C函数返回一个没有什么用的参数（即函数返回 `void`），那么对应的Python函数就应该返回 `None`，你就需要使用如下语句习惯来实现：

```cpp
Py_INCREF(Py_None);
return Py_None;
```

这里的 `Py_None` 是Python中特殊对象 `None` 在C中的名字，它是一个标准的Python对象，而不是一个 `NULL` 指针，它一般在上下文中代表发生了错误，就像我们之前见到的一样。

### 1.4. The Module’s Method Table and Initialization Function

之前承诺提到要展示 `spam_system()` 这个C函数是如何在Python程序中调用的。首先，我们要把它的名字和（函数）地址在一个叫做“方法表”（method table）的数据结构（其实就是一个C中的静态数组）中列出：

```cpp
static PyMethodDef SpamMethods[] = {
    ...
    {"system", spam_system, METH_VARARGS, "Execute a shell command."},
    ...
    {NULL, NULL, 0, NULL}        /* Sentinel */
};
```

注意，第三项 `METH_VARARGS`，它是一个标记，用来告知Python解释器如何调用对应C函数的一种约定。通常情况下，它应该总是 `METH_VARARGS` 或者 `METH_VARARGS | METH_KEYWORDS`；值 `0` 表示使用了一个废弃的变种函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple)。

当仅使用 `METH_VARARGS` 的时候，函数应该只接收Python层面的参数，并将其当做一个元组，以供函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 进行解析，下面是该函数详细的分析。

如果是以关键字参数的形式传参给函数，那么就可以在第三项上设置 `METH_KEYWORDS` 这一位（bit）。这种情况下，对应的C函数应该有第三个参数，这第三个参数是一个关键字的字典（keyword dictionary），而且应该使用函数 [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords") 去解析传递进来的参数。

在模块定义结构中，必须引用前面提到的函数表（方法表，method table）：

```cpp
static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    spam_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};
```

进一步，这个（模块定义）结构，必须在模块初始化函数中传递给解释器。初始化函数的名字结构形式必须是 `PyInit_name()`，这里 `name` 就是这个模块的名称，并且这个初始化函数必须是模块文件中定义的唯一一个非静态函数（only non-`static`）。

```cpp
PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
```

注意，`PyMODINIT_FUNC` 声明了这个函数是以 `PyObject *`的类型作为返回值类型，但这个函数也可以被声明为按照系统平台要求的其他特殊链接类型的返回值类型，也可以按照 `extern "C"` 的方式在C++中声明。

当Python程序第一次导入模块（import module）时，`PyInit_spam()` 就会被调用。（下面的代码片段中有注释说明）它又调用了函数 [`PyModule_Create()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create)，这个函数返回一个模块对象，并且会根据模块定义中的表（table，一个 [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef) 结构的数组），把一些内置函数对象插入到这个新创建的模块中去。函数 [`PyModule_Create()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create) 返回一个指向新创建的模块对象的指针。它可能因为某些错误而中止执行并退出，也有可能因为这个模块不能顺利地被初始化而返回 `NULL`。这个初始化函数必须给它的调用者返回一个模块对象，以便它能够被插入到 `sys.modules` 中去。

当嵌入到Python中去的时候，函数 `PyInit_spam()` 不会被自动调用，除非在 `PyImport_Inittab` 表中有这一项。为了在初始化表中添加这个模块（即把这个自定义的模块当做一个内置模块来对待），使用 [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab)，后面可以选择性地跟上一个导入模块语句：

```cpp
int
main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    if (PyImport_AppendInittab("spam", PyInit_spam) == -1) {
        fprintf(stderr, "Error: could not extend in-built modules table\n");
        exit(1);
    }

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required.
       If this step fails, it will be a fatal error. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyObject *pmodule = PyImport_ImportModule("spam");
    if (!pmodule) {
        PyErr_Print();
        fprintf(stderr, "Error: could not import module 'spam'\n");
    }

    ...

    PyMem_RawFree(program);
    return 0;
}
```

（这里可以看到，`PyImport_AppendInittab()` 函数是为了将我们自定义的模块Python的模块初始化表中去，而且要在调用 `Py_Initialize()` 之前执行），而导入模块并不一定要在此时完成，而是可以等到在Python脚本中需要导入该模块的时候再做。

注意，删除 `sys.modules` 中的某些项，或者在同一个进程中（或者还有后面跟上 `fork()` ，但没有函数 `exec()` 介入），把编译好的模块导入到多个Python解释器中，都会导致某些扩展模块产生问题。扩展模块的作者应该在初始化内部数据结构的时候谨慎行事。

一个更加实际的模块例子是 `Modules/xxmodule.c`，它包含在Python的源代码文件中，这个文件可以当做（创建模块的）模板，或者当做一个例子来阅读。

注意，和本文中 `spam` 例子不同的是，`xxmodule` 模块使用了*多步初始化*（Python 3.5中引入）。如果使用这个办法，那么本文例子中 `PyInit_spam()` 返回的就是一个 `PyModuleDef` 结构，并且模块的创建工作就会交给导入机制完成。关于多步初始化更详细的内容，参考 [**PEP 489**](https://peps.python.org/pep-0489/)。

### 1.5. Compilation and Linkage

在使用新的扩展模块之前，还有两件事情要做：编译，并且链接到Python系统上去。如果使用的是动态链接，那么（实现）细节就依赖于所使用的系统的动态链接方式；可以参考有关构建扩展模块的章节（[Building C and C++ Extensions](https://docs.python.org/3/extending/building.html#building)），以及只适用于在Windows平台上构建方法的更多细节。

如果不能使用动态链接，或者就想使扩展模块成为Python解释器永久的一部分，那么就需要改变设定，并且重新编译Python解释器。幸运的是，这在Unix平台上实现起来十分简单：只需要把（扩展模块）文件（比如本文中的 `spammodule.c`）放到Python源分发包的 `Modules/`目录中，然后在 `Modules/Setup.local` 加入如下一行来描述你的文件即可。

```python
spam spammodule.o
```

然后在最上层的目录中，使用 `make` 重新编译Python解释器。当然，也可以就只在 `Modules/` 这个字目录中直接执行 `make` 来编译，但是，之后就必须在这个目录中，通过执行 `make Makefile` 来重新构建 `Makefile`，而且这个步骤在每次修改完 `Setup` 文件之后必须执行。

如果你的扩展模块需要链接额外的库，那么就需要在配置文件中同样列出来，如下。

```python
spam spammodule.o -lX11
```


### 1.6. Calling Python Functions from C

直接目前，我们关注的是如何在Python中调用C的函数，反之，在C（函数中）调用Python代码，也同样有用。对于支持所谓的“回调”函数（callback function）的库中，作用更加突出。如果C的接口利用了回调，那么等价的Python代码通常也需要给Python编程者提供回调机制。这样的实现通常要求从C的回调函数中调用Python的回调函数。此外，（这种在C中调用Python代码的方法）在其他方面的用途也是可以想象的。

幸运的是，Python解释器可以容易地进行递归调用。首先，Python程序必须以某种方式把Python函数对象（Python function object）传入。通常你需要提供一个函数来做这件事情。当这个函数被调用的时候，在一个全局变量中存储一个指向这个Python函数对象的指针，或者在其他适当的非全局范围内存储。如下的函数，是某个模块定义的一部分。

```cpp
static PyObject *my_callback = NULL;

static PyObject *
my_set_callback(PyObject *dummy, PyObject *args)
{
    PyObject *result = NULL;
    PyObject *temp;

    if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
        if (!PyCallable_Check(temp)) {
            PyErr_SetString(PyExc_TypeError, "parameter must be callable");
            return NULL;
        }
        Py_XINCREF(temp);         /* Add a reference to new callback */
        Py_XDECREF(my_callback);  /* Dispose of previous callback */
        my_callback = temp;       /* Remember new callback */
        /* Boilerplate to return "None" */
        Py_INCREF(Py_None);
        result = Py_None;
    }
    return result;
}
```

这个函数必须通过Python解释器，使用 [`METH_VARARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_VARARGS "METH_VARARGS") 这个标记注册（1.4 The Module’s Method Table and Initialization Function 描述了这种办法）。函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 以及它的参数在下一节 [Extracting Parameters in Extension Functions](https://docs.python.org/3/extending/extending.html#parsetuple) 中讨论。

宏 [`Py_XINCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XINCREF) 和 [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF) 用来增加/减小一个对象的引用计数，并且可以使用在 `NULL` 指针上。更多讨论参考 [Reference Counts](https://docs.python.org/3/extending/extending.html#refcounts) 这一节。

之后，当需要调用这个函数的时候，可以通过调用C函数 [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject) 来实现。这个函数接受两个参数，都是指向专用的Python对象：一个是Python函数，另一个是对于的参数列表。这个参数列表必须总是一个元组对象（tuple object），它的长度就是参数的个数。如果要调用没有参数的Python函数，就传入一个 `NULL` 指针，或者一个空的元组对象；如果调用的函数只接受一个参数，那么就传入一个只有一个元素的元组对象。在函数 [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue) 中，使用带圆括号的格式化字符串，就可以返回一个对应的空的元组，或者有一个或多个元素的元组。例如：

```cpp
int arg;
PyObject *arglist;
PyObject *result;
...
arg = 123;
...
/* Time to call the callback */
arglist = Py_BuildValue("(i)", arg);
result = PyObject_CallObject(my_callback, arglist);
Py_DECREF(arglist);
```

函数 [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject) 返回一个指向Python对象的指针，这个返回值就是Python函数的返回值。[`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject) 并不增减传入它参数的引用计数。在上面的例子中，创建了一个新的元组，作为参数列表，然后在 函数 [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject) 调用之后，就立即使用  [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF) 来减少（这个元组对象的）引用计数。

函数 [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject) 的返回值是新的，它要么是一个全新的对象，要么是一个已经存在的对象，但对应的引用计数已经加一。所以，除非你想把它存储在一个全局变量中，否则你就应该使用  [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF) 来把它的引用计数减一，尤其是当你不再需要这个变量的时候。

然而，在做这件事情（减少引用计数）之前，检查返回值是否是 `NULL` 很重要。如果是（`NULL`），（就说明）所调用的Python函数通过抛异常而被中止了。如果调用 [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject) 函数的C代码是在Python中被调用的，那么就应该在此时给Python的调用者返回一个错误指示，这样Python解释器就能打印函数堆栈，或者调用这个Python函数的代码就能处理这个异常。如果这样的错误异常无关紧要，那么这个异常就需要调用 [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear) 来清理，比如：

```cpp
if (result == NULL)
    return NULL; /* Pass error back */
...use result...
Py_DECREF(result);
```

根据（在C中）想要调用的Python函数的接口信息，你可能还要给函数 [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject) 提供一个参数列表。在一些情况下，这个参数列表同样也是Python程序所提供的，即通过指定了回调函数的同样的接口。然后它就可以被保存起来，并以使用函数对象同样的方式来使用。在例外一些情况下，你可能需要构造一个新的元组来传递参数列表，最简单的办法是调用函数 [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue) 。比如，如果想传入一个整型的事件代码（integral event code），可以使用如下代码：

```cpp
PyObject *arglist;
...
arglist = Py_BuildValue("(l)", eventcode);
result = PyObject_CallObject(my_callback, arglist);
Py_DECREF(arglist);
if (result == NULL)
    return NULL; /* Pass error back */
/* Here maybe use the result */
Py_DECREF(result);
```

注意，在调用函数（[`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject)）之后，做错误检查之前，调用 `Py_DECREF(arglist)` 。同样也要注意到，这个代码（的检查）是不完整的，因为函数 [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue) 也可能会耗尽内存，而这同样需要检查。

同样，你也可以使用**关键字-值**的方式来调用一个函数，这就需要用到函数 [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call)，这个函数支持以**关键字-值**的方式传入参数列表。比如在前面的例子中，可以通过函数 [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue) 来构造一个字典。

```cpp
PyObject *dict;
...
dict = Py_BuildValue("{s:i}", "name", val);
result = PyObject_Call(my_callback, NULL, dict);
Py_DECREF(dict);
if (result == NULL)
    return NULL; /* Pass error back */
/* Here maybe use the result */
Py_DECREF(result);
```


### 1.7. Extracting Parameters in Extension Functions

 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple") 的函数原型如下：
 
```cpp
int PyArg_ParseTuple(PyObject *arg, const char *format, ...);
```

其中参数 `arg` 必须是一个元组对象，它包含的是从Python传递到C函数的参数列表；参数 `format` 必须是一个格式化的字符串，关于它的语法，可以参考Python/C API参考手册的 [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html#arg-parsing)；剩余的参数必须是和格式化字符串中对应类型的变量的地址。 

需要注意的是，尽管函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple") 检查从Python传入的参数是否是这里所要求类型，但它并不检查传入这个函数的C变量的地址是否合法。换句话说，如果在这里犯了错误，那么程序很可能崩溃或者在内存的随机地址上写入（非法的）值。所以要小心！

需要注意的另一点是，提供给调用者的Python对象的引用计数是*borrowed* reference，所以不需要将它们的引用计数减一。

下面是一些调用示例。

```cpp
#define PY_SSIZE_T_CLEAN  /* Make "s#" use Py_ssize_t rather than int. */
#include <Python.h>
```

```cpp
int ok;
int i, j;
long k, l;
const char *s;
Py_ssize_t size;

ok = PyArg_ParseTuple(args, ""); /* No arguments */
    /* Python call: f() */
```

```cpp
ok = PyArg_ParseTuple(args, "s", &s); /* A string */
    /* Possible Python call: f('whoops!') */
```

```cpp
ok = PyArg_ParseTuple(args, "lls", &k, &l, &s); /* Two longs and a string */
    /* Possible Python call: f(1, 2, 'three') */
```

```cpp
ok = PyArg_ParseTuple(args, "(ii)s#", &i, &j, &s, &size);
    /* A pair of ints and a string, whose size is also returned */
    /* Possible Python call: f((1, 2), 'three') */
```

```cpp
{
    const char *file;
    const char *mode = "r";
    int bufsize = 0;
    ok = PyArg_ParseTuple(args, "s|si", &file, &mode, &bufsize);
    /* A string, and optionally another string and an integer */
    /* Possible Python calls:
       f('spam')
       f('spam', 'w')
       f('spam', 'wb', 100000) */
}
```

```cpp
{
    int left, top, right, bottom, h, v;
    ok = PyArg_ParseTuple(args, "((ii)(ii))(ii)",
             &left, &top, &right, &bottom, &h, &v);
    /* A rectangle and a point */
    /* Possible Python call:
       f(((0, 0), (400, 300)), (10, 10)) */
}
```

```cpp
{
    Py_complex c;
    ok = PyArg_ParseTuple(args, "D:myfunction", &c);
    /* a complex, also providing a function name for errors */
    /* Possible Python call: myfunction(1+2j) */
}
```


### 1.8. Keyword Parameters for Extension Functions

[`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) 的函数原型如下：

```cpp
int PyArg_ParseTupleAndKeywords(PyObject *arg, PyObject *kwdict,
                                const char *format, char *kwlist[], ...);
```

参数 `arg` 和 `format` 和函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 中的含义相同。`kwdict` 参数是一个关键字的字典（dictionary of keywords），它作为Python运行时候的第三个参数传入。`kwlist` 参数是一个字符串列表，它的最后一个字符串必须是 `NULL`，这个字符串列表用来标识各个参数，而且名字和类型信息是按照 `format` 字符串中的格式，从左向右依次对应。如果解析参数成功，函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 返回 `true`，如果失败，就返回 `false`，并且会抛出一个对应的异常。

注意，但使用关键字参数（keyword argument）的时候，嵌套的元组不能被解析；传入的关键字实参如果在 `kwlist` 中不存在，就会抛出一个 `TypeError` 的异常。

下面的模块例子中，使用了关键字。该例子的作者是Geoff Philbrick。

```cpp

#define PY_SSIZE_T_CLEAN  /* Make "s#" use Py_ssize_t rather than int. */
#include <Python.h>

static PyObject *
keywdarg_parrot(PyObject *self, PyObject *args, PyObject *keywds)
{
    int voltage;
    const char *state = "a stiff";
    const char *action = "voom";
    const char *type = "Norwegian Blue";

    static char *kwlist[] = {"voltage", "state", "action", "type", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, keywds, "i|sss", kwlist,
                                     &voltage, &state, &action, &type))
        return NULL;

    printf("-- This parrot wouldn't %s if you put %i Volts through it.\n",
           action, voltage);
    printf("-- Lovely plumage, the %s -- It's %s!\n", type, state);

    Py_RETURN_NONE;
}

static PyMethodDef keywdarg_methods[] = {
    /* The cast of the function is necessary since PyCFunction values
     * only take two PyObject* parameters, and keywdarg_parrot() takes
     * three.
     */
    {"parrot", (PyCFunction)(void(*)(void))keywdarg_parrot, METH_VARARGS | METH_KEYWORDS,
     "Print a lovely skit to standard output."},
    {NULL, NULL, 0, NULL}   /* sentinel */
};

static struct PyModuleDef keywdargmodule = {
    PyModuleDef_HEAD_INIT,
    "keywdarg",
    NULL,
    -1,
    keywdarg_methods
};

PyMODINIT_FUNC
PyInit_keywdarg(void)
{
    return PyModule_Create(&keywdargmodule);
}
```


### 1.9. Building Arbitrary Values

这个函数（`Py_BuildValue`）和函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 是相对应的关系，它的声明是：

```cpp
PyObject *Py_BuildValue(const char *format, ...);
```

和函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 类似，它识别相同的一系列格式化的单元，但这个函数的参数必须不能是指针，而必须是值。这里的不能是指针的参数指的是作为函数输入的变量，就是 `const char *format` 后面的那些值，而 `format` 本身就是输出结果，可以是指针。这个函数返回一个新的Python对象，适合从Python中调用一个C函数作为返回。

和函数  [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 不同的一点是，函数  [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 的第一个参数（`PyObject *args`）必须是一个元组，因为Python的参数列表总是特意以元组的方式来表示，而函数 [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue) 就不总是构建一个元组。只有当它的字符串包含两个或更多的格式单元时，它才构造为一个元组。如果格式化字符串是空的，那么它就返回 `None`；如果它只包含一个格式化单元，那么它返回的就是那个格式化单元对应的对象的类型。当元组的格式为0或1时，为了特意返回一个元组，就需要给格式化字符串加上圆括号。

下面是一些例子，左侧是函数调用，右侧是返回的Python结果。

```cpp
Py_BuildValue("")                        // None
Py_BuildValue("i", 123)                  // 123
Py_BuildValue("iii", 123, 456, 789)      // (123, 456, 789)
Py_BuildValue("s", "hello")              // 'hello'
Py_BuildValue("y", "hello")              // b'hello'
Py_BuildValue("ss", "hello", "world")    // ('hello', 'world')
Py_BuildValue("s#", "hello", 4)          // 'hell'
Py_BuildValue("y#", "hello", 4)          // b'hell'
Py_BuildValue("()")                      // ()
Py_BuildValue("(i)", 123)                // (123,)
Py_BuildValue("(ii)", 123, 456)          // (123, 456)
Py_BuildValue("(i,i)", 123, 456)         // (123, 456)
Py_BuildValue("[i,i]", 123, 456)         // [123, 456]
Py_BuildValue("{s:i,s:i}",
              "abc", 123, "def", 456)    // {'abc': 123, 'def': 456}
Py_BuildValue("((ii)(ii)) (ii)",
              1, 2, 3, 4, 5, 6)          // (((1, 2), (3, 4)), (5, 6))
```


### 1.10. Reference Counts

在像C和C++这样的程序设计语言中，编程者自己需要负责堆上内存的动态分配和释放。在C语言中，使用函数 `malloc()` 和 `free()` 完成这一工作。在C++中，使用运算符 `new` 和 `delete` 来做本质上相同的事情。下面的讨论基于C语言。

由函数 `malloc()` 函数分配的每一块内存，最终都应该使用一次而且仅有一次的函数 `free()`，将所分配的内存归还给内存池中。在合适的时机调用 `free()` 很关键。如果一块内存的地址被遗忘了，而且`free()` 函数没有用来释放这个地址对应的内存，那么这块内存在整个程序结束之前，都会被占用而且不能再次利用。这就是所谓的**内存泄露**（*memory leak*）。另一方面，如果对一块内存已经调用了函数 `free()` 来释放内存，但之后仍然使用这块内存，那么当另一个 `malloc()` 被调用并使用这块相同地址的内存时，就会产生冲突。这就是**非法内存访问**（*using freed memory*）。和引用没有被初始化的数据一样，这也会产生一些严重的后果，比如内存转储（core dump），错误的结果（wrong results），以及莫名其妙的崩溃（mysterious crashes）。

造成内存泄露的原因，通常是代码中不同寻常的调用路径。比如，一个函数分配了一块内存，做了一些计算，然后释放了这块内存。现在有要求要做些变动，函数要在做计算时加入测试，当检测到有错误的条件时，就从函数当中提前返回。所以在提前返回的过程当中，很容易忘记释放之前所分配的内存，尤其是这部分代码是后来才加入的。这样的泄露，一旦引入，在很长时间里都很难被发觉：这个错误的返回只发生在所有调用中的一小个片段中，而且现代的机器硬件又拥有充足的虚拟内存，所以，只有当这个函数被长时间地经过频繁调用之后，这个泄露情况才会显现出来。因此，为了防止发生这样的泄露，采样减少这种错误的代码传统或策略，就很重要。

因为Python重度使用函数 `malloc()` 和 `free()`，它就需要采用一种策略，避免内存泄露和非法内存访问。这个被选中的策略叫做***引用计数***（*reference counting*）。原则很简单，每个对象包含一个计数器，当在其他地方存储了一个对这个对象的引用时，就将其加一，当对它的一个引用被删除的时候，就减一。当这个计数器变成0时，（就说明）最后一个对这个对象的引用被删掉了，这个对象（占用的内存）就应该被释放了。

另一种策略叫做***自动垃圾回收***（*automatic garbage collection*）（有时候，引用计数也被当做是一种垃圾回收策略，因此这里使用了**自动** automatic 一词来加以区别）自动垃圾回收机制最大的优点是，不需要使用者显式地调用 `free()` 函数了。（另一个声称的优点是对性能和内存的提示，但这没有确凿的事实证据）缺点是，在C中，没有一个真正意义上的可移植的自动垃圾回收器，然而引用计数却能够实现为可移植的（只要函数 `malloc()` 和 `free()`可以使用，实际上C标准保证了这一点）也许有一天，C语言会有一个有效率的、可移植的自动垃圾回收器。但在那之前，我们就需要使用引用计数。

尽管Python使用的是传统的引用计数的实现，它提供了一共循环引用检测器，用来检查循环引用。这就使得应用程序可以不用担心创建出来有向或无向的循环引用，而这些是只使用引用计数的垃圾回收机制的缺陷。循环引用的对象，直接或间接包含了指向它们直接的引用，那么这就造成循环引用中的每个对象的引用计数总也不为0。典型的引用计数的实现是无法回收循环引用中的对象的内存，或者无法回收被循环引用中的对象所引用的对象的内存（哪怕没有进一步引用这个循环）。

这种循环检测器能够检查垃圾循环，并且回收它们所占用的对象的内存。 [`gc`](https://docs.python.org/3/library/gc.html#module-gc) 模块提供了可以运行检测器的方法（即函数 [`collect()`](https://docs.python.org/3/library/gc.html#gc.collect)），以及进行接口配置、在运行期间关闭循环检查的方法。


#### 1.10.1. Reference Counting in Python

`Py_INCREF(x)` 和 `Py_DECREF(x)` 这两个宏，是分别用来处理引用计数的增减。如果引用计数减为0，宏 [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF) 还用来释放对应对象所占用的内存。为了灵活起见，它不直接调用 `free()` 函数，相反，它调用的是这个对象所包含的一个类型对象（*type object*）中的一个函数指针。因为这个缘故（还有其他），每个对象都包含一个它的类型对象的指针。

现在就有一个重要的问题：什么时候调用 `Py_INCREF(x)` 和 `Py_DECREF(x)`？我们首先介绍一些术语。没有人“拥有”一个对象（Nobody “owns” an object），然后你可以拥有一个指向对象的引用（reference to an object）。因此一个对象的引用计数，就是指向它的引用的个数。一个引用的拥有者（owner），在这个引用不再需要的时候，就负责调用宏 [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF) 。引用的拥有权可以被转移，有三种方式释放引用的所有权，它们分别是：传递，存储，以及调用宏 [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF)。忘记释放一个被拥有的引用（*owned reference*），就可能造成内存泄露。

也可以**借用**（*borrow*）【2】一个指向对象的引用，借用这个引用的借用者，就不应该调用宏  [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF)。这个借用者“借用”这个对象的时间不应该超过这个对象引用拥有者（的生命周期）。当引用的拥有者释放了该引用（所对应的内存）之后，继续使用**借用引用**（*borrowed reference*），就会产生非法访问内存（using freed memory）的风险，而这是应该完全避免的【3】。

和拥有一个引用相比，使用借用引用的优点是，不用关心在任何的代码路径（*code path*）上何时释放这个引用（对应的内存）。换句话说，使用一个借用引用（*borrowed reference*），在可能的提前退出的时候，就不用承担内存泄露的风险。另一方面，缺点是，在一些微妙的情况下，一些看起正确的代码，有可能在引用的拥有者已经释放了它的情况下，仍然使用这个借用来的引用。

一个借用引用，可以通过调用 [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF) 转换为一个拥有引用（*owned reference*），这并不会影响被借用者（引用拥有者）的状态，因为它创建了一个新的引用，并且赋予了拥有者的责任。和之前的拥有者一样，新的拥有者必须合理地释放所拥有的引用（所占用的内存）。

#### 1.10.2. Ownership Rules

当一个对象引用传入或传出一个函数的时候，它的所有权是否被转移，是这个函数接口说明的一部分。大多数返回一个对象引用的函数，都会传递（转移）这个引用的所有权。特别地，所有用来创建一个新的对象的函数，都会把（引用的）所有权转移给（函数返回值的）接收者，比如函数 [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong) 和 [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue)。甚至当这个对象实际上不是新创建的时候，接受的仍然是对这个对象的一个新的引用。比如，函数 [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong)，它维护了一些常用的值的缓存（cache），并且能够返回一个指向其中一个缓存项的引用。

从另一些对象中抽取（*extract*）一些对象的函数，通常都会转移引用的所有权，比如函数 [`PyObject_GetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttrString)。然而，这里有一些模糊的场景，因为有一些常见的函数是例外，比如: [`PyTuple_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetItem)， [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem)， [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem) 和 [`PyDict_GetItemString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemString) 它们返回的都是从元组，列表，或者字典中借用的引用（*borrowed reference*）。

即，返回的是borrowed reference的抽取函数是：

- `PyTuple_GetItem()`
- `PyList_GetItem()`
- `PyDict_GetItem()`
- `PyDict_GetItemString()`

除此之外，大多数抽取函数返回了对象，也转移了对象引用的所有权（*owned reference*）。

函数  [`PyImport_AddModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModule) 返回的也是一个借用引用（*borrowed reference*），甚至有时候它可能创建一个对象，然后返回，（但不需要担心），因为它会把需要返回的对象的owned reference存储在 `sys.modules` 下面。

当你把一个对象引用传递给另一个函数的时候，一般来说，函数使用的是借用引用（*borrowed reference*），如果它需要存储这个引用，它就会使用宏 [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF) 来变成这个引用的（另一个）单独的拥有者。但这条规则，有两个重要的例外：[`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem) 和 [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem) 函数。这两个函数会接管传入的对象的所有权，甚至当函数执行失败的时候也是（接管所有权）。注意，函数 [`PyDict_SetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItem) 和类似的函数并不接管对象的所有权，它们就是使用一般的借用引用。

在Python中调用一个C函数的时候，它借用了调用者的参数的引用，即borrowed reference。调用者拥有一个指向对象的引用，所以借用引用的生命周期会在函数返回的同时终止。只有当这样的borrowed reference需要被存储或传递下去的时候，它才需要通过调用宏 [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF) 将其转变为一个owned reference来获得这个对象引用的所有权。

在Python中调用的一个C函数的返回对象引用，必须是一个owned reference，即具有拥有权的对象引用，这就是说，所有权从这个函数转移到了它的调用者上。

#### 1.10.3. Thin Ice

有一些看起来对borrowed reference正常无害的使用，可能会导致一些问题。这些都是和Python解释器的一些隐式的调用有关，而这会导致引用的所有者释放它。

第一个需要知道的案例，并且也是最重要的一个，就是当借用一个list类型对象的引用的时候，对一个不相关的对象使用宏 [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF)。比如，

```cpp
void
bug(PyObject *list)
{
    PyObject *item = PyList_GetItem(list, 0);

    PyList_SetItem(list, 1, PyLong_FromLong(0L));
    PyObject_Print(item, stdout, 0); /* BUG! */
}
```

首先这个函数借用了`list[0]`的一个引用，然后使用`0`替换了`list[1]`对应的值，最后打印了那个borrowed reference。看起来没有对吧？然而事实上并不是！

我们来跟踪函数 [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem) 中的控制流。列表对其中每一项的引用都是owned reference，因此当第一项（即第二个元素）被替换时，它就要释放原先的第一项。我们假设原先的第一项元素是一个用户自定义的类，并且我们进一步假设这个类有一个 `__del__()` 方法。如果这个类的实例对象有一个引用计数是1，那么释放它的时候就会调用它的 `__del__()` 方法。

因为它是在Python中定义编写的，所以 `__del__()` 方法执行的是纯粹的Python代码。那么有没有可能它会做一些事情，使得函数 `bug()` 中对 `item` 的引用失效？答案是肯定的。假设传入这里这个函数 `bug()` 的参数 `list` 可以访问 `__del__()` 方法，那么它就有可能执行到可能造成`list[0]`被释放的语句，比如 `del list[0]`，又假设引用计数在该语句之前是1，那么在执行这个语句之后，它对应的内存会被释放，从而导致 `item` 这个对象不再合法（invalid）。

一旦你知道了问题的来龙去脉，那么解决方案也很简单：临时增加引用计数。下面是这个函数的正确版本：

```cpp
void
no_bug(PyObject *list)
{
    PyObject *item = PyList_GetItem(list, 0);

    Py_INCREF(item);
    PyList_SetItem(list, 1, PyLong_FromLong(0L));
    PyObject_Print(item, stdout, 0);
    Py_DECREF(item);
}
```

这是一个真实的（悲伤的）故事，一个旧版本的Python中存在这样类型bug的一个变种，并且有人花了想当可观的时间使用C调试器调试，试图找到为什么它的 `__del__()` 方法会失效...

第二个和borrowed reference相关的案例，是和线程有关一个变种（代码缺陷）。正常情况下，Python解释器中的不同线程不会户型干扰，因为有一个全局锁来保护Python的整个对象空间。然而，使用宏 [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3/c-api/init.html#c.Py_BEGIN_ALLOW_THREADS) 能暂时释放这个线程锁，而使用宏 [`Py_END_ALLOW_THREADS`](https://docs.python.org/3/c-api/init.html#c.Py_END_ALLOW_THREADS) 又能够重新加锁。这在阻塞I/O调用的时候很常见，目的是为了让其他线程使用处理器，并且等等I/O完成。下面的这个例子，显然就有和上面的一个例子相同的问题。

```cpp
void
bug(PyObject *list)
{
    PyObject *item = PyList_GetItem(list, 0);
    Py_BEGIN_ALLOW_THREADS
    ...some blocking I/O call...
    Py_END_ALLOW_THREADS
    PyObject_Print(item, stdout, 0); /* BUG! */
}
```

#### 1.10.4. Writing Extensions in C++

一般而言，接收对象引用作为参数的函数，一般不希望你传递给它们 `NULL` 空指针，如果这么做了，就会导致core dump（或者之后产生core dump）。也是一般情况下，如果一个返回对象引用的函数返回了 `NULL`，它指示用来表示有异常产生。之所以不检查参数是否为 `NULL`，原因是函数接收到对象之后往往会继续将其传递给其他函数。如果每个函数都检查参数是否为 `NULL`，那将产生很多冗余的代码，并且代码会运行的更慢。

所以，最后是在“源头”检查（参数释放为 `NULL`），这个源头就是有可能接收到一个空指针 `NULL` 的地方，比如，接收到 `malloc()` 返回值，或接收到一个函数的对象，但这个函数可能会抛异常。

宏 [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF) 和 [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF) 不检查空指针 `NULL` ，但它们的两个变种会检查：[`Py_XINCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XINCREF) and [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF)。

用来检查对象特定类型的宏 `Pytype_Check()` 不检查空指针 `NULL`，同样是因为，太多的代码在同一行里面调用它，用来检查不同的所预期的类型，而这样就产生了很多的冗余。这个宏没有对应的检查空指针 `NULL` 的变种宏。

C函数的调用机制，保证了传递到C函数中的参数列表（比如例子中的 `args`），永远不会是空指针 `NULL`，实际上它保证了这个参数永远是一个元组（tuple）【4】。

任何时候，如果让一个空指针 `NULL` “逃逸”到了Python使用者那里，将是一个严重的错误。


### 1.11. Writing Extensions in C++

在C++中也能编写Python扩展程序，但有一些限制。如果主程序（Python解释器）是通过C编译器编译并链接的，那么有构造函数的全局变量或静态变量对象，将不能使用。但如果主程序是通过C++编译器链接的，那这就不是问题了。被Python解释器调用的函数（特别是模块初始化函数），需要被声明为 `extern "C"`。在 `extern "C" {...}` 中不需要包含Python头文件，原因是，如果 `__cplusplus` 标识有定义了的话，它们（这些Python头文件）就已经使用了这种格式。对于现代C++编译器来说，都有定义这样的标识。

### 1.12. Providing a C API for an Extension Module

许多扩展模块提供的新函数和新类型，目的都是用于Python中的，但有时候，一个扩展模块中的代码对其他一些模块来说，也是有用的。比如，一个扩展模块实现了一个类似列表（`list`）的新类型 `collection`，但是其中的元素是无序的。就像标准Python库中的列表类型（`list` type）一样，给扩展模块提供了C API用来创建和操作列表，这种新的 `collection` 类型，也应该提供一系列的C函数，以便其他扩展模块直接操作它。

乍一看这很简单：只需要写一些函数（当然不能声明为 `static`），提供一个合适的头文件，并且记录好C的API文档。实际上，如果所有的扩展模块，一直都是和Python解释器静态链接到一起的花，这样确实可以正常工作。但是，如果模块使用了动态链接，一个模块中的标识，在另一个模块中也许就不可见了。这种可见性依赖于操作系统，有些系统（比如Windows）对Python解释器和所有的模块，都使用了同一个全局的命名空间（namespace），然而有些其他的系统（比如AIX），要求在模块链接的阶段，提供一个显示的需要导入的标识符列表（an explicit list of imported symbols），再或者在其他一些系统上（比如大多数的Unix系统，复数Unices），提供了不同策略的选项。甚至如果一个标识符是全局可见的，需要调用的函数所在的那个模块，甚至都还没有被加载进来！

因此，可移植性不能对标识符的可见性做任何的前提假设。这意味着扩展模块中所有的标识符都应该声明为 `static`，除了那些模块初始化函数，这样是为了避免和其他模块中函数的名字发生冲突。同时，这也意味着，应该能被其他扩展模块访问到的标识符，都必须使用不同的办法导出（exported in a different way）。

Python提供了一种特殊的机制，用来把C-level的信息（即指针）从一个扩展模块传递到另一个扩展模块，这种机制叫做Capsule。Capsule是一种包含了指针（`void*`）的Python数据类型。Capsule只能通过对应的C API来创建和访问，但它们同时也可以想其他Python对象一样，相互传递。特别地，可以在一个扩展模块的namespace中，赋予它一个名字。其他的扩展模块可以导入这个模块，获取这个名字，然后再从Capsule里面获取对应的指针。

有许多办法来使用Capsule，用它将一个扩展模块中的C API导出（export）。每个函数都能够获取它自己的Capsule，或者所有的C API的指针都可以存储在一个指针数组中，然后有一个Capsule来包含它。在不同的扩展模块之间，可以以提供代码和客户模块（client module）的方式，用不同的方法，完成各种存储和获取指针任务的分发。

不管你选择了哪种办法，最重要的是合理地命名你的Capsule。函数 [`PyCapsule_New()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_New) 接收一个名字（`const char*`）作为参数，虽然它也允许传入一个 `NULL` 指针，但最好还是指定一个（正常的）名字。取名合理的Capsule提供了一种运行期间类型安全的程度（degree？）。没有办法区分两个没有名字的Capsule。

特别地，用来导出C API的Capsule，应该以下面这种方式命名：

```cpp
modulename.attributename
```

便捷函数 [`PyCapsule_Import()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Import) 能够方便地加载一个Capsule包含的C API，但这种加载方式加载的C API的Capsule必须以这种方式进行命名。这种方式可以很大程度上给予C API的使用者以确认，保证他们加载的是正确的C API。

下面的例子展示了一种办法，这种办法将大部分繁重的任务留给了需要导出模块的作者，这也是常用库模块导出的合理办法。它把所有的C API的指针（本例中只有一个）存储到了一个 `void*` 指针数组中，而这个数组就成为了Capsule的值。这个模块的头文件提供了一个宏，它负责导入模块并获取它的C API的指针。客户模块（client module）只需要在访问C API之前调用这个宏即可。

下面要导出的模块是 [A Simple Example](https://docs.python.org/3/extending/extending.html#extending-simpleexample) 这一节中 `spam` 模块的一个修改版本。函数 `spam.system()` 没有直接调用C的库函数 `system()`，相反它调用了一个叫做 `PySpam_System()` 的函数，当然，这个函数在实际应用中肯定要做更复杂的事情。这个叫做 `PySpam_System()` 的函数也会被导出到其他各个扩展模块中。

`PySpam_System()` 函数是一个普通的C函数，和其他函数一样，被声明为 `static`：

```cpp
static int
PySpam_System(const char *command)
{
    return system(command);
}
```

函数 `spam_system()` 只有轻微的改动：

```cpp
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = PySpam_System(command);
    return PyLong_FromLong(sts);
}
```

下面的语句是模块文件的第一行：

```cpp
#include <Python.h>
```

在第一行后面，必须加入下面两行：

```cpp
#define SPAM_MODULE
#include "spammodule.h"
```

这里的 `#define` 预编译指令，是用来告诉头文件，它是包含于正在被导出的模块（exporting module）中，而不是客户模块（client module）。最后，模块的初始化函数必须负责完成对C API指针数组的初始化工作：

```cpp
PyMODINIT_FUNC
PyInit_spam(void)
{
    PyObject *m;
    static void *PySpam_API[PySpam_API_pointers];
    PyObject *c_api_object;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    /* Initialize the C API pointer array */
    PySpam_API[PySpam_System_NUM] = (void *)PySpam_System;

    /* Create a Capsule containing the API pointer array's address */
    c_api_object = PyCapsule_New((void *)PySpam_API, "spam._C_API", NULL);

    if (PyModule_AddObject(m, "_C_API", c_api_object) < 0) {
        Py_XDECREF(c_api_object);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
```

注意，这里的C API指针数组的声明带有静态标识 `static`，如果不带 `static`，那么当函数 `PyInit_spam()` 结束的时候，这个指针数组就会消失（因为到了生命周期的结束的时候）。

下面就是头文件 `spammodule.h` 中代码的样子：

```cpp
#ifndef Py_SPAMMODULE_H
#define Py_SPAMMODULE_H
#ifdef __cplusplus
extern "C" {
#endif

/* Header file for spammodule */

/* C API functions */
#define PySpam_System_NUM 0
#define PySpam_System_RETURN int
#define PySpam_System_PROTO (const char *command)

/* Total number of C API pointers */
#define PySpam_API_pointers 1

#ifdef SPAM_MODULE
/* This section is used when compiling spammodule.c */

static PySpam_System_RETURN PySpam_System PySpam_System_PROTO;

#else
/* This section is used in modules that use spammodule's API */

static void **PySpam_API;

#define PySpam_System \
 (*(PySpam_System_RETURN (*)PySpam_System_PROTO) PySpam_API[PySpam_System_NUM])

/* Return -1 on error, 0 on success.
 * PyCapsule_Import will set an exception if there's an error.
 */
static int
import_spam(void)
{
    PySpam_API = (void **)PyCapsule_Import("spam._C_API", 0);
    return (PySpam_API != NULL) ? 0 : -1;
}

#endif

#ifdef __cplusplus
}
#endif

#endif /* !defined(Py_SPAMMODULE_H) */
```

一个客户模块（client module），为了访问函数 `PySpam_System()`，它所需要做的全部工作，就仅仅是在它直接的初始化函数中，调用函数（甚至是宏） `import_spam()`。

```cpp
PyMODINIT_FUNC
PyInit_client(void)
{
    PyObject *m;

    m = PyModule_Create(&clientmodule);
    if (m == NULL)
        return NULL;
    if (import_spam() < 0)
        return NULL;
    /* additional initialization can happen here */
    return m;
}
```

这种办法的主要缺点是，文件 `spammodule.h` 会相对复杂。但是，对每一个需要导出的函数来说，基本的结构是一样的，所以这样的情况只需要学习一次即可。

最后，需要提及的是，Capsule提供了额外的一些功能，这些功能对保存在一个Capsule中的指针的内存分配和释放，尤其有用。在Python/C API 参考手册的 [Capsules](https://docs.python.org/3/c-api/capsule.html#capsules) 这一节对这部分内容做了详细描述，同时也可以参数Capsule的代码实现：代码文件位于Python 分发包的 `Include/pycapsule.h` 和 `Objects/pycapsule.c` 中。

### 1.13 Footnotes

【1】 An interface for this function already exists in the standard module [`os`](https://docs.python.org/3/library/os.html#module-os) — it was chosen as a simple and straightforward example.

【2】The metaphor of “borrowing” a reference is not completely correct: the owner still has a copy of the reference.

【3】Checking that the reference count is at least 1 **does not work** — the reference count itself could be in freed memory and may thus be reused for another object!

【4】These guarantees don’t hold when you use the “old” style calling convention — this is still found in much existing code.


## 2. Defining Extension Types: Tutorial

Python 允许C扩展的书写者定义新的类型（class类），就像built-in的`str` 和 `list` 类型一样，这个新类型也能在Python代码中对其进行操作。书写这些新类型有既定的模式步骤，本文主要介绍这个话题。

### 2.1. The Basics

CPython把所有的Python object都当成是 `PyObject*`，它是所有Python object的“基本类型”。这个 `PyObject` 类型，只包含这个对象的引用计数（reference count），以及一个指向这个object对应的类型的类型对象（type object）。这就是行为所在：这个类型对象（type object）决定了Python解释器会调用对应的哪些函数，比如，当查找一个object上的attribute或method的时候，或和其他类型的object相乘。这些C函数叫做类型方法（“type method”）。

因此，如果要定义一个新的类型，就要创建一个新的类型对象。

使用例子来解释会更能说明问题，本文就讨论了一个最小限度但确实完全的例子，定义了一个模块，定义了一个新的类型叫做 `Custom`，它位于C扩展`custom`中。

```cpp
#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef struct {
    PyObject_HEAD
    /* Type-specific fields go here. */
} CustomObject;

static PyTypeObject CustomType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "custom.Custom",
    .tp_doc = PyDoc_STR("Custom objects"),
    .tp_basicsize = sizeof(CustomObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew,
};

static PyModuleDef custommodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "custom",
    .m_doc = "Example module that creates an extension type.",
    .m_size = -1,
};

PyMODINIT_FUNC
PyInit_custom(void)
{
    PyObject *m;
    if (PyType_Ready(&CustomType) < 0)
        return NULL;

    m = PyModule_Create(&custommodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&CustomType);
    if (PyModule_AddObject(m, "Custom", (PyObject *) &CustomType) < 0) {
        Py_DECREF(&CustomType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
```

上面的例子中，定义了三件事：

- 一个`Custom`对象包含了什么：它是一个`CustomObject`的结构，每当一个`Custom`实例创建的时候，这个数据结构就会创建。
- `Custom`类型如何运作：它是`CustomType`结构，它定义了一些flag和函数指针，当触发一些特定的操作时，解释器会检查它们，并在其中查找。
- 如何初始化 `custom` 这个模块：定义 `custommodule` 结构，并使用 `PyInit_custom` 函数。


1. 首先定义了 `CustomObject` 类型，

   ```cpp
   typedef struct {
       PyObject_HEAD
   } CustomObject;
   ```

   每个 `Custom` 类型的对象，都会包含它。`PyObject_HEAD` 是必须包含进来的宏，它出现在每个类型对象结构的开始，并且定义了一个 `PyObject` 类型的对象 `ob_base`，它包含一个指向类型对象的指针（可用 `Py_TYPE` 宏访问），以及一个引用计数器（可用 `Py_REFCNT` 宏访问）。使用这个宏的原因是，进行结构布局的抽象，以及在编译debug版本时，添加额外的数据（field）。

   注意：`PyObject_HEAD` 后面没有分号（`;`），如果添加了，有些编译器可能会报错。

   当然这里是为了说明而举的例子，而通常都会保护一些数据，比如Python中标准浮点型的定义是：

   ```cpp
   typedef struct {
       PyObject_HEAD
       double ob_fval;
   } PyFloatObject;
   ```

2. 其次，对于这个新的类型，定义一个对应它的 `PyTypeObject` 对象，

   ```cpp
   static PyTypeObject CustomType = {
       PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT,
       .tp_new = PyType_GenericNew,
   };
   ```

   这里推荐使用C99形式的初始化定义方法，这样，这个`PyTypeObject`对象中其他不关心的数据的初始化，就可以交给编译器赋予其默认值。

   ```cpp
   PyVarObject_HEAD_INIT(NULL, 0)
   ```

   这个语句是初始化前面提到的 `ob_base` 。

   ```cpp
   .tp_name = "custom.Custom",
   ```

   这句是用来指明这个新类型的字符串名称，比如它可以出现在打印错误信息当中。注意点号 `.` 之前是模块的名称，点号 `.` 后面是这个新类型的名称。

   ```cpp
   .tp_basicsize = sizeof(CustomObject),
   ```

   这句是在创建 `Custome` 这个类型的实例时，指明需要分配多少内存空间。

   ```cpp
   .tp_itemsize = 0,
   ```

   当这个值是非 `0` 时，一般用于变长大小的对象。如果不是变长对象，那么就应该是 `0` 。

   需要注意的是，如果定义的这个类型要在Python中被其他类型所继承，那么它对应的这 `.tp_basicsize` 需要更大一些，否则会发生错误。

   ```cpp
   .tp_flags = Py_TPFLAGS_DEFAULT,
   ```

   一般情况下，所有类型的`.tp_flags` 中都需要包含 `Py_TPFLAGS_DEFAULT` ，它包含了截至Python 3.3时所有的成员（flag），如果需要其他额外的flag，就需要或起来（`|`）。

   ```cpp
   .tp_doc = PyDoc_STR("Custom objects"),
   ```

   这句就是定义这个类型的 doc string。

   ```cpp
   .tp_new = PyType_GenericNew,
   ```

   这句指明了Python类型的 `__new__` 方法，而且它必须被显式地指明。这里使用了默认的API函数 `PyType_GenericNew`。

   ```cpp
   if (PyType_Ready(&CustomType) < 0)
       return;
   ```

   这句用来初始化 `Custom` 这个新类型，赋予一些成员默认的值，包括把 `ob_type` 赋值为 `NULL` 。

   ```cpp
   Py_INCREF(&CustomType);
   if (PyModule_AddObject(m, "Custom", (PyObject *) &CustomType) < 0) {
       Py_DECREF(&CustomType);
       Py_DECREF(m);
       return NULL;
   }
   ```

   这句是把 `Custom` 这个类型加入到模块字典中去（module dictionary），这样，就可以使用类似如下语句创建 `Custom` 类型的对象了，

   ```python
   import custom
   mycustom = custom.Custom()
   ```

   差不多需要的就这些了，把上面这些代码放到一个 `custom.c` 的文件中，然后创建一个 `setup.py` 的文件，内容如下，

   ```python
   from distutils.core import setup, Extension
   setup(name="custom", version="1.0",
         ext_modules=[Extension("custom", ["custom.c"])])
   ```

   然后编译，

   ```shell
   python setup.py build
   ```

   这样在一个子目录中，会生成一个 `custom.so` 的动态库，在那个子目录中启动Python，就可以使用 `import custom`，然后创建 `Custom` 的对象了。

   注意，这里为了举例说明，使用了较陈旧的 `distutils` 来编译Python的C扩展，实际当中，应该使用新的 `setuptools` 库，参考网页查看说明：[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)




### 2.2. Adding data and methods to the Basic example

在上一节（2.1）的基础上，这一节，引入新的模块 `custom2`，在其中，我们给原先的例子里添加一些数据和方法，并使得它可以被继承。

```cpp
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

typedef struct {
    PyObject_HEAD
    PyObject *first; /* first name */
    PyObject *last;  /* last name */
    int number;
} CustomObject;

static void
Custom_dealloc(CustomObject *self)
{
    Py_XDECREF(self->first);
    Py_XDECREF(self->last);
    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    CustomObject *self;
    self = (CustomObject *) type->tp_alloc(type, 0);
    if (self != NULL) {
        self->first = PyUnicode_FromString("");
        if (self->first == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->last = PyUnicode_FromString("");
        if (self->last == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->number = 0;
    }
    return (PyObject *) self;
}

static int
Custom_init(CustomObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"first", "last", "number", NULL};
    PyObject *first = NULL, *last = NULL, *tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_XDECREF(tmp);
    }
    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_XDECREF(tmp);
    }
    return 0;
}

static PyMemberDef Custom_members[] = {
    {"first", T_OBJECT_EX, offsetof(CustomObject, first), 0,
     "first name"},
    {"last", T_OBJECT_EX, offsetof(CustomObject, last), 0,
     "last name"},
    {"number", T_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /* Sentinel */
};

static PyObject *
Custom_name(CustomObject *self, PyObject *Py_UNUSED(ignored))
{
    if (self->first == NULL) {
        PyErr_SetString(PyExc_AttributeError, "first");
        return NULL;
    }
    if (self->last == NULL) {
        PyErr_SetString(PyExc_AttributeError, "last");
        return NULL;
    }
    return PyUnicode_FromFormat("%S %S", self->first, self->last);
}

static PyMethodDef Custom_methods[] = {
    {"name", (PyCFunction) Custom_name, METH_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject CustomType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "custom2.Custom",
    .tp_doc = PyDoc_STR("Custom objects"),
    .tp_basicsize = sizeof(CustomObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = Custom_new,
    .tp_init = (initproc) Custom_init,
    .tp_dealloc = (destructor) Custom_dealloc,
    .tp_members = Custom_members,
    .tp_methods = Custom_methods,
};

static PyModuleDef custommodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "custom2",
    .m_doc = "Example module that creates an extension type.",
    .m_size = -1,
};

PyMODINIT_FUNC
PyInit_custom2(void)
{
    PyObject *m;
    if (PyType_Ready(&CustomType) < 0)
        return NULL;

    m = PyModule_Create(&custommodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&CustomType);
    if (PyModule_AddObject(m, "Custom", (PyObject *) &CustomType) < 0) {
        Py_DECREF(&CustomType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}

```

在这个版本中，有一些改动。

1. 首先多包含了头文件，用来处理属性。

   ```cpp
   #include <structmember.h>
   ```

2. 现在，新的 `Custom` 类型里，多了三个数据（属性），`first`，`last` 和 `number`。

   其中，`first` 和 `last` 都是 Python string，而 `number` 是C的integer。

   ```cpp
   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;
   ```

   因为现在我们有了需要处理的数据，需要对数据（所占用内存）的分配和释放要更加小心，至少，需要一个释放的方法，

   ```cpp
   static void
   Custom_dealloc(CustomObject *self)
   {
       Py_XDECREF(self->first);
       Py_XDECREF(self->last);
       Py_TYPE(self)->tp_free((PyObject *) self);
   }
   ```

   并且这个方法，被赋予了 `.tp_dealloc` ，

   ```cpp
   .tp_dealloc = (destructor) Custom_dealloc,
   ```

   这个方法先把两个Python属性的计数减去一。这里使用的函数是 `Py_XDECREF`，它可以处理参数是 `NULL` 的情况（比如在 `tp_new` 的时候发生了错误，那么返回的指针就是 `NULL`）。

   然后它调用了这个对象的类型的释放函数来释放内存。注意这里是通过 `Py_TYPE(self)` 来得到它对应的类型的object的，因为我们的这个新类型 `CustomType`，有可能被其他类型继承。

   还有，赋值给 `.tp_dealloc` 时，要指明 `(destructor)`。原因是，`.tp_dealloc` 是一个函数指针变量，它接受的参数是 `PyObject*`，而我们的 `Custom_dealloc` 的参数是 `CustomObjec*`，如不指明就会报错。这里是C中的面向对象的多态！

   因为我们希望在初始化时，把 `first` 和 `last` 的值初始化为空字符串，所以定义如下的 `tp_new` 实现，

   ```cpp
   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = PyUnicode_FromString("");
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = PyUnicode_FromString("");
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }
   ```

   然后把这个函数（指针）赋予 `.tp_new` 成员，

   ```cpp
   .tp_new = Custom_new,
   ```

   这个成员在Python中就是对应 `__new__` 方法，它是用来创建一个此类型的新的对象。这一项并不是必须的，实际上在很多实现当中，都使用了前面提到过的 `PyType_GenericNew` 函数，而这里举例，是说明我们可以在其中把对应的成员变量初始化为想要的值。

   `tp_new` 函数（指针）的第一个参数是 `PyTypeObject *` 而不是 `CustomType`，原因是可能是继承出来的对象，后面的参数是当这个类型的对象被创建时传入的其他参数（positional arguments & keyword arguments），通常这些参数（positional arguments & keyword arguments）会被忽略，并留给初始化函数（C中是 `tp_init`，Python中是 `__init__`）去处理。

   注意，`tp_new` 不需要显式地调用 `tp_init`，因为Python解释会自己做这件事情。

   在 `tp_new` 的实现中，使用了 `tp_alloc` 函数来分配内存，

   ```cpp
   self = (CustomObject *) type->tp_alloc(type, 0);
   ```

   这里我们没有找到（定义）`tp_alloc`，原因是通常 `PyType_Ready()` 函数会帮忙填上这个成员：因为继承了父类，而这个父类通常是 `object` 。绝大多数的类型使用的是默认的内存分配策略。

   注意，如果创建的是一个“协作”的`tp_new`（即调用父类的 `tp_new` 或 `__new__`）时，永远确定地调用想要调用（父类）的 `tp_new`，或 `type->tp_base->tp_new`，而不是在运行的时候，试图去确定调用哪个方法。如果不是这样做，那么继承自该类型的新类型，很可能不会正常工作。

   我们同样提供初始化函数，接收参数，用来初始化对象，

   ```cpp
   static int
   Custom_init(CustomObject *self, PyObject *args, PyObject *kwds)
   {
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL, *tmp;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           tmp = self->first;
           Py_INCREF(first);
           self->first = first;
           Py_XDECREF(tmp);
       }
       if (last) {
           tmp = self->last;
           Py_INCREF(last);
           self->last = last;
           Py_XDECREF(tmp);
       }
       return 0;
   }
   ```

   这个函数被赋予 `tp_init`。

   ```cpp
   .tp_init = (initproc) Custom_init,
   ```

   C中的 `tp_init` expose到Python就是 `__init__` 方法，它在对象创建完毕之后，用来初始化这个对象的值。初始化函数同样应该永远接受位置参数和关键字参数（positional arguments & keyword arguments），并且它在成功时返回 `0` ，失败时返回 `-1` 。

   和 `tp_new` 不同的是，`tp_init` 不能保证一定被调用到（比如 `pickle` 模块），而且它也有可能会被多次调用。

   比如，任何人都能调用我们所定义类型的 `object` 上的 `__init__` 方法。而正因为如此，应该对赋予新属性（attribute）要格外小心。

   比如下面的例子中，因为没有限制 `first` 这个member成员的类型，所以它可以是任意类型的对象。它也许有一个能访问 `first` 这个member成员的析构函数；或者，它能够释放 global interpreter lock，并让特定的代码在另外的线程中访问并修改我们的对象。

   为了保护我们的代码，防止这种可能发生，我们总是在赋值成员之后，才把它的引用计数减一。那么，在什么时候不需要这么做？

   - 我们确定知道引用计数是大于 `1` 的
   - 我们确定对象的析构函数不会释放 GIL（Global Interpreter Lock），也不会回调这个类型的代码。
   - 在一种类型的 `tp_dealloc` 函数里，把引用计数减一，但这个类型不支持循环垃圾回收（cyclic garbage collection）机制。

   如果我们希望把成员数据当做属性（attribute）expose到Python，有几种办法可以做到，最简单的办法就是定义member definition，

   ```cpp
   static PyMemberDef Custom_members[] = {
    {"first", T_OBJECT_EX, offsetof(CustomObject, first), 0,
     "first name"},
    {"last", T_OBJECT_EX, offsetof(CustomObject, last), 0,
     "last name"},
    {"number", T_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /* Sentinel */
};
   ```

   然后把这个定义赋值给 `tp_members`（函数指针），

   ```cpp
   .tp_members = Custom_members,
   ```

   每一个成员的定义，有对应的名称，类型，偏移，访问标识，以及文档字符串。在 3.3.1 中的 Generic Attribute Management 里面有更多详细的介绍。

   这种办法的缺点是，对于赋值给这种类型属性的值（另外的对象），无法限定其类型。比如这个例子中的 `first` 和 `last` ，我们期望它的类型是 `str`，但（按照）这样的办法，实际上任意类型的对象，都可以赋值给它们。进一步，通过赋值C的空指针（`NULL`），属性也可以是被删除的，这样，尽管我们能确保它在初始化时被赋予非空的指针，但在删除的时候，也有可能被赋予空指针。

   接下来定义另外一个成员函数，`Custom.name()`，它的作用就是把 `first` 和 `last` 这两个字符串拼接起来，

   ```cpp
   static PyObject *
   Custom_name(CustomObject *self, PyObject *Py_UNUSED(ignored))
   {
	   if (self->first == NULL) {
		   PyErr_SetString(PyExc_AttributeError, "first");
		   return NULL;
		}
		if (self->last == NULL) {
			PyErr_SetString(PyExc_AttributeError, "last");
		return NULL;
	    }
    return PyUnicode_FromFormat("%S %S", self->first, self->last);
    }
   ```

   这个函数的第一个参数是 `Custom` 类型（或继承它的子类型）的对象（实例），成员函数（方法）的第一个参数总是一个它的实例（指针），而且成员函数也经常接受positional arguments 和 keyword arguments。不过本例中为了简单起见，没有声明这两种参数。而上面这个函数（方法），在Python中就相当于如下的函数（方法），

   ```python
   def name(self):
	   return "%s %s" % (self.first, self.last)
   ```

   在下一节，有介绍办法能够防止 `first` 和 `last` 这两个属性被赋予空指针，还能限定它们只能被赋予字符串类型。

   在我们定义了（类型的）方法之后，我们需要建立一个方法定义的数组，

   ```cpp
   static PyMethodDef Custom_methods[] = {
	   {"name", (PyCFunction) Custom_name, METH_NOARGS,
	   "Return the name, combining the first and last name"
	   },
	   {NULL}  /* Sentinel */
	};
   ```

   这里使用到了宏 `METH_NOARGS`，用来声明这个方法只接受 `self` 参数，而不接收位置参数和字典参数等。

   然后把这个数组（指针）复制给 `tp_methods`，

   ```cpp
   .tp_methods = Custom_methods,
   ```

  截止目前，我们前面所写的代码中，并没有假设这些方法所作用的类型。所以为了使得我们的这个新类型可以当做一个父类被继承，目前我们所要做的，就只是添加一个标识：`Py_TPFLAGS_BASETYPE`，

   ```cpp
   .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
   ```

   为了和上一个例子区分开开来，我们把函数 `PyInit_custom()` 重命名为 `PyInit_custom2()` ，在 `PyModuleDef` 也更改过来，同时也在 `PyTypeObject` 结构体中更改过来。

   最后，修改 `setup.py` ，编译新的模块（module）。

   ```python
   from distutils.core import setup, Extension

   setup(name="custom", version="1.0",
         ext_modules=[
            Extension("custom", ["custom.c"]),
            Extension("custom2", ["custom2.c"]),
        ])
   ```


### 2.3. Providing finer control over data attributes

本节讲述了对前面 `Custom` 例子成员变量 `first` 和 `last` 做更精细的控制。前面的版本中，对象中的 `first` 和 `last` 成员可以被赋予非string类型的值，或者被删除掉，但我们希望的是，它们总是string类型的值。

```cpp
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

typedef struct {
    PyObject_HEAD
    PyObject *first; /* first name */
    PyObject *last;  /* last name */
    int number;
} CustomObject;

static void
Custom_dealloc(CustomObject *self)
{
    Py_XDECREF(self->first);
    Py_XDECREF(self->last);
    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    CustomObject *self;
    self = (CustomObject *) type->tp_alloc(type, 0);
    if (self != NULL) {
        self->first = PyUnicode_FromString("");
        if (self->first == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->last = PyUnicode_FromString("");
        if (self->last == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->number = 0;
    }
    return (PyObject *) self;
}

static int
Custom_init(CustomObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"first", "last", "number", NULL};
    PyObject *first = NULL, *last = NULL, *tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_DECREF(tmp);
    }
    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_DECREF(tmp);
    }
    return 0;
}

static PyMemberDef Custom_members[] = {
    {"number", T_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /* Sentinel */
};

static PyObject *
Custom_getfirst(CustomObject *self, void *closure)
{
    Py_INCREF(self->first);
    return self->first;
}

static int
Custom_setfirst(CustomObject *self, PyObject *value, void *closure)
{
    PyObject *tmp;
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "The first attribute value must be a string");
        return -1;
    }
    tmp = self->first;
    Py_INCREF(value);
    self->first = value;
    Py_DECREF(tmp);
    return 0;
}

static PyObject *
Custom_getlast(CustomObject *self, void *closure)
{
    Py_INCREF(self->last);
    return self->last;
}

static int
Custom_setlast(CustomObject *self, PyObject *value, void *closure)
{
    PyObject *tmp;
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "The last attribute value must be a string");
        return -1;
    }
    tmp = self->last;
    Py_INCREF(value);
    self->last = value;
    Py_DECREF(tmp);
    return 0;
}

static PyGetSetDef Custom_getsetters[] = {
    {"first", (getter) Custom_getfirst, (setter) Custom_setfirst,
     "first name", NULL},
    {"last", (getter) Custom_getlast, (setter) Custom_setlast,
     "last name", NULL},
    {NULL}  /* Sentinel */
};

static PyObject *
Custom_name(CustomObject *self, PyObject *Py_UNUSED(ignored))
{
    return PyUnicode_FromFormat("%S %S", self->first, self->last);
}

static PyMethodDef Custom_methods[] = {
    {"name", (PyCFunction) Custom_name, METH_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject CustomType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "custom3.Custom",
    .tp_doc = PyDoc_STR("Custom objects"),
    .tp_basicsize = sizeof(CustomObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = Custom_new,
    .tp_init = (initproc) Custom_init,
    .tp_dealloc = (destructor) Custom_dealloc,
    .tp_members = Custom_members,
    .tp_methods = Custom_methods,
    .tp_getset = Custom_getsetters,
};

static PyModuleDef custommodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "custom3",
    .m_doc = "Example module that creates an extension type.",
    .m_size = -1,
};

PyMODINIT_FUNC
PyInit_custom3(void)
{
    PyObject *m;
    if (PyType_Ready(&CustomType) < 0)
        return NULL;

    m = PyModule_Create(&custommodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&CustomType);
    if (PyModule_AddObject(m, "Custom", (PyObject *) &CustomType) < 0) {
        Py_DECREF(&CustomType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
```


为了对变量 `first` 和 `last` 做更精细的控制，这里使用了定制的 getter 和 setter 函数，下面是 `first` 对应的 getter 和 setter 函数，

```cpp
static PyObject *
Custom_getfirst(CustomObject *self, void *closure)
{
    Py_INCREF(self->first);
    return self->first;
}

static int
Custom_setfirst(CustomObject *self, PyObject *value, void *closure)
{
    PyObject *tmp;
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "The first attribute value must be a string");
        return -1;
    }
    tmp = self->first;
    Py_INCREF(value);
    self->first = value;
    Py_DECREF(tmp);
    return 0;
}
```

这个 getter 函数的参数是一个 `Custom` 对象，和一个空指针 `closure` 。本例中实际上没有使用空指针 `closure` ，但它可以包含一些数据，以便传递给 setter 和 getter 函数。

这个 setter 函数的参数是一个  `Custom` 对象，一个新的值，以及一个空指针 `closure` 。本例中，不允许给 `first` 赋值空（`NULL`），或者赋值非string类型，所以有这两个检查。

再定义了这两个函数之后，需要定义一个 `PyGetSetDef` 结构类型的数组，

```cpp
static PyGetSetDef Custom_getsetters[] = {
    {"first", (getter) Custom_getfirst, (setter) Custom_setfirst,
     "first name", NULL},
    {"last", (getter) Custom_getlast, (setter) Custom_setlast,
     "last name", NULL},
    {NULL}  /* Sentinel, but actually it is closure method above */
};
```

然后把这个数组（指针）注册到 `.tp_getset` 上，

```cpp
.tp_getset = Custom_getsetters,
```

注意，这个 `PyGetSetDef` 结构类型的数组，它的最后一项实际上应该是前面提到的 `closure` 指针，但本例中因为是空，所以直接给了 `NULL` 。

和第一个版本的 `custom` 相比，我们同样需要把 `first` 和 `last` 这两个变量对应的函数从 `Custom_members` 中移除，而只剩下对另外一个成员 `number` 的设置，

```cpp
static PyMemberDef Custom_members[] = {
    {"number", T_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /* Sentinel */
};
```

同样地，在 `.tp_init` 对应的初始化函数里面，对 `first` 和 `last` 这两个属性的赋值，限定为仅允许string类型，

```cpp
static int
Custom_init(CustomObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"first", "last", "number", NULL};
    PyObject *first = NULL, *last = NULL, *tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_DECREF(tmp);
    }
    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_DECREF(tmp);
    }
    return 0;
}
```

经过这些改动，对 `first` 和 `last` 这两个属性的大多数操作，就可以不再检查 `NULL` 了，因为它们已经不会是 `NULL`了，这也意味着调用函数 `Py_XDECREF` 就可以被替换为 `Py_XDECREF` 了。但在 `.tp_dealloc` 函数（指针）里，仍然需要检查 `NULL` ，原因是，在 `.tp_new` 的时候（创建的时候），有可能失败，这样的这两个成员（属性）就可能是 `NULL` 。

把模块的名称，以及初始化函数的名称做了修改之后，在 `setup.py` 中添加这新的一项，就可以编译第三个版本的 `custom3` 。

### 2.4. Supporting cyclic garbage collection

Python的垃圾回收器可以识别不再需要的对象，甚至它们的引用计数不是零。这种情况有可能发生于存在循环引用的情况下，

```python
l = []
l.append(l)
del l
```

上面的这个例子中，一个列表包含了它自身。但要删除它的时候，它的引用计数仍然不是零。幸运的是，Python的循环引用垃圾回收器，最终可以发现这种情况，识别出来它是垃圾对象，然后回收它。

在第二版的 `Custom` 中，我们允许任何类型的值赋值给 `first` 和 `last` ，而在第二版的 `Custom` 和第三版的`Custom`中，我们允许 `Custom` 或 `Custom` 被继承，这样子类就可以允许被添加上任何类型的属性。因为这两种原因， `Custom` 对象就可能发生循环引用，比如，

```python
import custom3
class Derived(custom3.Custom): pass

n = Derived()
n.some_attribute = n
```

为了使得发生了循环引用的 `Custom` 对象，能够被循环引用垃圾回收器所识别，并回收，我们要在 `Custom` 类型中定义两个额外的函数（指针），然后设置一个标识，使得这两个添加的函数起作用。

```cpp
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

typedef struct {
    PyObject_HEAD
    PyObject *first; /* first name */
    PyObject *last;  /* last name */
    int number;
} CustomObject;

static int
Custom_traverse(CustomObject *self, visitproc visit, void *arg)
{
    Py_VISIT(self->first);
    Py_VISIT(self->last);
    return 0;
}

static int
Custom_clear(CustomObject *self)
{
    Py_CLEAR(self->first);
    Py_CLEAR(self->last);
    return 0;
}

static void
Custom_dealloc(CustomObject *self)
{
    PyObject_GC_UnTrack(self);
    Custom_clear(self);
    Py_TYPE(self)->tp_free((PyObject *) self);
}

static PyObject *
Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    CustomObject *self;
    self = (CustomObject *) type->tp_alloc(type, 0);
    if (self != NULL) {
        self->first = PyUnicode_FromString("");
        if (self->first == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->last = PyUnicode_FromString("");
        if (self->last == NULL) {
            Py_DECREF(self);
            return NULL;
        }
        self->number = 0;
    }
    return (PyObject *) self;
}

static int
Custom_init(CustomObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"first", "last", "number", NULL};
    PyObject *first = NULL, *last = NULL, *tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                     &first, &last,
                                     &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_DECREF(tmp);
    }
    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_DECREF(tmp);
    }
    return 0;
}

static PyMemberDef Custom_members[] = {
    {"number", T_INT, offsetof(CustomObject, number), 0,
     "custom number"},
    {NULL}  /* Sentinel */
};

static PyObject *
Custom_getfirst(CustomObject *self, void *closure)
{
    Py_INCREF(self->first);
    return self->first;
}

static int
Custom_setfirst(CustomObject *self, PyObject *value, void *closure)
{
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "The first attribute value must be a string");
        return -1;
    }
    Py_INCREF(value);
    Py_CLEAR(self->first);
    self->first = value;
    return 0;
}

static PyObject *
Custom_getlast(CustomObject *self, void *closure)
{
    Py_INCREF(self->last);
    return self->last;
}

static int
Custom_setlast(CustomObject *self, PyObject *value, void *closure)
{
    if (value == NULL) {
        PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
        return -1;
    }
    if (!PyUnicode_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "The last attribute value must be a string");
        return -1;
    }
    Py_INCREF(value);
    Py_CLEAR(self->last);
    self->last = value;
    return 0;
}

static PyGetSetDef Custom_getsetters[] = {
    {"first", (getter) Custom_getfirst, (setter) Custom_setfirst,
     "first name", NULL},
    {"last", (getter) Custom_getlast, (setter) Custom_setlast,
     "last name", NULL},
    {NULL}  /* Sentinel */
};

static PyObject *
Custom_name(CustomObject *self, PyObject *Py_UNUSED(ignored))
{
    return PyUnicode_FromFormat("%S %S", self->first, self->last);
}

static PyMethodDef Custom_methods[] = {
    {"name", (PyCFunction) Custom_name, METH_NOARGS,
     "Return the name, combining the first and last name"
    },
    {NULL}  /* Sentinel */
};

static PyTypeObject CustomType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "custom4.Custom",
    .tp_doc = PyDoc_STR("Custom objects"),
    .tp_basicsize = sizeof(CustomObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
    .tp_new = Custom_new,
    .tp_init = (initproc) Custom_init,
    .tp_dealloc = (destructor) Custom_dealloc,
    .tp_traverse = (traverseproc) Custom_traverse,
    .tp_clear = (inquiry) Custom_clear,
    .tp_members = Custom_members,
    .tp_methods = Custom_methods,
    .tp_getset = Custom_getsetters,
};

static PyModuleDef custommodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "custom4",
    .m_doc = "Example module that creates an extension type.",
    .m_size = -1,
};

PyMODINIT_FUNC
PyInit_custom4(void)
{
    PyObject *m;
    if (PyType_Ready(&CustomType) < 0)
        return NULL;

    m = PyModule_Create(&custommodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&CustomType);
    if (PyModule_AddObject(m, "Custom", (PyObject *) &CustomType) < 0) {
        Py_DECREF(&CustomType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
```

要添加的这两个函数，一个是遍历函数（traverse），另一个是清理函数（clear）。

首先，遍历函数可以使得Python的循环引用垃圾回收器，识别循环引用的情况，

```cpp
static int
Custom_traverse(CustomObject *self, visitproc visit, void *arg)
{
    int vret;
    if (self->first) {
        vret = visit(self->first, arg);
        if (vret != 0)
            return vret;
    }
    if (self->last) {
        vret = visit(self->last, arg);
        if (vret != 0)
            return vret;
    }
    return 0;
}
```

遍历函数有三个参数，第一个是 `CustomObject` 这个类型的对象，第二个是一个所谓的访问（visit）函数，第三个参数是一个空指针`void *arg`，是传递给这个访问（visit）函数用的。这个访问（visit）函数把要检查的subobject当做第一个参数，然后把 `arg` 当做第二个参数。访问（visit）函数的返回值是一个整数，如果这个整数是非`0`，那么变量函数就必须直接返回这个非`0`的值。

Python里提供了一个宏 `Py_VISIT`，它（展开之后）可以自动调用访问（visit）函数，所以上面变量函数的样板代码可以简化成如下的几行。但需要注意的是，如果使用宏 `Py_VISIT`，那么这个遍历函数的第二、三个参数名字必须是 `visit` 和 `arg` 。

```cpp
static int
Custom_traverse(CustomObject *self, visitproc visit, void *arg)
{
    Py_VISIT(self->first);
    Py_VISIT(self->last);
    return 0;
}
```

除了提供遍历函数，还要提供清理（clear）函数，以便清理存在循环引用的subobject，

```cpp
static int
Custom_clear(CustomObject *self)
{
    Py_CLEAR(self->first);
    Py_CLEAR(self->last);
    return 0;
}
```

这里使用了宏 `Py_CLEAR`，它是当需要减少引用计数时，清理任意类型的数据属性的推荐、安全的方法。如果在给一个属性赋值为 `NULL`之前，就使用 `Py_XDECREF` 函数，那么析构函数就有可能读到这个正要被删除的属性。

宏 `Py_CLEAR` 的展开类似如下，

```cpp
PyObject *tmp;
tmp = self->first;
self->first = NULL;
Py_XDECREF(tmp);
```

析构函数 `Custom_dealloc` 在清理属性数据的时候，可能调用任意代码，这意味着循环引用垃圾回收器可能被触发。因为GC假定引用计数是非`0`的，所以，需要调用函数 `PyObject_GC_UnTrack`，使其暂停引用计数操作，然后清理成员属性，

```cpp
static void
Custom_dealloc(CustomObject *self)
{
    PyObject_GC_UnTrack(self);
    Custom_clear(self);
    Py_TYPE(self)->tp_free((PyObject *) self);
}
```

最后，在标识中添加 `Py_TPFLAGS_HAVE_GC` ，开启循环引用识别的能力，

```cpp
.tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
```

大概就是这么多了。

如果有定制的 `tp_alloc` 和 `tp_free` 函数，那么我们就需要为了具备循环引用回收的能力，而修改它们。但大多数的C扩展，实际上会使用默认的（函数指针）。

### 2.5. Subclassing other types

可以基于现有的类型，继承新的类型扩展。最容易的办法就是继承built-in类型，原因是它们可以很容易地使用那些类型的 `PyTypeObject` 。但是在不同的C扩展模块直接，使用这些 `PyTypeObject` 就比较困难。

本节的例子，引入了一个 `SubList` 的类型，它继承自built-in的 `list` 类型。这个新的类型和普通的 `list` 类型是完全兼容的，只不过它有一个额外的函数 `increment()` ，用来对内部的计数器加一：

```python
>>> import sublist
>>> s = sublist.SubList(range(3))
>>> s.extend(s)
>>> print(len(s))
6
>>> print(s.increment())
1
>>> print(s.increment())
2
```

本节所提到的 `SubList` 类型的代码如下，

```cpp
#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef struct {
    PyListObject list;
    int state;
} SubListObject;

static PyObject *
SubList_increment(SubListObject *self, PyObject *unused)
{
    self->state++;
    return PyLong_FromLong(self->state);
}

static PyMethodDef SubList_methods[] = {
    {"increment", (PyCFunction) SubList_increment, METH_NOARGS,
     PyDoc_STR("increment state counter")},
    {NULL},
};

static int
SubList_init(SubListObject *self, PyObject *args, PyObject *kwds)
{
    if (PyList_Type.tp_init((PyObject *) self, args, kwds) < 0)
        return -1;
    self->state = 0;
    return 0;
}

static PyTypeObject SubListType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "sublist.SubList",
    .tp_doc = PyDoc_STR("SubList objects"),
    .tp_basicsize = sizeof(SubListObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_init = (initproc) SubList_init,
    .tp_methods = SubList_methods,
};

static PyModuleDef sublistmodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "sublist",
    .m_doc = "Example module that creates an extension type.",
    .m_size = -1,
};

PyMODINIT_FUNC
PyInit_sublist(void)
{
    PyObject *m;
    SubListType.tp_base = &PyList_Type;
    if (PyType_Ready(&SubListType) < 0)
        return NULL;

    m = PyModule_Create(&sublistmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&SubListType);
    if (PyModule_AddObject(m, "SubList", (PyObject *) &SubListType) < 0) {
        Py_DECREF(&SubListType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
```

和前面几节中的 `Custom` 版本的代码很相近，下面注意介绍其中有主要区别的部分。

```cpp
typedef struct {
    PyListObject list;
    int state;
} SubListObject;
```

第一个差异是，对于这个继承类的对象类型结构，它的第一个成员（属性）是，基类类型对象，而这个基类类型对象已经包含了 `PyObject_HEAD` ，作为它的第一个成员（属性）。

当一个对象是 `SubList` 类型的实例时，它的 `PyObject*` 指针就可以安全地转换为 `PyListObject*` 和 `SubListObject*` 。

```cpp
static int
SubList_init(SubListObject *self, PyObject *args, PyObject *kwds)
{
    if (PyList_Type.tp_init((PyObject *) self, args, kwds) < 0)
        return -1;
    self->state = 0;
    return 0;
}
```

上面这个初始化函数中，调用了基类的初始化函数 `PyList_Type.tp_init` 来完成初始化，然后在对子类中的数据成员再坐初始化。

当存在自定义的 `tp_new` 和 `tp_dealloc` 成员方法的时候，这种调用模式很重要。 （子类的）`tp_new` 函数不要使用它自己的 `tp_alloc` 来申请内存，而是直接调用父类的 `tp_new` 来完成这项工作。

`PyTypeObject` 结构中有一项 `tp_base`，用来指明这个类的基类（concrete base class）。因为跨平台编译器的问题，没有办法在定义 `SubListType` 的时候，把这一项 `tp_base` 填入（比如像`tp_name` 一样），而是要在模块的初始化函数里面，再把它填入，如下，

```cpp
PyMODINIT_FUNC
PyInit_sublist(void)
{
    PyObject* m;
    SubListType.tp_base = &PyList_Type;
    if (PyType_Ready(&SubListType) < 0)
        return NULL;

    m = PyModule_Create(&sublistmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&SubListType);
    if (PyModule_AddObject(m, "SubList", (PyObject *) &SubListType) < 0) {
        Py_DECREF(&SubListType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
```

在调用 `PyType_Ready()` 函数的时候，`SubListType` 必须要有 `tp_base` 这一项。当继承一个现有的类型时，不需要把 `PyType_GenericNew()` 赋予 `tp_alloc` （函数指针），因为子类会继承父类的内存分配函数。

调用 `PyType_Ready()` 函数，把 type object加入到module中，就和前面 `Custom` 例子中的代码一样了。


## 3. Defining Extension Types: Assorted Topics

本章快速地介绍了一些可以自己定义的类型方法（type method），以及它们的作用。

下面是 `PyTypeObject` 数据结构，省略了一些只在debug模式下有用的属性。

```cpp
typedef struct _typeobject {
    PyObject_VAR_HEAD
    const char *tp_name; /* For printing, in format "<module>.<name>" */
    Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */

    /* Methods to implement standard operations */

    destructor tp_dealloc;
    Py_ssize_t tp_vectorcall_offset;
    getattrfunc tp_getattr;
    setattrfunc tp_setattr;
    PyAsyncMethods *tp_as_async; /* formerly known as tp_compare (Python 2)
                                    or tp_reserved (Python 3) */
    reprfunc tp_repr;

    /* Method suites for standard classes */

    PyNumberMethods *tp_as_number;
    PySequenceMethods *tp_as_sequence;
    PyMappingMethods *tp_as_mapping;

    /* More standard operations (here for binary compatibility) */

    hashfunc tp_hash;
    ternaryfunc tp_call;
    reprfunc tp_str;
    getattrofunc tp_getattro;
    setattrofunc tp_setattro;

    /* Functions to access object as input/output buffer */
    PyBufferProcs *tp_as_buffer;

    /* Flags to define presence of optional/expanded features */
    unsigned long tp_flags;

    const char *tp_doc; /* Documentation string */

    /* Assigned meaning in release 2.0 */
    /* call function for all accessible objects */
    traverseproc tp_traverse;

    /* delete references to contained objects */
    inquiry tp_clear;

    /* Assigned meaning in release 2.1 */
    /* rich comparisons */
    richcmpfunc tp_richcompare;

    /* weak reference enabler */
    Py_ssize_t tp_weaklistoffset;

    /* Iterators */
    getiterfunc tp_iter;
    iternextfunc tp_iternext;

    /* Attribute descriptor and subclassing stuff */
    struct PyMethodDef *tp_methods;
    struct PyMemberDef *tp_members;
    struct PyGetSetDef *tp_getset;
    // Strong reference on a heap type, borrowed reference on a static type
    struct _typeobject *tp_base;
    PyObject *tp_dict;
    descrgetfunc tp_descr_get;
    descrsetfunc tp_descr_set;
    Py_ssize_t tp_dictoffset;
    initproc tp_init;
    allocfunc tp_alloc;
    newfunc tp_new;
    freefunc tp_free; /* Low-level free-memory routine */
    inquiry tp_is_gc; /* For PyObject_IS_GC */
    PyObject *tp_bases;
    PyObject *tp_mro; /* method resolution order */
    PyObject *tp_cache;
    PyObject *tp_subclasses;
    PyObject *tp_weaklist;
    destructor tp_del;

    /* Type attribute cache version tag. Added in version 2.6 */
    unsigned int tp_version_tag;

    destructor tp_finalize;
    vectorcallfunc tp_vectorcall;
} PyTypeObject;
```

虽然 `PyTypeObject` 中的成员（函数指针）很多，但多数情况下，只需要定义其中的一些即可。

`PyTypeObject` 中成员的顺序是有着历史遗留问题的包袱，所以本章介绍时不会按照顺序讲解。

```cpp
const char *tp_name; /* For printing */
```

这一项名称，主要是为了调试使用，所以应该赋予其一个有意义好分辨的字符串。

```cpp
Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */
```

这一项主要是告诉runtime，这种类型新的对象在创建的时候，应该分配多少内存。`tp_itemsize` 对于像 `str`， `tuple` 这样Python中变长的类型，就有用处。

```cpp
const char *tp_doc;
```

这项是文档字符串，用于Python中类似 `obj.__doc__` 的返回值。

### 3.1. Finalization and De-allocation

```cpp
destructor tp_dealloc;
```

在这种类型的对象的引用计数减至0时，此函数会被调用，然后内存被Python解释器回收。如果有要清理的内存或其他事项，就应该把对应的函数赋予它。同样地，对象本身也需要被释放，例如，

```cpp
static void
newdatatype_dealloc(newdatatypeobject *obj)
{
    free(obj->obj_UnderlyingDatatypePtr);
    Py_TYPE(obj)->tp_free((PyObject *)obj);
}
```

需要注意的是，deallocator函数需要把目前pending的那个exception暂时放置于一边，原因是，当解释器展开（出栈）函数堆栈的时候，deallocator会被频繁地调用到，然而当因为一个exception而发生函数出栈时，deallocator也可以看到那个exception以及被设置了，这样，就有可能发生，当执行deallocator中的代码时，会发现那个以及被设定的exception，从而发生混淆。

因此，合理的做法是，首先把这个正在pending的exception保存起来，然后处理有可能发生exception的代码，处理完成之后，在把之前那个pending的exception恢复出来。所以用到的两个函数是 `PyErr_Fetch()` 和 `PyErr_Restore()` ，下面是一个例子。

```cpp
static void
my_dealloc(PyObject *obj)
{
    MyObject *self = (MyObject *) obj;
    PyObject *cbresult;

    if (self->my_callback != NULL) {
        PyObject *err_type, *err_value, *err_traceback;

        /* This saves the current exception state */
        PyErr_Fetch(&err_type, &err_value, &err_traceback);

        cbresult = PyObject_CallNoArgs(self->my_callback);
        if (cbresult == NULL)
            PyErr_WriteUnraisable(self->my_callback);
        else
            Py_DECREF(cbresult);

        /* This restores the saved exception state */
        PyErr_Restore(err_type, err_value, err_traceback);

        Py_DECREF(self->my_callback);
    }
    Py_TYPE(obj)->tp_free((PyObject*)self);
}
```


需要注意的是，在函数 `tp_dealloc` 中，如何安全地执行代码，是有一些限制的：

- 首先，如果这个类型支持垃圾回收机制（使用 `tp_traverse` 和 `tp_clear`），那么，在调用 `tp_dealloc`的时候，这个对象的有些成员就可能以及被清除（clear）掉或终结（finalized）了。
- 其次，在函数 `tp_dealloc` 中，这个对象不是出于一种安全的状态，因为它的引用计数已经变成0了。调用这个对象的API或是non-trivial object，最终可能会再次调用到 `tp_dealloc`，从而导致double free的问题，进而产生crash。

从Python 3.4开始，推荐不要在 `tp_dealloc` 中实现复杂的终止逻辑，而是把这些放到 `tp_finalize` 方法里面去。

### 3.2. Object Presentation

在Python中，一个对象的文本表示方法有两种，分别是函数 `repr()` 和 `str()`，它们都是（这个object类型的）可选项。其中 `print()` 函数只调用 `str()` 。

```cpp
reprfunc tp_repr;
reprfunc tp_str;
```

其中 `tp_repr` 返回的是一个 string 类型的对象，表示如何表示这个对象，例如，

```cpp
static PyObject *
newdatatype_repr(newdatatypeobject * obj)
{
    return PyUnicode_FromFormat("Repr-ified_newdatatype{{size:%d}}",
                                obj->obj_UnderlyingDatatypePtr->size);
}
```

如果没有提供 `tp_repr` 函数，那么解释器会提供一种表达方式：使用 `tp_name` 和对象的id唯一值。

函数 `tp_str` 对应Python方法 `str()`，而 `tp_repr` 对应Python方法 `repr()`。它和 `tp_repr` 很类似，但它更强调可读性。如果没有提供 `tp_str` ，那么就会使用 `tp_repr` 代替。

下面举了个例子，

```cpp
static PyObject *
newdatatype_str(newdatatypeobject * obj)
{
    return PyUnicode_FromFormat("Stringified_newdatatype{{size:%d}}",
                                obj->obj_UnderlyingDatatypePtr->size);
}
```

### 3.3. Attribute Management

每种支持属性的对象类型，都要提供对应的函数，以便支持如何解析属性的存取，即，既包括如何获取这个属性，以及如何设置这个属性。删除属性是特殊的一种情况，它就是把对应的函数设定为 `NULL`。

Python支持两种（亦即两对）这样的存取方式，一种对象类型只需要实现其中的一种即可。它们的区别是，一对把属性的名称当做是 `char*` 的参数，而另一种则是接收 `PyObject*` 类型的参数。可以视情况方便与否，选择其中一种实现即可。

```cpp
getattrfunc  tp_getattr;        /* char * version */
setattrfunc  tp_setattr;
/* ... */
getattrofunc tp_getattro;       /* PyObject * version */
setattrofunc tp_setattro;
```

如果获取属性的方式总是*简单操作*（后面解释），那么对于 `PyObject*` 版本的属性管理函数，就有通用的实现方式。类型专有的属性handler，在Python 2.2之后基本就消失了，只不过有些以前的代码还没有更新过来。

#### 3.3.1. Generic Attribute Management

绝大多数的扩展只使用 **简单** 的属性，那么什么是**简单属性**？需要满足两个条件：

- 它的名字，在调用 `PyType_Ready()`函数的时候，必须已经可知。
- 当查询或设置属性的时候，无需特殊的处理，或者是无需根据其值，需要采取相应的操作。

上面的条件中，并没有限制属性的值，无论是值是被计算出来的，还是数据是如何存储的。

在调用 `PyType_Ready()`函数的时候，要使用这个类型对象所引用的三个table（即三个对应的成员函数指针），去创建descriptors，然后放入这个类型对象的dict中去。每个descriptor控制着访问对象实例的操作。这里的每个table都是可选的（即可以不设置），如果这3个table都是 `NULL` ，那么这个类型的实例，就只有从基类继承来的属性了，这样 `tp_getattro` 和 `tp_setattro` 就也要设置为 `NULL` ，以便使用基类的函数指针。

下面就是这三个table（函数指针），

```cpp
struct PyMethodDef *tp_methods;
struct PyMemberDef *tp_members;
struct PyGetSetDef *tp_getset;
```

其中，

-  `tp_methods` 指向的是一个 `PyMethodDef` 的数组（当然也可以是 `NULL`），`PyMethodDef` 数据结构如下，

```cpp
typedef struct PyMethodDef {
    const char  *ml_name;       /* method name */
    PyCFunction  ml_meth;       /* implementation function */
    int          ml_flags;      /* flags */
    const char  *ml_doc;        /* docstring */
} PyMethodDef;
```

`tp_methods` 指向的这个 `PyMethodDef` 的数组，每一个元素就是一个 `PyMethodDef` 结构的对象，对应一个方法；从基类继承来的方法不需要放入这个数组中。这个数组的最后一个元素是一个警戒值，用来表示数组的最后一个元素，它的 `ml_name` 必须是 `NULL` 。

- `tp_members` 指向的是一个 `PyMemberDef` 的数组（当然也可以是 `NULL`），每一项都是存于这个对象实例上的一个属性数据。这样的定义支持很多C类型，也支持读写访问，`PyMemberDef` 数据结构如下，

```cpp
typedef struct PyMemberDef {
    const char *name;
    int         type;
    int         offset;
    int         flags;
    const char *doc;
} PyMemberDef;
```

`tp_members` 指向数组的每一项，都会被创建为一个 descriptor，然后加入到这个类型中，用以从这个类型中获取对应的属性。`type` 变量的值，必须是 `structmember.h` 中定义的，而这个值说明了如何把Python中的值，转变为C中类型的值，或者是从C中类型的值转换回Python中去。`flags` 变量是用来控制这一项属性如何访问的标识位。

下面的标识定义在 `structmember.h` 中，可以使用按位或（bitwise-OR）结合起来使用，

|Constant| Meaning     |
|:-----|:-----|
|READONLY|只读 |
|PY_AUDIT_READ|在读之前，发射 `object.__getattr__` 事件（audit event）|

在Python 3.10中，`RESTRICTED`, `READ_RESTRICTED` and `WRITE_RESTRICTED` are deprecated. However, `READ_RESTRICTED` 都变成了 `PY_AUDIT_READ` 的别名，所以，`RESTRICTED` 或 `READ_RESTRICTED` 都会发射这个 audit event。

在运行时，使用 `tp_members` 的一个优点是，如果一个属性是以这种方式定义的，那么一个相应的文档字符串就可以随之而提供。一个应用程序，能够使用侵入性的API，从类对象的descriptor上，使用 `__doc__` 得到这些字符串文档。

和 `tp_methods` 指向的数组是类似的，这个数组的最后一个元素是一个警戒值。

#### 3.3.2. Type-specific Attribute Management

本节以 `char*` 版本的属性存取函数为例进行说明，因为 `PyObject*` 版本只是在接口上有所不同而已。本节的例子和上一节的基本相同，但不是使用从Python 2.2开始的通用办法。这个例子解释了这些操作函数是如何被调用的，这样就可以按照需求，实现所对应的函数。

当需要查找一个属性的时候，就调用 `tp_getattr` 函数。当一个类的 `__getattr__()` 方法被调用的时候， `tp_getattr` 函数同样会被调用。

下面是一个例子，

```cpp
static PyObject *
newdatatype_getattr(newdatatypeobject *obj, char *name)
{
    if (strcmp(name, "data") == 0)
    {
        return PyLong_FromLong(obj->data);
    }

    PyErr_Format(PyExc_AttributeError,
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, name);
    return NULL;
}
```

当一个类实例的 `__setattr__()` 或 `__delattr__()` 被调用的时候， `tp_setattr` 就会被调用。当删除一个属性的时候，这个函数的第三个参数就应该是 `NULL` 。下面例子里，只是简单实现了一个exception，

```cpp
static int
newdatatype_setattr(newdatatypeobject *obj, char *name, PyObject *v)
{
    PyErr_Format(PyExc_RuntimeError, "Read-only attribute: %s", name);
    return -1;
}
```

### 3.4. Object Comparison

```cpp
richcmpfunc tp_richcompare;
```

当需要比较两个对象的时候， `tp_richcompare` 就会被调用。它类似rich comparison method，比如 `__lt__()` ，而函数 `PyObject_RichCompare()` 和  `PyObject_RichCompareBool()` 也会调用到这个函数。

这个函数有三个参数，前两个分别是两对象，第三个是操作符。操作符是：`Py_EQ`, `Py_NE`, `Py_LE`, `Py_GE`, `Py_LT` or `Py_GT` 其中的一个。根据操作符，它们需要比较这两个对象。如果比较成功，就返回 `Py_True` 或 `Py_False` ，如果没有对应的操作符操作（或应该尝试其他操作符），就返回 `Py_NotImplemented` ，如果设定了异常，就返回 `NULL` 。

下面是一个例子，

```cpp
static PyObject *
newdatatype_richcmp(PyObject *obj1, PyObject *obj2, int op)
{
    PyObject *result;
    int c, size1, size2;

    /* code to make sure that both arguments are of type
       newdatatype omitted */

    size1 = obj1->obj_UnderlyingDatatypePtr->size;
    size2 = obj2->obj_UnderlyingDatatypePtr->size;

    switch (op) {
    case Py_LT: c = size1 <  size2; break;
    case Py_LE: c = size1 <= size2; break;
    case Py_EQ: c = size1 == size2; break;
    case Py_NE: c = size1 != size2; break;
    case Py_GT: c = size1 >  size2; break;
    case Py_GE: c = size1 >= size2; break;
    }
    result = c ? Py_True : Py_False;
    Py_INCREF(result);
    return result;
 }
```












### 3.5. Abstract Protocol Support











### 3.6. Weak Reference Support











### 3.7. More Suggestions








# Notes for Extending and Embedding the Python Interpreter

## 1. Extending Python with C or C++

### 添加一个模块的具体步骤

定义一个模块（module）的步骤：

定义一个method table，

```cpp
static PyMethodDef SpamMethods[] = {
    ...
    {"system", spam_system, METH_VARARGS, "Execute a shell command."},
    ...
    {NULL, NULL, 0, NULL}        /* Sentinel */
};
```

定义模块数据结构，必须引用前面定义好的method table

```cpp
static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    spam_doc, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};
```

定义模块初始化函数

- 必须是non-static
- 其名字必须是 `PyInit_name`，这里 `name` 就是模块的名字。

```cpp
PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
```

如果需要程序启动时，把这个模块当做一个built-in模块，就需如下，在程序启动时，在初始化列表中添加进去：

```cpp
int
main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    if (PyImport_AppendInittab("spam", PyInit_spam) == -1) {
        fprintf(stderr, "Error: could not extend in-built modules table\n");
        exit(1);
    }

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required.
       If this step fails, it will be a fatal error. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyObject *pmodule = PyImport_ImportModule("spam");
    if (!pmodule) {
        PyErr_Print();
        fprintf(stderr, "Error: could not import module 'spam'\n");
    }

    ...

    PyMem_RawFree(program);
```

### 使用 setuptools 来编译这个C extension

参考官方文档：[Building Extension Modules](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html)

还有另外一篇文章提到如何在CMake中使用 setuptools：[使用CMake扩展setuptools](https://cloud.tencent.com/developer/information/%E4%BD%BF%E7%94%A8CMake%E6%89%A9%E5%B1%95setuptools%E3%80%82%E6%9C%AA%E5%AE%89%E8%A3%85%E7%94%9F%E6%88%90%E6%89%A9%E5%B1%95)

步骤：

（一）确认 setuptool，python以及 gcc都已安装并工作正常。

（二）创建项目目录，把上面的代码写入文件 `custom.c` 中

（三）创建 `pyproject.toml` 文件如下

```toml
# pyproject.toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "my_custom"  # as it would appear on PyPI
version = "0.42"
```

（四）创建 `setup.py` 文件

```python
from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="custom",  # as it would be imported
                               # may include packages/namespaces separated by `.`

            sources=["custom.c"], # all sources are compiled into a single binary file
        ),
    ]
)
```

至此，该项目目录下文件的情况如下

```shell
<project_folder>
├── pyproject.toml
├── setup.py
└── custom.c
```


（五）使用如下命令，编译C extension

```shell
python setup.py build_ext
```

命令的输出如下，

```shell
running build_ext

building 'custom' extension

creating build

creating build/temp.mingw_x86_64-3.10

gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -march=x86-64 -mtune=generic -O2 -pipe -O3 -march=x86-64 -mtune=generic -O2 -pipe -O3 -ID:/procs/msys64/mingw64/include/python3.10 -c custom.c -o build/temp.mingw_x86_64-3.10/custom.o

writing build/temp.mingw_x86_64-3.10/custom.cp310-mingw_x86_64.def

creating build/lib.mingw_x86_64-3.10

gcc -shared -Wl,--enable-auto-image-base -pipe -pipe -s build/temp.mingw_x86_64-3.10/custom.o build/temp.mingw_x86_64-3.10/custom.cp310-mingw_x86_64.def -LD:/procs/msys64/mingw64/lib/python3.10/config-3.10 -LD:/procs/msys64/mingw64/lib -lpython3.10 -lm -lversion -lshlwapi -o build/lib.mingw_x86_64-3.10/custom.cp310-mingw_x86_64.pyd
```

它会生成一个编译目录 `build`，它的结构如下，

```shell
$ tree build/
build/
├── lib.mingw_x86_64-3.10
│   └── custom.cp310-mingw_x86_64.pyd
└── temp.mingw_x86_64-3.10
    ├── custom.cp310-mingw_x86_64.def
    └── custom.o

2 directories, 3 files
```

切换到 `lib.mingw_x86_64-3.10` 目录下，启动 python，即可使用 `import custom` ，将编写完毕的C extension module导入。



### 杂记

根据约定俗成的说明，如果一个模块名字叫做 `spam` ，那包含它的C文件就叫做 `spammodule.c` ，或直接叫做 `spam.c` （如果名字比较长） 。（这只是个约定，简单情况可以遵从，但不一定永远遵守）

C文件一开始如下

```cpp
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```

其中需要定义 `#define PY_SSIZE_T_CLEAN` 的理由是，在解析函数（方法）的参数的时候，`PyArg_ParseTuple` 把 `s#` （格式化字符串）的长度要当成 `Py_ssize_t`，而不是 `int` 。具体说明参考函数 [PyArg_ParseTuple() - Python3 C-API](https://docs.python.org/3/c-api/arg.html#strings-and-buffers)。

可以设置一个模块独有的错误信息，并创建它，然后使用 [`PyErr_SetString()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString)，或[`PyErr_SetFromErrno()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrno) 等函数来设置这个错误信息。之后要清理就使用[`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear)，如果不想独自处理这个错误，不想把他传递给解释器，就使用  [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear)。

```cpp
static PyObject *SpamError;
SpamError = PyErr_NewException("spam.error", NULL, NULL);
Py_XINCREF(SpamError);
```


使用 CMake 和 setuptools，把二者结合起来，编译 C extension 的参考文章：

[使用CMake扩展setuptools](https://cloud.tencent.com/developer/information/%E4%BD%BF%E7%94%A8CMake%E6%89%A9%E5%B1%95setuptools%E3%80%82%E6%9C%AA%E5%AE%89%E8%A3%85%E7%94%9F%E6%88%90%E6%89%A9%E5%B1%95)
