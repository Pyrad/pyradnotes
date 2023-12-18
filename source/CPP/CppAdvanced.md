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


### C++ Open Source Frameworks

[有哪些优秀的 C/C++ 开源代码框架？这些框架的设计思路是怎样的？ - 觅新笑话中的回答 - 知乎](https://www.zhihu.com/question/20201738/answer/2928936881)

## Python如何调用C/C++，及问题解决

[Python调用.dll文件,报错FileNotFoundError: Could not find module ‘xx\....\xx.dll](https://blog.csdn.net/weixin_43980331/article/details/132556194)

这篇博客里面提到的使用`winmode=0`的办法，在msys2中试过，可行，但`ctype`只能调用C/C++中的函数，不能构造其中的class，所以有一定的限制。（记录于2023年12月17日19:13:15）

[Python调用C/C++ - 51CTO博客](https://blog.51cto.com/u_15930680/5990951)

本篇主要介绍了几种常见的Python调用C/C++的DLL的方法。

### How to use C++ classes with ctypes?

如何通过`ctypes`调用C++的class

[python - How to use C++ classes with ctypes? - Stack Overflow](https://stackoverflow.com/questions/1615813/how-to-use-c-classes-with-ctypes)

### Python调用C++ DLL库 ------OSError: WinError 126 找不到指定的模块。

[https://blog.csdn.net/qq_34430371/article/details/112261682](https://blog.csdn.net/qq_34430371/article/details/112261682)

### Dependency Walker

[Dependency Walker](http://www.dependencywalker.com/)

[Dependencies - An open-source modern Dependency Walker](https://github.com/lucasg/Dependencies)

[Let's make dependency walker fast again!](https://zhuanlan.zhihu.com/p/268629149)

### Win10+MinGw编译可被Python调用的dll库

网页链接：[https://zhuanlan.zhihu.com/p/361844595](https://zhuanlan.zhihu.com/p/361844595)

### 使用C++编写Python扩展

网页链接：[https://www.jianshu.com/p/eb2618067eae](https://www.jianshu.com/p/eb2618067eae)

### python - 如何在 Python 中使用 MinGW-w64 构建我的 C 扩展？

网页链接：[https://www.coder.work/article/90276](https://www.coder.work/article/90276)

### Compiling Extension Modules on Windows using mingw

网页链接：
[https://scipy-cookbook.readthedocs.io/items/CompilingExtensionsOnWindowsWithMinGW.html](https://scipy-cookbook.readthedocs.io/items/CompilingExtensionsOnWindowsWithMinGW.html)

### MSYS2 - Python

网页链接：[https://www.msys2.org/docs/python/](https://www.msys2.org/docs/python/)


### Building a Python C Extension Module

网页链接：[https://realpython.com/build-python-c-extension-module/](https://realpython.com/build-python-c-extension-module/)

### Installing Python Modules  - Building Extensions: Tips and Tricks

[https://davis.lbl.gov/Manuals/PYTHON-2.3.3/inst/tweak-flags.html](https://davis.lbl.gov/Manuals/PYTHON-2.3.3/inst/tweak-flags.html)


### Building a Python C extension module with CMake

[https://martinopilia.com/posts/2018/09/15/building-python-extension.html](https://martinopilia.com/posts/2018/09/15/building-python-extension.html)


### (?) Solution to undefined reference to `__imp__Py_Dealloc'

[Embedded Python fails to compile](https://raspberrypi.stackexchange.com/questions/119453/embedded-python-fails-to-compile)

[https://raspberrypi.stackexchange.com/questions/119453/embedded-python-fails-to-compile](https://raspberrypi.stackexchange.com/questions/119453/embedded-python-fails-to-compile)

也许能解决下面的问题，但还没时（2023年10月3日19:32:26）

```bash
FAILED: pyrun/bpyrun.dll pyrun/libbpyrun.dll.a

cmd.exe /C "cd . && D:\procs\msys64\mingw64\bin\c++.exe -O3 -DNDEBUG -shared -o pyrun\bpyrun.dll -Wl,--out-implib,pyrun\libbpyrun.dll.a -Wl,--major-image-version

,0,--minor-image-version,0 pyrun/CMakeFiles/bpyrun.dir/bpyrun.cpp.obj -LD:/procs/boost_1_83_0/lib D:/procs/boost_1_83_0/lib/libboost_python38-mgw12-mt-x64-1_83.dll

-lkernel32 -luser32 -lgdi32 -lwinspool -lshell32 -lole32 -loleaut32 -luuid -lcomdlg32 -ladvapi32 && cd ."

D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: pyrun/CMakeFiles/bpyrun.dir/bpyrun.cpp.obj:bpyrun.cpp:(

.text+0x32): undefined reference to `__imp__Py_Dealloc'

D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: pyrun/CMakeFiles/bpyrun.dir/bpyrun.cpp.obj:bpyrun.cpp:(

.text+0xc2): undefined reference to `__imp__Py_Dealloc'

D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: pyrun/CMakeFiles/bpyrun.dir/bpyrun.cpp.obj:bpyrun.cpp:(

.text+0xdd): undefined reference to `__imp__Py_Dealloc'

D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: pyrun/CMakeFiles/bpyrun.dir/bpyrun.cpp.obj:bpyrun.cpp:(

.text$_ZN5boost6python6detail21converter_target_typeINS0_15to_python_valueIRKPKcEEE10get_pytypeEv[_ZN5boost6python6detail21converter_target_typeINS0_15to_python_va

lueIRKPKcEEE10get_pytypeEv]+0x3): undefined reference to `__imp_PyUnicode_Type'

D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/bin/ld.exe: pyrun/CMakeFiles/bpyrun.dir/bpyrun.cpp.obj:bpyrun.cpp:(

.text.startup+0x7): undefined reference to `__imp__Py_NoneStruct'

collect2.exe: error: ld returned 1 exit status

ninja: build stopped: subcommand failed.
```



### “undefined reference to XXX“问题分析及解决方法总结

[https://blog.csdn.net/Charmve/article/details/126387362](https://blog.csdn.net/Charmve/article/details/126387362)

### Windows下Python中常见的几种DLL load failed问题的原因以及解决方案

[Windows下Python中常见的几种DLL load failed问题的原因以及解决方案 - 知乎](https://zhuanlan.zhihu.com/p/133986373)

### linux编译动态库之fPIC

[linux编译动态库之fPIC - 知乎](https://zhuanlan.zhihu.com/p/368364069)

[linux编译动态库之fPIC- CSDN](https://blog.csdn.net/TH_NUM/article/details/86541234)

### How can I see parse tree, intermediate code, optimization code and assembly code during COMPILATION?

[https://stackoverflow.com/questions/1496497/how-can-i-see-parse-tree-intermediate-code-optimization-code-and-assembly-code](https://stackoverflow.com/questions/1496497/how-can-i-see-parse-tree-intermediate-code-optimization-code-and-assembly-code)


## C++异常处理的底层机制 - dingtingli的文章

链接：[C++异常处理的底层机制 - dingtingli的文章 - 知乎 https://zhuanlan.zhihu.com/p/656940263](https://zhuanlan.zhihu.com/p/656940263)