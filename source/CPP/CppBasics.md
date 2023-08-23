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


## C++ Variadic Macros

See page on [3.6 Variadic Macros](https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html)