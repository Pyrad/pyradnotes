# 右值引用与移动语义

Reference page: [右值引用与移动语义](https://zhuanlan.zhihu.com/p/545494408)

代码文件：[`lvalue_rvalue.hpp`](https://github.com/Pyrad/cpp11/blob/master/src/cppfeatures/lvalue_rvalue.hpp)，[`lvalue_rvalue.cpp`](https://github.com/Pyrad/cpp11/blob/master/src/cppfeatures/lvalue_rvalue.cpp)

## 三种大概分类

现代 c++ 把表达式分为三种主要类型：

- **lvalue**（left value，左值）
- **prvalue**（pure rvalue，纯右值）
- **xvalue**（eXpiring value， 将亡值）

实际上 **prvalue** 和 **xvalue** 都属于右值。



## 左值（lvalue）

### 概念

**左值不能简单理解为就是等号左边的值，其实只要能取地址，那这个表达式就是左值。**

可以取地址意味着在程序的**某块内存地址**上已经存储了他的内容。

### 常见左值

一些常见的左值：

- 具名的变量名（即有名字的变量）
- 左值引用
- **右值引用也是左值**（*想想这个比较特别，但实际上就应该是这样*）
- 返回左值引用的函数或是操作符重载的调用语句
- `a=b`, `a+=b`, 等内置的赋值表达式
- **前缀自增自减**。如 `++a`, `--a` 是左值
- **字符串常量**（这是个例外，见如下例子）
- 左值引用的类型转换语句。如 `static_cast<int&>(x)`

### 例子（以及例外）

```cpp
int a = 1;
const char* str = "hello";
```

- `a` 是左值，因为 `a` 这个变量确实被存到内存里了，并且在内存里面写入的值是`1`
- `str` 也是左值（原因同上）
- **数字常量 `1`** 并不是左值。（`1` 是在运行到这行代码是，临时产生的一个值，它是没有地址的, 仅仅存在**寄存器**中用作临时运算）
- **`hello` 这个字符串常量实实在在的是左值**

`hello`为什么是左值？

- 编译的时候， `hello` 这个字符串会真的被单独的存放在某一内存地址上存储，一般是**静态数据区**。所以直接对 `hello` 这个字符串常量 取地址（`&`），是完全可以取到的。能取到地址说明他就是个左值。

```cpp
const char *mystr = "hello, world";
fprintf(stdout, "&mystr = %p\n", &mystr);
fprintf(stdout, "&\"hello, world\" = %p\n", &"hello, world");
```

- 如上代码片段，可以得到如下（类似）的结果

```cpp
&mystr = 000000000023f200
&"hello, world" = 000000013fdee0b0
```



为何把字符串常量放在**静态数据区**？

- 编译时期就已经可以知道总共用到了哪些字符串常量，提前把所有的字符串常量都放在某块内存地址上，使用时再从此处拷贝，该字符串常量重复使用的话，就可以节省效率。如果运行时让寄存器构造一个字符串常量的值，这显然不是高效的做法。

### 总结

**只要能取得地址，那就说明是左值**。

因为能取地址，那么就能修改它的值（理论上都能修改，只是比如字符串常量一般是不能修改的），所以左值能放在等号左边，可以给左值进行赋值。

所以引出的问题

- **左值一定能赋值 ?** 不是， 字符串常量是左值，但不能修改其值。
- **左值一定能取地址？** 是的。

总结起来就是：**左值一定能取地址，但不一定能赋值（字符串常量）**。



## 纯右值（prvalue）

### 概念

**rvalue** 是纯右值，它是右值的一种。

**右值是临时产生的值，不能对右值取地址，因为它本身就没存在内存地址空间上。**

### 常见右值

举例纯右值如下：

- 除字符串以外的常量，如 `1`，`true`，`nullptr`
- **返回非引用的函数或操作符重载的调用语句**
- **后缀自增自减**是右值：`a++`, `a--`
- `a+b`, `a << b` 等一般表达式
- `&a`，对变量取地址的表达式是右值
- `this`指针
- `lambda`表达式

理解也很简单，其实就是一些**运算时的中间值**，**这些值只存在寄存器中辅助运算**，**不会实际写到内存地址空间中**，因此也无法对他们取地址。



## 将亡值（xvalue）

### 概念

**xvalue** 叫将亡值（e**X**piring value），顾名思义，就是即将销毁的东西。**xvalue** 也是**右值**的一种。

### 常见的两种xvalue

主要记住前面两种就行了，第三种不如前两种常见

- 返回**右值引用**的函数或者操作符重载的调用表达式。
  - 如某个函数返回值是 **`std::move(x)`**并且函数返回类型是 **`T&&`**

  - 再比如下面，调用`f()`，返回的就是一个`xvalue`

    ```cpp
    int&& f(){ return 3; }
    ```

- 对对象类型右值引用的转换（目标为**右值引用**的类型转换表达式）
  - 如 **`static<int&&>(a)`**

- 类成员访问表达式，指定非引用类型的非静态数据成员，其中对象表达式是xvalue

  ```cpp
  struct As { int i; };
  As&& f(){ return As(); }
  int main() {
      // The expression f().i belongs to the xvalue category,
      // because As::i is a non-static data member of non-reference type,
      // and the subexpression f() belongs to the xvlaue category.
      f().i;
      return 0;
  }
  ```

  

**xvalue** 和 **prvalue** 都是属于右值，不必对它们过度的区分。



## 左值引用和右值引用

没必要去真的纠结哪些是左值，哪些是右值，能区分常见的即可，右值引用才是需要重点关注。

### 左值引用

左值引用可以分为两种：

- **非const左值引用** （non-const lvalue reference ）
- **const左值引用**（const lvalue reference）

很重要的一点：**非const左值引用只能绑定左值；const左值引用既能绑定左值，又能绑定右值！**

为何const lvalue reference既能绑定左值，又能绑定右值？

简单地说，为了避免值传递的时候拷贝所产生的额外开销，比如一个打印函数为了避免值传递的开销，采用如下的non-const lvalue reference，那么调用的时候就必须要先定义一个左值才行，比较麻烦

```cpp
// non-const lvalue reference argument
void print(int &v);
// when to use, a lvalue has to be defined first
int a = 1;
print(a);
```

如果是const lvalue reference，那么就可以直接传入一个右值来调用

```cpp
// const lvalue reference argument
void print(const int &v);
// No need to define a lvalue first, but pass in a rvalue directly
print(1);
```



### 右值引用

**右值引用只能绑定到右值上**

```cpp
int b = 2;
// Error, a rvalue reference can ONLY be bound to a rvalue
// int&& rref_b = b; // error, here b is a lvalue

int &&rref_2 = 2; // ok
cout << "rref_2=" << rref_2 << endl; // output 2
rref_2++;
cout << "rref_2=" << rref_2 << endl; // output 3
```



### 移动语义

可以通过`std::move(...)`把一个**左值**标记为**右值**。

`std::move` 唯一做的事情其实就是个**类型转换**，标记为一个xvalue，

[cppreference](https://en.cppreference.com/w/cpp/utility/move)描述原文：

> In particular, `std::move` produces an [xvalue expression](https://en.cppreference.com/w/cpp/language/value_category) that identifies its argument `t`. It is exactly equivalent to a `static_cast` to an rvalue reference type.
>
> Parameters
>
> `t` - the object to be moved
>
> Return value
>
> `static_cast<typename std::remove_reference<T>::type&&>(t)`



因此，**move 并不作任何的资源转移操作。单纯的 move(x) 不会有任何的性能提升，不会有任何的资源转移。**它的作用仅仅是产生一个标识x的右值表达式。

经过`std::move(...)`移动语义，可以把一个**左值**用**右值引用**绑定

```cpp
int k = 2;
// int&& rref_k = k; // error,右值引用只能绑定到右值上，k是一个左值
int&& rref_k = std::move(k); // ok, std::move(k) 是一个右值，可以用右值引用绑定
```





### 函数重载

当函数参数既有左值引用重载，又有右值引用重载的时候, 我们得到重载规则如下:

- 若传入参数是**非const左值**，调用**非const左值引用**重载函数
- 若传入参数是**const左值**，调用**const左值引用**重载函数
- 若传入参数是**右值**，调用**右值引用重载函数**(即使是有 `const` 左值引用重载的情况下)



```cpp
void f(int& x) { cout << "lvalue reference overload f(" << x << ")\n"; }
void f(const int& x) { cout << "lvalue reference to const overload f(" << x << ")\n"; }
void f(int&& x) { cout << "rvalue reference overload f(" << x << ")\n"; }

int main() {
    int i = 1;
    const int ci = 2;
    f(i);  // calls f(int&)
    f(ci); // calls f(const int&)
    f(3);  // calls f(int&&) even if f(const int&) exists
           // but it would call f(const int&) if f(int&&) overload wasn't provided
    f(std::move(i)); // calls f(int&&)

    // rvalue reference variables are lvalues when used in expressions
    int&& x = 1;
    f(x);            // calls f(int& x)
    f(std::move(x)); // calls f(int&& x)
}
```





## 生命周期延长

临时对象生命周期C++ 的规则是：**一个临时对象，会在包含这个临时对象的完整表达式估值完成后、按生成顺序的逆序被销毁，除非有生命周期延长发生。**

可以查看源文件代码：[`lvalue_rvalue.hpp`](https://github.com/Pyrad/cpp11/blob/master/src/cppfeatures/lvalue_rvalue.hpp)

定义以下几个`class`和函数

```c++
class shape {
public:
    shape() { std::cout << "shape" << std::endl; }
    virtual ~shape() { std::cout << "~shape" << std::endl; }
};
class circle : public shape {
public:
    circle() { std::cout << "circle" << std::endl; }
    ~circle() { std::cout << "~circle" << std::endl; }
};
class triangle : public shape {
public:
    triangle() { std::cout << "triangle" << std::endl; }
    ~triangle() { std::cout << "~triangle" << std::endl; }
};
class rectangle : public shape {
public:
    rectangle() { std::cout << "rectangle" << std::endl; }
    ~rectangle() { std::cout << "~rectangle" << std::endl; }
};
class result {
public:
    result() { std::cout << "result()" << std::endl; }
    ~result() { std::cout << "~result()" << std::endl; }
};
result process_shape(const shape &shape1, const shape &shape2) {
    std::cout << "process_shape()" << std::endl;
    return result();
}

```

### 无声明周期延长

在主程序中做如下的调用

```cpp
// call process_shape
void test_no_extend() {
    fprintf(stdout, "----- BEGIN of function %s -----\n", __FUNCTION__);
	process_shape(circle(), triangle());
    fprintf(stdout, "----- END of function %s -----\n\n", __FUNCTION__);
}
test_no_extend();
```

在调用函数`process_shape`之后，打印出来的顺序如下

```bash
----- BEGIN of function test_no_extend -----
shape
triangle
shape
circle
process_shape()
result()
~result()
~circle
~shape
~triangle
~shape
----- END of function test_no_extend -----
```

首先是构造`process_shape`的第二个参数`triangle()`，它是一个继承自`shape`的`class`，所以首先调用`shape`的构造函数，然后再调用`triangle`这个子类的构造函数。

其次是构造`process_shape`的第一个参数`circle()`，构造过程类似上述。

因为函数压栈是从左至右依次将参数压入堆栈，所以参数的构造顺序是从右至左。

之后`process_shape`函数内构造`result()`，在离开函数`process_shape`之后这个临时变量的作用域就结束了，所以调用`result`的析构函数。

等到`process_shape`调用完毕，按照临时变量的构造顺序的**逆序**，依次析构`circle`和`triangle`。



### 有声明周期延长

为方便对临时对象的使用，C++ 对临时对象有**特殊的生命周期延长规则**

- **如果一个 prvalue 被绑定到一个引用上，它的生命周期则会延长到跟这个引用变量一样长。**

需要**特别注意**的是，这个延长生命周期的规则只适用于`prvalue`，对于`xvalue`就无效了

如果在主程序中做如下的调用，把`process_shape`函数的返回值用一个右值引用来引用起来

```cpp
// call process_shape
void test_has_extend() {
    fprintf(stdout, "----- BEGIN of function %s -----\n", __FUNCTION__);
	result &&r = process_shape(circle(), triangle());
    fprintf(stdout, "----- END of function %s -----\n\n", __FUNCTION__);
}
test_no_extend();
```

那么打印的输出结果就是

```bash
----- BEGIN of function test_has_extend -----
shape
triangle
shape
circle
process_shape()
result()
~circle
~shape
~triangle
~shape
----- END of function test_has_extend -----

~result()
```

可以看到，直到`process_shape`函数构造`result`时的打印顺序都是一致的，但离开了`process_shape`函数的作用域之后，发现构造的临时对象`result()`并没有被析构，反而是等到了连传入`process_shape`的临时参数都析构了之后，在离开调用它的函数`test_has_extend`的时候，才被析构。



## 值类别 vs. 值类型

值类别和值类型（***value category*** vs ***value type***）

### 值类别 *Value Category*

- 指左值、右值相关的概念
  - 白话：就是左值还是右值
- 分为左值性（***lvaluenes***）和右值性（***rvalueness***）

### 值类型 *Value Type*

- 指引用类型（***reference type***），表示是否代表实际值，还是引用另外一个数值
  - 白话：就是引用还是非引用（值）

- 所有的原生类型、枚举、结构、联合、类都代表***值类型***，引用（`&`）和指针（`*`）是***引用类型***

**表达式的 lvalueness (左值性)或者 rvalueness (右值性)和它的类型无关。**

```cpp
Widget makeWidget();                       // factory function for Widget
 
Widget&& var1 = makeWidget()               // var1 is an lvalue, but
                                           // its type is rvalue reference (to Widget)
 
Widget var2 = static_cast<Widget&&>(var1); // the cast expression yields an rvalue, but
                                           // its type is rvalue reference  (to Widget)
```

`var1`：**类别**是左值，**类型**是右值引用

`static_cast<Widget&&>(var1)`：**类别**是右值，但**类型**是右值引用

从`lvalue`（左值）转换为`rvalue`（右值）的常规方式是使用`std::move`。



### 为何对右值引用使用移动语义？

```cpp
template<typename T>
class Widget {
    ...
    Widget(Widget&& rhs);        // rhs’s type is rvalue reference,
    ...                          // but rhs itself is an lvalue
};
```

上面`Widget`构造函数中，`rhs`是一个右值引用（值类型），但它本身是一个左值（值类别）。因为右值引用只能绑定到右值上，所以肯定是有个右值传入。

但`rhs`本身又是左值，所以如果想要使用到绑定到`rhs`上的右值（rvalue）的右值性（rvalueness）的时候，就需要用`std::move`把它转换回一个右值（rvalue）。转换的目的是想把它作为一个移动操作的source。



```cpp
template<typename T1>
class Gadget {
    ...
    template <typename T2>
    Gadget(T2&& rhs);            // rhs is a universal reference whose type will
    ...                          // eventually become an rvalue reference or
};                               // an lvalue reference, but rhs itself is an lvalue
```

上面的`Gadget`的构造函数中，`rhs`是一个万能引用（universal reference），它既可能绑定到一个右值上，也可能绑定到一个右值上，但因为`rhs`本身是一个具名变量，所以它的值类别是左值。

试想，如果`rhs`绑定到了一个右值上，当我们想利用它的右值性（rvalueness）的时候，我们就需要使用`std::move`把`rhs`转换回一个rvalue；但是如果`rhs`绑定到了一个左值上，那么我们就不想把它当做一个rvalue，自然也不想使用`std::mvoe`对它做转换。

**一个绑定到universal reference上的对象可能具有 lvalueness 或者 rvalueness，正是因为有这种二义性**，所以催生了`std::forward`。



## 万能引用与完美转发

Refer to [现代C++之万能引用、完美转发、引用折叠](https://zhuanlan.zhihu.com/p/99524127)

万能引用，即**Forwarding Reference**，a.k.a **Universal Reference**



### 符号`&&`

类型声明中，`&&`并不总意味着右值引用（rvalue reference），它实际上可以代表两种含义

- **rvalue reference，右值引用**
- **lvalue reference，左值引用**

就是说，有时候，`&&`看上去像是一个右值引用（rvalue reference），实际上却代表一个左值引用（lvalue reference，`&`）。



### 万能引用

万能引用（***Universal Reference***）又被叫做**转发引用**（***forwarding reference***），**它既可能是左值引用，又可能是右值引用**，有以下两种情况（*实际上还有其他情况，这里没展开说明*）

- **函数参数**是**`T &&`**, 且**`T`是这个函数模板的模板类型**（注意是**函数参数**！**函数参数**！）
- **`auto &&`**，并且不能是由初始化列表推断出来

```cpp
// Case 1
template<class T>
int f(T&& x) // x is a forwarding reference
{
    // ...
}

// Case 2
auto&& vec = foo();
```



### 如何区分是否为万能引用

因为`&&`在有的情况下可以表示***右值引用***，但有的时候又是***万能引用***，所以需要一定的规则去判断和区分。

一般地，万能引用（universal reference）有如下定义

> If a variable or parameter is declared to have type **T&&** for some **deduced type** `T`, that variable or parameter is a *universal reference*.
> 如果一个变量或者参数被声明为**T&&**，其中T是**被推导**的类型，那这个变量或者参数就是一个*universal reference*。

根据万能引用的特点，想要正确使用万能，就需要解答两个问题

- 如何区分一个引用（`&&`）是否是万能引用？
- 如果是万能引用，如何区分是左值引用还是右值引用？

下面继续介绍



#### 是否为万能引用？

记住：***只有在发生类型推导*** 的时候 **`&&`** 才代表 **universal reference**

- 一种最常见的情形

```cpp
template<typename T>
void f(T&& param);
```

这种情况，在调用函数`f`的时候，就需要推断参数`param`的类型，那么这时候`T&&`就是一个万能引用（但具体是左值引用还是右值引用，需要再根据下面的规则判断）

- 几个其他显而易见容易判断的例子

```cpp
template<typename T>
class Widget {
    // ...
    Widget(Widget&& rhs);        // fully specified parameter type ⇒ no type deduction;
    // ...                       // && ≡ rvalue reference
};
 

```

上面这个例子里面，虽然有类的模板参数`T`，但`Widget&& rhs`显然没有发生类型推导，所以`Widget&&`显然不是万能引用

```cpp
template<typename T1>
class Gadget {
    // ...
    template<typename T2>
    Gadget(T2&& rhs);            // deduced parameter type ⇒ type deduction;
    // ...                       // && ≡ universal reference
};
```

上面这个例子里面，类的模板参数是`T1`，除此之外，构造函数同时也是一个函数模板，它的参数是`T2&& rhs`，所以哪怕这个`Gadget`类已经实例化了，但构造一个`Gadget`类的对象，同样需要推导`rhs`的类型，所以这时候`T2&& rhs`就是一个万能引用。

```cpp
void f(Widget&& param);          // fully specified parameter type ⇒ no type deduction;
                                 // && ≡ rvalue reference
```

上面这个例子，显然没有发生类型推导，所以不是万能引用，仅仅是右值引用而已（虽然万能引用最后也可能是绑定到右值的右值引用）

- 容易混淆的几个例子

```cpp
template<typename T>
void f(std::vector<T>&& param);     // “&&” means rvalue reference
```

上面这个函数，这里，同时有类型推导和一个带“`&&`”的参数，但是参数确不具有 “`T&&`” 的形式，而是 “`std::vector<t>&&`”。其结果就是，参数就只是一个普通的rvalue reference，而不再是universal reference。

```cpp
template<typename T>
void f(const T&& param);               // “&&” means rvalue reference
```

上面这个函数，“`T&&`” 正是universal reference所需要的形式，但因为加了`const`，就不再是万能引用了。

```cpp
template <class T, class Allocator = allocator<T> >
class vector {
public:
    ...
    void push_back(T&& x);       // fully specified parameter type ⇒ no type deduction;
    ...                          // && ≡ rvalue reference
};
```

上面这个例子，`T`是模板参数，函数参数`T&& x`确实也具有`T&&`的形式，但它却不是universal reference。

这是因为，一旦`class vector`被实例化了之后，`T`的具体类型就被确定下来了，而此时`T&& x`就完全不需要推导类型，因此它并不是一个万能引用，而仅仅是一个rvalue reference。

举个例子如下，

```cpp
Widget makeWidget();             // factory function for Widget
std::vector<Widget> vw;
...
Widget w;
vw.push_back(makeWidget());      // create Widget from factory, add it to vw
```

代码中对 `push_back` 的使用会让编译器实例化类 `std::vector<Widget>` 相应的函数。这个`push_back` 的声明看起来就会像这样

```cpp
void std::vector<Widget>::push_back(Widget&& x);
```

所以，显然就不是一个万能引用了。

作为对比，`std::vector` 的`emplace_back`，它类似如下的代码片段

```cpp
template <class T, class Allocator = allocator<T> >
class vector {
public:
    ...
    template <class... Args>
    void emplace_back(Args&&... args); // deduced parameter types ⇒ type deduction;
    ...                                // && ≡ universal references
};
```

>Here, the type parameter Args is independent of vector’s type parameter T, so
>Args must be deduced each time emplace_back is called. (Okay, Args is really a
>parameter pack, not a type parameter, but for purposes of this discussion, we can
>treat it as if it were a type parameter.)
>
>—— *Effective Modern CPP*, Scott Meyers

正如上面引用中提到的，这里确实具有万能引用的形式（`Args&&`），而`args`实际上是一堆参数，而且在函数调用的时候，每个参数都需要被推导，所以，此时`Args&&`就是一个万能引用。



#### 万能引用 左值引用or右值引用？

因为万能引用也是**引用**，所以也是**引用**，而且正是万能引用的的initializer决定了它到底代表的是左值引用（lvalue reference）还是右值引用（ rvalue reference）

- **如果用来初始化universal reference的表达式是一个左值，那么universal reference就变成lvalue reference**
- **如果用来初始化universal reference的表达式是一个右值，那么universal reference就变成rvalue reference**

##### 举例1

根据前面的万能引用出现的情况，利用`auto`做如下举例

- Part 1中，`curf`是一个**右值引用**，所以它是**左值**（具名变量就是左值），那么用一个左值去初始化`auto &&r`，那么实际上得到的`r`，就是一个**左值引用**！而且可以取得其地址
- Part 2中，`v`是`std::vector`，而重载的运算符`operator[]`返回的实际上是一个**左值引用**(rvalue ref)，即一个左值，所以实际上`auto &&val`是用一个左值去初始化的，所以实际上`val`同样是一个**左值引用**！而且可以取得其地址

```cpp
// static foo foo::get_foo() { return foo(); }
// Part 1
foo &&curf = foo::get_foo();
auto &&r = curf;
fprintf(stdout, "The address of r is %p\n", &r); // 0x00000000003cf640

// Part 2
std::vector<int> v{-1, 0, 1};
auto &&val = v[0];
fprintf(stdout, "The address of val is %p\n", &val); // 0x0000000000419f10
```



##### 举例2

使用 *template function* 做举例，定义一个带有 *universal reference* （万能引用）的模板函数如下，

```cpp
template<typename T>
void show_universal_reference_with_str(T &&param, const char *s) {
    constexpr const bool is_lr = std::is_lvalue_reference<decltype(param)>::value;
    constexpr const bool is_rr = std::is_rvalue_reference<decltype(param)>::value;
    constexpr const bool is_intgl = std::is_integral<decltype(param)>::value;

    constexpr const bool is_T_lr = std::is_lvalue_reference<T>::value;
    constexpr const bool is_T_rr = std::is_rvalue_reference<T>::value;
    constexpr const bool is_T_intgl = std::is_integral<T>::value;

    fprintf(stdout, "Parameter type info (param = %s)\n", s);
    fprintf(stdout, "  param is: lvalue ref(%s)", is_lr ? "1" : "0");
    fprintf(stdout, " rvalue ref(%s)", is_rr ? "1" : "0");
    fprintf(stdout, " integral(%s)\n", is_intgl ? "1" : "0");
    fprintf(stdout, "      T is: lvalue ref(%s)", is_T_lr ? "1" : "0");
    fprintf(stdout, " rvalue ref(%s)", is_T_rr ? "1" : "0");
    fprintf(stdout, " integral(%s)\n", is_T_intgl ? "1" : "0");
} // show_universal_reference_with_str

#define SHOW_UNI_REF(v) show_universal_reference_with_str(v, #v)
```

调用如下函数

```cpp
void test_show_lr_ref() {
    int x = 10; int &&a = 13; int &b = x; int m = 19;

    SHOW_UNI_REF(a); SHOW_UNI_REF(b);  SHOW_UNI_REF(x);
    SHOW_UNI_REF(std::move(x)); SHOW_UNI_REF(static_cast<int&&>(x));
    SHOW_UNI_REF(14);

    foo &&curf = foo::get_foo(); SHOW_UNI_REF(curf);
    SHOW_UNI_REF(foo::get_foo());

    auto &&r = curf; SHOW_UNI_REF(r);

    std::vector<int> v{-1, 0, 1}; SHOW_UNI_REF(v[0]);
    auto &&val = v[0]; SHOW_UNI_REF(val);

} // test_show_lr_ref

test_show_lr_ref();
```

得到如下的打印输出

```bash
Parameter type info (param = a)
  param is: lvalue ref(1) rvalue ref(0) integral(0)
      T is: lvalue ref(1) rvalue ref(0) integral(0)
Parameter type info (param = b)
  param is: lvalue ref(1) rvalue ref(0) integral(0)
      T is: lvalue ref(1) rvalue ref(0) integral(0)
Parameter type info (param = x)
  param is: lvalue ref(1) rvalue ref(0) integral(0)
      T is: lvalue ref(1) rvalue ref(0) integral(0)
Parameter type info (param = std::move(x))
  param is: lvalue ref(0) rvalue ref(1) integral(0)
      T is: lvalue ref(0) rvalue ref(0) integral(1)
Parameter type info (param = static_cast<int&&>(x))
  param is: lvalue ref(0) rvalue ref(1) integral(0)
      T is: lvalue ref(0) rvalue ref(0) integral(1)
Parameter type info (param = 14)
  param is: lvalue ref(0) rvalue ref(1) integral(0)
      T is: lvalue ref(0) rvalue ref(0) integral(1)
Parameter type info (param = curf)
  param is: lvalue ref(1) rvalue ref(0) integral(0)
      T is: lvalue ref(1) rvalue ref(0) integral(0)
Parameter type info (param = foo::get_foo())
  param is: lvalue ref(0) rvalue ref(1) integral(0)
      T is: lvalue ref(0) rvalue ref(0) integral(0)
Parameter type info (param = r)
  param is: lvalue ref(1) rvalue ref(0) integral(0)
      T is: lvalue ref(1) rvalue ref(0) integral(0)
Parameter type info (param = v[0])
  param is: lvalue ref(1) rvalue ref(0) integral(0)
      T is: lvalue ref(1) rvalue ref(0) integral(0)
Parameter type info (param = val)
  param is: lvalue ref(1) rvalue ref(0) integral(0)
      T is: lvalue ref(1) rvalue ref(0) integral(0)
```

对于`a`，`b`而言，虽然它们分别是左值引用和右值引用，但这是它们的类型（value type），而它们的类别（value category）依然是左值，所以万能引用是被一个左值初始化，所以万能引用被推导为左值引用。

对于`x`，它显然是一个左值，所以万能引用被推导为左值引用。

对于`std::move(x)`，它把`x`转换为了一个右值，所以万能引用被推导为右值引用。

同样地，`static_cast<int&&>(x)`把`x`转换为了一个右值，所以万能引用被推导为右值引用。

对于`14`，它是一个右值，所以万能引用被推导为右值引用。

对于`curf`，类似上面的`a`和`b`，它是一个右值引用，但这是它的类型（value type），而它的类别（value category）依然是左值，所以万能引用是被一个左值初始化，所以万能引用被推导为左值引用。

对于`foo::get_foo()`，它返回一个右值，那么万能引用是被一个右值初始化，所以万能引用被推导为右值引用。

对于`r`，这里出现了两处万能引用，首先是`auto &&r = curf`，这表明`r`是被一个左值初始化，所以`r`被推导为一个左值引用。当然它本身也是一个左值，当它再被传入模板函数时，万能引用就被推导为左值引用。

对于`v[0]`，它是`vector`的一个重载成员函数，返回一个左值引用。同样地不管左值引用还是右值引用，它们本身也是一个左值，所以传入模板函数时，万能引用就被推导为左值引用。

对于`val`，这里也出现了两处万能引用，首先是`auto &&val = v[0]`，这表明`val`是被一个左值初始化，所以`val`被推导为一个左值引用。当然它本身也是一个左值，当它再被传入模板函数时，万能引用就被推导为左值引用。



### 万能引用模板参数类型推导

概况地，同一个类型的 ***lvalue*** 和 ***rvalue*** 会被推导为不同的类型。这可能会导致编译器遇到出现 ***引用的引用*** 这个问题。（C++98和C++03标准里面对引用的引用会报错）

具体地

- 类型为`T`的 ***lvalue*** 被推导为`T&`（即 lvalue reference to `T`）
- 类型为`T`的 ***rvalue*** 被推导为`T`（注意，不是rvalue reference）

举例，如果有如下的函数模板，其参数为一个万能引用。

```cpp
template<typename T>
void f(T&& param);
```

如果有如下的调用

```cpp
int x;
f(10); // invoke f on rvalue
f(x);  // invoke f on lvalue
```

当使用 ***rvalue 10***，来调用函数`f`的时候，`T` 被推导为`int`，实例化的`f`看起来如下

```cpp
void f(int&& param); // f instantiated from rvalue
```

但是当我们用 ***lvalue x*** 来调用 `f` 的时候，`T` 被推导为`int&`，而实例化的 `f` 就包含了一个引用的引用:

```cpp
void f(int& && param);           // initial instantiation of f with lvalue
```

这里出现了***引用的引用*** ，为了解决这个问题，**C++11** 引入了引用折叠（***Reference Collapsing***）。



### 引用折叠

#### 引用折叠的规则

引用折叠，即 ***Reference Collapsing***，是为了解决可能出现的 ***引用的引用*** 这个问题。

因为有**lvalue reference** 以及 **rvalue reference**，所以**引用的引用**就有四种组合

- **lvalue** reference to **lvalue** reference
- **lvalue** reference to **rvalue** reference
- **rvalue** reference to **lvalue** reference
- **rvalue** reference to **rvalue** reference

这些引用会按照一定的规则最终折叠起来

- **右值引用的右值引用**折叠为**右值引用**
  - An rvalue reference to an rvalue reference will be collapsed to an rvalue reference

- 其他所有类型折叠为**左值引用** （lvalue reference）
  - 即组合当中含有**左值引用**的


两种情况下允许出现**引用的引用**

- **模板**
- **typedef**

举例

```cpp
typedef int&  lref;
typedef int&& rref;
int n;

lref&  r1 = n; // type of r1 is int&
lref&& r2 = n; // type of r2 is int&
rref&  r3 = n; // type of r3 is int&
rref&& r4 = 1; // type of r4 is int&&
```



#### 引用折叠出现的情况

实际上，在前面如何区分万能引用被推导为左值引用和右值引用的时候，也可以使用引用折叠来解释。

##### 出现于万能引用函数参数处



##### 出现于`auto`处

出现于`auto`处的引用折叠

```cpp
Widget&& var1 = someWidget;      // var1 is of type Widget&& (no use of auto here)
auto&& var2 = var1;              // var2 is of type Widget& (see below)
```

如上面举例，`var1` 是一个右值引用，它被用来初始化一个`auto &&`。

- 按照之前的解释，`var1`虽然是一个右值引用，但它本身也是一个左值，所以用左值初始化一个万能引用，得到的就是一个左值引用。
- 如果按照引用折叠解释，`var1`是一个引用，当用引用去初始化一个万能引用的时候，类型中所带的引用就被忽略带，所以`var1`就被当做`Widget`来看待，而它是一个左值，所以得到的就是一个左值引用。



##### 出现于`typdef`处

出现于`typedef`处的引用折叠

```cpp
template<typename T>
class foo2 {
public:
    typedef T& LvalueRefType;
    typedef T&& RvalueRefType;
public:
    void judge_0() {
        static_assert(std::is_lvalue_reference<LvalueRefType>::value,
                        "LvalueRefType & is lvalue ref");
        static_assert(std::is_lvalue_reference<RvalueRefType>::value,
                        "RvalueRefType & is lvalue ref");
        fprintf(stdout, "LvalueRefType and RvalueRefType is lvalue ref\n");
    }
    void judge_1() {
        static_assert(std::is_lvalue_reference<LvalueRefType>::value,
                        "LvalueRefType & is lvalue ref");
        static_assert(std::is_rvalue_reference<RvalueRefType>::value,
                        "RvalueRefType & is rvalue ref");
        fprintf(stdout, "LvalueRefType is lvalue ref and RvalueRefType is rvalue ref\n");
    }
}; // class foo2
```

在如下函数中创建对象并分别调用函数`judge_0`和`judge_1`

```cpp
void test_ref_collapse() {
    foo2<int&> myf1;
    myf1.judge_0();
    // myf1.judge_1(); // Compiler will issue an static_assert error

    foo2<int&&> myf2;
    // myf2.judge_0(); // Compiler will issue an static_assert error
    myf2.judge_1();
}
```

根据引用折叠的规则，只要带有左值引用的（`lvalue reference`）的，都最终会被折叠为**左值引用**；而只有右值引用的右值引用会折叠为**右值引用**。

因为`myf1`的模板参数类型是`int&`，所以实际上`LvalueRefType`和`RvalueRefType`都是左值引用，因此它可以调用函数`myf1.judge_0()`，但是不能调用`myf1.judge_1()`，因为`myf1.judge_1()`中断言`RvalueRefType`为右值引用（但实际上它在此处为左值引用）。

因为`myf2`的模板参数类型是`int&&`，所以根据引用折叠规则，`LvalueRefType`是左值引用，而`RvalueRefType`是右值引用，因此它可以调用函数`myf1.judge_1()`，但是不能调用`myf1.judge_0()`，因为`myf1.judge_0()`中断言`RvalueRefType`为左值引用（但实际上它在此处为右值引用）。



##### 出现于`decltype`处

`decltype` 对表达式进行类型推导时候可能会返回 `T` 或者 `T&`，然后`decltype` 会应用 C++11 的引用折叠规则。

但实际上，`decltype` 的类型推导规则其实和模板或者 `auto` 的类型推导不一样，即 `decltype` 对一个具名的、非引用类型的变量，会推导为类型 `T` (i.e., 一个非引用类型)，在相同条件下，`模板`和 `auto` 却会推导出 `T&`。

这里的细节比较隐晦，参见 [Universal References in C++11 -- Scott Meyers](https://isocpp.org/blog/2012/11/universal-references-in-c11-scott-meyers#FurtherInformation)。



### `std::remove_reference`

`std::remove_reference`的（可能）[实现](https://en.cppreference.com/w/cpp/types/remove_reference)，以及左值引用和右值引用的特化（specialization）版本

```cpp
template< class T > struct remove_reference      { typedef T type; };
// Specialization for lvalue reference
template< class T > struct remove_reference<T&>  { typedef T type; };
// Specialization for rvalue reference
template< class T > struct remove_reference<T&&> { typedef T type; };
```

可见，`remove_reference`的作用是去除`T`中的引用部分，只获取其中的类型部分。

无论`T`是左值还是右值，最后只获取它的类型部分。



### 完美转发

在STL中，完美转发由`std::forward`实现。

在文件`./c++/10.3.0/bits/move.h`中，有定义`std::forward`和`std::move`的源代码

#### `std::forward`转发左值

```cpp
/**
 *  @brief  Forward an lvalue.
 *  @return The parameter cast to the specified type.
 *
 *  This function is used to implement "perfect forwarding".
 */
template<typename _Tp>
  constexpr _Tp&&
  forward(typename std::remove_reference<_Tp>::type& __t) noexcept
  { return static_cast<_Tp&&>(__t); }
```

在转发**左值**的源代码中，参数`__t`实际上接收的是一个**左值引用**，因为`std::remove_reference<_Tp>::type`就是不带有引用的类型（见前面的`std::remove_reference`）。

这就导致`_Tp`被推导为**左值引用**，即`_Tp&`，这样就导致在`return`语句中的引用折叠为`_Tp& &&`，根据引用折叠的规则，它会被折叠为一个**左值引用**，即`_Tp&`。

同样地，返回值的引用折叠为`_Tp& &&`，同样地，根据引用折叠的规则，它会被折叠为一个**左值引用**，即`_Tp&`。



#### `std::forward`转发右值

```cpp
/**
 *  @brief  Forward an rvalue.
 *  @return The parameter cast to the specified type.
 *
 *  This function is used to implement "perfect forwarding".
 */
template<typename _Tp>
  constexpr _Tp&&
  forward(typename std::remove_reference<_Tp>::type&& __t) noexcept
  {
    static_assert(!std::is_lvalue_reference<_Tp>::value, "template argument"
          " substituting _Tp is an lvalue reference type");
    return static_cast<_Tp&&>(__t);
  }
```

在转发**右值**的源代码中，参数`__t`实际上接收的是一个**右值引用**，因为`std::remove_reference<_Tp>::type`就是不带有引用的类型（见前面的`std::remove_reference`）。

这就导致`_Tp`被推导为**右值引用**，即`_Tp&&`，这样就导致在`return`语句中的引用折叠为`_Tp&& &&`，根据引用折叠的规则，它会被折叠为一个**右值引用**，即`_Tp&&`。

同样地，返回值的引用折叠为`_Tp& &&`，同样地，根据引用折叠的规则，它会被折叠为一个**右值引用**，即`_Tp&`。



#### `std::move`

STL中`std::move`的源代码

```cpp
/**
 *  @brief  Convert a value to an rvalue.
 *  @param  __t  A thing of arbitrary type.
 *  @return The parameter cast to an rvalue-reference to allow moving it.
 */
template<typename _Tp>
  constexpr typename std::remove_reference<_Tp>::type&&
  move(_Tp&& __t) noexcept
  { return static_cast<typename std::remove_reference<_Tp>::type&&>(__t); }
```

传入参数`__t`是一个万能引用，它会根据传入参数的左右值性（lvalueness or rvalueness）而得出该参数是一个左值引用（绑定到左值）还是右值引用（绑定到右值）。

根据前面`std::remove_reference`的作用，实际上根据`__t`的引用类型，不管是左值引用`_Tp&`还是右值`_Tp&&`，都会得出`std::remove_reference<_Tp>::type&&`是一个**右值引用**，因为`std::remove_reference<_Tp>::type` 是一个不带有引用的类型。

同样地，返回值的类型也是一个**右值引用**。

综上所述，`std::move` 实现了将传入的左值或右值强制转换为**右值引用**的功能。



## `&&`的部分总结

> （1）在类型声明当中， `&&`  要不就是一个 rvalue reference ，要不就是一个 *universal reference* – 一种可以解析为 lvalue reference 或者 rvalue reference的引用。对于某个被推导的类型`T`，universal references 总是以 `T&&` 的形式出现。
>
> （2）*引用折叠*是 会让 universal references （其实就是一个处于引用折叠背景下的 rvalue references ) 有时解析为 lvalue references 有时解析为 rvalue references 的根本机制。引用折叠只会在一些特定的可能会产生"引用的引用"场景下生效。 这些场景包括模板类型推导，`auto` 类型推导， `typedef` 的形成和使用，以及`decltype` 表达式。
>
> （3）`std::move` 与 `std::forward`本质都是`static_cast`转换，**对于右值引用使用`std::move`，对于万能引用使用`std::forward`**。`std::move` 解决的问题是对于一个本身是左值的右值引用变量需要绑定到一个右值上，所以需要使用一个能够传递右值的工具，而 `std::move` 就干了这个事。而 `std::forward` 解决的问题是一个绑定到 universal reference 上的对象可能具有 lvalueness 或者 rvalueness，正是因为有这种二义性，所以催生了`std::forward`: 如果一个本身是 左值 的 万能引用如果绑定在了一个 右边值 上面，就把它重新转换为右值。函数的名字 (“`forward`”) 的意思就是。**我们希望在传递参数的时候，可以保存参数原来的lvalueness 或 rvalueness，即是说把参数转发给另一个函数。**
>
> （4）移动语义使得在 C++ 里返回大对象（如容器）的函数和运算符成为现实，因 而可以提高代码的简洁性和可读性，提高程序员的生产率。
>
> 
>
> ​                                                                                        ——*引用自 [现代C++之万能引用、完美转发、引用折叠](https://zhuanlan.zhihu.com/p/99524127)*







## 真正实现资源转移

### 右值引用重载函数 + 移动语义

如前所述，**单纯的 move 不会有任何的资源转移**，如要实现真正的资源转移，必须要配合如下两者来完成：

- **使用带有右值引用的重载函数**
- **使用`std::move`语义**

### 例子说明

可以查看源文件代码：[`lvalue_rvalue.hpp`](https://github.com/Pyrad/cpp11/blob/master/src/cppfeatures/lvalue_rvalue.hpp)

定义两个`class`如下，第一个类`char_string`和第二个类`char_string`的唯一区别是：第二个类有一个**参数是右值引用的重载的构造函数**（即**移动构造函数**）

```cpp
class char_string {
public:
    char_string(const char *s, const int len) {
        m_len = len;
        m_ptr = (char*)malloc(m_len);
        memcpy(m_ptr, s, m_len);
        fprintf(stdout, "Constructor of char_string(%s)\n", m_ptr);
    }

    char_string(const char_string &cs) {
        m_len = cs.len();
        m_ptr = (char*)malloc(m_len);
        memcpy(m_ptr, cs.ptr(), m_len);
        fprintf(stdout, "Copy constructor of char_string(%s)\n", m_ptr);
    }

    ~char_string() { if (m_ptr) { free(m_ptr); } }

public:
    char * ptr() const { return m_ptr; }
    int len() const { return m_len; }

protected:
    char *m_ptr;
    int m_len;
}; // class char_string

class char_string2 {
public:
    char_string2(const char *s, const int len) {
        m_len = len;
        m_ptr = (char*)malloc(m_len);
        memcpy(m_ptr, s, m_len);
        fprintf(stdout, "Constructor of char_string2(%s)\n", m_ptr);
    }

    char_string2(const char_string2 &cs) {
        m_len = cs.len();
        m_ptr = (char*)malloc(m_len);
        memcpy(m_ptr, cs.ptr(), m_len);
        fprintf(stdout, "Copy constructor of char_string2(%s)\n", m_ptr);
    }

    char_string2(char_string2 &&cs) {
        m_len = cs.len();
        m_ptr = cs.ptr();
        cs.reset_ptr();
        fprintf(stdout, "Move constructor of char_string2(%s)\n", m_ptr);
    }

    ~char_string2() { if (m_ptr) { free(m_ptr); } }

public:
    char * ptr() const { return m_ptr; }
    int len() const { return m_len; }
    void reset_ptr() { m_ptr = nullptr; }

protected:
    char *m_ptr;
    int m_len;
}; // class char_string2
```



然后如下调用

```cpp
void test_resource_move() {
    // test 1
    std::vector<char_string> cvec;
    char_string tmp("dogs", 4);
    cvec.push_back(tmp);
    cvec.clear();

    // test 2
    std::vector<char_string2> cvec2;
    char_string2 tmp2("cats", 4);
    cvec2.push_back(tmp2);
    cvec2.clear();

    // test 3
    char_string2 tmp3("fish", 4);
    cvec2.push_back(std::move(tmp3));
    cvec2.clear();

} // test_resource_move
```

得到的结果如下

```bash
Constructor of char_string(dogs)
Copy constructor of char_string(dogs)
Constructor of char_string2(cats)
Copy constructor of char_string2(cats)
Constructor of char_string2(fish)
Move constructor of char_string2(fish)
```

可以看到

- `test 1`

  因为`char_string`没有移动构造函数，所以向`cvec`中`push_back`的时候，实际上调用的是`push_back(const & T)`，那么就会在里面调用`char_string`的**拷贝构造函数**。

- `test 2`

  虽然`char_string2`有移动构造函数，但传入`push_back`的是一个左值，所以只会调用`push_back`的左值引用的重载函数，即`push_back(const & T)`，那么同样的，里面调用的仍然是`char_string2`的**拷贝构造函数**。

- `test 3`

  这次向`push_back`**传入的是一个右值**，而`std::vector::push_back`**提供了右值引用的重载函数**，所以实际上调用的是`push_back(&& T)`，那么里面就会调用`char_string2`的**移动构造函数**。

所以，必须要**右值引用重载函数 + 移动语义**两者配合使用，才能真正实现资源的转移。











## 何时实现移动构造函数？

- 移动构造函数对比拷贝构造函数而言，**大多数地方都是相同的复制操作**

- **只有堆上的资源，才能复用旧的对象的资源**
- 为何**栈上**的资源不能复用，而要重新复制一份？
  - 因为你不知道旧的对象何时析构，**旧的对象一旦析构，其栈上所占用的资源也会完全被销毁掉，新的对象如果复用的这些资源就会产生崩溃。**
- 为什么**堆上**的资源可以复用，从而不必重新复制一份？
  - 因为**堆上的资源不会自动释放**，除非你手动去释放资源。

### 总结

因此，只有当自己定义的类**申请到了堆上的内存资源**的时候，才需要专门实现**移动构造函数**，否则其实没有必要，因为**他的消耗跟拷贝构造函数是一模一样的。**







## Reference Pages

- [Microsoft - Lvalues and Rvalues (C++)](https://docs.microsoft.com/en-us/cpp/cpp/lvalues-and-rvalues-visual-cpp?view=msvc-170)
- [Is it possible to print a variable's type in standard C++?](https://newbedev.com/is-it-possible-to-print-a-variable-s-type-in-standard-c/#)
- [Modern-cpp-tutorial on the fly by changkun](https://github.com/changkun/modern-cpp-tutorial)
-  [现代C++之万能引用、完美转发、引用折叠](https://zhuanlan.zhihu.com/p/99524127)
- [右值引用与移动语义](https://zhuanlan.zhihu.com/p/545494408)
- [C++编译期获得完整类型名称](https://zhuanlan.zhihu.com/p/443591951)
- [C++ 生成式的编译期类型名](https://zhuanlan.zhihu.com/p/336243278)
- [c++中返回值优化（RVO）和命名返回值优化（NRVO）介绍](https://blog.csdn.net/lr_shadow/article/details/123332927)
- 

