# C/C++ Advanced

This file shows some advanced usages of C/C++



## C++ Related Topics

- What is a **literal type**?

- What is **cv-qualified** ?
  - **cv** means `const` or `volatile`

- What is **trival default constructor**

- What is **an aggregate (class) **?

- What is **NRVO** ?
  - **N**amed **R**eturn **V**alue **O**ptimization（返回值优化）

- What is **copy elision** ?

- What is **RTTI**?
  - **RTTI = Run-Time Type Information**

- What is **closure type**？
  - What is ***lambda*** indeed ?
  - What is ***closure*** ?
  - What is ***closure type*** ?

- What is **init capture**？
  - What is **generalized lambda capture** ?

- What is **most vexing parse** ?

- What is **narrowing conversions** ?
  - （类型）范围缩减转换

- What is **CRTP**?
  - CRTP = the Curiously Recurring Template Pattern

- What is **PImpl** ?
  - **PImpl** = Pointer to implementation
  - Refer to page in [***cppreference***](https://en.cppreference.com/w/cpp/language/pimpl)

- What is **SFINAE** ?
  - **SFINAE** = **S**ubstitution **F**ailure **I**s **N**ot **A**n **E**rror
  - Refer to page in [SFINAE](https://en.cppreference.com/w/cpp/language/sfinae)

- What is **SSO** ?
  - **SSO** = **S**mall **S**tring **O**ptimization
  - A technique to improve performance for string implementations.

- What is **zero-overhead principle**?

  - What you don't use, you don't pay for (in time or space) and further: What you do use, you couldn't hand code any better.

- `inline`关键字到底有没有用？

  - 其实就这么简单的原则：

    `cpp`里的函数实现通通都无须要加`inline`。

    `h`里的独立函数实现必须加`inline`。

    编译器可以对不加`inline`关键字的函数内联，也可以对加了`inline`的函数拒绝内联。简单说：是否内联与`inline`关键字几乎没有关系。

    目前`inline`关键字的主要用途，就是为了将一个函数写到头文件中，从而无须专门进行链接。

    [参考回答](https://www.zhihu.com/question/53082910/answer/2771636200)



## Links

### C++ Online Tools

- [C++ Shell](http://www.cpp.sh )
- [Online GDB](https://www.onlinegdb.com/)
- [GDB Tutorial](http://www.gdbtutorial.com/)
- [Quick C++ Benckmark](https://www.quick-bench.com/)
- [Perfbench](https://www.perfbench.com/)
- [Buildbench](https://build-bench.com/)
- [Compiler Explorer](https://godbolt.org)
- [C++ insights](https://cppinsights.io/)