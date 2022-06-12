# CMake Tutorial Notes

本文是记录学习CMake官方教程时的笔记与注意事项

- [官方教程链接地址](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
- [CMake下载链接地址](https://cmake.org/download/)
- [CMake Build System Page](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#introduction)
- [CMake Reference Documentation](https://cmake.org/cmake/help/latest/index.html)
- [Help Documentation of cmake-commands](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html)
- [A similar CMake tutorial (not official, but looks useful)](https://www.bilibili.com/video/BV18t4y1Q7sa?p=7)



**注意**：与本文对应的repository

| GitHub/Gitee |                             Link                             |
| :----------: | :----------------------------------------------------------: |
|    GitHub    | [CMakeOfficialTutorial](https://github.com/Pyrad/CMakeOfficialTutorial.git) |
|    Gitee     | [CMakeOfficialTutorial](https://gitee.com/pyrad/CMakeOfficialTutorial.git) |



## 前期准备

为了能够在windows平台下使用CMake，以避免可能出现的问题，需要准备以下两项

- [MinGW](https://sourceforge.net/projects/mingw-w64/files/)
- [CMake](https://cmake.org/download/)

对于CMake，下载最新版的（当前最新为3.23.2）即可，记得添加cmake的路径到`PATH`中去。

对于MinGW，需要进入[下载页面](https://sourceforge.net/projects/mingw-w64/files/)，不要下载*MinGW-W64 Online Installer*（太慢），而是选择最新的下载选项（如下）中的`x86_64-win32-seh`，它是对应windows平台的压缩包。

- **MinGW-W64 GCC-8.1.0**

  - [x86_64-posix-sjlj](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-posix/sjlj/x86_64-8.1.0-release-posix-sjlj-rt_v6-rev0.7z>)

  - [x86_64-posix-seh](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z>)

  - [x86_64-win32-sjlj](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-win32/sjlj/x86_64-8.1.0-release-win32-sjlj-rt_v6-rev0.7z>)

  - [x86_64-win32-seh](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-win32/seh/x86_64-8.1.0-release-win32-seh-rt_v6-rev0.7z>)

  - [i686-posix-sjlj](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-posix/sjlj/i686-8.1.0-release-posix-sjlj-rt_v6-rev0.7z>)

  - [i686-posix-dwarf](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-posix/dwarf/i686-8.1.0-release-posix-dwarf-rt_v6-rev0.7z>)

  - [i686-win32-sjlj](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-win32/sjlj/i686-8.1.0-release-win32-sjlj-rt_v6-rev0.7z>)

  - [i686-win32-dwarf](<https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-win32/dwarf/i686-8.1.0-release-win32-dwarf-rt_v6-rev0.7z>)


下载完毕之后，将其中的目录`mingw64`解压出来，然后把对应的路径加入到环境变量`PATH`中去，以便在terminal中使用时可以被搜索到。

对于**MinGW**需要特别注意的是，在其`bin`目录下面有`mingw32-make.exe`，但没有`make.exe`，需要自己单独把`mingw32-make.exe`复制出来一份并重新命名为`make.exe`，否则会出现如下的错误

```shell
$ cmake ../Step1 -G "Unix Makefiles"
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "F:/Pyrad/CMakeLearning/CMakeTutorialLearning/Step1_build/CMakeFiles/CMakeOutput.log".
```

（可能的原因是CMake查找的是`make`而不是`mingw32-make.exe`，哪怕`mingw32-make.exe`已经在`PATH`中了）

此外，需要在`CMakeLists.txt`中指明需要使用`mingw64`对应的toolchain来编译，

```cmake
SET(MY_MINGW64_HOME "D:/procs/mingw64")
SET(CMAKE_MAKE_PROGRAM "${MY_MINGW64_HOME}/bin/mingw32-make.exe")
SET(CMAKE_C_COMPILER "${MY_MINGW64_HOME}/bin/gcc.exe")
SET(CMAKE_CXX_COMPILER "${MY_MINGW64_HOME}/bin/g++.exe")
```

并且，在`cmake`编译时使用如下option

```shell
cmake <SRC_DIR> -G "Unix Makefiles"
```

否则在windows平台下，系统可能会按照VS的toolchain生成project文件，而不是像Linux下一样生成`Makefile`文件。



## Step 1 基本

教程第一节



### 简述

本节介绍了一个简单的例子，只有一个`cpp`文件（以及稍后引入的通过`cmake`创建的一个头文件），通过引入一个简单的`CMakeLists.txt`来说明了如何编译这个简单的`cpp`源文件。



### 新的语法和命令

|           functions            |     functions      |
| :----------------------------: | :----------------: |
|   `CMAKE_MINIMUM_REQUIRED()`   |    `PROJECT()`     |
|       `ADD_EXECUTABLE()`       | `CONFIGURE_FILE()` |
|            `SET()`             |    `MESSAGE()`     |
| `TARGET_INCLUDE_DIRECTORIES()` |                    |



|      variables       |           variables           |
| :------------------: | :---------------------------: |
| `CMAKE_CXX_STANDARD` | `CMAKE_CXX_STANDARD_REQUIRED` |
| `CMAKE_MAKE_PROGRAM` |      `CMAKE_C_COMPILER`       |
| `CMAKE_CXX_COMPILER` |     `PROJECT_BINARY_DIR`      |
| `PROJECT_SOURCE_DIR` |                               |



关于`CMakeLists.txt`中基本语法（synopsis）的几点说明

- 关键字大小写**不敏感**（但最好统一用大写或小写）
- 变量是大小写**敏感**的



这里的`CMakeLists.txt`文件的内容：

```cmake
CMAKE_MINIMUM_REQUIRED(VERSION 3.10)

# Set the project name
PROJECT(Tutorial VERSION 1.0)

# specify the C++ standard
SET(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_STANDARD_REQUIRED True)

MESSAGE(STATUS "[PYRAD] This is the BINARY directory: " ${Tutorial_BINARY_DIR})
MESSAGE(STATUS "[PYRAD] This is the SOURCE directory: " ${Tutorial_SOURCE_DIR})

# Add the executable
ADD_EXECUTABLE(Tutorial tutorial.cxx)

# If you'd like to build in a Unix way in windows platform,
# add the following
SET(MY_MINGW64_HOME "D:/procs/mingw64")
SET(CMAKE_MAKE_PROGRAM "${MY_MINGW64_HOME}/bin/mingw32-make.exe")
SET(CMAKE_C_COMPILER "${MY_MINGW64_HOME}/bin/gcc.exe")
SET(CMAKE_CXX_COMPILER "${MY_MINGW64_HOME}/bin/g++.exe")


CONFIGURE_FILE(TutorialConfig.h.in TutorialConfig.h)


TARGET_INCLUDE_DIRECTORIES(Tutorial PUBLIC "${PROJECT_BINARY_DIR}" )


```





使用`cmake`进行编译

命令为

```shell
$ mkdir Step1_build
$ cd ./Step1_build
$ cmake ../Step1 -G "Unix Makefiles"
$ cmake --build .
```

在windows平台下显示了信息如下：

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step1_build (master)
$ cmake ../Step1 -G "Unix Makefiles"
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: D:/procs/mingw64/bin/gcc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: D:/procs/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- [PYRAD] This is the BINARY directory: D:/Gitee/CMakeOfficialTutorial/Step1_build
-- [PYRAD] This is the SOURCE directory: D:/Gitee/CMakeOfficialTutorial/Step1
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step1_build

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step1_build (master)
$ cmake --build .
[ 50%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[100%] Linking CXX executable Tutorial.exe
[100%] Built target Tutorial

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step1_build (master)
$ ls
cmake_install.cmake  CMakeCache.txt  CMakeFiles/  Makefile  Tutorial.exe*  TutorialConfig.h
```

编译完毕之后，可以在编译目录（当前是`Step1_build`）里面执行如下命令，得到如下结果

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step1_build (master)
$ ./Tutorial.exe 4294967296
The square root of 4.29497e+09 is 65536

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step1_build (master)
$ ./Tutorial.exe 10
The square root of 10 is 3.16228

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step1_build (master)
$ ./Tutorial.exe
D:\Gitee\CMakeOfficialTutorial\Step1_build\Tutorial.exe Version 1.0
Usage: D:\Gitee\CMakeOfficialTutorial\Step1_build\Tutorial.exe number
```









### `PROJECT` 关键字

[`PROJECT`文档帮助页面](https://cmake.org/cmake/help/latest/command/project.html#command:project)

其中`PROJECT`关键字指明工程名字，后面可以跟上所支持的语言（默认支持所有语言）。

```cmake
PROJECT(Tutorial) # 指定工程名为Tutorial
PROJECT(Tutorial CXX) # 指定工程名为Tutorial，支持语言为C++
PROJECT(Tutorial C CXX) # 指定工程名为Tutorial，支持语言为C和C++
PROJECT(Tutorial VERSION 1.0) # 指定工程名为Tutorial，并且设定版本号为1.0
```

（[`PROJECT`文档帮助页面](https://cmake.org/cmake/help/latest/command/project.html#command:project)）

其中，这个声明同时也隐式定义了两个`CMake`变量，分别是

- `${PROJECT_NAME}_BINARY_DIR`

  这个变量指明了存放一些binary等可执行文件的目录。比如在该项目里这个变量就会在cmake执行时被替换为`Tutorial_BINARY_DIR`。

- `${PROJECT_NAME}_SOURCE_DIR`

  这个变量指明了存放源文件的目录。比如在该项目里这个变量就会在cmake执行时被替换为`Tutorial_SOURCE_DIR`。

这两个隐式生成的`CMake`变量，会由于工程名的变化而产生变化，为了防止其发生变化，`CMake`还提供了两个预定义的变量，可以单独对其进行命名，防止因为工程名称发生变化而变化。





### `SET`  关键字

[`SET`帮助文档页面](https://cmake.org/cmake/help/latest/command/set.html)

`SET`关键字用来指定变量，如果后面跟一个列表，需要用空格隔开（如果文件名中有空格，那么该文件名就需要用双引号括起来）

```cmake
SET(SRC_LIST main.cpp) # 声明了变量SRC_LIST
SET(SRC_LIST main.cpp t.cpp t2.cpp) # 声明了变量SRC_LIST
```

其中文件名可以带上后缀，也可以不带后缀，但是最好带上后缀，防止有歧义的情况发生（比如同时存在两个文件`main.cpp`和`main`）。



### `MESSAGE` 关键字

[`MESSAGE`帮助文档页面](https://cmake.org/cmake/help/latest/command/message.html)

这个关键字向终端输出用户的自定义的信息，包括三种

- **`SEND_ERROR`**

  产生错误，跳过生成过程

- **`STATUS`**

  输出信息，前缀是`--`

- **`FATAL_ERROR`**

  立即终止所有的`cmake`过程

在本例中，输出了两条信息，

```cmake
# 变量${Tutorial_BINARY_DIR}是由cmake通过PROJECT所设定的名字自动赋值得到的
MESSAGE(STATUS "[PYRAD] This is the BINARY directory: " ${Tutorial_BINARY_DIR})

# 变量${Tutorial_SOURCE_DIR}也是由cmake通过PROJECT所设定的名字自动赋值得到的
MESSAGE(STATUS "[PYRAD] This is the SOURCE directory: " ${Tutorial_SOURCE_DIR})
```









## Step2 添加库

教程第二节

Adding A Library 添加一个库



### 新的命令和语法

|     functions      |           functions            |         functions         |
| :----------------: | :----------------------------: | :-----------------------: |
|  `add_library()`   |      `add_subdirectory()`      | `target_link_libraries()` |
|     `option()`     |       `configure_file()`       |         `list()`          |
| `add_executable()` | `target_include_directories()` |                           |



指令

| instructions | instructions |
| :----------: | :----------: |
|  `if/endif`  |              |
|              |              |



### 初始目录结构

```shell
Step2/
│───CMakeLists.txt
│───tutorial.cxx
│───TutorialConfig.h.in
│
└───MathFunctions/
    │───MathFunctions.h
    └───mysqrt.cxx
```



### 修改的部分

首先需要在`Step2/CMakeLists.txt`这个顶层的文件里面，添加如下的修改（这里不包含原有的部分）

```cmake
# PART 1
# If you'd like to build in a Unix way in windows platform,
# add the following
SET(MY_MINGW64_HOME "D:/procs/mingw64")
SET(CMAKE_MAKE_PROGRAM "${MY_MINGW64_HOME}/bin/mingw32-make.exe")
SET(CMAKE_C_COMPILER "${MY_MINGW64_HOME}/bin/gcc.exe")
SET(CMAKE_CXX_COMPILER "${MY_MINGW64_HOME}/bin/g++.exe")

# PART 2
option(USE_MYMATH "Use tutorial provided math implementation" ON)

if(USE_MYMATH)
	# Add the MathFunctions library
	add_subdirectory(MathFunctions)
	list(APPEND EXTRA_LIBS MathFunctions)
	list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")
endif()

# PART 3
# add the executable
add_executable(Tutorial tutorial.cxx MathFunctions/mysqrt.cxx)

# PART 4
target_link_directories(Tutorial PUBLIC ${EXTRA_LIBS})

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           "${EXTRA_INCLUDES}"
                           )
```

上面修改中：

- **第一部分**：仍然是指定在windows平台下的gcc/g++编译

- **第二部分**：设定了一个CMake的宏`USE_MYMATH`，以便可以在cmake编译期间打开或关闭。

  然后根据这个宏，通过命令`add_subdirectory`添加一个lib的目录（`MathFunctions`），以便cmake可以得知我们的lib源文件的目录

  同时，还定义了两个cmake中的list变量：`EXTRA_LIBS`和`EXTRA_INCLUDES`，

- **第三部分**：通过`add_executable`告诉cmake最终编译得到的二进制文件`Tutorial`需要从源文件`tutorial.cxx`和lib库的源文件`MathFunctions/mysqrt.cxx`。**（注意，这里在网页上忘记写了后者，会导致最后链接错误）**

- **第四部分**：首先通过`target_link_directories`告诉了linker需要去搜索lib文件（比如这里的`MathFunctions.a`）的路径，它所指定的二进制名`Tutorial`，必须是在之前已经通过`add_executable`活着`add_library`已经定义。

  其次通过`target_include_directories`定义了在编译期间compiler需要去搜索的目录，以便找到所需的头文件。



在`TutorialConfig.h.in`文件中，添加如下指令

```shell
#cmakedefine USE_MYMATH
```

这个指令的**目的**，主要是定义一个可以在cmake期间灵活修改（打开/关闭）的宏，以方便使用。

实际上，`USE_MYMATH`这个宏在两个地方被定了，

- 第一个地方：top-level的`CMakeLists.txt`中，使用CMake的`option()`这个函数定义了`USE_MYMATH`这个宏，并赋予其初始值，这个地方是`USE_MYMATH`这个宏真正被定义的地方，而且是通过CMake来定义的

- 第二个地方：文件`TutorialConfig.h.in`这个文件中。这个地方里面使用了CMake的指令`#cmakedefine`来定义`USE_MYMATH`这个宏，但它在cmake编译期间会被cmake做自动替换，替换为真正的`C/C++`的预编译指令：`#define USE_MYMATH 0` 或 `#define USE_MYMATH 1`

  而由于`USE_MYMATH`这个宏是cmake定义的，所以在cmake期间，可以通过command line option来改变这个宏的值（ON/OFF），而随着改变的，是`TutorialConfig.h.in`这个文件根据cmake的编译指令而生成的文件中真正的`C/C++`的预编译指令所定义的`USE_MYMATH`这个宏值。

  比如，打开这个编译选项，使用`cmake ../Step2 -G Unix Makefiles" -DUSE_MYMATH=ON`（或者直接用`cmake ../Step2 -G Unix Makefiles"`，因为`USE_MYMATH`的默认值是`ON`），那么通过`TutorialConfig.h.in`这个文件生成的头文件`TutorialConfig.h`中，预编译指令就是：`#define USE_MYMATH 1` 。

  如果关闭这个编译选项，使用`cmake ../Step2 -G Unix Makefiles" -DUSE_MYMATH=OFF`，那么通过`TutorialConfig.h.in`这个文件生成的头文件`TutorialConfig.h`中，预编译指令就是：`#define USE_MYMATH 0` ，总之，就是cmake会根据option中定义的宏，在根据编译时的command liine option是否打开，自动替换`#cmakedefine USE_MYMATH`成正确的真正的`C/C++`的预编译指令。



在`tutorial.cxx`源文件的中，修改的部分如下，

```cpp
// PART 1
#ifdef USE_MYMATH
#include "MathFunctions.h"
#endif // USE_MYMATH

int main(int argc, char* argv[])
{
  // ... ... 

  // PART 2
  // calculate square root
  #ifdef USE_MYMATH
  const double outputValue = mysqrt(inputValue);
  #else
  const double outputValue = sqrt(inputValue);
  #endif // USE_MYMATH
 
  // ... ...
  
  return 0;
}
```

上面修改的，

**第一部分**：是根据宏`USE_MYMATH`来决定是否添加头文件`MathFunctions.h`

**第二部分**：是根据宏`USE_MYMATH`来决定是否使用标准库中的函数`sqrt`还是我们这里自定义的库中的函数`mysqrt`



### 修改之后

添加并修改文件完毕之后，目录结构如下

```shell
STEP2/
│───CMakeLists.txt*
│───tutorial.cxx*
│───TutorialConfig.h.in*
│
└───MathFunctions/
    │───CMakeLists.txt* (Newly added)
    │───MathFunctions.h
    └───mysqrt.cxx
```



### 打开`USE_MYMATH`编译

编译（打开`USE_MYMATH`宏）

```shell
cmake ../Step2 -G "Unix Makefiles"
cmake --build .
```



输出结果

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ cmake ../Step2 -G "Unix Makefiles"
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: D:/procs/mingw64/bin/gcc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: D:/procs/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step2_build

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ cmake --build .
[ 20%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[ 40%] Building CXX object CMakeFiles/Tutorial.dir/MathFunctions/mysqrt.cxx.obj
[ 60%] Linking CXX executable Tutorial.exe
[ 60%] Built target Tutorial
[ 80%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.obj
[100%] Linking CXX static library libMathFunctions.a
[100%] Built target MathFunctions
```



执行编译后的二进制文件，得到如下输出，可以看到，使用的是**我们自定义库**中的`mysqrt`函数。

```shell

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ ./Tutorial.exe 4294967296
Computing sqrt of 4.29497e+09 to be 2.14748e+09
Computing sqrt of 4.29497e+09 to be 1.07374e+09
Computing sqrt of 4.29497e+09 to be 5.36871e+08
Computing sqrt of 4.29497e+09 to be 2.68435e+08
Computing sqrt of 4.29497e+09 to be 1.34218e+08
Computing sqrt of 4.29497e+09 to be 6.71089e+07
Computing sqrt of 4.29497e+09 to be 3.35545e+07
Computing sqrt of 4.29497e+09 to be 1.67773e+07
Computing sqrt of 4.29497e+09 to be 8.38878e+06
Computing sqrt of 4.29497e+09 to be 4.19465e+06
The square root of 4.29497e+09 is 4.19465e+06

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ ./Tutorial.exe 10
Computing sqrt of 10 to be 5.5
Computing sqrt of 10 to be 3.65909
Computing sqrt of 10 to be 3.19601
Computing sqrt of 10 to be 3.16246
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
The square root of 10 is 3.16228

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ ./Tutorial.exe
D:\Gitee\CMakeOfficialTutorial\Step2_build\Tutorial.exe Version 1.0
Usage: D:\Gitee\CMakeOfficialTutorial\Step2_build\Tutorial.exe number
```





### 关闭`USE_MYMATH`编译

使用如下命令，在关闭自定义的宏`USE_MYMATH`之后编译

```shell
cmake ../Step2 -G "Unix Makefiles" -DUSE_MYMATH=OFF
cmake --build .
```



编译输出（这里偷懒了，没有`rm -rf ./*`，就让cmake增量编译吧）

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ cmake ../Step2 -G "Unix Makefiles" -DUSE_MYMATH=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step2_build

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ cmake --build .
Consolidate compiler generated dependencies of target Tutorial
[ 33%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[ 66%] Building CXX object CMakeFiles/Tutorial.dir/MathFunctions/mysqrt.cxx.obj
[100%] Linking CXX executable Tutorial.exe
[100%] Built target Tutorial
```



执行编译后的二进制文件，得到如下输出，可以看到，使用的是**标准库**中的`sqrt`函数。

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ ./Tutorial.exe 4294967296
The square root of 4.29497e+09 is 65536

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ ./Tutorial.exe 10
The square root of 10 is 3.16228

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step2_build (master)
$ ./Tutorial.exe
D:\Gitee\CMakeOfficialTutorial\Step2_build\Tutorial.exe Version 1.0
Usage: D:\Gitee\CMakeOfficialTutorial\Step2_build\Tutorial.exe number
```





## Step3 添加库优化

教程第三节



### 新的语法和命令

|            commands            |          commands          |
| :----------------------------: | :------------------------: |
| `target_compile_definitions()` | `target_compile_options()` |
| `target_include_directories()` | `target_link_libraries()`  |



|  variables  |         variables          |
| :---------: | :------------------------: |
| `INTERFACE` | `CMAKE_CURRENT_SOURCE_DIR` |
|             |                            |



本节主要讲述了，如何在一个库（lib）目录里面的`CMakeLists.txt`里面通过添加如下语句，使得当该库（lib）目录在被使用时（即被link时），由cmake自动include当前库的源文件目录。这样，在主目录下面的`CMakeLists.txt`里面就不用再显式地include这个库（lib）的目录以便查找其头文件。（但还是要在top-level的`CMakeLists.txt`里面显示地通过`target_link_libraries`来指明需要链接的目录）

```cmake
target_include_directories(MathFunctions
                           INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
                           )
```



### 改动一

在`MathFunctions/CMakeLists.txt`中，添加如下指令

```cmake
# Remember INTERFACE means things that consumers 
# require but the producer doesn't. 
# State that anybody linking to us needs to include the current source dir
# to find MathFunctions.h, while we don't.
target_include_directories(MathFunctions
                           INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
                           )
```



### 改动二

在主目录的`CMakeLists.txt`中，把如下指令

```cmake
# add the MathFunctions library
if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
  list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")
endif()
```

修改为

```cmake
# add the MathFunctions library
if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
endif()
```

即，**删除`list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")`。**



对应的，还是在主目录的`CMakeLists.txt`中，把如下指令

```cmake
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           ${EXTRA_INCLUDES}
                           )
```

修改为

```cmake
# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
target_include_directories(Tutorial PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )
```

也就是说，cmake会自动查找需要的库的源文件目录，而不用再在主目录的`CMakeLists.txt`中显式指明。



### 编译结果

同样地，使用如下两条命令进行编译

```shell
cmake ../Step3 -G "Unix Makefiles"
cmake --build .
```

结果

```sh
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step3_build (master)
$ cmake ../Step3 -G "Unix Makefiles"
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: D:/procs/mingw64/bin/gcc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: D:/procs/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step3_build

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step3_build (master)
$ cmake --build .
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.obj
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[100%] Linking CXX executable Tutorial.exe
[100%] Built target Tutorial
```





## Step4 安装和测试

教程第四节

本节主要讲述了如何设置install目录，以便编译完成之后，把对应的二进制文件、头文件以及库文件拷贝到设定好的目录中去。（The install rules are fairly simple: for `MathFunctions` we want to install the library and header file and for the application we want to install the executable and configured header.）



### 新的语法和命令

|  commands   |       variables        |
| :---------: | :--------------------: |
| `install()` | `CMAKE_INSTALL_PREFIX` |




### 改动一

在主目录的`CMakeLists.txt`中，添加如下的指令

```cmake
install(TARGETS Tutorial DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
		DESTINATION include
		)
```

这样是说明

- 把二进制文件`Tutorial`拷贝到install目录下的`bin`目录中去
- 把头文件`TutorialConfig.h`拷贝到install目录下的`include`目录中去

需要说明的是，如果在`CMakeLists.txt`中没有指明变量`CMAKE_INSTALL_PREFIX`，那么这个变量的默认值在windows平台是`C:/Program Files(x86)/${PROJECT_NAME}`，在linux平台是`/usr/local`。

所以这两条指令实际上是说

- 把二进制文件`Tutorial`拷贝到`C:/Program Files(x86)/Tutorial/bin`目录里去
- 把头文件`TutorialConfig.h`拷贝到`C:/Program Files(x86)/Tutorial/include`目录里去去

那么在这里就会有权限的问题，如果后面使用`make --install .`就会出现没有权限拷贝的问题，所以为了避免该问题，需要在`CMakeLists.txt`中设定合适的`CMAKE_INSTALL_PREFIX`

```cmake
# Set install path
set(MY_INSTALL_DIR "MyInstallPath")
set(CMAKE_INSTALL_PREFIX "${PROJECT_BINARY_DIR}/${MY_INSTALL_DIR}")

install(TARGETS Tutorial DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
		DESTINATION include
		)
```

或者，另一种办法是在`cmake --install .`时，添加`--prefix <prefix_to_path>`来覆盖`CMAKE_INSTALL_PREFIX`变量的值。

### 改动二

在`MathFunctions/CMakeLists.txt`中，添加如下指令

```cmake
install(TARGETS MathFunctions DESTINATION lib)
install(FILES MathFunctions.h DESTINATION include)
```

同样地，根据前面**改动一**中的说明，这两条指令实际上是说

- 把库文件`libMathFunctions.a`拷贝到install目录下的`lib`目录中去
- 把头文件`MathFunctions.h`拷贝到install目录下的`include`目录中去



### 编译和安装

使用如下的三条命令来编译和安装

同样地，使用如下两条命令进行编译

```shell
cmake ../Step4 -G "Unix Makefiles"
cmake --build .
cmake --install .
```

结果

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step4_build (master)
$ cmake ../Step4 -G "Unix Makefiles"
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: D:/procs/mingw64/bin/gcc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: D:/procs/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step4_build

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step4_build (master)
$ cmake --build .
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.obj
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[100%] Linking CXX executable Tutorial.exe
[100%] Built target Tutorial

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step4_build (master)
$ cmake --install .
-- Install configuration: ""
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step4_build/MyInstallPath/bin/Tutorial.exe
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step4_build/MyInstallPath/include/TutorialConfig.h
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step4_build/MyInstallPath/lib/libMathFunctions.a
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step4_build/MyInstallPath/include/MathFunctions.h
```



注意，如果需要在cmake的时候手动指明install path，就用如下指令

```shell
cmake ../Step4 -G "Unix Makefiles"
cmake --build .
cmake --install . --prefix /my/install/prefix
```



### 编译安装结果

在编译和安装结束之后，这里`CMakeLists.txt`中指明的目录`MyInstallPath`目录的tree结构如下

```shell
MyInstallPath/
├───bin/
│       Tutorial.exe
│
├───include/
│       MathFunctions.h
│       TutorialConfig.h
│
└───lib/
        libMathFunctions.a
```



### 添加测试支持

在top-level的`CMakeLists.txt`中添加如下的testing support

```cmake
enable_testing()

# PART 1
# does the application run
add_test(NAME Runs COMMAND Tutorial 25)

# does the usage message work?
add_test(NAME Usage COMMAND Tutorial)
set_tests_properties(Usage
  PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number"
  )

# PART 2
# define a function to simplify adding tests
function(do_test target arg result)
  add_test(NAME Comp${arg} COMMAND ${target} ${arg})
  set_tests_properties(Comp${arg}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result}
    )
endfunction()

# do a bunch of result based tests
do_test(Tutorial 4 "4 is 2")
do_test(Tutorial 9 "9 is 3")
do_test(Tutorial 5 "5 is 2.236")
do_test(Tutorial 7 "7 is 2.645")
do_test(Tutorial 25 "25 is 5")
do_test(Tutorial -25 "-25 is (-nan|nan|0)")
do_test(Tutorial 0.0001 "0.0001 is 0.01")
```

- 第一部分使用了`cmake`的`add_test`和`set_tests_properties`来做简单测试
- 第二部分定义了一个定制化的函数，并用来测试



### 如何运行测试

不要切换到`install`目录下面去，而是要到编译目录下面去（因为有文件`CTestTestfile.cmake`才行，否则`ctest`找不到test）。

使用如下命令测试

```shell
ctest -N
ctest -VV
```

结果

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step4_build (master)
$ ls
cmake_install.cmake  CMakeFiles/
install_manifest.txt  MathFunctions/  Tutorial.exe*
CMakeCache.txt       CTestTestfile.cmake  Makefile  

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step4_build (master)
$ ctest.exe -N
Test project D:/Gitee/CMakeOfficialTutorial/Step4_build
  Test #1: Runs
  Test #2: Usage
  Test #3: Comp4
  Test #4: Comp9
  Test #5: Comp5
  Test #6: Comp7
  Test #7: Comp25
  Test #8: Comp-25
  Test #9: Comp0.0001

Total Tests: 9

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step4_build (master)
$ ctest.exe -VV
UpdateCTestConfiguration  from :D:/Gitee/CMakeOfficialTutorial/Step4_build/DartConfiguration.tcl
UpdateCTestConfiguration  from :D:/Gitee/CMakeOfficialTutorial/Step4_build/DartConfiguration.tcl
Test project D:/Gitee/CMakeOfficialTutorial/Step4_build
Constructing a list of tests
Done constructing a list of tests
Updating test list for fixtures
Added 0 tests to meet fixture requirements
Checking test dependency graph...
Checking test dependency graph end
test 1
    Start 1: Runs

1: Test command: D:\Gitee\CMakeOfficialTutorial\Step4_build\Tutorial.exe "25"
1: Test timeout computed to be: 10000000
1: Computing sqrt of 25 to be 13
... ...
... ...
9: Computing sqrt of 0.0001 to be 0.01
9: The square root of 0.0001 is 0.01
9/9 Test #9: Comp0.0001 .......................   Passed    0.07 sec

100% tests passed, 0 tests failed out of 9

Total Test time (real) =   1.15 sec
  
```





## Step5 系统自省（System Introspection）

教程第五节

本节主要讲述了如何通过cmake指令来查找系统平台是否提供了所预期的函数，并根据检查结果进行（条件选择）编译。



### 新的语法和命令

|  commands   |            commands            |
| :---------: | :----------------------------: |
| `include()` |    `check_symbol_exists()`     |
|  `unset()`  | `target_compile_definitions()` |



### 改动一

在`MathFunctions/CMakeLists.txt`中，添加如下指令

```cmake
# PART 1
# does this system provide the log and exp functions?
include(CheckSymbolExists)
check_symbol_exists(log "math.h" HAVE_LOG)
check_symbol_exists(exp "math.h" HAVE_EXP)
if(NOT (HAVE_LOG AND HAVE_EXP))
  unset(HAVE_LOG CACHE)
  unset(HAVE_EXP CACHE)
  set(CMAKE_REQUIRED_LIBRARIES "m")
  check_symbol_exists(log "math.h" HAVE_LOG)
  check_symbol_exists(exp "math.h" HAVE_EXP)
  if(HAVE_LOG AND HAVE_EXP)
    target_link_libraries(MathFunctions PRIVATE m)
  endif()
endif()

# PART 2
if(HAVE_LOG AND HAVE_EXP)
  target_compile_definitions(MathFunctions
                             PRIVATE "HAVE_LOG" "HAVE_EXP")
endif()
```

有两部分

- 第一部分（PART 1）
  - 通过`include(CheckSymbolExists)`引入宏`CheckSymbolExists`，用来检查一个Symbol是否存在
  - 检查系统中（platform头文件）是否存在`log`和`exp`这两个函数，把检查结果分别存入两个变量`HAVE_LOG`以及`HAVE_EXP`
  - 如果没有，就说明有可能现在是其他的一些platform，再次做检查
- 第二部分（PART 2）
  - 如果前面设置的两个变量`HAVE_LOG`以及`HAVE_EXP`都是`True`，那么就设定两个**在源代码中**可以使用的宏，名字叫`HAVE_LOG`以及`HAVE_EXP`

### 改动二

在`MathFunctions/mysqrt.cxxt`中，修改代码如下

把如下这行代码

```cpp
  double result = x;
```

修改为

```cpp
#if defined(HAVE_LOG) && defined(HAVE_EXP)
  double result = exp(log(x) * 0.5);
  std::cout << "Computing sqrt of " << x << " to be " << result
            << " using log and exp" << std::endl;
#else
  double result = x;
#endif
```

可以看到，这里在源代码中检查了宏`HAVE_LOG`以及`HAVE_EXP`，这两个宏是在CMake期间定义的。

同时也要加上`#include <cmath>`这一行。



### 编译和安装

同样地，使用如下的三条命令来编译和安装

```shell
cmake ../Step5 -G "Unix Makefiles"
cmake --build .
cmake --install . --prefix /my/install/prefix
```

结果

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step5_build (master)
$ cmake ../Step5 -G "Unix Makefiles"
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: D:/procs/mingw64/bin/gcc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: D:/procs/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for log
-- Looking for log - found
-- Looking for exp
-- Looking for exp - found
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step5_build

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step5_build (master)
$ cmake --build .
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.obj
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[100%] Linking CXX executable Tutorial.exe
[100%] Built target Tutorial

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step5_build (master)
$ cmake --install .
-- Install configuration: ""
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step5_build/MyInstallPath/bin/Tutorial.exe
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step5_build/MyInstallPath/include/TutorialConfig.h
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step5_build/MyInstallPath/lib/libMathFunctions.a
-- Installing: D:/Gitee/CMakeOfficialTutorial/Step5_build/MyInstallPath/include/MathFunctions.h
```



需要注意的是，`cmake ../Step4 -G "Unix Makefiles"`时有打印如下信息，

```shell
-- Looking for log
-- Looking for log - found
-- Looking for exp
-- Looking for exp - found
```

这表示，按照我们在`CMakeLists.txt`中的定义，在查找当前平台对应的`log`和`exp`函数（并且找到了）。





## Step6 添加自定义命令和生成文件

教程第六节



### 简述

本节主要讲述了

- 通过cmake的语法，如何生成一个头文件，使得其他源文件可以引用该头文件
- 该头文件不是手动写的，而是在cmake编译期间生成的，不在源代码的目录内（当然源代码的目录里有如何生成这个头文件的源代码）

具体地，本节是通过一个源代码文件（C++），生成一个头文件，该头文件里面是一个数组，表示的是10以内的数的平方根的结果，然后由`MathFunctions/mysqrt.cxx`引用它，以便在计算0以内的数的平方根的时候，直接查询该数组得出结果。



### 新的语法和命令

|        commands        |         variables          |
| :--------------------: | :------------------------: |
| `add_custom_command()` | `CMAKE_CURRENT_BINARY_DIR` |
|                        |                            |



`CMAKE_CURRENT_BINARY_DIR`是当前cmake编译的目录（full path）

`add_custom_command()`这个command相当于在Makefile中的一条生成-依赖指令，目的是通过定义的一条command来生成一个output，比如教程中的

```cmake
add_custom_command(
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  DEPENDS MakeTable
)
```

它相当于是Makefile中的

```makefile
OUTPUT: DEPENDS
	COMMAND
```

具体地是

```makefile
${CMAKE_CURRENT_BINARY_DIR}/Table.h: MakeTable
	MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
```

也就是说，根据`MakeTable`这个依赖，会生成一个对应的`Table.h`头文件（target）。



### 改动一

首先删除了上一节中关于`HAVE_LOG`和`HAVE_EXP`的宏的创建、检查和引用的代码部分。



### 改动二

其次，在`MathFunctions/CMakeLists.txt`中，添加如下两条指令

```cmake
add_executable(MakeTable MakeTable.cxx)

add_custom_command(
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.h
  DEPENDS MakeTable
  )
```

第一条是说，要通过`MakeTable.cxx`生成一个二进制文件（用来运行产生`Table.h`这个文件）

第二条相当于定义了一条规则，要生成一个`Table.h`这个target，它的依赖是`MakeTable`这个二进制文件。



### 改动三

再次，在`MathFunctions/CMakeLists.txt`中，修改如下两条指令

```cmake
add_library(MathFunctions
            mysqrt.cxx
            ${CMAKE_CURRENT_BINARY_DIR}/Table.h
            )
target_include_directories(MathFunctions
          INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
          PRIVATE ${CMAKE_CURRENT_BINARY_DIR}
          )
```

第一条指令是指`mysqrt.cxx`文件在生成`MathFunctions`这个lib是时候，实际上依赖于我们的生成文件`Table.h`的。

第二条指令是把`cmake`当前编译的目录加入到头文件的包含的目录列表中去，以便`mysqrt.cxx`中include这个生成的头文件时，可以找到它。



### 改动四

最后，需要修改`MathFunctions/mysqrt.cxx`中源代码，见下，需要注意的是，官网上的代码似乎有错，这里做了修复。

```cpp
#include <iostream>
#include "MathFunctions.h"
// A generated header file by cmake
#include "Table.h"
// a hack square root calculation using simple operations
double mysqrt(double x) {
  if (x <= 0) {    return 0;  }
  // Use the table to help find an initial value
  // Note that varialbe sqrtTable is defined in a generated
  // header file "Table.h"
  double result = x;
  if (x >= 1 && x < 10) {
    std::cout << "Use the table to help find an initial value " << std::endl;
    result = sqrtTable[static_cast<int>(x)];
	std::cout << "Computing sqrt of " << x << " to be " << result << std::endl;
	return result;
  }

  // do ten iterations
  for (int i = 0; i < 10; ++i) {
    if (result <= 0) { result = 0.1; }
    double delta = x - (result * result);
    result = result + 0.5 * delta / result;
    std::cout << "Computing sqrt of " << x << " to be " << result << std::endl;
  }

  return result;
}
```

实际上，生成文件`Table.h`的内容如下，

```cpp
double sqrtTable[] = {
0,
1,
1.41421,
1.73205,
2,
2.23607,
2.44949,
2.64575,
2.82843,
3,
0};
```

它就是是一个数组，表示的是10以内的数的平方根的结果，然后由`MathFunctions/mysqrt.cxx`引用它，



### 编译和安装

同样地，使用如下的三条命令来编译和安装

```shell
cmake ../Step6 -G "Unix Makefiles"
cmake --build .
cmake --install . --prefix /my/install/prefix
```

结果

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step6_build (master)
$ cmake ../Step6 -G "Unix Makefiles"
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: D:/procs/mingw64/bin/gcc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: D:/procs/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step6_build

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step6_build (master)
$ cmake --build .
[ 14%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.obj
[ 28%] Linking CXX executable MakeTable.exe
[ 28%] Built target MakeTable
[ 42%] Generating Table.h
[ 57%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.obj
[ 71%] Linking CXX static library libMathFunctions.a
[ 71%] Built target MathFunctions
[ 85%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[100%] Linking CXX executable Tutorial.exe
[100%] Built target Tutorial
```

注意，在`cmake --build .`时，有明显的信息说明生成了生成文件`Table.h`，如下

```shell
[ 28%] Built target MakeTable
[ 42%] Generating Table.h
```

最后，测试生成的二进制文件，发现在计算10以内的平方根时，确实使用了查表的方法，故结果正确。

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step6_build (master)
$ ./Tutorial.exe 2
Use the table to help find an initial value
Computing sqrt of 2 to be 1.41421
The square root of 2 is 1.41421

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step6_build (master)
$ ./Tutorial.exe 10
Computing sqrt of 10 to be 5.5
Computing sqrt of 10 to be 3.65909
Computing sqrt of 10 to be 3.19601
Computing sqrt of 10 to be 3.16246
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
Computing sqrt of 10 to be 3.16228
The square root of 10 is 3.16228
```







## Step7 生成安装包

教程第七节



### 简述

本节主要讲述了，通过`cpack`，如何生成一个安装包文件

关于generator的帮助页面：[`cpack-generators(7)`](https://cmake.org/cmake/help/latest/manual/cpack-generators.7.html#manual:cpack-generators(7))

或者可以直接查询：`cpack --help`



### 新的语法和命令

工具：`cpack`（它是和`cmake`在一个`bin`目录下）

module：`InstallRequiredSystemLibraries`

|           variables            |           variables            |
| :----------------------------: | :----------------------------: |
| `CPACK_RESOURCE_FILE_LICENSE`  | `CPACK_PACKAGE_VERSION_MAJOR ` |
| `CPACK_PACKAGE_VERSION_MINOR ` |    `CPACK_SOURCE_GENERATOR`    |



其中，在top-level的`CMakeLists.txt`中`include(InstallRequiredSystemLibraries)`这个module，使得它能够找到对应的runtime lib以便生成安装包。

后面的几个变量，是`cpack`在打包过程当中用到的，其中`CPACK_SOURCE_GENERATOR`指定了安装包的文件格式（`.tar.gz`等）



### 改动

在top-level的`CMakeLists.txt`中，添加如下指令

```cmake
# For packing use (by cpack)
include(InstallRequiredSystemLibraries)
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set(CPACK_PACKAGE_VERSION_MAJOR "${Tutorial_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${Tutorial_VERSION_MINOR}")
set(CPACK_SOURCE_GENERATOR "TGZ")
include(CPack)
```





### 打包

首先仍然需要编译生成二进制文件，然后调用`cpack`打包

```shell
cmake ../Step7 -G "Unix Makefiles"
cmake --build .
cpack -G ZIP
```

这里需要注意的是，虽然在top-level的`CMakeLists.txt`中指明了generator是`TGZ`，但它需要用到NSIS，否则就无法完成打包（这里本地没有安装NSIS）

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step7_build (master)
$ cpack
CPack Error: Cannot find NSIS compiler makensis: likely it is not installed, or not in your PATH
CPack Error: Could not read NSIS registry value. This is usually caused by NSIS not being installed. Please install NSIS from http://nsis.sourceforge.net
CPack Error: Cannot initialize the generator NSIS
```



所以，这里在`cpack`的command line中重新指明generator为`ZIP`，以便生成`.zip`包

```shell
Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step7_build (master)
$ cpack -G ZIP
CPack: Create package using ZIP
CPack: Install projects
CPack: - Run preinstall target for: Tutorial
CPack: - Install project: Tutorial []
CPack: Create package
CPack: - package: D:/Gitee/CMakeOfficialTutorial/Step7_build/Tutorial-1.0-win64.zip generated.
```

打包完成后，在目录下就生成了安装包`Tutorial-1.0-win64.zip`，正如上述log中所说。





## Step8 添加Testing Dashboard支持

教程第八节



### 简述

本节主要讲述了如何添加Testing Dashboard的支持。

实际上，`ctest`这里就是QA系统的一部分，它帮助完成编译，运行testcases，并且将结果上传到定义好的网站上去（这里利用了Kitware提供的一个公共网站）。



工具：`ctest`

module：`CTest`

|       variables       |          variables          |
| :-------------------: | :-------------------------: |
| `CTEST_PROJECT_NAME`  | `CTEST_NIGHTLY_START_TIME ` |
|  `CTEST_DROP_METHOD`  |      `CTEST_DROP_SITE`      |
| `CTEST_DROP_LOCATION` |   `CTEST_DROP_SITE_CDASH`   |



### 改动一

因为`CTest`这个module在被`include`进来的时候，会自动调用`enable_testing()`，所以在top-level的`CMakeLists.txt`里面，把

```cmake
# enable testing
enable_testing()
```

替换为

```cmake
# enable dashboard scripting
# CTest module will automatically call enable_testing()
include(CTest)
```



### 改动二

在top-level目录下面，需要创建一个`CTestConfig.cmake`文件，用来给`CTest`这个module指明以下信息

- The project name
- The project "Nightly" start time
  - The time when a 24 hour "day" starts for this project.
- The URL of the CDash instance where the submission's generated documents will be sent



```cmake
set(CTEST_PROJECT_NAME "CMakeTutorial")
set(CTEST_NIGHTLY_START_TIME "00:00:00 EST")

set(CTEST_DROP_METHOD "http")
set(CTEST_DROP_SITE "my.cdash.org")
set(CTEST_DROP_LOCATION "/submit.php?project=CMakeTutorial")
set(CTEST_DROP_SITE_CDASH TRUE)
```



### 运行结果

首先像以往一样，利用`cmake`生成`Makefile`

```shell
cmake ../Step8 -G "Unix Makefiles"
```

但之后不用编译，而是直接运行`ctest`

```cmake
ctest -VV -D Experimental
```

运行之后的log如下：

```shell

Pyrad@SSEA MINGW64 /d/Gitee/CMakeOfficialTutorial/Step8_build (master)
$ ctest -VV -D Experimental
UpdateCTestConfiguration  from :D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Parse Config file:D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
   Site: SSEA
   Build name: Win32-make
Create new tag: 20220610-1344 - Experimental
Configure project
Configure with command: "D:/procs/CMake/bin/cmake.exe" "D:/Gitee/CMakeOfficialTutorial/Step8"
Run command: "D:/procs/CMake/bin/cmake.exe" "D:/Gitee/CMakeOfficialTutorial/Step8"
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/CMakeOfficialTutorial/Step8_build
Command exited with the value: 0
UpdateCTestConfiguration  from :D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Parse Config file:D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Build project
MakeCommand:D:/procs/CMake/bin/cmake.exe --build . --config "${CTEST_CONFIGURATION_TYPE}"
Run command: "D:/procs/CMake/bin/cmake.exe" "--build" "." "--config" "Release"
[ 14%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.obj
[ 28%] Linking CXX executable MakeTable.exe
[ 28%] Built target MakeTable
[ 42%] Generating Table.h
[ 57%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.obj
[ 71%] Linking CXX static library libMathFunctions.a
[ 71%] Built target MathFunctions
[ 85%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.obj
[100%] Linking CXX executable Tutorial.exe
[100%] Built target Tutorial
Command exited with the value: 0
MakeCommand:D:/procs/CMake/bin/cmake.exe --build . --config "${CTEST_CONFIGURATION_TYPE}"
   0 Compiler errors
   0 Compiler warnings
UpdateCTestConfiguration  from :D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Parse Config file:D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Test project D:/Gitee/CMakeOfficialTutorial/Step8_build
Constructing a list of tests
Done constructing a list of tests
Updating test list for fixtures
Added 0 tests to meet fixture requirements
Checking test dependency graph...
Checking test dependency graph end
test 1
    Start 1: Runs

1: Test command: D:\Gitee\CMakeOfficialTutorial\Step8_build\Tutorial.exe "25"
1: Test timeout computed to be: 1500
1: Computing sqrt of 25 to be 13
1: Computing sqrt of 25 to be 7.46154
1: Computing sqrt of 25 to be 5.40603
1: Computing sqrt of 25 to be 5.01525
1: Computing sqrt of 25 to be 5.00002
1: Computing sqrt of 25 to be 5
1: Computing sqrt of 25 to be 5
1: Computing sqrt of 25 to be 5
1: Computing sqrt of 25 to be 5
1: Computing sqrt of 25 to be 5
1: The square root of 25 is 5
1/9 Test #1: Runs .............................   Passed    0.20 sec

#### 省略了一些log

UpdateCTestConfiguration  from :D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Parse Config file:D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
 target directory list [D:/Gitee/CMakeOfficialTutorial/Step8_build/CMakeFiles/TargetDirectories.txt]
Performing coverage
 COVFILE environment variable not found, not running  bullseye
   globbing for coverage in: D:/Gitee/CMakeOfficialTutorial/Step8_build/CMakeFiles/Continuous.dir
   globbing for coverage in: D:/Gitee/CMakeOfficialTutorial/Step8_build/CMakeFiles/ContinuousBuild.dir
   globbing for coverage in: 

### 省略了一些log
   
D:/Gitee/CMakeOfficialTutorial/Step8_build/MathFunctions/CMakeFiles/test.dir
 Cannot find any GCov coverage files.
 Not a valid Intel Coverage command.
 Cannot find any Python Trace.py coverage files.
 Cannot find Cobertura XML file: D:/Gitee/CMakeOfficialTutorial/Step8_build/coverage.xml
 Cannot find GTM coverage file: D:/Gitee/CMakeOfficialTutorial/Step8_build/gtm_coverage.mcov
 Cannot find Cache coverage file: D:/Gitee/CMakeOfficialTutorial/Step8_build/cache_coverage.cmcov
 Cannot find Jacoco coverage files: D:/Gitee/CMakeOfficialTutorial/Step8/*jacoco.xml
 Cannot find BlanketJS coverage files: D:/Gitee/CMakeOfficialTutorial/Step8/*.json
 Cannot find Delphi coverage files: D:/Gitee/CMakeOfficialTutorial/Step8_build/*(*.pas).html
 Cannot find any coverage files. Ignoring Coverage request.
UpdateCTestConfiguration  from :D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Parse Config file:D:/Gitee/CMakeOfficialTutorial/Step8_build/DartConfiguration.tcl
Submit files
   SubmitURL: http://my.cdash.org/submit.php?project=CMakeTutorial
   Upload file: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Configure.xml to http://my.cdash.org/submit.php?project=CMakeTutorial&FileName=SSEA___Win32-make___20220610-1344-Experimental___XML___Configure.xml&build=Win32-make&site=SSEA&stamp=20220610-1344-Experimental&MD5=68697147e46c795bd021649a4a8fbb06 Size: 1731
   Uploaded: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Configure.xml
   Upload file: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Build.xml to http://my.cdash.org/submit.php?project=CMakeTutorial&FileName=SSEA___Win32-make___20220610-1344-Experimental___XML___Build.xml&build=Win32-make&site=SSEA&stamp=20220610-1344-Experimental&MD5=5eebae65efe28a7be70508f63cea7428 Size: 1561
   Uploaded: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Build.xml
   Upload file: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Test.xml to http://my.cdash.org/submit.php?project=CMakeTutorial&FileName=SSEA___Win32-make___20220610-1344-Experimental___XML___Test.xml&build=Win32-make&site=SSEA&stamp=20220610-1344-Experimental&MD5=a2c6321fc5ad2113c587ca5e404c65ba Size: 13335
   Uploaded: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Test.xml
   Upload file: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Done.xml to http://my.cdash.org/submit.php?project=CMakeTutorial&FileName=SSEA___Win32-make___20220610-1344-Experimental___XML___Done.xml&build=Win32-make&site=SSEA&stamp=20220610-1344-Experimental&MD5=c37457026038fb68e75bd8fb1e50d2ef Size: 112
   Uploaded: D:/Gitee/CMakeOfficialTutorial/Step8_build/Testing/20220610-1344/Done.xml
   Submission successful

```



可以看到，`ctest`自动进行了编译，并且之后运行了`CMakeLists.txt`中的unittest，**然后**，把结果上传到了Kitware的公共网页：https://my.cdash.org/index.php?project=CMakeTutorial.





## Step9 

教程第八节



### 简述

本节主要讲述了



### 新的语法和命令

|           command            | variables |
| :--------------------------: | :-------: |
| `target_compile_definitions` |           |
|                              |           |



其中，在top-level的`CMakeLists.txt`中`include(InstallRequiredSystemLibraries)`这个module，使得它能够找到对应













