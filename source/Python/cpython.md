# CPython

## Learning CPython Source Code

[CPython源码学习：1、Python int类型 - 晓帆笔记本的文章 - 知乎](https://zhuanlan.zhihu.com/p/641525079)

[CPython源码学习：2、使用GDB调试Python - 晓帆笔记本的文章 - 知乎](https://zhuanlan.zhihu.com/p/643213142)

[CPython源码学习：3、Python的执行流程 - 晓帆笔记本的文章 - 知乎](https://zhuanlan.zhihu.com/p/644435559)

[CPython源码学习：4、语法解释器 - 晓帆笔记本的文章 - 知乎](https://zhuanlan.zhihu.com/p/646171933)

[CPython源码学习：5、Python如何加载so/pyd动态库？ - 晓帆笔记本的文章 - 知乎](https://zhuanlan.zhihu.com/p/661902441)



## python源码剖析

python源码剖析 - 陈儒 - 电子工业出版社 - 2008-06 - 480页

[如何学习才能达到能浅读CPython源码? - 南山烟雨珠江潮的回答 - 知乎](https://www.zhihu.com/question/8490330195/answer/70415053969)

下面链接是上面链接中提到的参考网页资料：

[python3-source-code-analysis - GitHub](https://github.com/flaggo/python3-source-code-analysis) ：是参考 **python源码剖析 - 陈儒** 对Python 3.7的源码分析。

[Building a Python compiler and interpreter - mathspp.com](https://mathspp.com/blog/building-a-python-compiler-and-interpreter)

[A Python Interpreter Written in Python - Allison Kaptur - 中文版](http://qingyunha.github.io/taotao/)

[A Python Interpreter Written in Python - Allison Kaptur - 英文版](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

[一个相关的视频教程](https://www.youtube.com/watch%3Fv%3DdCCcDj8YtDI)



## Python Buffer Protocol

[An Introduction to the Python Buffer Protocol - GitHub](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/)

See the article below.

# An Introduction to the Python Buffer Protocol

Mon 05 May 2014

This is a bit of a niche topic, but I figured there might be one or two people out there who would find this useful (including my future self)... today I managed to implement a simple Python object which exposes the buffer protocol. If that means nothing to you, you may want to stop reading and instead browse this [gallery of puppy gifs](http://imgur.com/gallery/zWeJ5).

But if you're the kind of person who becomes mildly excited at the words *Python buffer protocol*, I hope this short post will help you in your quest...

## [What is the Python Buffer Protocol?](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#What-is-the-Python-Buffer-Protocol?)

The Python buffer protocol, also known in the community as [PEP 3118](http://legacy.python.org/dev/peps/pep-3118/), is a framework in which Python objects can expose raw byte arrays to other Python objects. This can be extremely useful for scientific computing, where we often use packages such as [NumPy](http://numpy.org/) to efficiently store and manipulate large arrays of data. Using the buffer protocol, we can let multiple objects efficiently manipulate views of the same data buffers, without having to make copies of the often large datasets.

Here, for example, we'll use Python's built-in `array` object to create an array:

```python
In [1]:

import array
A = array.array('i', range(10))
A

Out[1]:

array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

Note that the array object is different than a Python list, in that it stores the data as **a contiguous block** of integers. For this reason, the data are stored much more compactly than a list, and certain operations can be performed much more quickly.

`array` objects by themselves are not particularly useful, but a similar type of object can be found in the `numpy` array. Because both Python's `array` and NumPy's `ndarray` objects implement the buffer protocol, it's possible to seamlessly pass data between them using views – that is, without the need to copy the raw data:

```python
In [2]:

import numpy as np
np_A = np.asarray(A)
np_A

Out[2]:

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int32)
```

We can confirm that this is a view of the same buffer by modifying the numpy array: we'll set one of the elements to 555...

```python
In [3]:

np_A[4] = 555
np_A

Out[3]:

array([  0,   1,   2,   3, 555,   5,   6,   7,   8,   9], dtype=int32)
```

...and once this is done we see that the original array has been modified as well:

```python
In [4]:

A

Out[4]:

array('i', [0, 1, 2, 3, 555, 5, 6, 7, 8, 9])
```

This shows that both `A` and `np_A` are pointing to the same block of data, and it required nothing special on our part to make that happen! That's the beauty of the buffer protocol.

## [Why Is This Useful?](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#Why-Is-This-Useful?)

At first glance, this might seem rather trivial. Why is this so useful?

Well, in scientific computing, most of the interesting algorithms are implemented in compiled code: for example, [scipy](http://scipy.org/) is essentially a set of wrappers around [NetLib](http://www.netlib.org/) utilities, which are well-tested implementations of scientific algorithms written mostly in Fortran and C. The ability for Python to natively share data with these compiled libraries is incredibly important for scientific computing. This is one big reason that NumPy and its predecessors were initially developed, and it's why the buffer protocol was later proposed and added to Python's standard library. The buffer protocol is extremely useful for what scientists do with Python: build intuitive interfaces to compiled legacy code.

With apologies to the [PyPy](http://pypy.org/) project's extremely active community, I should also mention that this is one of the main reasons that scientists don't really pay much attention to it: until PyPy can easily interface to all the C and Fortran code we use on a daily basis, all its JIT-ed performance gain is of very little use to us.

This cannot be emphasized enough: **it is fundamentally the Buffer Protocol and related NumPy functionality that make Python useful as a scientific computing platform.**

## [Implementing a Custom Buffer Interface](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#Implementing-a-Custom-Buffer-Interface)

Fortunately, most scientists can simply use the buffer protocol via tools like NumPy without knowing too much of the details of what's behind it. Because the buffer protocol is fundamentally a C-API entity, implementing new functionality with it generally requires digging into the guts of Python's C API. For example, the code that enables the above numpy example is found in NumPy's [buffer.c](https://github.com/numpy/numpy/blob/master/numpy/core/src/multiarray/buffer.c) file, and reading through it is not particularly enlightening. This is the power of Python in a nutshell: it abstracts away C-level messiness like this and instead gives us the nice, powerful, and clean Python interface we all know and love.

But sometimes you need to get your hands dirty. Imagine, for instance, that you have a C object that you'd like to wrap and make available to Python. Your first course might be to use something like [f2py](http://wiki.scipy.org/Cookbook/F2Py), [cython](http://cython.org/), or [SWIG](http://www.swig.org/) to do this: I'd definitely recommend these tools for most problems of this nature.

But you may, for various reasons, want to go even deeper and implement the buffer protocol directly. (For example, you may be interested in taking data structures from another language, such as Julia, and exposing them to Python in a flexible manner). Below I'll give you an example of how to do this.

### [Preliminaries](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#Preliminaries)

Before you go on, you should know that this topic is fairly advanced as far as Python tutorials go, and requires more background knowledge than the average Python hacker probably has. To get started, I'd take a look at the following resources:

- [Python Modules in C](http://dan.iel.fm/posts/python-c-extensions/): a tutorial by Dan Foreman-Mackey. This is a great first intro to writing C-API code.

- [Defining New Types](https://docs.python.org/3/extending/newtypes.html): an excellent tutorial from the official Python documentation. This goes through the basics of creating a type (a class) using C, which can then be visible in Python.

If you get through these tutorials, the following links serve as a really handy reference on the Buffer Protocol itself:

- [The Buffer Protocol](https://docs.python.org/3/c-api/buffer.html): Python's official documentation of the Buffer Protocol. I've found this to be a helpful reference, but I must admit that after staring at it for a couple hours I still had no idea where to start in actually *doing* anything. That's why I'm writing this post.

- [PEP 3118](http://legacy.python.org/dev/peps/pep-3118/): the Python Enhancement Proposal (PEP) outlining the new buffer interface, introduced in Python 3.3.

I should emphasize here that **I'll using the syntax of Python 3.3+**; it's possible to modify this to be compatible with older Python versions, but that requires some judicious use of C compiler directives (see the [NumPy buffer module](https://github.com/numpy/numpy/blob/master/numpy/core/src/multiarray/buffer.c) for an excellent example of this cross-version approach). If you try to run this notebook under older Python versions, things will probably not go very well for you.

### [Setting the Stage](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#Setting-the-Stage)

Let's imagine that we have a C library which creates a buffer of data that we're interested in wrapping. For simplicity, we'll assume it can be boiled-down to the following structure. Notice throughout that we will use IPython's `%%file` magic to save the scripts we write to files, from which they will later be compiled:

```cpp
In [5]:

%%file mylib.c
#include <stdlib.h>
#include <stdio.h>
/* Structure defines a 1-dimensional strided array */
typedef struct{
    int* arr;
    long length;
} MyArray;
/* initialize the array with integers 0...length */
void initialize_MyArray(MyArray* a, long length){
    a->length = length;
    a->arr = (int*)malloc(length * sizeof(int));
    for(int i=0; i<length; i++){
        a->arr[i] = i;
    }
}
/* free the memory when finished */
void deallocate_MyArray(MyArray* a){
    free(a->arr);
    a->arr = NULL;
}
/* tools to print the array */
char* stringify(MyArray* a, int nmax){
    char* output = (char*) malloc(nmax * 20);
    int pos = sprintf(&output[0], "[");
    for (int k=0; k < a->length && k < nmax; k++){
        pos += sprintf(&output[pos], " %d", a->arr[k]);
    }
    if(a->length > nmax)
        pos += sprintf(&output[pos], "...");
    sprintf(&output[pos], " ]");
    return output;
}
void print_MyArray(MyArray* a, int nmax){
    char* s = stringify(a, nmax);
    printf("%s", s);
    free(s);
}
```

Overwriting mylib.c

This code essentially defines a structure `MyArray` which contains information about an array of values, and we have functions to allocate, deallocate, and stringify the array. This C code is overly simplistic; in real life there would be a lot more checks to prevent memory errors and other issues, but it will be a useful stand-in for our purposes.

We can write a quick script to test these functionalities, and compile it using the `g++` compiler:

```python
In [6]:

%%file test_mylib.c
#include "mylib.c"
int main(void){
    MyArray a;
    initialize_MyArray(&a, 10);
    print_MyArray(&a, 10);
    deallocate_MyArray(&a);
}
```

Overwriting test_mylib.c

Now we'll compile it (using the `g++` compiler; you may have to modify this for your system):

```cpp
In [7]:

!g++ test_mylib.c -o test_mylib
```

And running the tests...

```python
In [8]:

!./test_mylib

[ 0 1 2 3 4 5 6 7 8 9 ]
```

It worked! This basically creates an array similar to Python's `range(10)`, but using Python's C API rather than Python itself (aren't you glad you use Python rather than C every day?)

Our task now is to create a simple wrapper for this `MyArray` structure which exposes the buffer interface. We'll basically follow the [Noddy](https://docs.python.org/3/extending/newtypes.html) example from the Python documentation, with a few little extra enhancements, and see how this looks.

Let's start by ignoring the Buffer protocol entirely, and simply create a Python wrapper of the `MyArray` object:

```python
In [9]:

%%file pymyarray.c
#include <Python.h>
#include "mylib.c"
/* This is where we define the PyMyArray object structure */
typedef struct {
    PyObject_HEAD
    /* Type-specific fields go below. */
    MyArray arr;
} PyMyArray;
/* This is the __init__ function, implemented in C */
static int
PyMyArray_init(PyMyArray *self, PyObject *args, PyObject *kwds)
{
    // init may have already been called
    if (self->arr.arr != NULL);
        deallocate_MyArray(&self->arr);
    int length = 0;
    static char *kwlist[] = {"length", NULL};
    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|i", kwlist, &length))
        return -1;
    if (length < 0)
        length = 0;
    initialize_MyArray(&self->arr, length);
    return 0;
}
/* this function is called when the object is deallocated */
static void
PyMyArray_dealloc(PyMyArray* self)
{
    deallocate_MyArray(&self->arr);
    Py_TYPE(self)->tp_free((PyObject*)self);
}
/* This function returns the string representation of our object */
static PyObject *
PyMyArray_str(PyMyArray * self)
{
  char* s = stringify(&self->arr, 10);
  PyObject* ret = PyUnicode_FromString(s);
  free(s);
  return ret;
}
/* Here is the type structure: we put the above functions in the appropriate place
   in order to actually define the Python object type */
static PyTypeObject PyMyArrayType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "pymyarray.PyMyArray",        /* tp_name */
    sizeof(PyMyArray),            /* tp_basicsize */
    0,                            /* tp_itemsize */
    (destructor)PyMyArray_dealloc,/* tp_dealloc */
    0,                            /* tp_print */
    0,                            /* tp_getattr */
    0,                            /* tp_setattr */
    0,                            /* tp_reserved */
    (reprfunc)PyMyArray_str,      /* tp_repr */
    0,                            /* tp_as_number */
    0,                            /* tp_as_sequence */
    0,                            /* tp_as_mapping */
    0,                            /* tp_hash  */
    0,                            /* tp_call */
    (reprfunc)PyMyArray_str,      /* tp_str */
    0,                            /* tp_getattro */
    0,                            /* tp_setattro */
    0,                            /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,           /* tp_flags */
    "PyMyArray object",           /* tp_doc */
    0,                            /* tp_traverse */
    0,                            /* tp_clear */
    0,                            /* tp_richcompare */
    0,                            /* tp_weaklistoffset */
    0,                            /* tp_iter */
    0,                            /* tp_iternext */
    0,                            /* tp_methods */
    0,                            /* tp_members */
    0,                            /* tp_getset */
    0,                            /* tp_base */
    0,                            /* tp_dict */
    0,                            /* tp_descr_get */
    0,                            /* tp_descr_set */
    0,                            /* tp_dictoffset */
    (initproc)PyMyArray_init,     /* tp_init */
};
/* now we initialize the Python module which contains our new object: */
static PyModuleDef pymyarray_module = {
    PyModuleDef_HEAD_INIT,
    "pymyarray",
    "Extension type for myarray object.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};
PyMODINIT_FUNC
PyInit_pymyarray(void) 
{
    PyObject* m;
    PyMyArrayType.tp_new = PyType_GenericNew;
    if (PyType_Ready(&PyMyArrayType) < 0)
        return NULL;
    m = PyModule_Create(&pymyarray_module);
    if (m == NULL)
        return NULL;
    Py_INCREF(&PyMyArrayType);
    PyModule_AddObject(m, "PyMyArray", (PyObject *)&PyMyArrayType);
    return m;
}
```

Overwriting pymyarray.c

That's all there is to it! Now we'll create a quick setup script and run it to compile the module in-place:

```python
In [10]:

%%file setup.py
from distutils.core import setup, Extension
setup(ext_modules=[Extension("pymyarray", ["pymyarray.c"])])
```

Overwriting setup.py

```python
In [11]:

!python setup.py build_ext --inplace

running build_ext
building 'pymyarray' extension
/usr/bin/clang -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jakevdp/anaconda/envs/py3k/include -arch x86_64 -I/Users/jakevdp/anaconda/envs/py3k/include/python3.3m -c pymyarray.c -o build/temp.macosx-10.5-x86_64-3.3/pymyarray.o
/usr/bin/clang -bundle -undefined dynamic_lookup -L/Users/jakevdp/anaconda/envs/py3k/lib -arch x86_64 build/temp.macosx-10.5-x86_64-3.3/pymyarray.o -L/Users/jakevdp/anaconda/envs/py3k/lib -o /Users/jakevdp/Opensource/bufint/pymyarray.so
```

Finally, we can import our new module and create a `MyArray` object from Python and see what we have:

```python
In [12]:

import pymyarray
arr = pymyarray.PyMyArray(10)
print(arr)

[ 0 1 2 3 4 5 6 7 8 9 ]
```

Yes! It worked!

But what if we want to use this with NumPy? It turns out that we're out of luck:

```python
In [13]:

import numpy as np
nparr = np.asarray(arr)
print(nparr.shape)
```

()

NumPy doesn't know what to do with this object, so it just creates a zero-dimensional array (i.e. a scalar), with a value equal to this object. This is not what we want, and addressing this issue is where the Buffer Protocol comes in.

### [Adding the Buffer Protocol](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#Adding-the-Buffer-Protocol)

To add the buffer protocol, we're going to have to re-write most of the above code, adding some specific functionality that NumPy and other tools know how to interface with. The buffer protocol in Python is basically structure which defines a very flexible interface to an offset & strided multi-dimensional array. From the [CPython source](https://github.com/python/cpython/blob/master/Include/object.h#L178-191), we can see what it looks like:

```python
typedef struct bufferinfo{
    void *buf;
    PyObject *obj;        /* owned reference */
    Py_ssize_t len;
    Py_ssize_t itemsize;
    int readonly;
    int ndim;
    char *format;
    Py_ssize_t *shape;
    Py_ssize_t *strides;
    Py_ssize_t *suboffsets;
    void *internal;
}Py_buffer;
```

What the buffer interface does is allow you to define a function which constructs a struct like this that points to your particular data. We see that the array can be multi-dimensional, it can have arbitrary NumPy-style strides along each dimension, as well as arbitrary [PIL](http://www.pythonware.com/products/pil/)-style suboffsets for each dimension.

For our simple 1D array example, we won't be using the full extent of this interface, but it's an easy extension of what we're doing here. Let's create a `pymyarray2` module, copying and pasting much of the above code, and adding the buffer protocol hooks along the way:

```python
In [14]:

%%file pymyarray2.c
#include <Python.h>
#include "mylib.c"
/* This is where we define the PyMyArray object structure */
typedef struct {
    PyObject_HEAD
    /* Type-specific fields go below. */
    MyArray arr;
} PyMyArray;
/* This is the __init__ function, implemented in C */
static int
PyMyArray_init(PyMyArray *self, PyObject *args, PyObject *kwds)
{
    // init may have already been called
    if (self->arr.arr != NULL);
        deallocate_MyArray(&self->arr);
    int length = 0;
    static char *kwlist[] = {"length", NULL};
    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|i", kwlist, &length))
        return -1;
    if (length < 0)
        length = 0;
    initialize_MyArray(&self->arr, length);
    return 0;
}
/* this function is called when the object is deallocated */
static void
PyMyArray_dealloc(PyMyArray* self)
{
    deallocate_MyArray(&self->arr);
    Py_TYPE(self)->tp_free((PyObject*)self);
}
/* This function returns the string representation of our object */
static PyObject *
PyMyArray_str(PyMyArray * self)
{
  char* s = stringify(&self->arr, 10);
  PyObject* ret = PyUnicode_FromString(s);
  free(s);
  return ret;
}
/* Here is the buffer interface function */
static int
PyMyArray_getbuffer(PyObject *obj, Py_buffer *view, int flags)
{
  if (view == NULL) {
    PyErr_SetString(PyExc_ValueError, "NULL view in getbuffer");
    return -1;
  }
  PyMyArray* self = (PyMyArray*)obj;
  view->obj = (PyObject*)self;
  view->buf = (void*)self->arr.arr;
  view->len = self->arr.length * sizeof(int);
  view->readonly = 0;
  view->itemsize = sizeof(int);
  view->format = "i";  // integer
  view->ndim = 1;
  view->shape = &self->arr.length;  // length-1 sequence of dimensions
  view->strides = &view->itemsize;  // for the simple case we can do this
  view->suboffsets = NULL;
  view->internal = NULL;
  Py_INCREF(self);  // need to increase the reference count
  return 0;
}
static PyBufferProcs PyMyArray_as_buffer = {
  // this definition is only compatible with Python 3.3 and above
  (getbufferproc)PyMyArray_getbuffer,
  (releasebufferproc)0,  // we do not require any special release function
};
/* Here is the type structure: we put the above functions in the appropriate place
   in order to actually define the Python object type */
static PyTypeObject PyMyArrayType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "pymyarray.PyMyArray",        /* tp_name */
    sizeof(PyMyArray),            /* tp_basicsize */
    0,                            /* tp_itemsize */
    (destructor)PyMyArray_dealloc,/* tp_dealloc */
    0,                            /* tp_print */
    0,                            /* tp_getattr */
    0,                            /* tp_setattr */
    0,                            /* tp_reserved */
    (reprfunc)PyMyArray_str,      /* tp_repr */
    0,                            /* tp_as_number */
    0,                            /* tp_as_sequence */
    0,                            /* tp_as_mapping */
    0,                            /* tp_hash  */
    0,                            /* tp_call */
    (reprfunc)PyMyArray_str,      /* tp_str */
    0,                            /* tp_getattro */
    0,                            /* tp_setattro */
    &PyMyArray_as_buffer,         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,           /* tp_flags */
    "PyMyArray object",           /* tp_doc */
    0,                            /* tp_traverse */
    0,                            /* tp_clear */
    0,                            /* tp_richcompare */
    0,                            /* tp_weaklistoffset */
    0,                            /* tp_iter */
    0,                            /* tp_iternext */
    0,                            /* tp_methods */
    0,                            /* tp_members */
    0,                            /* tp_getset */
    0,                            /* tp_base */
    0,                            /* tp_dict */
    0,                            /* tp_descr_get */
    0,                            /* tp_descr_set */
    0,                            /* tp_dictoffset */
    (initproc)PyMyArray_init,     /* tp_init */
};
/* now we initialize the Python module which contains our new object: */
static PyModuleDef pymyarray2_module = {
    PyModuleDef_HEAD_INIT,
    "pymyarray2",
    "Extension type for myarray object.",
    -1,
    NULL, NULL, NULL, NULL, NULL
};
PyMODINIT_FUNC
PyInit_pymyarray2(void) 
{
    PyObject* m;
    PyMyArrayType.tp_new = PyType_GenericNew;
    if (PyType_Ready(&PyMyArrayType) < 0)
        return NULL;
    m = PyModule_Create(&pymyarray2_module);
    if (m == NULL)
        return NULL;
    Py_INCREF(&PyMyArrayType);
    PyModule_AddObject(m, "PyMyArray", (PyObject *)&PyMyArrayType);
    return m;
}
```

Overwriting pymyarray2.c

```python
In [15]:

%%file setup2.py
from distutils.core import setup, Extension
setup(ext_modules=[Extension("pymyarray2", ["pymyarray2.c"])])
```

Overwriting setup2.py

```python
In [16]:

!python setup2.py build_ext --inplace

running build_ext
building 'pymyarray2' extension
/usr/bin/clang -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/jakevdp/anaconda/envs/py3k/include -arch x86_64 -I/Users/jakevdp/anaconda/envs/py3k/include/python3.3m -c pymyarray2.c -o build/temp.macosx-10.5-x86_64-3.3/pymyarray2.o
/usr/bin/clang -bundle -undefined dynamic_lookup -L/Users/jakevdp/anaconda/envs/py3k/lib -arch x86_64 build/temp.macosx-10.5-x86_64-3.3/pymyarray2.o -L/Users/jakevdp/anaconda/envs/py3k/lib -o /Users/jakevdp/Opensource/bufint/pymyarray2.so
```

Let's try it out, and see if numpy detects the correct shape

```python
In [17]:

import pymyarray2
arr = pymyarray2.PyMyArray(10)
nparr = np.asarray(arr)
print(nparr.shape)

(10,)
```

It worked!

We can now print the array and make sure it has the data we hope for:

```python
In [18]:

print(nparr)

[0 1 2 3 4 5 6 7 8 9]
```

Finally, we'll double-check that the two objects are really pointing to the same data array. We'll change the value of one of the elements in NumPy, and make sure the change is reflected in our `PyMyArray` object:

```python
In [19]:

nparr[5] = 555
print(nparr)

[  0   1   2   3   4 555   6   7   8   9]

In [20]:

print(arr)

[ 0 1 2 3 4 555 6 7 8 9 ]
```

Success!

### [Exploring the Buffer Protocol Code](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#Exploring-the-Buffer-Protocol-Code)

Let's take a look at the code that was added to the `pymyarray2` example. It's fairly straightforward, actually: we first define a function which builds a buffer from the object:

```python
/* Here is the buffer interface function */
static int
PyMyArray_getbuffer(PyObject *obj, Py_buffer *view, int flags)
{
  if (view == NULL) {
    PyErr_SetString(PyExc_ValueError, "NULL view in getbuffer");
    return -1;
  }

  PyMyArray* self = (PyMyArray*)obj;
  view->obj = (PyObject*)self;
  view->buf = (void*)self->arr.arr;
  view->len = self->arr.length * sizeof(int);
  view->readonly = 0;
  view->itemsize = sizeof(int);
  view->format = "i";  // integer
  view->ndim = 1;
  view->shape = &self->arr.length;  // length-1 sequence of dimensions
  view->strides = &view->itemsize;  // for the simple case we can do this
  view->suboffsets = NULL;
  view->internal = NULL;

  Py_INCREF(self);  // need to increase the reference count
  return 0;
}
```

If you're used to working with multi-dimensional arrays in C, the elements of the structure should be pretty self-explanatory. Here we're using integers so we've used the `"i"` format code. The item formats are extremely flexible: you can basically use any of the codes within Python's [`struct`](https://docs.python.org/3/library/struct.html) module, which gives you nearly endless possibilities for passing around structured data. For more complicated arrays with multiple dimensions, you may have to allocate arrays for the shape, strides, etc. In that case, it's possible to define a `release_buffer` function which deallocates these arrays when the buffer is no longer needed.

Finally, we put this function in a `PyBufferProcs` structure,

```python
static PyBufferProcs PyMyArray_as_buffer = {
  // this definition is only compatible with Python 3.3 and above
  (getbufferproc)PyMyArray_getbuffer,
  (releasebufferproc)0,  // we do not require any special release function
};
```

And then include this structure in the Python Type definition.

```python
static PyTypeObject PyMyArrayType = {
    ...
    &PyMyArray_as_buffer,         /* tp_as_buffer */
    ...
}
```

Simple, right?

## [Conclusion](https://jakevdp.github.io/blog/2014/05/05/introduction-to-the-python-buffer-protocol/#Conclusion)

This was just a simple example of defining the buffer protocol for an object in CPython. It's exactly the kind of description I *wished* I had had as I tried to figure out how this stuff worked. I hope this is as helpful to you as it would have been to me!

Now that I've figured it out, my hope is to apply what I've learned to building an interface between [Julia](http://julialang.org/) arrays and Python objects. We'll see how far I get on that front...

Thanks for reading, and happy coding!

*This post was composed within an IPython notebook; you can view a static version* [here](http://nbviewer.ipython.org/url/jakevdp.github.com/downloads/notebooks/BufferProtocol.ipynb) or download the full source [here](http://jakevdp.github.com/downloads/notebooks/BufferProtocol.ipynb).

