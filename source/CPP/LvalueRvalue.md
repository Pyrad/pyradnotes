# 右值引用与移动语义

Reference page: [右值引用与移动语义](https://zhuanlan.zhihu.com/p/545494408)

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
- 返回非引用的函数或操作符重载的调用语句。
- **后缀自增自减**是右值：`a++`, `a--`
- `a+b`, `a << b` 等一般表达式
- `&a`，对变量取地址的表达式是右值
- `this`指针
- `lambda`表达式

理解也很简单，其实就是一些**运算时的中间值**，**这些值只存在寄存器中辅助运算**，**不会实际写到内存地址空间中**，因此也无法对他们取地址。



## 将亡值（xvalue）

### 概念

**xvalue** 叫将亡值，顾名思义，就是即将销毁的东西。**xvalue** 也是**右值**的一种。

### 常见的两种xvalue

主要记住这两种就行了：

- 返回**右值引用**的函数或者操作符重载的调用表达式。
  - 如某个函数返回值是 **`std::move(x)`**并且函数返回类型是 **`T&&`**
- 目标为**右值引用**的类型转换表达式
  - 如 **`static<int&&>(a)`**

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

