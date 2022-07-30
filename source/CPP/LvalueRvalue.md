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



### 万能引用与完美转发

Refer to [现代C++之万能引用、完美转发、引用折叠](https://zhuanlan.zhihu.com/p/99524127)

### 引用折叠

两种情况下允许出现**引用的引用**

- **模板**
- **typedef**

这些引用会按照一定的规则最终折叠起来

- **右值引用的右值引用**折叠为**右值引用**
- 其他所有类型折叠为**左值引用**

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





### 万能引用 （Forwarding Reference，a.k.a Universal Reference）

#### &&

类型声明中，`&&`并不总意味着右值引用（rvalue reference），它实际上可以代表两种含义

- **rvalue reference，右值引用**
- **lvalue reference，左值引用**

就是说，有时候，`&&`看上去像是一个右值引用（rvalue reference），实际上却代表一个左值引用（lvalue reference，`&`）。



#### 万能引用

万能引用（Universal Reference）又被叫做**转发引用**，**它既可能是左值引用，又可能是右值引用**，有以下两种情况

- 函数参数是**`T &&`**, 且**`T`是这个函数模板的模板类型**
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



#### 万能引用出现的情况

> If a variable or parameter is declared to have type **T&&** for some **deduced type** `T`, that variable or parameter is a *universal reference*.
> 如果一个变量或者参数被声明为**T&&**，其中T是**被推导**的类型，那这个变量或者参数就是一个*universal reference*。

因为万能引用也是**引用**，所以也是**引用**，而且正是万能引用的的initializer决定了它到底代表的是左值引用（lvalue reference）还是右值引用（ rvalue reference）

- 如果用来初始化universal reference的表达式是一个左值，那么universal reference就变成lvalue reference
- 如果用来初始化universal reference的表达式是一个右值，那么universal reference就变成rvalue reference
