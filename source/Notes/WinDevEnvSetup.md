# Development Settings on Windows

主要记录在windows 7/10平台下安装terminal以及相对应的环境设置



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



#### 编译

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





pacman -Ss pip