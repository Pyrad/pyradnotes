# C/C++ Basics

This file shows some basic usages of C/C++

## Initialize a std::unique_ptr with `nullptr`

See [Why does my unique_ptr think is has a null function pointer deleter](https://stackoverflow.com/questions/22915631/why-does-my-unique-ptr-think-is-has-a-null-function-pointer-deleter)

```cpp
class FooObj {
  FooObj() {}
  ~FooObj() { std::cout << "dtor!\n"; }
};

void freeFooObj(FooObj *obj) {
  if (obj) {
    std::cout << "Free func for FooObj\n";
    delete obj;
  }
}

class Foo {
  // Use nullptr and a free func to initialize it
  Foo::Foo() :  m_val(nullptr, freeFooObj) { }

  std::unique_ptr<FooObj, decltype(freeFooObj)> m_val;
};



```


## static constexpr in class template

How to initialize a `static constexpr const` member of a class template in a **header** file?

```cpp
#include <numeric>

// Template class definition here
template<typename T>
class Foo {
public:
	// constexpr must have an initializer
	static constexpr const int VAL_MAX = std::numeric_limits<T>::max();

public:
	Foo(int val) : m_val(val) {}
	~Foo() {}

private:
	int m_val = 0;
};

// Since static member needs definition, define it here
template<typename T> const int Foo<T>::VAL_MAX;

```


## Why using `typename`？

[C++ typedef & typename知识点总结 - 腾讯技术工程的文章 - 知乎](https://zhuanlan.zhihu.com/p/617664673)


##  Why using `template` before a function when invoked?

[static template function in template class](https://stackoverflow.com/questions/43931734/static-template-function-in-template-class)

Quote from C++'03 Standard 14.2/4:

> When the name of a member template specialization appears after . or -> in a postfix-expression, or after nested-name-specifier in a qualified-id, and the postfix-expression or qualified-id explicitly depends on a template-parameter (14.6.2), the member **template** name must be prefixed by the keyword template. Otherwise the name is assumed to name a non-template.

也就是说，如果调用一个class template中的function temple，就要在function名字的前面加上`template`关键字，防止有时编译器不能resolve的情况（是的，有时候编译器可以识别，但有时又不行）。例如下面

```cpp
template<typename T>
class Foo {
	template<bool HoV, bool AscOrder>
	static int32_t check(int32_t i) {
		if (HoV) {
			return AscOrder ? i + 1 : i - 1;
		}
		return i + 3;
	}
	// data members...
	int k = 0;
}

template<typename T>
class Foo2 {
	bool set_ok(int32_t k);
	// data members...
	int m = 0;
}

template<typename T>
bool Foo2<T>::set_ok(int32_t k) {
	// Invoke
	return Foo<T>::template check<true, false>(8) > 0;
}

```


## What is placement new?

[What uses are there for "placement new"?](https://stackoverflow.com/questions/222557/what-uses-are-there-for-placement-new)

简而言之，就是先分配一块"raw"内存，然后在这个内存上构造一个object，这样就把内存分配和对象构造这两步分开了，比如有时候只需要先分配一大块内存，然后在需要的时候再构造，这样就可以提高性能，memory pool中可以用到这项技术。


## Locate the path of STL headers used by g++


You can display the full search paths with

```shell
g++ -print-search-dirs
```

or you can find a specific header without writing a source file with something along the lines of

```shell
echo '#include <vector>' | g++ -x c++ -E - | grep '/vector'
```


Link: [Locate the path of STL headers used by g++](https://stackoverflow.com/questions/21110693/locate-the-path-of-stl-headers-used-by-g)


## C++ unordered_map under the hood

[C++ Unordered Map Under the Hood](https://jbseg.medium.com/c-unordered-map-under-the-hood-9540cec4553a)


## How to measure memory usage of `std::unordered_map`

[https://stackoverflow.com/questions/25375202/how-to-measure-the-memory-usage-of-stdunordered-map](https://stackoverflow.com/questions/25375202/how-to-measure-the-memory-usage-of-stdunordered-map)



## C++ Variadic Macros

See page on [3.6 Variadic Macros](https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html)

下面的两个例子来自 [StackOverflow - Empty function macros](https://stackoverflow.com/questions/9187628/empty-function-macros)


第一个例子

```cpp
#define UNUSED(x)

int foo(int UNUSED(x)) {
	return 42;
}
```


第二个例子（有我自己的修改）

```cpp
#ifdef LOGGING_ENABLED
	#define DBG_MSG_PRINTF(...) fprintf(stdout, __VA_ARGS__)
	#define DBG_ERR_PRINTF(...) fprintf(stderr, __VA_ARGS__)
#else
	#define DBG_MSG_PRINTF(...)
	#define DBG_ERR_PRINTF(...)
#endif // LOGGING_ENABLED
```

## Does C++ lambda have any runtime cost?

Short answer: no.

detail: [Does Lambda Object Construction Cost a Lot - StackOverflow](https://stackoverflow.com/questions/50346822/does-lambda-object-construction-cost-a-lot)

> here, lambda is just an instance of an anonymous type. The type itself is processed at compile-time, so no worries. What happens at run-time though is the capture of variables (here var). When a capture is done by value, the value itself is copied into the lambda instance. This is what costs. When a capture is done by reference, the reference is copied into the lambda, which is cheap.


## Check C++ Macro Expansion by `g++`

Use `-E` option of `gcc/g++`.

```shell
g++ -E source_file.cpp > source_file_preprocess_out.cpp
```



## Cheat Sheets & Infographics

[Cheat Sheets & Infographics](https://hackingcpp.com/cpp/cheat_sheets.html)


## Foreign Function Interface

A foreign function interface (FFI) is a mechanism by which a program written in one programming language can call routines or make use of services written or compiled in another one. An FFI is often used in contexts where calls are made into binary dynamic-link library.

[Foreign Function Interface - Wikipedia](https://en.wikipedia.org/wiki/Foreign_function_interface)


## Doxygen - How to create a doxygen doc for C++ STL?

[https://www.doxygen.nl/manual/external.html](https://www.doxygen.nl/manual/external.html)

[https://en.cppreference.com/w/Cppreference:Archives](https://en.cppreference.com/w/Cppreference:Archives)

[https://flcwiki.desy.de/How%20to%20document%20your%20code%20using%20doxygen](https://flcwiki.desy.de/How%20to%20document%20your%20code%20using%20doxygen)


## Checking the code generated implicitly by the C++ compiler

https://stackoverflow.com/questions/24858014/checking-the-code-generated-implicitly-by-the-c-compiler


## Building and testing a hybrid Python/C++ package

[Building and testing a hybrid Python/C++ package](https://www.benjack.io/building-and-testing-a-hybrid-python/c-package/)

## Flex & Bison (pdf) by John Levine

[Flex & Bison - John Levine](https://web.iitd.ac.in/~sumeet/flex__bison.pdf)

[Compiler Construction using Flex and Bison](https://www.admb-project.org/tools/flex/compiler.pdf)



## 32-bit floating point

[单精度浮点数(float32)存储与表示方式](https://zhuanlan.zhihu.com/p/632347955)

一个32位浮点数由三部分组成（从左向右，依次为第0位、第1位、... 第31位）

- 符号位（sign）：共 $1$ 位，最高位（第31位）
- 指数部分（exponent）：共 $8$ 位，次高位（第30位至第23位）
- 尾数部分（fraction）：共 $23$ 位，次高位（第22位至第0位）

可以由下面的公司计算32位浮点数的真实值

$$
(-1)^{b_{31}} \times 2^{({b_{30}b_{29} \cdot \cdot \cdot b_{23}})-127} \times (1.b_{22}b_{21} \cdot \cdot \cdot b_{0})_2
$$

用 $sign$ 表示符号位，$E$ 标识指数部分，上式可以改写位：

$$
(-1)^{sign} \times 2^{E - 127} \times (1 + \sum_{i=1}^{23}b_{23-i}2^{-1})
$$