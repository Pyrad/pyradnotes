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

- 被Effective C++称为“引用计数型智能指针”（Reference Counting Smart Pointer，RCSP）
- 额外的开销
  - `std::shared_ptr<T>`对象包含一个对象的指针，和一个引用计数对象的指针。
  - 时间开销主要在初始化和拷贝操作上，`*`和`->`操作符的开销和`auto_ptr`相同









### Construction & Destruction



### Assignment



### Member Functions

- `get()`
- `reset()`
- `swap()`
- `use_count()`
- `unique()`
- `make_shared()`
- `static_pointer_cast()`



---

## std::weak_ptr\<T\>



### Construction & Destruction



### Assignment



### Member Functions
