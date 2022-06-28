# Smart Pointers

This file shows some usages of smart pointers in C/C++



### Reference

Reference articles: [C++ STL 四种智能指针](https://blog.csdn.net/K346K346/article/details/81478223)



---

### std::unique_ptr\<T\>

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

  





---

### std::shared_ptr\<T\>



#### Construction & Destruction



#### Assignment



#### Member Functions

- `get()`
- `reset()`
- `swap()`
- `use_count()`
- `unique()`
- `make_shared()`
- `static_pointer_cast()`



---

### std::weak_ptr\<T\>



#### Construction & Destruction



#### Assignment



#### Member Functions
