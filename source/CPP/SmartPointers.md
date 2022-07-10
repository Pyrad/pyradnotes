# Smart Pointers

This file shows some usages of smart pointers in C/C++



## Reference

Reference articles: [C++ STL 四种智能指针](https://blog.csdn.net/K346K346/article/details/81478223)



---

## std::unique_ptr\<T\>

- 旨在代替旧的`auto_ptr`

- 需`#include <memory>`头文件

- 只能通过移动语义来转移所管理对象的管理权

  - 可以通过`make_unique`这个helper函数来构造

    ```cpp
    auto ptrA = std::make_unique<string>("dablelv")
    ```

  - 能通过移动语义转移管理权

    ```c++
    auto ptrB = std::move(ptrA)
    ```

  - 不能赋值到其他`std::unique_ptr`

  - 不能值传递到函数中（无法作为函数参数，因为要值传递）

  - 不能用于需要副本的`STL`算法

  - **例外**：**如果unique_ptr 是个临时右值，编译器允许拷贝语义**

- 基本操作

  ```cpp
  // 创建空指针
  std::unique_ptr<int> u_i;
  // 绑定动态对象
  u_i.reset(new int(3));
  // 创建时绑定对象
  std::unique_ptr<int> u_i2(new int(4));
  // 指向类型为T的指针，用类型为D的对象d来代替默认的删除器
  std::unique_ptr<T, D> u(d)
  
  // 释放所有权
  int *p_i = u_i2.release();
  // 转移所有权
  std::unique_ptr<string> u_s(new string("abc"));
  std::unique_ptr<string> u_s2 = std::move(u_s);
  // 转移所有权
  u_s2.reset(u_s.release());
  // 显示销毁对象，相当于rest()
  u_s2 = nullptr;
  
  ```


- 需要注意的是，如果`std::unique_ptr`通过移动语义转移了所有权之后，原先的对象也不能再直接访问了，因为已经置空了。保险起见，此时应该加入判断空的条件防止出错。

  ```cpp
  std::unique_ptr<string> u0(new string("abc"));
  std::unique_ptr<string> u1 = std::move(u0);
  if (u0.get() != nullptr) {
      // do something
  }
  ```

- `std::uniqute_ptr<T>`禁止了拷贝语义（试图拷贝时编译会报错），但如果是临时右值的话，编译器允许拷贝语义。

  ```cpp
  std::unique_ptr<string> demo(const char *s) {
      std::unique_ptr<string> temp(new string(s));
      return temp; // 临时变量，右值
  }
  
  std::unique_ptr<string> ps;
  ps = demo('Unique Special Case') // 此时允许拷贝
  ```

- `std::uniqute_ptr<T>`可以管理动态数组，因为它有`std::uniqute_ptr<T[]>`的重载版本，销毁动态对象时使用`delete T[]`

  ```cpp
  std::uniqute_ptr<int []> p(new int[3]{0, 1, 2});
  p[0] = 0; // 重载了operator[]
  ```

- `std::uniqute_ptr<T, D>`可以自定义删除操作（deleter）

  ```cpp
  // clean up function
  void final_clean(Resource *p) { release_resource(p); }
  // 传入函数名，自动转换为函数指针
  std::uniqute_ptr<Resource, decltype(final_clean)*> p(&c, final_clean);
  ```

  

---

## std::auto_ptr\<T\>

- `std::auto_ptr`现已摒弃不再使用
- `std::auto_ptr`没有禁止拷贝语义，赋值给新的`std::auto_ptr`之后，原先对象会失效，如果此时再去访问原先的对象，就会在运行时产生错误，造成程序崩溃。（`std::unique_ptr`就是禁止了拷贝语义来改善这种情况）
- `std::auto_ptr`不能放在容器中





## std::shared_ptr\<T\>

### Basics

- 被Effective C++称为“引用计数型智能指针”（Reference Counting Smart Pointer，RCSP）

- 基本原理

  - 每个shared_ptr对象内部维护**两个指针**
    - 第一个**指针**是指向所管理的对象
    - 第二个**指针**是指向所管理对象的引用计数（注意，这个计数值以指针的方式保存，方便操作）


  - 一个简单的示意`SharedPtr`类（仅原理示意）

  ```cpp
  templat<typename T>;
  class SharedPtr {
  public:
      // ...
  private:
      T *_ptr;        // point to a managed object
      int *_refCount; //should be int*, rather than int
  };
  ```

- 特性

  - （**默认构造函数**）创建`shared_pt`新对象，不绑定普通指针，初始化指针，引用计数设置为`0`

    ```cpp
    ~SharedPtr() : _ptr((T *)0), _refCount(0) {}
    ```

    

  - （**构造函数**）创建`shared_pt`新对象，绑定普通指针，初始化指针，引用计数设置为`1`

    ```cpp
    explicit SharedPtr(T *obj) : _ptr(obj), _refCount(new int(1)) {}
    ```

    

  - （**析构函数**）`shared_ptr`对象离开作用域，通过析构函数来释放所管理的内存，但在释放之前会坚持引用计数，只有其为0时才释放

    ```cpp
    // check ref count when destructing
    ~SharedPtr() {
        if (_ptr && --*_refCount == 0) { delete _ptr; delete _refCount; }
    }
    ```

    

  - （**拷贝构造函数**）用一个`shared_ptr`对象初始化另外一个`shared_ptr`对象，引用计数加一，并且指针指向同一片内存

    ```cpp
    SharedPtr(SharedPtr &other) :
    	_ptr(other._ptr), _refCount(&(++*other._refCount))
    ```

    

  - （**赋值运算符重载**）用一个`shared_ptr`对象给另外一个`shared_ptr`对象**赋值**（`=`)，有两步

    - `this`所保存的指针`_ptr`因为要变成指向`other`所保存的指针`_ptr`，所以赋值之前，要将原先的`_refCount`自减`1`（并且检查自减之后是否为`0`，如为`0`，则释放原先的内存）
    - `this->_ptr`要被赋值为`other->_ptr`，所以`other`所指向的`_refCount`要自增`1`

    ```cpp
    SharedPtr &operator=(SharedPtr &other){
        if(this == &other) { return *this; }
    
        ++*other._refCount;
        if (--*_refCount == 0) { delete _ptr; delete _refCount; }
    
        _ptr = other._ptr;
        _refCount = other._refCount;
        return *this;
    }
    ```

    

  - 解引用运算符`*`：直接返回底层引用

    ```cpp
    T &operator*() {
        if (_refCount == 0) { return (T*)0; } // or throw exception
        return *_ptr;
    }
    ```

    

  - 指针运算符`->`：

    ```cpp
    T *operator->() {
        if(_refCount == 0) { return 0; } // or throw exception
        return _ptr;
    }
    ```

    

- 额外的开销

  - `std::shared_ptr<T>`对象包含一个对象的指针，和一个引用计数对象的指针。
  - 时间开销主要在初始化和拷贝操作上，`*`和`->`操作符的开销和`auto_ptr`相同



### Member Functions (Part)

|   Function    |       Use       |
| :-----------: | :-------------: |
|    `get()`    |                 |
|   `reset()`   |                 |
| `use_count()` |                 |
|  `unique()`   | Check if unique |



### Non-Member Functions (Part)

|        Function         |                   Use                    |
| :---------------------: | :--------------------------------------: |
|        `swap()`         | Exchange content of `shared_ptr` objects |
|     `make_shared()`     |            Make `shared_ptr`             |
| `static_pointer_cast()` |       Static cast of `shared_ptr`        |
|     `get_deleter()`     |      Get deleter from `shared_ptr`       |





## std::weak_ptr\<T\>

### 基本特性

- 主要用来配合`shared_ptr`使用，可以解决循环引用的问题
- `weak_ptr`可以像旁观者一样观察资源的使用情况，查看`shared_ptr`所引用的资源计数，但它`weak_ptr`本身不变引用计数
- `weak_ptr`必要时可以通过`lock()`生成一个对应的`shared_ptr`来获得资源的管理权（计数+1）
- `weak_ptr`可以被另一个`weak_ptr`或`shared_ptr`赋值（`=`)



### 基本用法

```cpp
// 创建空的weak_ptr，指向类型为T的对象
std::weak_ptr<T> w;
// 与shared_ptr指向相同的对象，但shared_ptr的计数不变
// T必须是可以转换成sp所指向的类型
std::weak_ptr<T> w(sp);
// w是weak_ptr，p可以是weak_ptr或shared_ptr
// 赋值后w和p共享对象，但p这个shared_ptr的计数不增加
w = p;
// 置空
w.reset();
// 返回和w共享的对象的shared_ptr的数量
w.use_count();
// 如果w.use_count()为0，返回true，否则返回false
w.expired();
// 如果w.expired()返回true，则返回一个空的shared_ptr
// 否则返回非空的shared_ptr
w.lock();
```



### weak_ptr配合shared_ptr解决循环引用

#### 循环引用问题示例

假如有两个`class`，它们分别有一个指向对方的`shared_ptr`作为自己的data member。

```cpp
class CircularTestB;
class CircularTestA {
public:
    CircularTestA() { std::cout << "Constructing CircularTestA\n"; }
    ~CircularTestA() { std::cout << "Destructing CircularTestA\n"; }
    void set_ptr(const std::shared_ptr<CircularTestB> &p) { m_ptr = p; }

private:
    // std::weak_ptr<CircularTestB> m_ptr;
    std::shared_ptr<CircularTestB> m_ptr;
}; // class CircularTestA

class CircularTestB {
public:
    CircularTestB() { std::cout << "Constructing CircularTestB\n"; }
    ~CircularTestB() { std::cout << "Destructing CircularTestB\n"; }
    void set_ptr(const std::shared_ptr<CircularTestA> &p) { m_ptr = p; }

private:
    std::shared_ptr<CircularTestA> m_ptr;
}; // class CircularTestB
```

假设如下赋值

```cpp
{
	using CTA = smart_pointer_test::CircularTestA;
	using CTB = smart_pointer_test::CircularTestB;
	std::shared_ptr<CTA> spa(new CTA);
	std::shared_ptr<CTB> spb(new CTB);
	spa->set_ptr(spb);
	spb->set_ptr(spa);
    // end of code block, life ends here
}
```

那么当程序结束时，实际上这两个object所占用的内存都不能被释放

```bash
Constructing CircularTestA
Constructing CircularTestB
```

原因是：在这两个对象离开其作用域时，相应的生命周期也应该结束，但此时各自的data member实际上是个`shared_ptr`，而且其`use_count()`都不为`0`，因此内存便一直无法释放。



#### 循环引用问题解决

解决的办法很简单，将其中的一个data member改为`weak_ptr`，比如

```cpp
class CircularTestA {
	// ...
    std::weak_ptr<CircularTestB> m_ptr;
}; // class CircularTestA
```

其他的代码不用修改，这样，`spa`和`spb`所指向的对象生命周期结束的时候，由于`CircularTestA`中存储的只是`CircularTestB`的`weak_ptr`，它没有增加`shared_ptr`的计数，所以`shared_ptr<CircularTestB> spb`在离开其作用域时，发现计数只有1，这样它就可以调用析构函数来释放内存。

实际上，如果先定义`spa`，后定义`spb`，资源释放和object析构的顺序如下：

- 因为首先定义了`spa`，后定义了`spb`，所以首先析构`spb`，再析构`spa`。需要注意的是，这里的析构，指的是`shared_ptr`的析构，而不是`CircularTestA`或`CircularTestB`的析构
- 第一步，析构`spb`：因为`spa`中存储的是`weak_ptr`，所以`spb`这个`shared_ptr`的计数实际上只有1，那么现在又要离开其作用域，所以`spb`此时要做两件事情，即销毁其所有的成员变量（调用各自对应的析构函数）+调用该`class shared_ptr<CircularTestB>`自己的析构函数
  - 销毁其所有的成员变量
    - 销毁其所有成员变量，就是调用每个成员变量的析构函数
    - 这里`shared_ptr<CircularTestB>`内部实际上存储的是指向`CircularTestB`的raw pointer，所以暂时不变，待其进入析构函数再重置或仍保留。
  - `shared_ptr`调用自己的析构函数
    - 此时`spb`检查`use_count()`，发现计数为1，又因为要就要离开作用域，所以意味着没有其他`shared_ptr`在引用该`CircularTestB`的内存，那么`spb`就把计数减为0，然后调用`CircularTestB`的析构函数，而调用`CircularTestB`的析构函数，意味着`CircularTestB`的对象要被析构，那么其成员也要首先被析构，即要析构`CircularTestB::m_ptr`，而这又是一个`shared_ptr`，所以又调用其析构函数，但此时发现`std::shared_ptr<CircularTestA>`的`use_count`是2，直接将其减去1结果为1，不为0（注意，此时`std::shared_ptr<CircularTestA>`的`use_count`就变成1了），所以就不再调用`CircularTestA`的析构函数了。
    - 然后，直接释放`spb`中的raw pointer所指向的该`CircularTestB`的内存（`delete`)
- 下一步，析构`spa`：同样地，要销毁其成员变量+调用析构函数
  - 该`shared_ptr`调用自己的析构函数
    - 此时`spa`检查`use_count()`，发现计数为1（因为已经在前面析构`spb`的时候减掉了1），又因为要就要离开作用域，所以意味着没有其他`shared_ptr`在引用该`CircularTestB`的内存，那么`spa`就把计数减为0，然后调用`CircularTestA`的析构函数，而调用`CircularTestA`的析构函数，意味着`CircularTestA`的对象要被析构，那么其成员也要首先被析构，即要析构`CircularTestA::m_ptr`，而这是一个`weak_ptr`，更何况其对应的`CircularTestB`的内存已经释放掉了，所以直接置空即可（当然，事实上步骤仍然是调用`weak_ptr`的析构函数，但它不会释放资源了，因为没有管理权）。
    - 然后，直接释放`spa`中的raw pointer所指向的该`CircularTestA`的内存（`delete`)



如果换一个顺序，如果先定义`spb`，后定义`spa`，资源释放和object析构的顺序如下：

- 因为先定义了`spb`，后定义了`spa`，所以先析构`spa`，后析构`spb`
- 第一步，析构`spa`:
  - 因为此时`spa`的计数为2，所以它所指向的内存资源并不能释放，所以只是简单地将计数减去1，因此`CircularTestA`的析构函数并没有被调用
- 第二步，析构`spb`：
  - 因为此时`spb`的计数为1，所以减去1，得到计数为0，那么此时就要调用`spb`所指向的`CircularTestB`的析构函数来释放`CircularTestB`的内存了
  - 调用`CircularTestB`的析构函数（打印了`Destructing CircularTestB`），那么`CircularTestB`的所有成员也要被析构，而`CircularTestB`中只有一个成员，即一个指向`CircularTestA`的`shared_ptr`。调用这个`shared_ptr`的析构函数，其内部计数目前是1，减去1得到0，那么就要调用`CircularTestA`的析构函数，释放其指向的`CircularTestA`的内存，所有在此时打印了`Destructing CircularTestA`。
  - 然后把`spb`内部的raw pointer置空

所以，无论是先定义`spa`，后定义`spb`，还是先定义`spb`，后定义`spa`，在本例中，析构函数里面打印的信息的顺序是相同的，如下

```bash
Destructing CircularTestB
Destructing CircularTestA
```







