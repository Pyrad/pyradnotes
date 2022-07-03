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





---

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





---

## std::weak_ptr\<T\>



### Construction & Destruction



### Assignment



### Member Functions
