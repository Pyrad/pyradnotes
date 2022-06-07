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



## Step 1

教程第一节



本节介绍了一个简单的例子，只有一个`cpp`文件（以及稍后引入的通过`cmake`创建的一个头文件），通过引入一个简单的`CMakeLists.txt`来说明了如何编译这个简单的`cpp`源文件。



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









## Step2

教程第二节

Adding A Library 添加一个库



### 新的命令和语法

|     commands     |      commands      |        commands         |
| :--------------: | :----------------: | :---------------------: |
|  `add_library`   | `add_subdirectory` | `target_link_libraries` |
|     `option`     |     `if/endif`     |         `list`          |
| `add_executable` |  `configure_file`  |                         |



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





## Step3

教程第三节



### 新的语法和命令

|            commands            |          commands          |
| :----------------------------: | :------------------------: |
| `target_compile_definitions()` | `target_compile_options()` |
| `target_include_directories()` | `target_link_libraries()`  |





本节主要讲述了，如何在一个库（lib）目录里面的`CMakeLists.txt`里面通过添加如下语句，使得当该库（lib）目录在被使用时（即被link时），由cmake自动include当前库的源文件目录。这样，在主目录下面的`CMakeLists.txt`里面就不用再显式地include这个库（lib）的目录以便链接。

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





## Step4

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
cmake ../Step3 -G "Unix Makefiles"
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

