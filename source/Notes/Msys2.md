# MSYS2 Related Setting Notes



## MSYS2 Installation

参考官方网站首页引导：[https://www.msys2.org/](https://www.msys2.org/)

简要步骤

- 下载安装程序吗

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

  



## MSYS2 Setup

### Terminal 中文显示切换为英文

原因是由于环境变量`LANG`被设定为`zh_CN.UTF-8`。为了切换为英文状态，设定为`C.UTF-8`即可

```bash
if [[ ! -z $LANG ]] && [[ $LANG == "zh_CN.UTF-8" ]]; then
	export LANG="C.UTF-8"
fi
```

reference page：[如何让 cygwin终端中显示的中文改成英文](https://blog.csdn.net/wb121010/article/details/53894901)



### 查看可以安装的工具套件

```bash
$ pacman -Sg
```

reference page：[Windows安装MSYS2 切换zsh_整合cmder](https://www.bbsmax.com/A/D854PQ225E/)



## MSYS2 CMake with boost

### 安装MSYS2版本的`CMake`

- 要下载安装的cmake版本必须是：**`mingw-w64-x86_64-cmake`**
  - 这里安装的是**`mingw64/mingw-w64-x86_64-cmake`**
  - 搜索命令：`pacman -Ss cmake`，然后查找对应的binary
  - 安装命令：`pacman -S mingw64/mingw-w64-x86_64-cmake`



### 安装boost library

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



### CMakeLists.txt中设定boost library

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



### 编译

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





## MSYS2 CMake with boost issues



CMake FindBoost doc ([link](https://cmake.org/cmake/help/v3.9/module/FindBoost.html))

A possible workaround/solution mentioned by flynneva - [link](https://github.com/ros-perception/vision_opencv/issues/349)

Guide from MSYS2 - [link](https://www.msys2.org/docs/cmake/)

Another similar issue - [link](https://github.com/giotto-ai/giotto-tda/issues/115)

pacman cheatsheet - [link](https://devhints.io/pacman)

MSYS is an variable of CMake - [link](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)

Remember that I made some changes to file `D:\procs\msys64\mingw64\share\cmake\Modules\FindPackageHandleStandardArgs.cmake`,  remember to restore it by the backup file in a same folder.



