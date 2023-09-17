
# [cmake：target_** 中的 PUBLIC，PRIVATE，INTERFACE](https://zhuanlan.zhihu.com/p/82244559)

本文源自：[https://zhuanlan.zhihu.com/p/82244559](https://zhuanlan.zhihu.com/p/82244559)

## **1. 指令说明**

**target_include_directories()**：指定**目标**包含的头文件路径。[官方文档](https://link.zhihu.com/?target=https%3A//cmake.org/cmake/help/v3.15/command/target_include_directories.html%3Fhighlight%3Dtarget_include_directories)

**target_link_libraries()**：指定**目标**链接的库。[官方文档](https://link.zhihu.com/?target=https%3A//cmake.org/cmake/help/v3.15/command/target_link_libraries.html%3Fhighlight%3Dtarget_link_libraries)

**target_compile_options()**：指定**目标**的编译选项。[官方文档](https://link.zhihu.com/?target=https%3A//cmake.org/cmake/help/v3.15/command/target_compile_options.html%23command%3Atarget_compile_options)

**目标** 由 _add_library()_ 或 _add_executable()_ 生成。

这三个指令类似，这里以 **target_include_directories()** 为例进行讲解。

## **2. 指令讲解**

**测试工程目录结构：**

```bash
cmake-test/                 工程主目录，main.c 调用 libhello-world.so
├── CMakeLists.txt
├── hello-world             生成 libhello-world.so，调用 libhello.so 和 libworld.so
│   ├── CMakeLists.txt
│   ├── hello               生成 libhello.so 
│   │   ├── CMakeLists.txt
│   │   ├── hello.c
│   │   └── hello.h         libhello.so 对外的头文件
│   ├── hello_world.c
│   ├── hello_world.h       libhello-world.so 对外的头文件
│   └── world               生成 libworld.so
│       ├── CMakeLists.txt
│       ├── world.c
│       └── world.h         libworld.so 对外的头文件
└── main.c
```

**调用关系：**

```bash
                                 ├────libhello.so
可执行文件────libhello-world.so
                                 ├────libworld.so
```

**关键字用法说明：**

**PRIVATE**：私有的。生成 libhello-world.so时，只在 hello_world.c 中包含了 hello.h，libhello-world.so **对外**的头文件——hello_world.h 中不包含 hello.h。而且 main.c 不会调用 hello.c 中的函数，或者说 main.c 不知道 hello.c 的存在，那么在 hello-world/CMakeLists.txt 中应该写入：

```cmake
target_link_libraries(hello-world PRIVATE hello)
target_include_directories(hello-world PRIVATE hello)
```

**INTERFACE**：接口。生成 libhello-world.so 时，只在libhello-world.so **对外**的头文件——hello_world.h 中包含 了 hello.h， hello_world.c 中不包含 hello.h，即 libhello-world.so 不使用 libhello.so 提供的功能，只使用 hello.h 中的某些信息，比如结构体。但是 main.c 需要使用 libhello.so 中的功能。那么在 hello-world/CMakeLists.txt 中应该写入：

```cmake
target_link_libraries(hello-world INTERFACE hello)
target_include_directories(hello-world INTERFACE hello)
```

**PUBLIC**：公开的。**PUBLIC = PRIVATE + INTERFACE**。生成 libhello-world.so 时，在 hello_world.c 和 hello_world.h 中都包含了 hello.h。并且 main.c 中也需要使用 libhello.so 提供的功能。那么在 hello-world/CMakeLists.txt 中应该写入：

```cmake
target_link_libraries(hello-world PUBLIC hello)
target_include_directories(hello-world PUBLIC hello)
```

实际上，这三个关键字指定的是目标文件依赖项的使用**范围（scope）**或者一种**传递（propagate）**。[官方说明](https://link.zhihu.com/?target=https%3A//cmake.org/cmake/help/v3.15/manual/cmake-buildsystem.7.html%23transitive-usage-requirements)

可执行文件依赖 libhello-world.so， libhello-world.so 依赖 libhello.so 和 libworld.so。

1.  main.c 不使用 libhello.so 的任何功能，因此 libhello-world.so 不需要将其依赖—— libhello.so 传递给 main.c，hello-world/CMakeLists.txt 中使用 PRIVATE 关键字；
2.  main.c 使用 libhello.so 的功能，但是libhello-world.so 不使用，hello-world/CMakeLists.txt 中使用 INTERFACE 关键字；
3.  main.c 和 libhello-world.so 都使用 libhello.so 的功能，hello-world/CMakeLists.txt 中使用 PUBLIC 关键字；

## **3. include_directories(dir)**

`target_include_directories()` 的功能完全可以使用 `include_directories()` 实现。但是我还是建议使用 `target_include_directories()`。为什么？保持清晰！

`include_directories(header-dir)` 是一个全局包含，向下传递。什么意思呢？就是说如果某个目录的 CMakeLists.txt 中使用了该指令，其下所有的子目录默认也包含了`header-dir` 目录。

上述例子中，如果在顶层的 cmake-test/CMakeLists.txt 中加入：

```cmake
include_directories(hello-world)
include_directories(hello-world/hello)
include_directories(hello-world/world)
```

那么整个工程的源文件在编译时**都**会增加：

```bash
-I hello-world -I hello-world/hello -I hello-world/world ...
```

各级子目录中无需使用 `target_include_directories()` 或者 `include_directories()`了。如果此时查看详细的编译过程（`make VERBOSE=1`）就会发现编译过程是一大坨，很不舒服。

当然了，在**最终子目录**的 CMakeLists.txt 文件中，使用 `include_directories()` 和 `target_include_directories()` 的效果是相同的。

## **4. 目录划分**

每一个目录都是一个模块，目录内部应将对外和对内的头文件进行区分，由模块的调用者决定模块是否被传递（PRIVATE，INTERFACE，PUBLIC）。

## **5. 参考：**

[https://cmake.org/pipermail/cmake/2016-May/063400.html](https://link.zhihu.com/?target=https%3A//cmake.org/pipermail/cmake/2016-May/063400.html)

[https://schneide.blog/2016/04/08/modern-cmake-with-target_link_libraries/](https://link.zhihu.com/?target=https%3A//schneide.blog/2016/04/08/modern-cmake-with-target_link_libraries/)

[https://stackoverflow.com/questions/26037954/cmake-target-link-libraries-interface-dependencies](https://link.zhihu.com/?target=https%3A//stackoverflow.com/questions/26037954/cmake-target-link-libraries-interface-dependencies)

[https://stackoverflow.com/quest](https://link.zhihu.com/?target=https%3A//stackoverflow.com/questions/26243169/cmake-target-include-directories-meaning-of-scope)



# [CMake的链接选项：PRIVATE，INTERFACE，PUBLIC](https://zhuanlan.zhihu.com/p/493493849)

本文源自：[https://zhuanlan.zhihu.com/p/493493849](https://zhuanlan.zhihu.com/p/493493849)

### 实验设置

为了验证这三种链接选项的作用，做了一个小实验。项目结构如下：

```bash
CMake_link_test
├── cmake-build-release
├── bar.cpp
├── bar.h
├── CMakeLists.txt
├── foo.cpp
├── foo.h
└── app.cpp
```

其中，cmake-build-release是构建目录。

代码如下：

`foo.h`

```cpp
int foo();
```

`foo.cpp`

```cpp
// foo.cpp
#include <foo.h>
int foo() {
  return 22;
}
```

`bar.h`

```cpp
// bar.h
#include <foo.h>
int bar();
```

`bar.cpp`

```cpp
// bar.cpp
#include <bar.h>
int bar() {
  return foo() + 1;
}
```

`app.cpp`

```cpp
// app.cpp
#include <bar.h>
#include <iostream>
int main() {
  std::cout << "From foo(): " << foo() << std::endl;
  std::cout << "From bar(): " << bar() << std::endl;
  return 0;
}
```

`CMakeLists.txt`

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.16)

project(foobar)
set(CMAKE_SKIP_RPATH TRUE)

include_directories(${CMAKE_SOURCE_DIR})

add_library(foo SHARED foo.cpp)

add_library(bar SHARED bar.cpp)
target_link_libraries(bar PUBLIC foo)

add_executable(app app.cpp)
target_link_libraries(app bar)
```

（上面的CMake代码中`set(CMAKE_SKIP_RPATH TRUE)` 是为了不在动态库中写入RUNPATH项，大家可以查一查这个东西是干嘛的）

库的依赖关系为：

$app \rightarrow libbar.so \rightarrow libfoo.so$

在下面的实验中，bar和foo两个库的依赖关系可以选三种之一，且源码需要作对应的改动：bar.cpp是否引用了foo定义的符号？如果是，foo.h头文件是在bar.h中包含还是在bar.cpp中包含？app.cpp中能否调用foo()函数？其他部分都是不动的：foo.cpp必定包含foo.h文件，bar.cpp必定包含bar.h，app.cpp必定包含bar.h。

这个模型是实际项目依赖结构的一个概括和简化，简单但不失一般性。在实际的项目中，我们一般是写bar库，依赖于现有的foo库，然后提供接口给客户，客户写app，此时bar的链接方式将会影响app的编写。

编译并运行代码：

```bash
cd cmake-build-release
cmake .. -DCMAKE_BUILD_TYPE=Release
make
export LD_LIBRARY_PATH=$(pwd)
./app
```

（这里要设置`LD_LIBRARY_PATH`环境变量，大家可以查一查这个东西是干嘛的 ）

### 理论解释

CMake官方对链接选项的解释异常晦涩难懂（其官方文档整体都是这个晦涩难懂的风格...），在stackoverflow上查到一个很好的解释，CMake的三种依赖关系分别对应于：

> **PRIVATE**  
> bar.h没有包含foo.h，只有bar.cpp包含了foo.h。此时，app没有包含foo.h，因此不能使用foo中定义的符号。换句话说，app只知道bar的存在，完全不知道foo的存在。
> 
> **INTERFACE**  
> bar.h中包含了foo.h，但是bar.cpp并没有用到foo定义的符号。此时，app包含了foo.h，可以引用foo的符号。换句话说，bar只是作为一个接口、界面，把foo传递给了app。
> 
> **PUBLIC**  
> 等于PRIVATE加INTERFACE，bar.h包含了foo.h，且bar.cpp引用了foo的符号。此时，app包含了foo.h，可以引用foo的符号。

### 实验结果

按照上面的理论解释，更改CMakeLists.txt中的链接选项，同时对应更改源码，得到如下实验结果：

|链接选项|app是否可用foo|ldd foo|readelf -d foo|ldd bar|readelf -d bar|ldd app |readelf -d app|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|PRIVATE|否|statically linked|无|foo |foo|foo, bar |bar|
|INTERFACE|是|statically linked|无 |statically linked|无|foo, bar|foo, bar|
|PUBLIC|是|statically linked|无|foo|foo|foo, bar|foo, bar|


（大家可以查一查ldd和readelf命令是干嘛的，它们有什么区别。想做实验验证区别的话，可以尝试在app中不调用foo函数，看看最后这两个命令的结果是什么）

使用`make VERBOSE=1`查看CMake生成的详细编译命令：

> **PRIVATE**  
> 链接bar：  
> `/usr/bin/g++-10 -fPIC -O3 -DNDEBUG -shared -Wl,-soname,libbar.so -o libbar.so CMakeFiles/bar.dir/bar.cpp.o libfoo.so`  
> 链接app：  
> `/usr/bin/g++-10 -O3 -DNDEBUG -rdynamic CMakeFiles/app.dir/app.cpp.o -o app libbar.so -Wl,-rpath-link,/path/to/cmake-build-release`  
> 
> **INTERFACE**  
> 链接bar：  
> `/usr/bin/g++-10 -fPIC -O3 -DNDEBUG -shared -Wl,-soname,libbar.so -o libbar.so CMakeFiles/bar.dir/bar.cpp.o`  
> 链接app：  
> `/usr/bin/g++-10 -O3 -DNDEBUG -rdynamic CMakeFiles/app.dir/app.cpp.o -o app libbar.so libfoo.so`  
> 
> **PUBLIC**  
> 链接bar：  
> `/usr/bin/g++-10 -fPIC -O3 -DNDEBUG -shared -Wl,-soname,libbar.so -o libbar.so CMakeFiles/bar.dir/bar.cpp.o libfoo.so`  
> 链接app：  
> `/usr/bin/g++-10 -O3 -DNDEBUG -rdynamic CMakeFiles/app.dir/app.cpp.o -o app libbar.so libfoo.so`  

我们知道，在gcc/g++编译命令选项中，`-rpath-link`指定编译时次级依赖库的查找位置，但是并不把次级依赖库传递给当前编译的目标文件。必须使用`--copy-dt-needed-entries`才能传递次级依赖库。因此，上面的编译命令的效果可以归纳如下：

|链接选项|bar|app|
|:-----|:-----|:-----|
|PRIVATE|传入foo|传入bar|
|INTERFACE|不传入foo|传入bar，传入foo|
|PUBLIC|传入foo|传入bar，传入foo|


可以猜想，CMake自己维护了一个库之间的依赖关系树，只要是CMake生成的gcc/g++编译命令，都会应用这些依赖关系。但是单纯看libbar.so或者app这些文件，是没有什么PRIVATE，INTERFACE，PUBLIC的依赖关系的。例如，PRIVATE或者PUBLIC生成的libbar.so就是完全一样的，它们的ELF头中都写入了libfoo.so的依赖项，我们完全可以把PRIVATE生成的libbar.so拿出来，然后自己手动编译app，指定`--copy-dt-needed-entries`参数，没有任何问题，跟上边PUBLIC的效果一模一样。

如果我们有一个现成的libbar.so，直接导入到CMake中成为一个library target，那么它默认的链接关系是什么呢？实验表明，在CMake生成的编译app的gcc/g++命令中，只是简单的传入libbar.so，没有其他处理，可以认为类似于PRIVATE。如果app中引用了foo的符号，那么可以使用CMake命令传入`--copy-dt-needed-entries`参数：

```cmake
add_library(bar SHARED IMPORTED)
set_target_properties(
        bar
        PROPERTIES IMPORTED_LOCATION
        ${CMAKE_SOURCE_DIR}/libbar.so
)

add_executable(app app.cpp)
target_link_libraries(app bar)
target_link_options(app PUBLIC "LINKER:--copy-dt-needed-entries")
```

`LINKER:`前缀对GCC会转化为`-Wl,`，对Clang会转化为`-Xlinker`。

但是，这样做并不太好，bar如果依赖很多库，而app只引用了其中一个foo库的符号，那么把bar的所有依赖库传给app就太浪费了，徒增编译压力。这也会污染项目结构，令依赖结构变得混乱。我认为，既然app引用foo库的符号，那就让app显式地链接到foo库，亦即，在CMake中显式地`target_link_libraries(app bar foo)`。

同时在这个实验中也可以看到，编译生成共享库时并不一定需要解析到所有符号，一些符号未定义也没问题，只要到最后编译可执行文件时解析出来所有符号就行。当然，这样做有大问题，给一个包含未定义符号的库，谁知道你还依赖哪些库？如果bar共享库引用了foo共享库，那编译bar库的时候就应该传入foo库，完成符号的解析和重定位，把依赖foo库的信息写入bar库的ELF头中。

编辑于 2023-07-29 11:41・IP 属地北京