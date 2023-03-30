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



