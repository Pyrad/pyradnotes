# Smart Pointers

This file shows some usages of smart pointers in C/C++



### Reference

Reference articles: [C++ STL 四种智能指针](https://blog.csdn.net/K346K346/article/details/81478223)



---

### std::unique_ptr\<T\>

- 旨在代替旧的`auto_ptr`
- 需`#include <memory>`头文件
- 只能通过移动语义来转移所管理对象的管理权
  - 不能赋值到其他`std::unique_ptr`
  - 不能值传递到函数中（无法作为函数参数，因为要值传递）
  - 不能用于需要副本的`STL`算法
  - **例外**：**如果unique_ptr 是个临时右值，编译器允许拷贝语义**
- 

#### Construction & Destruction



#### Assignment



#### Member Functions



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
