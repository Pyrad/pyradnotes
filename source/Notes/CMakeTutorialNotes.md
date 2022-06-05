# CMake Tutorial Notes

本文是记录学习CMake官方教程时的笔记与注意事项

- [官方教程链接地址](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)
- [CMake下载链接地址](https://cmake.org/download/)

- [CMake Build System Page](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#introduction)



## 前期准备

为了能够在windows平台下使用CMake，以避免可能出现的问题，需要准备以下两项

- [MinGW](https://sourceforge.net/projects/mingw-w64/files/)
- [CMake](https://cmake.org/download/)

对于CMake，下载最新版的（当前最新为3.23.2）即可，记得添加cmake的路径到`PATH`中去。

对于MinGW，需要进入[下载页面](https://sourceforge.net/projects/mingw-w64/files/)，不要下载*MinGW-W64 Online Installer*（太慢），而是选择最新的下载选项（如下）中的`x86_64-win32-seh`，它是对应windows平台的压缩包。

- **MinGW-W64 GCC-8.1.0**

  - [x86_64-posix-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-posix/sjlj/x86_64-8.1.0-release-posix-sjlj-rt_v6-rev0.7z)

  - [x86_64-posix-seh](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z)

  - [x86_64-win32-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-win32/sjlj/x86_64-8.1.0-release-win32-sjlj-rt_v6-rev0.7z)

  - [x86_64-win32-seh](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win64/Personal Builds/mingw-builds/8.1.0/threads-win32/seh/x86_64-8.1.0-release-win32-seh-rt_v6-rev0.7z)

  - [i686-posix-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-posix/sjlj/i686-8.1.0-release-posix-sjlj-rt_v6-rev0.7z)

  - [i686-posix-dwarf](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-posix/dwarf/i686-8.1.0-release-posix-dwarf-rt_v6-rev0.7z)

  - [i686-win32-sjlj](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-win32/sjlj/i686-8.1.0-release-win32-sjlj-rt_v6-rev0.7z)

  - [i686-win32-dwarf](https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/8.1.0/threads-win32/dwarf/i686-8.1.0-release-win32-dwarf-rt_v6-rev0.7z)


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



### `PROJECT` 关键字

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

`SET`关键字用来指定变量，如果后面跟一个列表，需要用空格隔开（如果文件名中有空格，那么该文件名就需要用双引号括起来）

```cmake
SET(SRC_LIST main.cpp) # 声明了变量SRC_LIST
SET(SRC_LIST main.cpp t.cpp t2.cpp) # 声明了变量SRC_LIST
```





### `MESSAGE` 关键字

