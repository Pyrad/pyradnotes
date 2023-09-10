# Extending and Embedding the Python Interpreter

本文档主要描述，如何通过C/C+-来创建新的Rython模块（module），从而扩展Python解释器（的使用）。这些Python module不仅可以定义新函数，而且还能定义新的对象类型（class）和对应的（类）方法。

本文档同样也描述了，如果把Python解释器嵌入另外一个程序，从而当做一个扩展语言使用。

最后，文档也展示了，当操作系统支持的时候，如何编译并链接这些扩展模块，以便在（程序）运行时，它们能够被解释器动态地加载。

本文档假定读者具备Python的基本知识。关于Python这门语言的非正式的介绍，可以查看[The python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)，而[The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index)给出了Python更正式的定义[The Python Standard Library](https://docs.python.org/3/library/index.html#library-index)描述了现有的对象类型（object types)，函数（functions)和模块 (modules)，它们都是使用Python编写，并且内置的，它们都有着广泛的应用范围关开完整的Python/C API接体文档，可以查看单独的[Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html#c-api-index)


## Words

exercise caution 谨慎行事

## Links

[Python 3.x.x documentation](https://docs.python.org/3/index.html)

[Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)

[The Python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)

[浅谈Python C扩展](https://blog.csdn.net/fitzzhang/article/details/79212411)


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

注意，这里给出的异常名称，在Python中是 `spam.error`。函数 [`PyErr_NewException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewException) 创建的class的基类是 [`Exception`](../library/exceptions.html#Exception "Exception")（除法传入的参数不是 `NULL` 而是其他class），它在中 [Built-in Exceptions](../library/exceptions.html#bltin-exceptions) 有描述。

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

在使用新的扩展模块之前，还有两件事情要做：编译，并且链接到Python系统上去。如果使用的是动态链接，那么（实现）细节就依赖于所使用的系统的动态链接方式；可以参考有关构建扩展模块的章节（[Building C and C++ Extensions](building.html#building)），以及只适用于在Windows平台上构建方法的更多细节。

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

这个函数必须通过Python解释器，使用 [`METH_VARARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_VARARGS "METH_VARARGS") 这个标记注册（1.4 The Module’s Method Table and Initialization Function 描述了这种办法）。函数 [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple) 以及它的参数在下一节 [Extracting Parameters in Extension Functions](#parsetuple) 中讨论。

宏 [`Py_XINCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XINCREF) 和 [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF) 用来增加/减小一个对象的引用计数，并且可以使用在 `NULL` 指针上。更多讨论参考 [Reference Counts](#refcounts) 这一节。

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
Py_BuildValue("")                        None
Py_BuildValue("i", 123)                  123
Py_BuildValue("iii", 123, 456, 789)      (123, 456, 789)
Py_BuildValue("s", "hello")              'hello'
Py_BuildValue("y", "hello")              b'hello'
Py_BuildValue("ss", "hello", "world")    ('hello', 'world')
Py_BuildValue("s#", "hello", 4)          'hell'
Py_BuildValue("y#", "hello", 4)          b'hell'
Py_BuildValue("()")                      ()
Py_BuildValue("(i)", 123)                (123,)
Py_BuildValue("(ii)", 123, 456)          (123, 456)
Py_BuildValue("(i,i)", 123, 456)         (123, 456)
Py_BuildValue("[i,i]", 123, 456)         [123, 456]
Py_BuildValue("{s:i,s:i}",
              "abc", 123, "def", 456)    {'abc': 123, 'def': 456}
Py_BuildValue("((ii)(ii)) (ii)",
              1, 2, 3, 4, 5, 6)          (((1, 2), (3, 4)), (5, 6))
```


### 1.10. Reference Counts

在像C和C++这样的程序设计语言中，编程者自己需要负责堆上内存的动态分配和释放。在C语言中，使用函数 `malloc()` 和 `free()` 完成这一工作。在C++中，使用运算符 `new` 和 `delete` 来做本质上相同的事情。下面的讨论基于C语言。

由函数 `malloc()` 函数分配的每一块内存，最终都应该使用一次而且仅有一次的函数 `free()`，将所分配的内存归还给内存池中。在合适的时机调用 `free()` 很关键。如果一块内存的地址被遗忘了，而且`free()` 函数没有用来释放这个地址对应的内存，那么这块内存在整个程序结束之前，都会被占用而且不能再次利用。这就是所谓的**内存泄露**（*memory leak*）。另一方面，如果对一块内存已经调用了函数 `free()` 来释放内存，但之后仍然使用这块内存，那么当另一个 `malloc()` 被调用并使用这块相同地址的内存时，就会产生冲突。这就是**非法内存访问**（*using freed memory*）。和引用没有被初始化的数据一样，这也会产生一些严重的后果，比如内存转储（core dump），错误的结果（wrong results），以及莫名其妙的崩溃（mysterious crashes）。

造成内存泄露的原因，通常是代码中不同寻常的调用路径。比如，一个函数分配了一块内存，做了一些计算，然后释放了这块内存。现在有要求要做些变动，函数要在做计算时加入测试，当检测到有错误的条件时，就从函数当中提前返回。所以在提前返回的过程当中，很容易忘记释放之前所分配的内存，尤其是这部分代码是后来才加入的。这样的泄露，一旦引入，在很长时间里都很难被发觉：这个错误的返回只发生在所有调用中的一小个片段中，而且现代的机器硬件又拥有充足的虚拟内存，所以，只有当这个函数被长时间地经过频繁调用之后，这个泄露情况才会显现出来。因此，为了防止发生这样的泄露，采样减少这种错误的代码传统或策略，就很重要。

因为Python重度使用函数 `malloc()` 和 `free()`，它就需要采用一种策略，避免内存泄露和非法内存访问。这个被选中的策略叫做***引用计数***（*reference counting*）。原则很简单，每个对象包含一个计数器，当在其他地方存储了一个对这个对象的引用时，就将其加一，当对它的一个引用被删除的时候，就减一。当这个计数器变成0时，（就说明）最后一个对这个对象的引用被删掉了，这个对象（占用的内存）就应该被释放了。

另一种策略叫做***自动垃圾回收***（*automatic garbage collection*）（有时候，引用计数也被当做是一种垃圾回收策略，因此这里使用了**自动** automatic 一词来加以区别）自动垃圾回收机制最大的优点是，不需要使用者显式地调用 `free()` 函数了。（另一个声称的优点是对性能和内存的提示，但这没有确凿的事实证据）缺点是，在C中，没有一个真正意义上的可移植的自动垃圾回收器，然而引用计数却能够实现为可移植的（只要函数 `malloc()` 和 `free()`可以使用，实际上C标准保证了这一点）也许有一天，C语言会有一个有效率的、可移植的自动垃圾回收器。但在那之前，我们就需要使用引用计数。

尽管Python使用的是传统的引用计数的实现，它提供了一共循环引用检测器，用来检查循环引用。这就使得应用程序可以不用担心创建出来有向或无向的循环引用，而这些是只使用引用计数的垃圾回收机制的缺陷。循环引用的对象，直接或间接包含了指向它们直接的引用，那么这就造成循环引用中的每个对象的引用计数总也不为0。典型的引用计数的实现是无法回收循环引用中的对象的内存，或者无法回收被循环引用中的对象所引用的对象的内存（哪怕没有进一步引用这个循环）。

这种循环检测器能够检查垃圾循环，并且回收它们所占用的对象的内存。 [`gc`](../library/gc.html#module-gc "gc: Interface to the cycle-detecting garbage collector.") 模块提供了可以运行检测器的方法（即函数 [`collect()`](../library/gc.html#gc.collect "gc.collect")），以及进行接口配置、在运行期间关闭循环检查的方法。


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

下面要导出的模块是 [A Simple Example](#extending-simpleexample) 这一节中 `spam` 模块的一个修改版本。函数 `spam.system()` 没有直接调用C的库函数 `system()`，相反它调用了一个叫做 `PySpam_System()` 的函数，当然，这个函数在实际应用中肯定要做更复杂的事情。这个叫做 `PySpam_System()` 的函数也会被导出到其他各个扩展模块中。

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

【1】 An interface for this function already exists in the standard module [`os`](../library/os.html#module-os "os: Miscellaneous operating system interfaces.") — it was chosen as a simple and straightforward example.

【2】The metaphor of “borrowing” a reference is not completely correct: the owner still has a copy of the reference.

【3】Checking that the reference count is at least 1 **does not work** — the reference count itself could be in freed memory and may thus be reused for another object!

【4】These guarantees don’t hold when you use the “old” style calling convention — this is still found in much existing code.





