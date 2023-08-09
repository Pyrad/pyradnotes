# Extending and Embedding the Python Interpreter

本文档主要描述，如何通过C/C+-来创建新的Rython模块（module），从而扩展Python解释器（的使用）。这些Python module不仅可以定义新函数，而且还能定义新的对象类型（class）和对应的（类）方法。

本文档同样也描述了，如果把Python解释器嵌入另外一个程序，从而当做一个扩展语言使用。

最后，文档也展示了，当操作系统支持的时候，如何编译并链接这些扩展模块，以便在（程序）运行时，它们能够被解释器动态地加载。

本文档假定读者具备Python的基本知识。关于Python这门语言的非正式的介绍，可以查看[The python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)，而[The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index)给出了Python更正式的定义[The Python Standard Library](https://docs.python.org/3/library/index.html#library-index)描述了现有的对象类型（object types)，函数（functions)和模块 (modules)，它们都是使用Python编写，并且内置的，它们都有着广泛的应用范围关开完整的Python/C API接体文档，可以查看单独的[Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html#c-api-index)

## 推荐的第三方工具

本指南只介绍了在此版本的CPython下，利用其提供的基本工具，创建扩展模块。其他第三方程序，如 [Cython](https://cython.org/), [cffi](https://cffi.readthedocs.io/), [SWIG](https://www.swig.org/) 以及 [Numba](https://numba.pydata.org/) 都提供了更简单便捷和更复杂功能多样的方法，用来创建Python的C和C++的扩展。

[Python Packaging User Guide: Binary Extensions](https://packaging.python.org/guides/packaging-binary-extensions/) 不仅介绍了几种可用工具，它们使得创建二进制扩展更加便捷，而且还讨论了为什么创建一个扩展模块或许是首要考虑的各种原因。

## 不使用第三方工具来创建扩展

这一节主要讲述，在不使用第三方工具的情况下，如何创建出C/C++的扩展模块，这主要是为了这些第三方工具的作者使用，并不是鼓励使用这种办法创建自己的C/C++的扩展模块。
