
# Boost.Python

## Boost.Python 文档

下载完tarball，然后解压，Boost.Python文档的路径如下：

```shell
$boost_1_65_1/libs/python/doc/html/index.html
```

根据帮助文档首页的信息，内容目录如下：

Contents
- Release Notes
  这部分是版本发布的信息
- Tutorial
  这是一个简单的介绍，主要讲述了如何在C/C++中，wrap一个C的class到Python scope，并提到了其中使用到的Boost.Python提供的基本的工具。
- Building and Testing
  这一章讲述的是如何（只单独）编译Boost.Python，因为Boost.Python不是一个header-only的库，而是需要编译对应的动态（或静态）库。
- Reference Manual
  参考手册，就是Boost.Python提供的所有工具，头文件，类，函数等。
- Configuration Information
- Glossary
- Support Resources
- Frequently Asked Questions (FAQs)
- NumPy Extension Documentation

## How to write Boost.Python converters

[How to write Boost.Python type converters - sixty-north blog](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html "Permalink to How to write Boost.Python type converters")

[How to write Boost.Python type converters - sixty-north blog](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html)

## [How to write Boost.Python type converters - blog](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html)

Fri 25 April 2014

By [Austin Bingham](https://sixty-north.com/blog/author/austin-bingham.html)

Boost.Python [(1)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id11) makes it possible to write C++ that "feels" like Python. The library is powerful and sometimes subtle. This is as compared with the Python C API, where the experience is very far removed from writing Python code.

Part of making C++ feel more like Python is allowing natural assignment of C++ objects to Python variables. For instance, assigning an standard library string to a Python object looks like this:

```cpp
// Create a C++ string
std::string msg("Hello, Python");

// Assign it to a python object
boost::python::object py_msg = msg;
```

Likewise (though somewhat less naturally), it is also important to be able to extract C++ objects from Python objects. Boost.Python provides the extract [2](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id12) type for this:

```cpp
boost::python::object obj = ... ;
std::string msg = boost::python::extract(obj);
```

To allow this kind of natural assignment, Boost.Python provides a system for registering converters between the languages. Unfortunately, the Boost.Python documentation does a pretty poor job of describing how to write them. A bit of searching on the internet will turn up a few links. [(3)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id13)

While these are fine (and, in truth, are the basis for what I know about the conversion system), they are not as explicit as I would like.

So, in an effort to clarify the conversion system both for myself and (hopefully) others, I wrote this little primer. I'll step through a full example showing how to write converters for Qt's QString [(4)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id14) class. In the end, you should have all the information you need to write and register your own converters.

### Converting QString

A Boost.Python type converter consists of two major parts. The first part, which is generally the simpler of the two, converts a C++ type into a Python type. I'll refer to this as the _to-python_ converter. The second part converts a Python object into a C++ type. I'll refer to this as the _from-python_ converter.

In order to have your converters be used at runtime, the Boost.Python framework requires you to register them. The Boost.Python API provides separate methods for registering to-python and from-python converters. Because of this, you are free to provide conversion in only one direction for a type if you so choose.

Note that, for certain elements of what I'm about to describe, there is more than one way to do things. For example, in some cases where I choose to use static member functions, you could also use free functions. I won't point these out, but if you wear your C++ thinking-cap you should be able to see what is mandatory and what isn't.

#### _To-python_ Converters

A _to-python_ converter converts a C++ type to a Python object. From an API perspective, a _to-python_ converter is used any time that you construct a `boost::python::object` [(5)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id15) from another C++ type. For example:

```cpp
// Construct object from an int
boost::python::object int_obj(42);

// Construct object from a string
boost::python::object str_obj = std::string("llama");

// Construct object from a user-defined type
Foo foo;
boost::python::object foo_obj(foo);
```

You implement a _to-python_ converter using a struct with static member function named convert(), which takes the C++ object to be converted as its argument, and it returns a PyObject*. A _to-python_ converter for QStrings looks like this:

```cpp
/* to-python convert to QStrings */
struct QString_to_python_str
{
    static PyObject* convert(QString const& s)
    {
        return boost::python::incref(
            boost::python::object(
                s.toLatin1().constData()).ptr());
    }
};
```

The crux what this does is as follows:

1. Extract the QString's underlying character data using toLatin1().constData()
2. Construct a boost::python::object with the character data
3. Retrieve the boost::python::object's PyObject* with ptr()
4. Increment the reference count on the PyObject* and return that pointer.

That last step bears a little explanation. Suppose that you didn't increment the reference count on the returned pointer. As soon as the function returned, the boost::python::object in the function would destruct, thereby reducing the ref-count to zero. When the PyObject's reference count goes to zero, Python will consider the object dead and it may be garbage-collected, meaning you would return a deallocated object from convert().

Once you've written the _to-python_ converter for a type, you need to register it with Boost.Python's runtime. You do this with the aptly-named to_python_converter [(6)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id16) template:

```cpp
// register the QString-to-python converter
boost::python::to_python_converter<
    QString,
    QString_to_python_str>()
```

The first template parameter is the C++ type for which you're registering a converter. The second is the converter struct. Notice that this registration process is done _at runtime_; you need to call the registration functions before you try to do any custom type converting.

#### _From-python_ Converters

_From-python_ converters are slightly more complex because, beyond simply providing a function to convert from Python to C++, they also have to provide a function that determines if a Python type can safely be converted to the requested C++ type. Likewise, they often require more knowledge of the Python C API.

_From-python_ converters are used whenever Boost.Python's extract type is called. For example:

```cpp
// get an int from a python object
int x = boost::python::extract(int_obj);

// get an STL string from a python object
std::string s = boost::python::extract(str_obj);

// get a user-defined type from a python object
Foo foo = boost::python::extract(foo_obj);
```

The recipe I use for creating _from-python_ converters is similar to _to-python_ converters: create a struct with some static methods and register those with the Boost.Python runtime system.

The first method you'll need to define is used to determine whether an arbitrary Python object is convertible to the type you want to extract. If the conversion is OK, this function should return the PyObject*; otherwise, it should return NULL. So, for QStrings you would write:

```cpp
struct QString_from_python_str {
    // ...

    // Determine if obj_ptr can be converted in a QString
    static void* convertible(PyObject* obj_ptr)
    {
        if (!PyString_Check(obj_ptr)) return 0;
        return obj_ptr;
    }

    // ...
};
```

This simply says that a PyObject* can be converted to a QString if it is a Python string.

The second method you'll need to write does the actual conversion. The primary trick in this method is that Boost.Python will provide you with a chunk of memory into which you must in-place construct your new C++ object. All of the funny "rvalue_from_python" stuff just has to do with Boost.Python's method for providing you with that memory chunk:

```cpp
struct QString_from_python_str {
    // ...

    // Convert obj_ptr into a QString
    static void construct(
        PyObject* obj_ptr,
        boost::python::converter::rvalue_from_python_stage1_data* data)
    {
        // Extract the character data from the python string
        const char* value = PyString_AsString(obj_ptr);

        // Verify that obj_ptr is a string (should be ensured by
        convertible())
        assert(value);

        // Grab pointer to memory into which to construct the new QString
        void* storage = (
            (boost::python::converter::rvalue_from_python_storage*)
            data)->storage.bytes;

        // in-place construct the new QString using the character data
        // extraced from the python object
        new (storage) QString(value);

        // Stash the memory chunk pointer for later use by boost.python
        data->convertible = storage;
    }

	// ...
};
```

The final step for _from-python_ converters is, of course, to register the converter. To do this, you use `boost::python::converter::registry::push_back()`. [(7)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id17) The first argument is a pointer to the function which tests for convertibility, the second is a pointer to the conversion function, and the third is a `boost::python::type_id` for the C++ type. In this case, we'll put the registration into the constructor for the struct we've been building up:

```cpp
struct QString_from_python_str
{
    QString_from_python_str()
    {
        boost::python::converter::registry::push_back(
            &convertible,
            &construct,
            boost::python::type_id());
    }
    // ...
};
```

Now, if you simply construct a single QString_from_python_str object in your initialization code (just like you how you called to_python_converter() for the _to-python_ registration), conversion from Python strings to QString will be enabled.

#### Taking a reference to the PyObject in convert()

One gotcha to be aware of in your construct() function is that the PyObject argument is a 'borrowed' reference. That is, its reference count has not already been incremented for you. [(8)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id18) If you plan to keep a reference to that object, you must use Boost.Python's borrowed construct. For example:

```cpp
class MyClass {
public:
    MyClass(boost::python::object obj) : obj_ (obj) {}

private:
    boost::python::object obj_;
};

struct MyClass_from_python {
    // ...

    static void construct(
        PyObject* obj_ptr,
        boost::python::converter::rvalue_from_python_stage1_data* data)
    {
        using namespace boost::python;

        void* storage = (
            (converter::rvalue_from_python_storage*)
                data)->storage.bytes;

        // Use borrowed to construct the object so that a reference
        // count will be properly handled.
        handle<> hndl(borrowed(obj_ptr));
        new (storage) MyClass(object(hndl));

        data->convertible = storage;
    }
};
```

Failing to use `borrowed()` in this situation will generally lead to memory corruption and/or garbage collection errors in the Python runtime.

There are a number of useful resources on the web for finding more information on Boost.Python objects, handles, and reference counting. [(9)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id19)

### When converters don't exist

Finally, a cautionary note. The Boost.Python type-conversion system works well, not only at the job of moving objects across the C++-python languages barrier, but at making code easier to read and understand. You must always keep in mind, though, this comes at the cost of very little compile-time checking.

That is, the boost::python::object copy-constructor is templatized and accepts _any_ type without complaint. This means that your code will compile just fine even if you're constructing boost::python::object s from types that have no registered converter. At runtime these constructors will find that they have no converter for the requested type, and this will result in exceptions.

These exceptions [(10)](https://sixty-north.com/blog/how-to-write-boost-python-type-converters.html#id20) will tend to happen in unexpected places, and you could spend quite a bit of time trying to figure them out. I say all of this so that maybe, when you encounter strange exceptions when using Boost.Python, you'll remember to check that your converters are registered first. Hopefully it'll save you some time.

### Resources

Boost.Python is fairly complex and can be difficult to understand all at once. Here are few more useful resources that might help you come up to speed on this useful technology:

- This IPython notebook-based [tutorial](https://github.com/abingham/boost_python_tutorial) covers a lot of the major (and some of the more obscure) topics in Boost.Python.
- The Boost.Python [wiki](https://wiki.python.org/moin/boost.python) contains a lot of collected Boost.Python knowledge.
- And of course, the Boost.Python [documentation](http://www.boost.org/doc/libs/1_55_0/libs/python/doc/) itself is very useful.

### Appendix: Full code for QString converter

```cpp
struct QString_to_python_str
{
    static PyObject* convert(QString const& s)
    {
        return boost::python::incref(
            boost::python::object(
                s.toLatin1().constData()).ptr());
    }
};

struct QString_from_python_str
{
    QString_from_python_str()
    {
        boost::python::converter::registry::push_back(
            &convertible,
            &construct,
            boost::python::type_id());
    }

    // Determine if obj_ptr can be converted in a QString
    static void* convertible(PyObject* obj_ptr)
    {
        if (!PyString_Check(obj_ptr)) return 0;
        return obj_ptr;
    }

    // Convert obj_ptr into a QString
    static void construct(
        PyObject* obj_ptr,
        boost::python::converter::rvalue_from_python_stage1_data* data)
    {
        // Extract the character data from the python string
        const char* value = PyString_AsString(obj_ptr);

        // Verify that obj_ptr is a string (should be ensured by convertible())
        assert(value);

        // Grab pointer to memory into which to construct the new QString
        void* storage = (
            (boost::python::converter::rvalue_from_python_storage*)
            data)->storage.bytes;

        // in-place construct the new QString using the character data
        // extraced from the python object
        new (storage) QString(value);

        // Stash the memory chunk pointer for later use by boost.python
        data->convertible = storage;
    }
};

void initializeConverters()
{
    using namespace boost::python;

    // register the to-python converter
    to_python_converter<
        QString,
        QString_to_python_str>();

    // register the from-python converter
    QString_from_python_str();
}
```
