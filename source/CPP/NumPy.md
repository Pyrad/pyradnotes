# NumPy Related

A note file for NumPy related stuffs



# NumPy Source



[NumPy源码解析 - csdn](https://blog.csdn.net/wq_0708/article/details/135610438)



## numpy.ndarray 是如何 expose 到 Python scope的？

是通过CPython的方式，expose到 Python scope的。

实际上，`numpy.ndarray` 这个新的类型，是在 `numpy/_core/src/multiarray/arrayobject.c` 中末尾处，以如下方式定义的：

```cpp
NPY_NO_EXPORT PyTypeObject PyArray_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "numpy.ndarray",
    .tp_basicsize = sizeof(PyArrayObject_fields),
    /* methods */
    .tp_dealloc = (destructor)array_dealloc,
    .tp_repr = (reprfunc)array_repr,
    .tp_as_number = &array_as_number,
    .tp_as_sequence = &array_as_sequence,
    .tp_as_mapping = &array_as_mapping,
    .tp_str = (reprfunc)array_str,
    .tp_as_buffer = &array_as_buffer,
    .tp_flags =(Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE),

    .tp_richcompare = (richcmpfunc)array_richcompare,
    .tp_weaklistoffset = offsetof(PyArrayObject_fields, weakreflist),
    .tp_iter = (getiterfunc)array_iter,
    .tp_methods = array_methods,
    .tp_getset = array_getsetlist,
    .tp_new = (newfunc)array_new,
};
```

其中，`array_new` 就是它对应的构造函数（C函数，对应Python的 `__new__`）。

这个函数 `array_new` 实际上也是在这个文件中（`numpy/_core/src/multiarray/arrayobject.c`）定义的。




