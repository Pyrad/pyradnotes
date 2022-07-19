# Development Settings on Windows

主要记录在windows 7/10平台下安装terminal以及相对应的环境设置



## Windows itself

### 关闭休眠功能

- 通过管理员打开命令行，然后执行`powercfg -hibernate off`
- 通过关闭该睡眠功能，可以删除`C:\hiberfil.sys`文件（文件大概6GB大小）
- 如想再开启，执行`powercfg -hibernate on`即可



## Visual Studio Code

[Do colorization of inactive preprocessor blocks](https://github.com/Microsoft/vscode-cpptools/issues/1466)

Hey @ivsanro1, thanks for bumping this issue. We added a setting in v0.16.0 to turn this off from settings.json.

To disable the setting:

Navigate to settings.json via the default shortcut of `ctrl + ,` or by using the menu bar `File > Preferences > Settings`

Select User Settings or Workspace Settings in the right panel depending on whether you'd prefer the setting to affect your user settings or your workspace settings

In the settings search bar, enter `C_Cpp.dimInactiveRegions`

Move the cursor to the left side of `C_Cpp.dimInactiveRegions` entry in the Default Settings panel (left panel)

Select the pencil icon

Select `false`

Observe that the `C_Cpp.dimInactiveRegions` entry exists in the user/workspace settings panel (right panel), set to `false`

Observe that inactive regions are no longer colorized

I'll edit my former post with a header so that people stumbling upon this thread don't get confused. Thanks again!



## MSYS2 Setting Notes



### MSYS2 Installation

参考官方网站首页引导：[https://www.msys2.org/](https://www.msys2.org/)

简要步骤

- 下载安装程序

- 安装，并且在安装对话框的最后一步勾选**Run MSYS2 now**（会弹出terminal窗口）

- 在弹出的terminal窗口中输入

  ```bash
  $ pacman -Syu
  ```

  并且在后面输入`Y`同意安装

  

- Run "MSYS2 MSYS" from Start menu，这个会弹出另外一个terminal窗口，并再次输入

  ```bash
  $ pacman -Syu
  ```

  

- 安装基本的套件，比如官网上提到的

  ```bash
  $ pacman -S --needed base-devel mingw-w64-x86_64-toolchain
  ```

  



### MSYS2 Setup

#### MSYS2 Packages Page

[Package page link](https://packages.msys2.org/queue)



#### Terminal 中文显示切换为英文

原因是由于环境变量`LANG`被设定为`zh_CN.UTF-8`。为了切换为英文状态，设定为`C.UTF-8`即可

```bash
if [[ ! -z $LANG ]] && [[ $LANG == "zh_CN.UTF-8" ]]; then
	export LANG="C.UTF-8"
fi
```

reference page：[如何让 cygwin终端中显示的中文改成英文](https://blog.csdn.net/wb121010/article/details/53894901)



#### 查看可以安装的工具套件

```bash
$ pacman -Sg
```

reference page：[Windows安装MSYS2 切换zsh_整合cmder](https://www.bbsmax.com/A/D854PQ225E/)



#### 安装`pip`

注意可以先使用命令查询

```bash
$ pacman -Ss pip
```

在列出的信息中发现有：`mingw64/mingw-w64-x86_64-python-pip`，选它安装

```bash
$ pacman -S mingw64/mingw-w64-x86_64-python-pip

resolving dependencies...
looking for conflicting packages...

Packages (3) mingw-w64-x86_64-python-distlib-0.3.4-1  mingw-w64-x86_64-python-setuptools-59.8.0-4
             mingw-w64-x86_64-python-pip-22.0.4-2

Total Download Size:    3.30 MiB
Total Installed Size:  21.12 MiB

:: Proceed with installation? [Y/n] Y
......
```

**注意**，不能直接使用`pacman -S pip`，否则会导致安装不符合版本要求的`pip`，并可能会导致`python`版本降级。



#### 安装`man`

Package[页面](https://packages.msys2.org/package/man-pages-posix?repo=msys&variant=x86_64)

```bash
$ pacman -S man-pages-posix
```



#### 安装`cgdb`

不使用`pacman -S cgdb`（看起来会导致python的版本降低）

在[Package Index](https://packages.msys2.org/queue)中搜索`cgdb`，点击搜索出来的结果进入对应的Package infor页面，在对应的页面中下载如下的文件

File：[https://mirror.msys2.org/msys/x86_64/cgdb-0.7.1-3-x86_64.pkg.tar.xz](https://mirror.msys2.org/msys/x86_64/cgdb-0.7.1-3-x86_64.pkg.tar.xz)

下载之后，解压tar ball，把对应的目录拷贝到`/home/Pyrad/procs`下面去，并把`cgdb`设置为alias

```bash
alias cgdb='/home/Pyrad/procs/cgdb/bin/cgdb'
```

安装之后，记得在`~/.cgdb/cgdbrc`文件中设定箭头的类型（[官方文档](http://cgdb.github.io/docs/cgdb.html)）



#### 安装MSYS2版本的`CMake`

- 要下载安装的cmake版本必须是：**`mingw-w64-x86_64-cmake`**
  - 这里安装的是**`mingw64/mingw-w64-x86_64-cmake`**
  - 搜索命令：`pacman -Ss cmake`，然后查找对应的binary
  - 安装命令：`pacman -S mingw64/mingw-w64-x86_64-cmake`



#### 安装MSYS2版本的`clang`

```bash
$ pacman -S mingw-w64-clang-x86_64-toolchain
```





#### 安装boost library

- 参考在MSYS2中使用CMake：**[Using CMake in MSYS2](https://www.msys2.org/docs/cmake/)**

- Boost library的安装编译命令如下

```powershell
b2.exe install --layout=system threading=multi variant=release \
	           link=shared toolset=gcc address-model=64 \
	           --build-dir="D:\procs\boost_1_79_0_src\PyradBuild" \
	           --prefix="D:\procs\boost_1_79_0_system"
```

注意，这里要使用`--layout=system`，这样生成的library才会是不带有编译器版本信息等名字的，比如`libboost_filesystem.dll`。

这里指定了`--layout=system`之后，就必须同时指定`variant=release`

完成编译之后，boost的目录结构如下：

```powershell
boost_1_79_0_system/
	|---include/
	|		|---boost/
	|			  |---<all *.hpp headers>
	|			  |---<all_header_filer_folders>
	|			  
	|---lib/
		 |---cmake/
		 |---<all *.dll.a files>
		 |---<all *.dll files>
```



#### CMakeLists.txt中设定boost library

- 参考CMake帮助文档，MSYS2帮助文档：
  - Boost相关设定： **[FindBoost](https://cmake.org/cmake/help/latest/module/FindBoost.html)**
  - CMake variables：**[cmake-variables](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)**
  - 在MSYS2中使用CMake：**[Using CMake in MSYS2](https://www.msys2.org/docs/cmake/)**
- 首先，有一些CMake的变量可以用来查看系统信息，比如

```cmake
MESSAGE(STATUS "[PYRAD] CYGWIN: " ${CYGWIN})
MESSAGE(STATUS "[PYRAD] MINGW: " ${MINGW})
MESSAGE(STATUS "[PYRAD] MSYS: " ${MSYS})
MESSAGE(STATUS "[PYRAD] UNIX: " ${UNIX})
MESSAGE(STATUS "[PYRAD] CMAKE_SYSTEM: " ${CMAKE_SYSTEM})
MESSAGE(STATUS "[PYRAD] CMAKE_SYSTEM_NAME: " ${CMAKE_SYSTEM_NAME})
MESSAGE(STATUS "[PYRAD] CMAKE_SYSTEM_PROCESSOR: " ${CMAKE_SYSTEM_PROCESSOR})
MESSAGE(STATUS "[PYRAD] CMAKE_HOST_SYSTEM: " ${CMAKE_HOST_SYSTEM})
MESSAGE(STATUS "[PYRAD] CMAKE_HOST_SYSTEM_NAME: " ${CMAKE_HOST_SYSTEM_NAME})
```

- 然后，因为是在Windows系统下，所以要设定如下的变量，以便CMake查找和搜索

  注意，这里的路径需要设置为Windows格式的路径：`D:/procs/boost_1_79_0_system`

```cmake
### Some hints for CMake to find boost
set(MY_BOOST_HOME_DIR "D:/procs/boost_1_79_0_system")
set(BOOST_ROOT ${MY_BOOST_HOME_DIR})
set(BOOST_INCLUDEDIR ${MY_BOOST_HOME_DIR}/include)
set(BOOST_LIBRARYDIR ${MY_BOOST_HOME_DIR}/lib)
### Let CMake find boost libraries
find_package(Boost 1.65.0 REQUIRED COMPONENTS filesystem regex)
### check if boost was found
if(Boost_FOUND)
	include_directories(${Boost_INCLUDE_DIRS})
    message(STATUS "[PYRAD] boost library is found")
	message(STATUS "[PYRAD] Boost_INCLUDE_DIRS = ${Boost_INCLUDE_DIRS}.")
    message(STATUS "[PYRAD] Boost_LIBRARIES = ${Boost_LIBRARIES}.")
    message(STATUS "[PYRAD] Boost_LIB_VERSION = ${Boost_LIB_VERSION}.")
else()
    message (FATAL_ERROR "Cannot find Boost")
endif()
```



#### CMake 编译

- 使用中推荐的`Ninja` generator

```bash
$ cmake -G Ninja <path-to-source> -DCMAKE_BUILD_TYPE=Release
$ cmake --build .
```

- 为了打印出来关于Boost CMake的一些debug信息，可以加入选项：`-DBoost_DEBUG=ON`

```bash
$ cmake -G Ninja <path-to-source> -DCMAKE_BUILD_TYPE=Release -DBoost_DEBUG=ON
$ cmake --build .
```

其中，命令`cmake -G Ninja <path-to-source> -DCMAKE_BUILD_TYPE=Release -DBoost_DEBUG=ON`有类似如下的输出

```bash
Pyrad@SSEA MINGW64 /d/Gitee/cpp11/build
$ cmake ../src/ -G Ninja -DCMAKE_BUILD_TYPE=Release -DBoost_DEBUG=ON
-- The C compiler identification is GNU 12.1.0
-- The CXX compiler identification is GNU 12.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: D:/procs/msys64/mingw64/bin/cc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: D:/procs/msys64/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- [PYRAD] This is the BINARY directory: D:/Gitee/cpp11/build
-- [PYRAD] This is the SOURCE directory: D:/Gitee/cpp11/src
-- Found Boost 1.79.0 at D:/procs/boost_1_79_0_system/lib/cmake/Boost-1.79.0
--   Requested configuration: QUIET REQUIRED COMPONENTS filesystem;regex
-- BoostConfig: find_package(boost_headers 1.79.0 EXACT CONFIG REQUIRED QUIET HINTS D:/procs/boost_1_79_0_system/lib/cmake)
-- Found boost_headers 1.79.0 at D:/procs/boost_1_79_0_system/lib/cmake/boost_headers-1.79.0
-- BoostConfig: find_package(boost_filesystem 1.79.0 EXACT CONFIG REQUIRED QUIET HINTS D:/procs/boost_1_79_0_system/lib/cmake)
-- Found boost_filesystem 1.79.0 at D:/procs/boost_1_79_0_system/lib/cmake/boost_filesystem-1.79.0
-- Boost toolset is mgw12 (GNU 12.1.0)
-- Scanning D:/procs/boost_1_79_0_system/lib/cmake/boost_filesystem-1.79.0/libboost_filesystem-variant*.cmake
--   Including D:/procs/boost_1_79_0_system/lib/cmake/boost_filesystem-1.79.0/libboost_filesystem-variant-shared.cmake
--   [x] libboost_filesystem.dll.a
-- Adding boost_filesystem dependencies: atomic;headers
-- Found boost_atomic 1.79.0 at D:/procs/boost_1_79_0_system/lib/cmake/boost_atomic-1.79.0
-- Boost toolset is mgw12 (GNU 12.1.0)
-- Scanning D:/procs/boost_1_79_0_system/lib/cmake/boost_atomic-1.79.0/libboost_atomic-variant*.cmake
--   Including D:/procs/boost_1_79_0_system/lib/cmake/boost_atomic-1.79.0/libboost_atomic-variant-shared.cmake
--   [x] libboost_atomic.dll.a
-- Adding boost_atomic dependencies: headers
-- BoostConfig: find_package(boost_regex 1.79.0 EXACT CONFIG REQUIRED QUIET HINTS D:/procs/boost_1_79_0_system/lib/cmake)
-- Found boost_regex 1.79.0 at D:/procs/boost_1_79_0_system/lib/cmake/boost_regex-1.79.0
-- Boost toolset is mgw12 (GNU 12.1.0)
-- Scanning D:/procs/boost_1_79_0_system/lib/cmake/boost_regex-1.79.0/libboost_regex-variant*.cmake
--   Including D:/procs/boost_1_79_0_system/lib/cmake/boost_regex-1.79.0/libboost_regex-variant-shared.cmake
--   [x] libboost_regex.dll.a
-- Adding boost_regex dependencies: headers
-- Found Boost: D:/procs/boost_1_79_0_system/lib/cmake/Boost-1.79.0/BoostConfig.cmake (found suitable version "1.79.0", minimum required is "1.65.0") found components: filesystem regex
-- [PYRAD] boost library is found
-- [PYRAD] Boost_INCLUDE_DIRS = D:/procs/boost_1_79_0_system/include.
-- [PYRAD] Boost_LIBRARIES = Boost::filesystem;Boost::regex.
-- [PYRAD] Boost_LIB_VERSION = 1_79.
-- Configuring done
-- Generating done
-- Build files have been written to: D:/Gitee/cpp11/build
```



#### 输出`compile_commands.json`文件

```bash
$ cmake -G Ninja ../src -DCMAKE_BUILD_TYPE=Release -DCMAKE_EXPORT_COMPILE_COMMANDS=1
```





#### 查找STL header file 头文件目录

在MSYS2的terminal中，可以使用下面的命令查看头文件的目录

```bash
gcc -v -c -xc++ /dev/null
```

如果是window powershell，用`null`代替`/dev/null`

输出的结果：

```bash
Pyrad@SSEA MINGW64 /e/temp
$ gcc -v -c -xc++ /dev/null
Using built-in specs.
COLLECT_GCC=D:\procs\msys64\mingw64\bin\gcc.exe
Target: x86_64-w64-mingw32
Configured with: ../gcc-12.1.0/configure --prefix=/mingw64 --with-local-prefix=/mingw64/local --build=x86_64-w64-mingw32 --host=x86_64-w64-mingw32 --target=x86_64-w64-mingw32 --with-native-system-header-dir=/mingw64/include --libexecdir=/mingw64/lib --enable-bootstrap --enable-checking=release --with-arch=x86-64 --with-tune=generic --enable-languages=c,lto,c++,fortran,ada,objc,obj-c++,jit --enable-shared --enable-static --enable-libatomic --enable-threads=posix --enable-graphite --enable-fully-dynamic-string --enable-libstdcxx-filesystem-ts --enable-libstdcxx-time --disable-libstdcxx-pch --enable-lto --enable-libgomp --disable-multilib --disable-rpath --disable-win32-registry --disable-nls --disable-werror --disable-symvers --with-libiconv --with-system-zlib --with-gmp=/mingw64 --with-mpfr=/mingw64
--with-mpc=/mingw64 --with-isl=/mingw64 --with-pkgversion='Rev2, Built by MSYS2 project' --with-bugurl=https://github.com/msys2/MINGW-packages/issues --with-gnu-as --with-gnu-ld --disable-libstdcxx-debug --with-boot-ldflags=-static-libstdc++ --with-stage1-ldflags=-static-libstdc++
Thread model: posix
Supported LTO compression algorithms: zlib zstd
gcc version 12.1.0 (Rev2, Built by MSYS2 project)
COLLECT_GCC_OPTIONS='-v' '-c' '-mtune=generic' '-march=x86-64'
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/cc1plus.exe -quiet -v -iprefix D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/ -D_REENTRANT nul -quiet -dumpbase nul -mtune=generic -march=x86-64 -version -o D:\procs\msys64\tmp\ccUesFRE.s
GNU C++17 (Rev2, Built by MSYS2 project) version 12.1.0 (x86_64-w64-mingw32)
        compiled by GNU C version 12.1.0, GMP version 6.2.1, MPFR version 4.1.0-p13, MPC version 1.2.1, isl version isl-0.24-GMP

GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring nonexistent directory "D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/include"
ignoring duplicate directory "D:/procs/msys64/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../include/c++/12.1.0"
ignoring duplicate directory "D:/procs/msys64/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../include/c++/12.1.0/x86_64-w64-mingw32"
ignoring duplicate directory "D:/procs/msys64/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../include/c++/12.1.0/backward"
ignoring duplicate directory "D:/procs/msys64/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/12.1.0/include"
ignoring nonexistent directory "D:/a/msys64/mingw64/include"
ignoring nonexistent directory "/mingw64/include"
ignoring duplicate directory "D:/procs/msys64/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/12.1.0/include-fixed"
ignoring nonexistent directory "D:/procs/msys64/mingw64/lib/gcc/../../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/include"
ignoring nonexistent directory "D:/a/msys64/mingw64/include"
#include "..." search starts here:
#include <...> search starts here:
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../include/c++/12.1.0
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../include/c++/12.1.0/x86_64-w64-mingw32
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../include/c++/12.1.0/backward
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/include
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../include
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/include-fixed
End of search list.
GNU C++17 (Rev2, Built by MSYS2 project) version 12.1.0 (x86_64-w64-mingw32)
        compiled by GNU C version 12.1.0, GMP version 6.2.1, MPFR version 4.1.0-p13, MPC version 1.2.1, isl version isl-0.24-GMP

GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: a11494dd7faf8c9fd9d9562fe7dfbb73
COLLECT_GCC_OPTIONS='-v' '-c' '-mtune=generic' '-march=x86-64'
 D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/bin/as.exe -v -o nul.o D:\procs\msys64\tmp\ccUesFRE.s
GNU assembler version 2.38 (x86_64-w64-mingw32) using BFD version (GNU Binutils) 2.38
COMPILER_PATH=D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/;D:/procs/msys64/mingw64/bin/../lib/gcc/;D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/bin/
LIBRARY_PATH=D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/;D:/procs/msys64/mingw64/bin/../lib/gcc/;D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/lib/../lib/;D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../lib/;D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../../x86_64-w64-mingw32/lib/;D:/procs/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/12.1.0/../../../
COLLECT_GCC_OPTIONS='-v' '-c' '-mtune=generic' '-march=x86-64'
```



使用`clang`也可以得到类似的结果

```bash
clang -v -c -xc++ /dev/null
```

输出结果：

```bash
Pyrad@SSEA MINGW64 /e/temp
$ /clang64/bin/clang -v -c -xc++ /dev/null
clang version 14.0.4
Target: x86_64-w64-windows-gnu
Thread model: posix
InstalledDir: D:/procs/msys64/clang64/bin
 (in-process)
 "D:/procs/msys64/clang64/bin/clang.exe" -cc1 -triple x86_64-w64-windows-gnu -emit-obj -mrelax-all --mrelax-relocations -disable-free -clear-ast-before-backend -disable-llvm-verifier -discard-value-names -main-file-name nul -mrelocation-model pic -pic-level 2 -mframe-pointer=none -fmath-errno -ffp-contract=on -fno-rounding-math -mconstructor-aliases -mms-bitfields -funwind-tables=2 -target-cpu x86-64 -tune-cpu generic -mllvm -treat-scalable-fixed-error-as-warning -debugger-tuning=gdb -v -fcoverage-compilation-dir=E:/temp -resource-dir D:/procs/msys64/clang64/lib/clang/14.0.4 -internal-isystem D:/procs/msys64/clang64/x86_64-w64-mingw32/include/c++/v1 -internal-isystem D:/procs/msys64/clang64/include/c++/v1 -internal-isystem D:/procs/msys64/clang64/lib/clang/14.0.4/include -internal-isystem D:/procs/msys64/clang64/x86_64-w64-mingw32/include -internal-isystem D:/procs/msys64/clang64/include -fdeprecated-macro -fdebug-compilation-dir=E:/temp -ferror-limit 19 -fmessage-length=135 -fno-use-cxa-atexit -fgnuc-version=4.2.1 -fcxx-exceptions -fexceptions -exception-model=seh -fcolor-diagnostics -faddrsig -o nul.o -x c++ nul
clang -cc1 version 14.0.4 based upon LLVM 14.0.4 default target x86_64-w64-windows-gnu
ignoring nonexistent directory "D:/procs/msys64/clang64/x86_64-w64-mingw32/include/c++/v1"
ignoring nonexistent directory "D:/procs/msys64/clang64/x86_64-w64-mingw32/include"
#include "..." search starts here:
#include <...> search starts here:
 D:/procs/msys64/clang64/include/c++/v1
 D:/procs/msys64/clang64/lib/clang/14.0.4/include
 D:/procs/msys64/clang64/include
End of search list.
```





#### MSYS2 CMake with boost issues



CMake FindBoost doc ([link](https://cmake.org/cmake/help/v3.9/module/FindBoost.html))

A possible workaround/solution mentioned by flynneva - [link](https://github.com/ros-perception/vision_opencv/issues/349)

Guide from MSYS2 - [link](https://www.msys2.org/docs/cmake/)

Another similar issue - [link](https://github.com/giotto-ai/giotto-tda/issues/115)

pacman cheatsheet - [link](https://devhints.io/pacman)

MSYS is an variable of CMake - [link](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)

Remember that I made some changes to file `D:\procs\msys64\mingw64\share\cmake\Modules\FindPackageHandleStandardArgs.cmake`,  remember to restore it by the backup file in a same folder.







## Tabby

官网链接：[https://github.com/Eugeny/tabby](https://github.com/Eugeny/tabby)

### 安装

正常安装即可

### 设置

- 安装成功后，打开Tabby

- Setting -> Profiles & Connections，点击New Profiles按钮，添加一个对应`MSYS2`的profile

- 在打开的窗口中填写

  - Name：填写`MSYS2-64`，实际上这项可以随便起名字

  - Command Line：按照[官方文档](https://www.msys2.org/docs/terminals/)的描述，填写如下，

    ```bash
    D\:/procs/msys64/msys2_shell.cmd -defterm -here -no-start -mingw64
    ```

    

  - Group：可以随便起名字

  - Working Directory：选择一个目录，是terminal启动时的默认路径

  - Icon：这项目前还不清楚如何设置才能使tab显示图标（已经于2022-06-25解决，即用`html`标记的写法：`<img src="D:/procs/msys64/mingw64.ico">`）

  - **Environment**中设置启动环境变量
  
    - **TERM**：这项**十分重要**，不能随便乱写，否则会导致**退格键异常**（每按键Backspace一次，光标不能删除左边的字符，反而向右移动一格），这里填写`cygwin`即可。
    - **添加一项`HOME`环境变量**，`HOME=/home/Pyrad`，否则tabby启动后会把window的用户目录当做`HOME`目录的路径（`HOME=/c/Users/Pyrad`）





## VIM

### 安装Tcl

查看tcl官网，并按照说明安装：[tcl.tk](https://www.tcl.tk/)

- 可以下载源码，并编译安装：[**Source code download**](https://www.tcl.tk/software/tcltk/download.html)
- 也可以下载由第三方编译好的binary版本：[**Binary distributions**](https://www.tcl.tk/software/tcltk/bindist.html)
- 这里由于下载ActiveTcl需要先注册，所以下载[IronTcl](https://www.irontcl.com/)，按照其网站说明，直接解压即可使用
  - Download link：[Tcl/Tk 8.6.7 (x64)](https://www.irontcl.com/downloads/irontcl-amd64-8.6.7.zip) 
  - Extract the downloaded [**ZIP archive**](https://en.wikipedia.org/wiki/Zip_(file_format)) to the base directory where Tcl/Tk should be installed, while preserving path information.
  - Optionally, add the directory `<base>\Tcl\bin` to the [**PATH**](https://en.wikipedia.org/wiki/PATH_(variable)) environment variable.
  - Optionally, create a copy of the file `<base>\Tcl\bin\tclsh86t.exe` named `<base>\Tcl\bin\tclsh.exe` (i.e. in the same directory) to ease integration with other software packages.



### 安装Python

支持Windows 7的最后一版Python是3.8，可以按照这一版来编译Vim，同时也能满足一些vim插件的要求

需要注意的是，安装完Python之后，记得要设置环境变量

- 设置`PYTHONPATH=C:\Python38`
- 设置`PYTHONHOME=C:\Python38`
- 像`PATH`环境变量中添加Python的安装位置`C:\Python38`

注意，如果不设置`PYTHONPATH`或者`PYTHONHOME`，有可能导致`python`或`pip`无法启动，并产生以下错误

```powershell
PS D:\Gitee\pyradnotes> python
Fatal Python error: Py_Initialize: unable to load the file system codec
ModuleNotFoundError: No module named 'encodings'
```



### 通过`PIP`安装Python module

#### 安装numpy

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com numpy
```

安装后显示仅安装了`numpy`一项

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe list
Package    Version
---------- -------
numpy      1.23.1
pip        22.1.2
setuptools 49.2.1
```

#### 安装`pandas`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com pandas
```

安装后显示安装了：`pytz, six, python-dateutil, pandas`

```powershell
... ...
Installing collected packages: pytz, six, python-dateutil, pandas
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe list
Package         Version
--------------- -------
numpy           1.23.1
pandas          1.4.3
pip             22.1.2
python-dateutil 2.8.2
pytz            2022.1
setuptools      49.2.1
six             1.16.0
```

#### 安装`sympy`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sympy
```

安装后显示安装了：`mpmath, sympy`

```powershell
... ...
Installing collected packages: mpmath, sympy
Successfully installed mpmath-1.2.1 sympy-1.10.1
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe list
Package         Version
--------------- -------
mpmath          1.2.1
numpy           1.23.1
pandas          1.4.3
pip             22.1.2
python-dateutil 2.8.2
pytz            2022.1
setuptools      49.2.1
six             1.16.0
sympy           1.10.1
```

#### 安装`sphinx`

```powershell
D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx
```

安装后显示安装了：

```powershell
Installing collected packages: snowballstemmer, alabaster, zipp, urllib3, sphinxcontrib-serializinghtml, sphinxcontrib-qthelp, sphinxcontrib-jsmath, sphinxcontrib-htmlhelp, sphinxcontrib-devhelp, sphinxcontrib-applehelp, pyparsing, Pygments, MarkupSafe, imagesize, idna, docutils, colorama, charset-normalizer, certifi, babel, requests, packaging, Jinja2, importlib-metadata, sphinx

Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Pygments-2.12.0 alabaster-0.7.12 babel-2.10.3 certifi-2022.6.15 charset-normalizer-2.1.0 colorama-0.4.5 docutils-0.18.1 idna-3.3 imagesize-1.4.1 importlib-metadata-4.12.0 packaging-21.3 pyparsing-3.0.9 requests-2.28.1 snowballstemmer-2.2.0 sphinx-5.0.2 sphinxcontrib-applehelp-1.0.2 sphinxcontrib-devhelp-1.0.2 sphinxcontrib-htmlhelp-2.0.0 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.3 sphinxcontrib-serializinghtml-1.1.5 urllib3-1.26.10 zipp-3.8.1
```

#### 安装`recommonmark`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com recommonmark
```

显示安装了：`commonmark, recommonmark`

其他的dependency已经在前面安装过了，所以没有安装

```powershell
Requirement already satisfied: sphinx>=1.3.1 in d:\procs\python38\lib\site-packages (from recommonmark) (5.0.2)
Requirement already satisfied: sphinxcontrib-htmlhelp>=2.0.0 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark)
(2.0.0)
Requirement already satisfied: Jinja2>=2.3 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (3.1.2)
Requirement already satisfied: imagesize in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (1.4.1)
Requirement already satisfied: colorama>=0.3.5 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (0.4.5)
Requirement already satisfied: sphinxcontrib-serializinghtml>=1.1.5 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (1.1.5)
Requirement already satisfied: sphinxcontrib-applehelp in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (1.0.2)
Requirement already satisfied: packaging in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (21.3)
Requirement already satisfied: requests>=2.5.0 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (2.28.1)
Requirement already satisfied: babel>=1.3 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (2.10.3)
Requirement already satisfied: Pygments>=2.0 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (2.12.0)
Requirement already satisfied: alabaster<0.8,>=0.7 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (0.7.12)
Requirement already satisfied: snowballstemmer>=1.1 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (2.2.0)
Requirement already satisfied: sphinxcontrib-jsmath in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (1.0.1)
Requirement already satisfied: sphinxcontrib-qthelp in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (1.0.3)
Requirement already satisfied: importlib-metadata>=4.4 in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (4.12.0)
Requirement already satisfied: sphinxcontrib-devhelp in d:\procs\python38\lib\site-packages (from sphinx>=1.3.1->recommonmark) (1.0.2)
Requirement already satisfied: pytz>=2015.7 in d:\procs\python38\lib\site-packages (from babel>=1.3->sphinx>=1.3.1->recommonmark) (2022.1)
Requirement already satisfied: zipp>=0.5 in d:\procs\python38\lib\site-packages (from importlib-metadata>=4.4->sphinx>=1.3.1->recommonmark) (3.8.1)
Requirement already satisfied: MarkupSafe>=2.0 in d:\procs\python38\lib\site-packages (from Jinja2>=2.3->sphinx>=1.3.1->recommonmark) (2.1.1)
Requirement already satisfied: idna<4,>=2.5 in d:\procs\python38\lib\site-packages (from requests>=2.5.0->sphinx>=1.3.1->recommonmark)
(3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in d:\procs\python38\lib\site-packages (from requests>=2.5.0->sphinx>=1.3.1->recommonmark) (1.26.10)
Requirement already satisfied: certifi>=2017.4.17 in d:\procs\python38\lib\site-packages (from requests>=2.5.0->sphinx>=1.3.1->recommonmark) (2022.6.15)
Requirement already satisfied: charset-normalizer<3,>=2 in d:\procs\python38\lib\site-packages (from requests>=2.5.0->sphinx>=1.3.1->recommonmark) (2.1.0)
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in d:\procs\python38\lib\site-packages (from packaging->sphinx>=1.3.1->recommonmark) (3.0.9)
Installing collected packages: commonmark, recommonmark
Successfully installed commonmark-0.9.1 recommonmark-0.7.1
```



#### 安装`pandoc`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com pandoc
```

显示安装了：`pywin32, ply, plumbum, pandoc`



#### 安装`sphinx_rtd_theme`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx_rtd_theme
```

显示安装了：`docutils, sphinx_rtd_theme`

这里发现其实前面docutils已经安装过了，但`sphinx_rtd_theme`会把之前安装好的卸载掉然后重新安装，导致版本降低了（不知有无问题）



#### 安装`sphinx_markdown_tables`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx_markdown_tables
```

显示安装了：`markdown, sphinx_markdown_tables`



#### 安装`esbonio`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com esbonio
```

显示安装了：`pyspellchecker, appdirs, typing-extensions, typeguard, pydantic, pygls, esbonio`



#### 安装`sphinx-mathjax-offline `

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx-mathjax-offline
```

显示安装了：`sphinx-mathjax-offline`



目前通过`pip`的安装module的状态列表

```powershell
Package                       Version   Installed by which module
----------------------------- --------- ------------------------------------
alabaster                     0.7.12	<-- sphinx
appdirs                       1.4.4		<-- esbonio
Babel                         2.9.1		<-- sphinx
certifi                       2021.5.30	<-- sphinx
charset-normalizer            2.0.3		<-- sphinx
colorama                      0.4.4		<-- sphinx
commonmark                    0.9.1		<-- recommonmark
dataclasses                   0.8           
docutils                      0.16		<-- sphinx / sphinx_rtd_theme will uninstall it and re-install again
esbonio                       0.11.2	<-- esbonio
greenlet                      1.1.2         
idna                          3.2		<-- sphinx
imagesize                     1.2.0		<-- sphinx
importlib-metadata            4.6.4		<-- sphinx
Jinja2                        3.0.1		<-- sphinx
Markdown                      3.3.4		<-- sphinx_markdown_tables
MarkupSafe                    2.0.1		<-- sphinx
mpmath                        1.2.1		<-- sympy
msgpack                       1.0.4         
numpy                         1.19.5	<-- numpy
packaging                     21.0		<-- sphinx
pandas                        1.1.5		<-- pandas
pandoc                        1.1.0		<-- pandoc
pip                           21.1.3	+++ 
plumbum                       1.7.0		<-- pandoc
ply                           3.11		<-- pandoc
powerline-status              2.7           
pydantic                      1.8.2		<-- esbonio
pygls                         0.11.3	<-- esbonio
Pygments                      2.9.0		<-- sphinx
pynvim                        0.4.3         
pyparsing                     2.4.7		<-- sphinx
pypiwin32                     223           
pyspellchecker                0.6.3		<-- esbonio
python-dateutil               2.8.2		<-- pandas
pytz                          2021.1	<-- pandas
pywin32                       301		<-- pandoc
recommonmark                  0.7.1		<-- recommonmark
requests                      2.26.0	<-- sphinx
setuptools                    39.0.1	+++ 
six                           1.16.0	<-- pandas
snowballstemmer               2.1.0		<-- sphinx
Sphinx                        4.1.1		<-- sphinx
sphinx-markdown-tables        0.0.15	<-- sphinx_markdown_tables
sphinx-mathjax-offline        0.0.1		<-- sphinx-mathjax-offline 
sphinx-rtd-theme              0.5.2		<-- sphinx_rtd_theme
sphinxcontrib-applehelp       1.0.2		<-- sphinx
sphinxcontrib-devhelp         1.0.2		<-- sphinx
sphinxcontrib-htmlhelp        2.0.0		<-- sphinx
sphinxcontrib-jsmath          1.0.1		<-- sphinx
sphinxcontrib-qthelp          1.0.3		<-- sphinx
sphinxcontrib-serializinghtml 1.1.5		<-- sphinx
sympy                         1.9		<-- sympy
typeguard                     2.13.3	<-- esbonio
typing-extensions             3.10.0.0	<-- esbonio
urllib3                       1.26.6	<-- sphinx
zipp                          3.5.0		<-- sphinx
```



### 安装注意事项

因为vim的很多plugin需要用到python的支持（目前主要是python3了），所以要注意

- 下载的vim 32/64bit的版本要和本地的python3的32/64bit的版本一致，否则`:echo has("python3")`永远返回`0`（即vim是64bit版本，那么python也要是64bit版本）

- 可以不用把新版本的python加到`PATH`环境变量中去，但是要在`$VIM\_vimr`中添加对应的变量设置，否则同样地`:echo has("python3")`永远返回`0`

  ```vim
  " ------------------------------------------------------
  " Python3 support
  " ------------------------------------------------------
  function s:setup_python3_dyn()
      let &pythonthreedll='D:/procs/python38/python38.dll'
      let &pythonthreehome='D:/procs/python38
  endfunction " End of function setup_python3_dyn
  
  """ ------------------------------------------------------
  """ Setup for the coc-nvim
  """ ------------------------------------------------------
  function s:setup_python3()
      let g:python3_host_prog='D:/procs/python38/python.exe'
  endfunction
  

- 在windows下，如果从source编译安装时，在MSYS2的terminal里，使用如下命令编译

  ```bash
  $ pwd
  /d/procs/Vim9Compiled/vim90/src
  $ make -f Make_ming.mak \
  	PYTHON3=D:/procs/python38 DYNAMIC_PYTHON3=yes PYTHON3_VER=38
  ```

  之后生成的`gvim.exe`就在这个`src`目录下面，需要注意的是从源码编译时，根据目录结构，`plug.vim`应该放在`D:\procs\Vim9Compiled\vim90\runtime\autoload`下面，以免启动时无法找到并加载。

- 

- 

- 

