# Reading Minutes for Effective Modern C++

This is for taking the notes when reading ***Effective Modern C++*** by ***Scott Meyers***.



# Errata Page

This is the ***[Errata Page](http://www.aristeia.com/BookErrata/emc++-errata.html)***



# Words

coax */kəʊks/* *v.*哄，劝诱；连哄带劝地得到；小心地摆弄（机器或装置）

turf

indebted

exasperation

pervasive

heuristic

variadic 

steer clear of 避开; 躲避; 绕开;

tyranny 暴虐，专横

reason about 推出

all but impossible 几乎不可能

enigmatic 神秘的；高深莫测的；谜一般的

hard-pressed 被紧紧追赶的；任务紧急而繁忙的；处境艰难的

hazy 雾蒙蒙的，朦胧的；记不清的，模糊的；

a pinch of 一撮，少许

adornment 装饰；装饰品（书中提到的是指一个类型的const or reference qualifiers）

niche *n.*合适（称心）的工作（活动）; *adj.* （产品）针对特定小群体的

foliage *n.*（植物的）枝叶，叶子

curve ball 使其很难被击打的弧线球

mondo *adj.*绝对的；完全的；（非正式）非凡的，卓绝的；相当

stir up 激起；煽动；搅拌；唤起

turbidity *n.*[分化] 浊度；浑浊；混浊度；混乱

purview *n.*范围，权限；视界；条款







# Introduction

> A useful heuristic to determine whether an expression is an lvalue is to ask if you
> can take its address. If you can, it typically is. If you can’t, it’s usually an rvalue.



rhs = right hand side

lhs = left hand side

move operations = move constructors, move assignment

copy operations = copy constructors, copy assignment

“…” --> narrow ellipsis

“...” --> wide ellipsis



variadic template



本书认为，***argument*** 叫作***形参***，而***parameter*** 叫作***实参***。

> In a function call, the expressions passed at the call site are the function’s **arguments**.
> The **arguments** are used to initialize the function’s **parameters**.

所以***形参*** （***argument***）永远是**lvalue**，而***实参***（***parameter*** ）可能是**lvalue**，也可能是**rvalue**。

> The distinction between **arguments** and **parameters** is important, because **parameters** are lvalues, but the **arguments** with which they are initialized may be rvalues or lvalues. 



本书中提到的**function object**，指的是重载了函数`operator()`的class。也可以直接叫这类object是**callable objects**。



lambda是一个闭包（closure）

> Function objects created through lambda expressions are known as closures



**declaration** 和 **definition** 的区别

> **Declarations** introduce names and types without giving details, such as where storage is located or how things are implemented.
>
> **Definitions** provide the storage locations or implementation details



Function signature

本书提到的function signature，指的是**函数返回值**加上**函数参数的类型**，而函数名称和参数的名称并不是function signature的一部分。

> I define a function’s signature to be the part of its declaration that specifies parameter
> and return types. Function and parameter names are not part of the signature. In the
> example above, func’s signature is **bool(const Widget&)**. 



***backport的痛苦*** 的描述方式

> Not only can they lead to future porting headaches



C++标准委员会提到的**Undefined Behavior**（UB），指的是它们的行为不可预测。

> Sometimes a Standard says that the result of an operation is undefined behavior. That
> means that runtime behavior is unpredictable.

常见的**Undefined Behavior**

- 使用`[]`对`std::vector`的越界访问
- 对未初始化的迭代器的解引用（dereferencing an uninitialized iterator）
- 发生数据竞争（engaging in a data race，即多个线程写同一块内存地址的数据）





# Chapter 1 Deducing Types



类型推导（type deduction）可能出现的地方

- In calls to function templates
- In most situations where `auto` appears
- In `decltype` expressions, and, as of C++14, where the enigmatic `decltype(auto)` construct is employed.



本章的主要内容

> It explains how template type deduction works, how auto builds on that, and how decltype goes its own way. It even explains how you can force compilers to make the results of their type deductions visible, thus enabling you to ensure that compilers are deducing the types you want them to.

- 类型推导如何工作（起作用）
- `auto`如何工作
- `decltype`如何起作用
- 如何强制编译器显式告知类型推导的结果



## Item 1: Understand template type deduction

一个（通用的）模板函数`f`的声明（定义），这里`ParamType`表示函数形参`param`的类型名称

```cpp
template<typename T>
void f(ParamType param); // A template function declarition
```

调用`f`，这里`expr`表示调用时的表达式（值）

```cpp
f(expr); // call f with some expression
         // compilers deduce T and ParamType from expr
```

在调用函数`f`时，编译器会通过`expr`来推导两个类型，`T`和`ParamType`。虽然有很多情况这两种类型最终是相同的，但也有很多情况下这两种类型是不同的。

推导类型`T`，不仅取决于`expr`表达式的类型，也取决于形参的类型`ParamType`。

> The type deduced for `T` is dependent not just on the type of `expr`, but also on the
> form of `ParamType`

事实上，情况分为三种：

- `ParamType`是一个**指针**或**引用**，但不是**万能引用**

  > `ParamType` is a pointer or reference type, but not a universal reference. 

- `ParamType` 是一个**万能引用**

  > `ParamType` is a universal reference.

- `ParamType`既不是**指针**也不是**引用**（包括**万能引用**）。

  > `ParamType` is neither a pointer nor a reference.

### 第一种情况

**`ParamType`是一个指针或引用，但不是万能引用**

这种情况下，对于类型`T`的推导原则如下。（是的！我们实际上当然是在推导类型`T`，而不是`ParamType`！，因为类型`T`推导出来之后，`ParamType`也就确定了，因为`ParamType`实际上这里指的是`T`带一个修饰关键字的变种类型，比如`const T&`）

- 首先忽略`ParamType`的引用部分（即`&`）
- 如果`expr`是一个引用，也忽略它的引用部分（即`&`）
- 按照模式匹配的办法，匹配`expr`和`ParamType`，并以此决**定类型`T`**！



#### `ParamType` - `T&`

如果`ParamType`是非`const`的引用类型，`f`函数如下，

```cpp
template<typename T>
void f(T &param);	// param is a reference
```

定义了一些变量，并且以其为表达式调用函数`f`，那么编译器就会推断出类型`T`如下

```cpp
int x = 27; // x is an int
const int cx = x; // cx is a const int
const int &rx = x; // rx is a reference to x as a const int

f(x);	// T is int, param's type is int&
f(cx);	// T is const int, param's type is const int&
f(rx);	// T is const int, param's type is const int&
```

- 调用函数`f(x)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的引用部分，得到`T`
  - 此时`x`不是引用，所以略过第二条规则
  - 直接用`int`和`T`匹配，推导出`T`就是`int`（同时也推导出`ParamType`就是`T&`）
- 调用函数`f(cx)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的引用部分，得到`T`
  - 此时`cx`不是引用，所以略过第二条规则
  - 直接用`const int`和`T`匹配，推导出`T`就是`const int`（同时也推导出`ParamType`就是`const int&`）
- 调用函数`f(rx)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的引用部分，得到`T`
  - 此时`rx`是引用，所以忽略它的引用部分得到`const int`。
  - 直接用`const int`和`T`匹配，推导出`T`就是`const int`（同时也推导出`ParamType`就是`const intT&`）



#### `ParamType` - `const T&`

如果`ParamType`是`const`的引用类型，`f`函数如下

```cpp
template<typename T>
void f(const T &param);	// param is a reference
```

同样地有如下变量定义，和函数调用，那么编译器就会推断出类型`T`如下

```cpp
int x = 27; // x is an int
const int cx = x; // cx is a const int
const int &rx = x; // rx is a reference to x as a const int

f(x);	// T is int, param's type is const int&
f(cx);	// T is int, param's type is const int&
f(rx);	// T is int, param's type is const int&
```

这种情况下，稍有区别的是，因为已经假定了`param`的类型是`const`了，所以对于类型`T`的推导就不用再考虑`const`修饰符了。

- 调用函数`f(x)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的引用部分（以及`const`修饰符），得到`T`。
  - 此时`x`不是引用，所以略过第二条规则
  - 直接用`int`和`T`匹配，推导出`T`就是`int`（同时也推导出`ParamType`就是`T&`）
- 调用函数`f(cx)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的引用部分（以及`const`修饰符），得到`T`。
  - 此时`cx`不是引用，所以略过第二条规则。但同时忽略`cx`的`const`，得到`int`
  - 直接用`int`和`T`匹配，推导出`T`就是`int`（同时也推导出`ParamType`就是`const int&`）
- 调用函数`f(rx)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的引用部分（以及`const`修饰符），得到`T`。
  - 此时`rx`是引用，所以忽略它的引用部分，同时也忽略`const`，得到`int`。
  - 直接用`int`和`T`匹配，推导出`T`就是`int`（同时也推导出`ParamType`就是`const intT&`）



#### `ParamType` - `T*`

如果`ParamType`是非`const`的指针类型，`f`函数如下

```cpp
template<typename T>
void f(T *param); // param is a pointer
```

有如下变量定义，和函数调用，那么编译器就会推断出类型`T`如下

```cpp
int x = 27; // x is an int
const int *px = &x; // px is a pointer to const int

f(&x);	// T is int, param's type is int*
f(px);	// T is const int, param's type is const int*
```

- 调用函数`f(&x)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的指针部分，得到`T`
  - 此时`x`不是指针，所以略过第二条规则
  - 直接用`int`和`T`匹配，推导出`T`就是`int`（同时也推导出`ParamType`就是`int*`）

- 调用函数`f(px)`，按照上述规则，推导过程如下

  - 忽略`ParamType`的指针部分，得到`T`

  - 此时`px`是指针，所以忽略它的引用部分得到`const int`。

  - 直接用`const int`和`T`匹配，推导出`T`就是`const int`（同时也推导出`ParamType`就是`const int*`）



#### `ParamType` - `const T*`

如果`ParamType`是`const`的指针类型，`f`函数如下

```cpp
template<typename T>
void f(const T *param); // param is a pointer
```

有如下变量定义，和函数调用，那么编译器就会推断出类型`T`如下

```cpp
int x = 27; // x is an int
const int *px = &x; // px is a pointer to const int

f(&x);	// T is int, param's type is const int*
f(px);	// T is int, param's type is const int*
```

同样的，这种情况下，因为已经假定了`param`的类型是`const`了，所以对于类型`T`的推导就不用再考虑`const`修饰符了。

- 调用函数`f(&x)`，按照上述规则，推导过程如下
  - 忽略`ParamType`的指针部分（以及`const`修饰符），得到`T`
  - 此时`x`不是指针，所以略过第二条规则
  - 直接用`int`和`T`匹配，推导出`T`就是`int`（同时也推导出`ParamType`就是`const int*`）

- 调用函数`f(px)`，按照上述规则，推导过程如下

  - 忽略`ParamType`的指针部分（以及`const`修饰符），得到`T`

  - 此时`px`是指针，所以忽略它的引用部分，同时也忽略`const`，得到`int`。

  - 直接用`int`和`T`匹配，推导出`T`就是`int`（同时也推导出`ParamType`就是`const int*`）



### 第二种情况

**`ParamType`是一个万能引用**

#### `ParamType` - `T&&`

这种情况有些特殊，对于类型`T`的推导原则如下。

- 如果`expr`是一个左值，那么`T`和`ParamType`都会被推导为**左值引用**
  - 这是在模板类型推导中，`T`会被推导为引用的唯一一种情况
  - 尽管`ParamType`使用了像右值引用一样的声明语法，但它最终却推导成了左值引用。
- 如果`expr`是一个右值，那么就按照前面提到的第一种情况进行推导
  - 首先忽略`ParamType`的引用部分（即`&&`）
  - 如果`expr`是一个引用，也忽略它的引用部分（即`&&`）
  - 按照模式匹配的办法，匹配`expr`和`ParamType`，并以此决**定类型`T`**

这种情况下，函数`f`如下

```cpp
template<typename T>
void f(T &&param); // param is now a universal reference
```

定义了一些变量，并且以其为表达式调用函数`f`，那么编译器就会推断出类型`T`如下

```cpp
int x = 27;			// x is an int
const int cx = x;	// cx is a const int
const int &rx = x;	// rx is a reference to x as a const int

f(x);	// x is lvalue, so T is int&, param's type is also int&
f(cx);	// cx is lvalue, so T is const int&, param's type is also const int&
f(rx);	// rx is lvalue, so T is const int&, param's type is also const int&
f(27);	// 27 is rvalue, so T is int, param's type is therefore int&&
```

- 调用函数`f(x)`
  - `x`是一个左值（因为是具名变量），所以`T`被推导为`int &`，同时`ParamType`也被推导为`int &`
- 调用函数`f(cx)`
  - `cx`是一个左值（因为是具名变量），所以`T`被推导为`const int &`，同时`ParamType`也被推导为`const int &`
- 调用函数`f(rx)`
  - `rx`是一个左值引用，但同样的，因为是具名变量，所以它也是左值，所以`T`被推导为`const int &`，同时`ParamType`也被推导为`const int &`

- 调用函数`f(27)`
  - `27`是一个右值，所以按照前面提到的第一种情况推导
  - 首先忽略`T&&`的引用部分，得到`T`
  - 其次`27`是右值，但不是引用（而是`int`）
  - 直接用`int`和`T`匹配，得到`T`就是`int`，所以得到`ParamType`就是`int &&`



### 第三种情况

**`ParamType`既不是指针，也不是任何一种引用**

#### `ParamType` - `T`

这种情况下，处理的是**值传递**（pass-by-value），那么`param`就是一个传入值的拷贝（新对象）。

推导规则如下，

- 如果`expr`是一个引用，忽略它的引用部分
- 如果`expr`同时还是`const`或`volatile`，忽略它的`const`或`volatile`部分

这种情况下，函数`f`如下

```cpp
template<typename T>
void f(T param); // param is now passed by value
```

定义了一些变量，并且以其为表达式调用函数`f`，那么编译器就会推断出类型`T`如下

```cpp
int x = 27;			// as before
const int cx = x;	// as before
const int& rx = x;	// as before
const char* const p = "Fun with pointers" // ptr is const pointer to const object

f(x);	// T's and param's types are both int
f(cx);	// T's and param's types are again both int
f(rx);	// T's and param's types are still both int
f(p);	// T's and param's types are const int*
```

- 调用函数`f(x)`
  - `x`不是引用
  - `x`既也不是`const`，也不是`volatile`
  - 因此直接用`x`的类型`int`和`T`做匹配，所以推导出`T`就是`int`，因此`param`的类型也是`int`（非`const`）
- 调用函数`f(cx)`
  - `x`不是引用
  - `x`是`const`，但不是`volatile`，所以只用忽略`const`
  - 因此直接`int`和`T`做匹配，所以推导出`T`就是`int`，因此`param`的类型也是`int`（非`const`）
- 调用函数`f(rx)`
  - `x`是引用，所以忽略它的引用部分
  - `x`是`const`，但不是`volatile`，所以只用忽略`const`
  - 因此直接`int`和`T`做匹配，所以推导出`T`就是`int`，因此`param`的类型也是`int`（非`const`）
- 调用函数`f(p)`
  - `x`不是引用
  - `x`是`const`，这个`const`指的是这个`pointer`不能指向其他的内存地址，即这个`pointer`本身是`const`，所以忽略它（因为值传递就是拷贝）。不是`volatile`所以不管`volatile`。
  - 因此直接`const char*`和`T`做匹配，所以推导出`T`就是`const char*`，因此`param`的类型也是`const char*`，即指针是指向一个内容不可以被修改的地址，但这个指针本身是可以指向其它内存地址的。



### 如果实参是数组

定义数组变量

```cpp
const char name[] = "J. P. Briggs";	// name's type is const char[13]
const char * ptrToName = name;		// array decays to pointer
```

首先，在C中，如果用一个数组去初始化一个指针，那么指针就指向数组的第一个元素，这叫作**array decays**。

这个**array-to-pointer decay rule**，和这里讨论的类型推导无关，是C的特性。

类似的，如果函数的参数是一个数组，那么实际上下面两种函数声明是等价的

```cpp
void myFunc(int param[]);
void myFunc(int* param); // same function as above
```

这实际上表明，指针和数组实际上是等价的。



函数模板`f`声明如下，调用函数并传入数组作为参数

```cpp
template<typename T>
void f(T param); // template with by-value parameter

f(name); // what types are deduced for T and param?
```

此时，`T`被推导为`const char*`。这是由于传入的数组，被等价地认为是一个指针，然后再进行类型推导。



函数模板`f`声明如下，调用函数并传入数组作为参数

```cpp
template<typename T>
void f(T &param); // template with by-value parameter

f(name); // what types are deduced for T and param?
```

由于声明了引用`&`的缘故，此时，`T`被推导为`const char [13]`，而不再推导为指针了，同时`ParamType`变为`const char (&)[13]`。



利用这种特性，可以通过声明成`T&`，在编译期间计算得到一个数组的长度。

```cpp
// Return size of an array as a compile-time constant. (The
// array parameter has no name, because we care only about
// the number of elements it contains.)
template<typename T, std::size_t N> 
constexpr std::size_t arraySize(T (&)[N]) noexcept {
    return N;
}
```

使用举例

```cpp
int keyVals[] = { 1, 3, 7, 9, 11, 22, 35 }; // keyVals has 7 elements
int mappedVals[arraySize(keyVals)]; // so does mappedVals

std::array<int, arraySize(keyVals)> mappedVals; // mappedVals' size is 7
```



### 如果实参是函数

同样地，如果是函数作为参数，也会和数组的array-to-pointer decay rule一样，函数会退化为函数指针。

```cpp
void someFunc(int, double); // someFunc is a function; type is void(int, double)

template<typename T>
void f1(T param); // in f1, param passed by value

template<typename T>
void f2(T &param); // in f2, param passed by ref

f1(someFunc); // param deduced as ptr-to-func; type is void (*)(int, double)
f2(someFunc); // param deduced as ref-to-func; type is void (&)(int, double)
```

`f1`声明的是值传递，如果函数作为参数传入，会推导出来类型`T`是函数指针：`void (*)(int, double)`

`f2`声明的是引用传递，如果函数作为参数传入，会推导出来类型`T`是函数引用：`void (&)(int, double)`



### Things To Remember

> Things to Remember
>
> - During template type deduction, arguments that are references are treated as non-references, i.e., their reference-ness is ignored.
> - When deducing types for universal reference parameters, lvalue arguments get special treatment.
> - When deducing types for by-value parameters, `const` and/or`volatile` arguments are treated as non-`const` and non-`volatile`.
> - During template type deduction, arguments that are array or function names decay to pointers, unless they’re used to initialize references.



## Item 2: Understand auto type deduction

`auto` 类型推导就是`template` 类型推导（有一个例外）

> `auto` type deduction ***is*** template type deduction.
>
> There’s a direct mapping between `template` type deduction and `auto` type deduction.
>
> Deducing types for auto is, with only one exception, the same as deducing types for templates.



在Item 1中，（通用的）函数模板和对应的调用分别如下

```cpp
template<typename T>
void f(ParamType param); // A template function declarition

f(expr); // call f with some expression
         // compilers deduce T and ParamType from expr
```

而编译器负责推导类型`T`以及类型`ParamType`。

对应于`auto`的类型推导，`auto`扮演了`T`的角色，而对应变量的***type specifier***扮演了`ParamType`的角色，例如

```cpp
auto x = 27;		// auto is T, type specifier is auto (ParamType is auto)
const auto cx = x;	// auto is T, type specifier is const auto (ParamType is const auto)
const auto& rx = x;// auto is T, type specifier is const auto& (ParamType is const auto&)
```

为了推导类型，编译器就好像假设存在以下对应的`template`函数（和相应的函数调用）一样

```cpp
template<typename T> 		// conceptual template for
void func_for_x(T param);	// deducing x's type
func_for_x(27);				// conceptual call: param's
							// deduced type is x's type

template<typename T>				// conceptual template for
void func_for_cx(const T param);	// deducing cx's type
func_for_cx(x);						// conceptual call: param's
									// deduced type is cx's type

template<typename T>				// conceptual template for
void func_for_rx(const T& param);	// deducing rx's type
func_for_rx(x);						// conceptual call: param's
									// deduced type is rx's type
```



### `auto`类型推导的情况

在Item1中，对template函数，根据`ParamType`把推导类型的情况分成了三种。

类似的，对于`auto` 可以根据 ***type specifier*** 把情况也分成三种。

- **type specifier 是一个指针或引用，但不是万能引用**
- **type specifier 是万能引用**
- **type specifier 既不是指针也不是任何一种引用**

> - Case 1: The type specifier is a pointer or reference, but not a universal reference.
> - Case 2: The type specifier is a universal reference.
> - Case 3: The type specifier is neither a pointer nor a reference.



> As you can see, auto type deduction works like template type deduction. They’re essentially two sides of the same coin.



三种情况对应的例子

```cpp
// Case 1: A reference/pointer, but not a universal reference
const auto& rx = x;

// Case 2: A universal reference
auto&& uref1 = x;	// x is int and lvalue, so uref1's type is int&
auto&& uref2 = cx;	// cx is const int and lvalue, so uref2's type is const int&
auto&& uref3 = 27;	// 27 is int and rvalue, so uref3's type is int&&

// Case 3: Neither a pointer nor a reference of any kind
auto x = 27;
const auto cx = x;
```



和Item1中相对应的，如果是数组或者函数的时候，会发生同样的 array-to-pointer decay和function-to-pointer decay rule。

```cpp
const char name[] = "R. N. Briggs"; // name's type is const char[13]

auto arr1 = name; // arr1's type is const char*
auto& arr2 = name; // arr2's type is const char (&)[13]

void someFunc(int, double); // someFunc is a function; type is void(int, double)

auto func1 = someFunc; // func1's type is void (*)(int, double)
auto& func2 = someFunc; // func2's type is void (&)(int, double)
```





### `auto`推导和`template`推导唯一的不同

简单来说，唯一的区别是：

**如果使用列表初始化，`auto`会推导为`std::initializer_list<TypeName>`类型，而`template`的推导却不能推断出来`std::initializer_list<TypeName>`类型。**

（这里的`TypeName`是指某个确定的类型名）

例如，可以如下定义一个`int`值，虽然形式不同，但值都是一样的：`int`。

```cpp
int x1 = 27;	// C++98
int x2(27);		// C++98
int x3 = { 27 };	// C++11
int x4{ 27 };		// C++11
```

如果使用`auto`关键字替换上面的`int`，得到下面的定义（可以编译通过）

```cpp
auto x1 = 27;		// type is int, value is 27
auto x2(27);		// ditto
auto x3 = { 27 };	// type is std::initializer_list<int>, value is { 27 }
auto x4{ 27 };		// ditto
```

但前面两个（`x1`，`x2`）的类型被推导为`int`，而后面两个（`x3`，`x4`）被推断为`std::initializer_list<int>`，其值是`{27}`。

需要注意的是，如果在花括号里面的值不是同一种类型的话，会编译失败

```cpp
auto x5 = { 1, 2, 3.0 }; // error! can't deduce T for std::initializer_list<T>
```



