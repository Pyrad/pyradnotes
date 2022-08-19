# Reading Minutes for Effective Modern C++

This is for taking the notes when reading ***Effective Modern C++*** by ***Scott Meyers***.



# Errata Page

This is the ***[Errata Page](http://www.aristeia.com/BookErrata/emc++-errata.html)***



# Words

coax

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

一个模板函数`f`的声明（定义），这里`ParamType`表示函数形参`param`的类型名称

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





