# Development Settings on Windows

主要记录在windows 7/10平台下安装terminal以及相对应的环境设置



## Windows itself

### 关闭休眠功能

- 通过管理员打开命令行，然后执行`powercfg -hibernate off`
- 通过关闭该睡眠功能，可以删除`C:\hiberfil.sys`文件（文件大概6GB大小）
- 如想再开启，执行`powercfg -hibernate on`即可

### Change weird username on Windows 11

1.  Open Run Command by `Win + R`, type `netplwiz` and hit `Enter`.    
2.  In the User Accounts window, select the user account for which the username needs to be changed.    
3.  Click on Properties.    
4.  In the General tab, you'll see your existing username. Rename it to your liking after removing it.    
5.  Once the new username has been added, click the Apply button and OK.    
6.  Then, log out of your account, and you'll be greeted with your new username on the sign-in screen when you sign in.

### How to Rename a User Folder in Windows 11

[https://www.alphr.com/rename-user-folder-windows-11/](https://www.alphr.com/rename-user-folder-windows-11/)

实际上，可以直接创建一个新的账户，然后给定合理的名字，然后登录新账户之后，删除掉原先的旧账户。但需要注意的是，包括桌面等原先账户的文件就会被删除掉，需要在删除之前做备份。


### Windows Rescue Related

[老毛桃官网 - https://www.laomaotao.net](https://www.laomaotao.net/)

[USBOS - https://www.puresys.net/701.html](https://www.puresys.net/701.html)


### Windows 7 升级 Windows 10

- 前往微软网站，下载Win10升级工具
   网址：[https://www.microsoft.com/zh-cn/software-download/windows10](https://www.microsoft.com/zh-cn/software-download/windows10)
   点击“**是否希望在您的电脑上安装 Windows 10？**”下面的“**立即下载工具**”，即可下载升级程序：`MediaCreationTool22H2.exe`。
   打开此升级程序，但可能出现 `0x80072F8F-0x20000`错误，此时需要下载解决工具（官方）：`MicrosoftEasyFix51044.msi`，可以参考文章 [win7升级到win10](https://blog.csdn.net/guyuelin123/article/details/127436084)。
   点击安装`MicrosoftEasyFix51044.msi`之后，再安装`MediaCreationTool22H2.exe`，即可启动升级程序。
- 然后参考升级讲解视频：[Win7免费升级Win10的6大问题，以及解决办法](https://www.bilibili.com/video/BV1tW4y1676w/?spm_id_from=333.999.0.0)，选择进行升级。
   




## Windows Powershell

### 修改prompt

reference pages

- [Change the Execution Policy](https://codeyarns.com/tech/2011-07-30-powershell-change-the-execution-policy.html)
- [Profile Script](https://codeyarns.com/tech/2011-07-30-powershell-profile-script.html)
- [Change the Color of the Prompt](https://codeyarns.com/tech/2011-09-02-powershell-change-the-color-of-the-prompt.html#:~:text=PowerShell%20opens%20up%20in%20a%20soothing%20white-on-blue%20console,method%20and%20placing%20it%20in%20your%20profile%20script.)

首先，修改**execution policy**

```powershell
Set-ExecutionPolicy RemoteSigned
```

其次，powershell默认不会创建`profile script`，因此需要在特定位置创建特定名称的`profile script`文件

可以在`powershell`中键入`$profile`命令，然后得到下面类似的路径以及文件名

```powershell
C:\Users\Pyrad\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

这个文件其实就相当于`~/.bashrc`文件

如上创建文件，再定义一个函数`Prompt`，这个函数会覆盖默认的`Prompt`函数

```powershell
function Prompt
{
    $promptString = "PS " + $(Get-Location) + ">"
    Write-Host $promptString -NoNewline -ForegroundColor Yellow
    return " "
}
```


### 显示文件内容

类似linux中`cat`命令的powershell命令是`type`

```powershell
type filename.txt
```


### 修改`dir`显示颜色

- 下载 [Davlind/PSColor](https://github.com/Davlind/PSColor)
   ```bash
   longc@ssea MINGW64 /d/Pyrad/GitHub $ git clone git@github.com:Davlind/PSColor.git
   ```
- 使用如下命令找到Powershell的module path
   ```powershell
   PS D:\Pyrad> $env:PSModulePath
   D:\OneDrive\Documents\WindowsPowerShell\Modules;C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
   ```
- 把`release`目录拷贝到上面的任意一个路径中去，然后重命名为`PSColor`
- 在Powershell的配置文件（可通过命令`$profile`得到）中，加入`Import-Module PSColor`
- 重新启动新的Powershell，即可生效。


### 设定alias

可以定义一个函数，然后使用`New-Alias`来设定同名链接，如下。

```powershell
# Go to Gitee folder
function GoToGiteeFolder {
	Set-Location "D:\Pyrad\Gitee\"
}
New-Alias cdworkgitee GoToGiteeFolder
```


### 使用Python查看CPU信息

关于 Win32类，参考 [MSDN说明](https://learn.microsoft.com/zh-cn/windows/win32/cimwin32prov/win32-processor)

```python
"""
This needs Python 3 and module pywin32
"""

import os, platform, subprocess, re

def get_cpu_type():
    from win32com.client import GetObject
    root_winmgmts = GetObject("winmgmts:root\cimv2")
    cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
    return cpus[0].Name

def get_cpu_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command = "sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        for line in all_info.split("\n"):
            if "model name" in line:
                return re.sub(".*model name.*:", "", line, 1)
    return ""

if __name__ == "__main__":
    print(f"Current machine's CPU is {get_cpu_type()}")
    print(f"Current machine's CPU name {get_cpu_name()}")
```


## 查看环境变量

使用 `Get-ChildItem` 列出所有的环境变量

```powershell
Get-ChildItem env:
```

由于`ls`，`dir` 和 `gci` 都是 `Get-ChildItem` 的别名，因此使用它们具有同样的效果

```powershell
Get-Alias -Definition Get-ChildItem
```

结果

```powershell
PS D:\Pyrad\Gitee\webcrawler\housecrawler> Get-Alias -Definition Get-ChildItem

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           dir -> Get-ChildItem
Alias           gci -> Get-ChildItem
Alias           ls -> Get-ChildItem
```


查看单个环境变量

比如，查看`PATH`变量。

```powershell
$env:PATH
Get-Item Env:PATH
```

因为 `PATH` 变量是由分号 `;` 分隔开来，也可以使用如下命令来做字符串分割，

```powershell
$Env:Path.Split(';')
```


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



### C++ setting in VSCode

```json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "compilerPath": "C:\\path\\to\\gcc.exe",
            "cStandard": "gnu17",
            "cppStandard": "gnu++14",
            "intelliSenseMode": "windows-gcc-x64"
        }
    ],
    "version": 4
}
```





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

  

### MSYS2 installation list

目前（2023年10月10日 19:28）可以按照以下列表进行安装

```bash
pacman -S --needed base-devel mingw-w64-x86_64-toolchain
pacman -S msys/openssh
pacman -S msys/vim
pacman -S mingw64/mingw-w64-x86_64-python-pip
```

### MSYS2 Setup

#### MSYS2 Packages Page

[Package page link](https://packages.msys2.org/queue)

#### Windows Terminal加入Msys2

链接地址：[MSYS2 - Terminals](https://www.msys2.org/docs/terminals/)

简单来说，就是在Windows Terminal中的启动项里，使用如下命令

```powershell
C:/msys64/msys2_shell.cmd -defterm -here -no-start -mingw64
```

或者如下在`json`文件中进行设置（在[链接地址](https://www.msys2.org/docs/terminals/)里面有讲到）

```json
// This makes UCRT64 the default shell
"defaultProfile": "{17da3cac-b318-431e-8a3e-7fcdefe6d114}",
"profiles": {
  "list":
  [
    // ...
    {
      "guid": "{17da3cac-b318-431e-8a3e-7fcdefe6d114}",
      "name": "UCRT64 / MSYS2",
      "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -ucrt64",
      "startingDirectory": "C:/msys64/home/%USERNAME%",
      "icon": "C:/msys64/ucrt64.ico",
      "font": 
      {
        "face": "Lucida Console",
        "size": 9
      }
    },
    {
      "guid": "{71160544-14d8-4194-af25-d05feeac7233}",
      "name": "MSYS / MSYS2",
      "commandline": "C:/msys64/msys2_shell.cmd -defterm -here -no-start -msys",
      "startingDirectory": "C:/msys64/home/%USERNAME%",
      "icon": "C:/msys64/msys2.ico",
      "font": 
      {
        "face": "Lucida Console",
        "size": 9
      }
    },
    // ...
  ]
}
```



#### Terminal 中文显示切换为英文

原因是由于环境变量`LANG`被设定为`zh_CN.UTF-8`。为了切换为英文状态，设定为`C.UTF-8`即可

```bash
if [[ ! -z $LANG ]] && [[ $LANG == "zh_CN.UTF-8" ]]; then
	export LANG="C.UTF-8"
fi
```

reference page：[如何让 cygwin终端中显示的中文改成英文](https://blog.csdn.net/wb121010/article/details/53894901)


#### 如何检查当前运行的是Windows Terminal环境？

直接检查环境变量 `WT_SESSION`，或者 `WT_PROFILE_ID`是否为空，如果非空，就说明是运行在Windows Terminal环境下。

```shell
echo $WT_SESSION
echo $WT_PROFILE_ID
```

上面两条命令的结果类似如下，

```shell
4fd166dd-afc3-4b91-87ba-c74485dd8e67
{4fd166dd-afc3-4b91-87ba-c74485dd8e67}
```


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

#### 安装MSYS2版本的`bc`

这里的`bc`是指Basic Calculator。

首先搜索`bc`

```shell
pacman -Ss bc
```

在搜索结果中找到`mingw64`的版本，如下

```shell
... ...

mingw64/mingw-w64-x86_64-avr-libc 2.0.0-3 (mingw-w64-x86_64-avr-toolchain)
    The C runtime library for the AVR family of microcontrollers (mingw-w64)
mingw64/mingw-w64-x86_64-bc 1.07.1-1
    bc is an arbitrary precision numeric processing language (mingw-w64)

... ...
```

然后安装即可

```shell
pacman -S mingw64/mingw-w64-x86_64-bc
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



#### Github updated RSA SSH host key

[Explanation Page Link](https://github.blog/2023-03-23-we-updated-oour-rsa-ssh-host-key/)

Error occurs when to `git pull`

```shell
Pyrad@Pyrad MINGW64 /d/Pyrad/GitHub/all_notes
$ gp
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:uNiVztksCsDhcc0u9e8BujQXVUpKZIDTMczCvj3tD2s.
Please contact your system administrator.
Add correct host key in /home/Pyrad/.ssh/known_hosts to get rid of this message.
Offending RSA key in /home/Pyrad/.ssh/known_hosts:1
Host key for github.com has changed and you have requested strict checking.
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

To fix this,
- Remove old key
```shell
ssh-keygen -R github.com
```
- Update GitHub.com's RSA SSH key in `/.ssh/known_hosts`
```shell
curl -L https:/api.github.com/meta | jq -r '.ssh_keys | .[]' | sed -e 's/^/github.com/' >> ~/.ssh/known_hosts
```

Note, `jq` is a json parser which needs to be installed first by `pacman`.
Search package,
```shell
Pyrad@Pyrad MINGW64 /d/Pyrad/GitHub/all_notes
$ pacman -Ss jq
mingw32/mingw-w64-i686-jq 1.6-5
    Command-line JSON processor (mingw-w64)
mingw64/mingw-w64-x86_64-jq 1.6-5
    Command-line JSON processor (mingw-w64)
ucrt64/mingw-w64-ucrt-x86_64-jq 1.6-5
    Command-line JSON processor (mingw-w64)
clang32/mingw-w64-clang-i686-jq 1.6-5
    Command-line JSON processor (mingw-w64)
clang64/mingw-w64-clang-x86_64-jq 1.6-5
    Command-line JSON processor (mingw-w64)
```
Install package,
```shell
Pyrad@Pyrad MINGW64 /d/Pyrad/GitHub/all_notes
$ pacman -S mingw64/mingw-w64-x86_64-jq
resolving dependencies...
looking for conflicting packages...
...

Pyrad@Pyrad MINGW64 /d/Pyrad/GitHub/all_notes
$ which jq
/mingw64/bin/jq

```

After RSA SSH key was updated, type `yes` to add `github.com` to know hosts

```
Pyrad@Pyrad MINGW64 /d/Pyrad/GitHub/all_notes
$ gp
The authenticity of host 'github.com (20.205.243.166)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```


#### Scrapy no module named 'attrs'

[https://github.com/returntocorp/seggrep/issues/4794](https://github.com/returntocorp/seggrep/issues/4794)

简单而言，就是`attrs`这个python module比较老，哪怕已经安装了，但scrapy可能也认为找不到，所以使用`pip install --upgrade attrs`做一次升级就行。

```shell
pip install --upgrade attrs
```


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



## 通过`PIP`安装Python module

### 可安装Python package列表

最新的可以按需安装的Python package列表 2023年10月10日 17:54

目前有如下的Python package可以安装：

```bash
numpy
pandas
sphinx_rtd_theme
recommonmark
pandoc
sphinx_markdown_tables
esbonio
sympy
sphinx
sphinx-mathjax-offline
myst-parser
openpyxl
sphinxcontrib-mermaid
scrapy
```

将上述内容写入文件 `pypkglist.txt`，然后使用如下命令，一次性依次安装

```powershell
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com  -r pypkglist.txt
```

截止2023年10月10日22:21:54，Asus Windows 7上通过`pip install`安装的Python package列表如下：

```powershell
Package                       Version
----------------------------- ---------
alabaster                     0.7.12
appdirs                       1.4.4
attrs                         22.2.0
Automat                       22.10.0
Babel                         2.10.3
certifi                       2022.6.15
cffi                          1.15.1
charset-normalizer            2.1.0
colorama                      0.4.5
commonmark                    0.9.1
constantly                    15.1.0
cryptography                  39.0.2
cssselect                     1.2.0
docutils                      0.17.1
esbonio                       0.13.1
et-xmlfile                    1.1.0
filelock                      3.10.0
getmac                        0.9.3
hyperlink                     21.0.0
idna                          3.3
imagesize                     1.4.1
importlib-metadata            4.12.0
incremental                   22.10.0
itemadapter                   0.7.0
itemloaders                   1.0.6
Jinja2                        3.1.2
jmespath                      1.0.1
lxml                          4.9.2
Markdown                      3.4.1
markdown-it-py                2.1.0
MarkupSafe                    2.1.1
mdit-py-plugins               0.3.3
mdurl                         0.1.2
mpmath                        1.2.1
myst-parser                   0.18.1
numpy                         1.23.1
openpyxl                      3.1.2
packaging                     21.3
pandas                        1.4.3
pandoc                        2.2
parsel                        1.7.0
pip                           22.2.1
plumbum                       1.7.2
ply                           3.11
Protego                       0.2.1
pyasn1                        0.4.8
pyasn1-modules                0.2.8
pycparser                     2.21
pydantic                      1.9.1
PyDispatcher                  2.0.7
pygls                         0.12
Pygments                      2.12.0
pyOpenSSL                     23.0.0
pyparsing                     3.0.9
PyPDF2                        2.11.2
pyspellchecker                0.6.3
python-dateutil               2.8.2
pytz                          2022.1
pywin32                       304
PyYAML                        6.0
queuelib                      1.6.2
recommonmark                  0.7.1
requests                      2.28.1
requests-file                 1.5.1
Scrapy                        2.8.0
service-identity              21.1.0
setuptools                    49.2.1
six                           1.16.0
snowballstemmer               2.2.0
Sphinx                        5.1.1
sphinx-markdown-tables        0.0.16
sphinx-rtd-theme              1.0.0
sphinxcontrib-applehelp       1.0.2
sphinxcontrib-devhelp         1.0.2
sphinxcontrib-htmlhelp        2.0.0
sphinxcontrib-jsmath          1.0.1
sphinxcontrib-mermaid         0.7.1
sphinxcontrib-qthelp          1.0.3
sphinxcontrib-serializinghtml 1.1.5
sympy                         1.10.1
tldextract                    3.4.0
Twisted                       22.10.0
twisted-iocpsupport           1.0.2
typeguard                     2.13.3
typing_extensions             4.3.0
urllib3                       1.26.11
w3lib                         2.1.1
wheel                         0.37.1
zipp                          3.8.1
zope.interface                6.0
```


### 安装numpy

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

### 安装`pandas`

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

### 安装`sympy`

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

### 安装`sphinx`

```powershell
D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx
```

鉴于安装`sphinx_rtd_theme`会把`sphinx`这个module一起安装，所以省略安装`sphinx` module，而是直接安装`sphinx_rtd_theme` module。

如果先安装`sphinx`，再按照`sphinx_rtd_theme`，`sphinx_rtd_theme`会把之前安装好的卸载掉然后重新安装，导致版本降低了。

### 安装`sphinx_rtd_theme`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx_rtd_theme
```

安装后显示安装了：

```powershell
Installing collected packages: snowballstemmer, alabaster, zipp, urllib3, sphinxcontrib-serializinghtml, sphinxcontrib-qthelp, sphinxcontrib-jsmath, sphinxcontrib-htmlhelp, sphinxcontrib-devhelp, sphinxcontrib-applehelp, pyparsing, Pygments, MarkupSafe, imagesize, idna, docutils, colorama, charset-normalizer, certifi, babel, requests, packaging, Jinja2, importlib-metadata, sphinx

Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Pygments-2.12.0 alabaster-0.7.12 babel-2.10.3 certifi-2022.6.15 charset-normalizer-2.1.0 colorama-0.4.5 docutils-0.18.1 idna-3.3 imagesize-1.4.1 importlib-metadata-4.12.0 packaging-21.3 pyparsing-3.0.9 requests-2.28.1 snowballstemmer-2.2.0 sphinx-5.0.2 sphinxcontrib-applehelp-1.0.2 sphinxcontrib-devhelp-1.0.2 sphinxcontrib-htmlhelp-2.0.0 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-1.0.3 sphinxcontrib-serializinghtml-1.1.5 urllib3-1.26.10 zipp-3.8.1 sphinx_rtd_theme
```





### 安装`recommonmark`

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



### 安装`pandoc`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com pandoc
```

显示安装了：`pywin32, ply, plumbum, pandoc`



### 安装`sphinx_markdown_tables`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com sphinx_markdown_tables
```

显示安装了：`markdown, sphinx_markdown_tables`



### 安装`esbonio`

```powershell
PS C:\Users\Pyrad> D:\procs\python38\Scripts\pip.exe install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com esbonio
```

显示安装了：`pyspellchecker, appdirs, typing-extensions, typeguard, pydantic, pygls, esbonio`



### 安装`sphinx-mathjax-offline `

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



### How to uninstall some/all Python packages?

[Reference page](https://stackoverflow.com/questions/11248073/what-is-the-easiest-way-to-remove-all-packages-installed-by-pip)

```bash
pip freeze > packagelist.txt
pip uninstall -r packagelist.txt -y
```



### How to install some/all Python packages?

可以直接把以下module名称写入到一个文件中，然后使用上面提到的命令中的`-r <package_list_file>`来一次性完成安装，`pip`会根据依赖关系寻找并下载其他需要的module，并且如果有版本要求，可能会卸载当前低版本的module，然后重新安装高版本的package。(2022-10-07)

目前所用到的package（`pip`会一起安装别的依赖package），保存为文件`pypkglist.txt`

```shell
pandas
sphinx_rtd_theme
recommonmark
pandoc
sphinx_markdown_tables
esbonio
```

然后执行（因为墙的缘故，使用阿里云的镜像来代替默认的镜像地址）

```shell
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com esbonio -r pypkglist.txt -y
```



## ReadTheDocs

### Python Packages Installed

当前ReadTheDocs的Python package路径py-site-packages是

```shell
rtd_package_path = /home/docs/checkouts/readthedocs.org/user_builds/pyrads-notes/envs/latest/lib/python3.7/site-packages
```



目前（2023-01-07）来看，ReadTheDocs网站提供了如下的Python package。

```shell
----------------<py-site-packages>/-----------------
0 docutils-0.17.1.dist-info
1 zipp-3.11.0.dist-info
2 imagesize
3 Jinja2-3.1.2.dist-info
4 mock-1.0.1.dist-info
5 urllib3
6 readthedocs_ext
7 alabaster
8 recommonmark-0.5.0.dist-info
9 pkg_resources
10 urllib3-1.26.13.dist-info
11 Pillow.libs
12 setuptools
13 wheel-0.38.4.dist-info
14 pytz
15 alabaster-0.7.12.dist-info
16 sphinxcontrib_applehelp-1.0.2-py3.8-nspkg.pth
17 readthedocs_sphinx_ext-2.2.0.dist-info
18 pygments
19 sphinxcontrib_serializinghtml-1.1.5.dist-info
20 sphinxcontrib_devhelp-1.0.2.dist-info
21 recommonmark
22 sphinx-5.3.0.dist-info
23 typing_extensions-4.4.0.dist-info
24 snowballstemmer
25 imagesize.py
26 sphinxcontrib_htmlhelp-2.0.0-py3.9-nspkg.pth
27 imagesize-1.4.1.dist-info
28 _distutils_hack
29 sphinxcontrib_qthelp-1.0.3.dist-info
30 sphinxcontrib_qthelp-1.0.3-py3.8-nspkg.pth
31 wheel
32 idna-3.4.dist-info
33 sphinx_rtd_theme-1.1.1.dist-info
34 pip-22.3.1.dist-info
35 commonmark-0.9.1.dist-info
36 requests-2.28.1.dist-info
37 snowballstemmer-2.2.0.dist-info
38 babel
39 charset_normalizer
40 docutils
41 pip
42 packaging
43 typing_extensions.py
44 pytz-2022.7.dist-info
45 packaging-22.0.dist-info
46 requests
47 certifi-2022.12.7.dist-info
48 Babel-2.11.0.dist-info
49 sphinxcontrib_serializinghtml-1.1.5-py3.9-nspkg.pth
50 Pillow-9.4.0.dist-info
51 markupsafe
52 sphinxcontrib_htmlhelp-2.0.0.dist-info
53 sphinxcontrib_applehelp-1.0.2.dist-info
54 charset_normalizer-2.1.1.dist-info
55 sphinxcontrib
56 sphinx_rtd_theme
57 __pycache__
58 zipp
59 distutils-precedence.pth
60 sphinx
61 Pygments-2.14.0.dist-info
62 importlib_metadata-6.0.0.dist-info
63 sphinxcontrib_devhelp-1.0.2-py3.8-nspkg.pth
64 setuptools-58.2.0.dist-info
65 mock.py
66 idna
67 certifi
68 importlib_metadata
69 PIL
70 commonmark
71 sphinxcontrib_jsmath-1.0.1.dist-info
72 jinja2
73 sphinxcontrib_jsmath-1.0.1-py3.7-nspkg.pth
74 MarkupSafe-2.1.1.dist-info
---------------------------------------------------
Total packages: 75
```



### Python Packages in sphinx sub-folder

目前（2023-01-07）来看，ReadTheDocs网站提供sphinx的Python package中，有如下的子Python package。

```shell
----------------<py-site-packages>/sphinx/ext-----------------
0 parsers.py
1 jinja2glue.py
2 events.py
3 setup_command.py
4 py.typed
5 locale
6 __main__.py
7 deprecation.py
8 themes
9 directives
10 config.py
11 theming.py
12 io.py
13 pygments_styles.py
14 ext
15 highlighting.py
16 addnodes.py
17 texinputs
18 errors.py
19 search
20 cmd
21 registry.py
22 environment
23 application.py
24 pycode
25 domains
26 __init__.py
27 extension.py
28 util
29 builders
30 testing
31 templates
32 roles.py
33 __pycache__
34 transforms
35 writers
36 versioning.py
37 project.py
38 texinputs_win
---------------------------------------------------
Total packages in sphinx_path: 39
```



### Python Packages in sphinxcontrib sub-folder

目前（2023-01-07）来看，ReadTheDocs网站提供sphinxcontrib的Python package中，有如下的子Python package。

```shell
----------------<py-site-packages>/sphinxcontrib-----------------
0 applehelp
1 devhelp
2 qthelp
3 htmlhelp
4 serializinghtml
5 jsmath
---------------------------------------------------
Total packages in sphinxcontrib_path: 6
```



### Python Packages in sphinx/ext sub-folder

目前（2023-01-07）来看，ReadTheDocs网站提供sphinx/ext下面的Python package

```shell
----------------<py-site-packages>/sphinx/ext-----------------
0 imgmath.py
1 ifconfig.py
2 coverage.py
3 githubpages.py
4 imgconverter.py
5 mathjax.py
6 viewcode.py
7 inheritance_diagram.py
8 __init__.py
9 doctest.py
10 autodoc
11 duration.py
12 autosectionlabel.py
13 todo.py
14 autosummary
15 __pycache__
16 napoleon
17 graphviz.py
18 extlinks.py
19 linkcode.py
20 apidoc.py
21 intersphinx.py
Total packages: 22
```







## Sphinx

### MyST-Parser

[MyST-Paser](https://myst-parser.readthedocs.io/en/latest/index.html)是一款增强型的Markdown语法处理程序，是Sphinx和Docutils的用来解析的Markedly Structured Text（MyST）扩展程序。

```sh
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com myst-parser
```

在目前的机器上，因为其他需要的package已经安装过了，所以只安装了以下几个package。

```bash
Successfully installed markdown-it-py-2.1.0 mdit-py-plugins-0.3.3 mdurl-0.1.2 myst-parser-0.18.1 pyyaml-6.0
```

为了在ReadTheDocs上托管并生成对应的文档，这几个package也是需要下载下来

```bash
pip download myst-parser -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -d "D:\Programs\MyPyPackages\MyST_Parser"
```

然后把每个package的后缀修改为`.zip`，然后解压出来对应的Python module文件或文件目录，然后上传到repo里，修改（和修改）Sphinx的`conf.py`如下

```python
## ...
if os.environ.get('READTHEDOCS', None) == 'True':
    sys.path.insert(0, os.path.abspath(os.path.join('.', 'pyextensions')))
    sys.path.insert(0, os.path.abspath('.'))
    import myst_parser

## ...
extensions.append('myst_parser')

## ...
```

注意，上传到的目录是`_static/source/pyextensions`这个目录，它是我专门用来放置这些ReadTheDocs上没有的module的package目录。

之后，在sphinx的顶层目录`make html`时，就会调用`myst-parser`来解析Markdown文件。

【2023年10月19日 18点57分】在0.19.2版本之后，可以直接使用mermaid正常的语法了。



### MathJax

为了更方便清晰美观地在Markdown和reStructuredText中表达和书写数学公式，可以使用[MathJax](https://www.mathjax.org/)。

在[MathJax](https://www.mathjax.org/)的[GitHub Repository](https://github.com/MathJax/MathJax)下载最新的source code（当前版本是3.2.2），解压之后把目录`es5`拷贝到sphinx的`_static`目录下。

然后修改Sphinx的`conf.py`如下

```python
extensions.append('sphinx.ext.mathjax')
mathjax_path = 'es5/tex-chtml.js'
```

需要注意的是，目前sphinx似乎对Markdown文件中的公式不能使用MathJax做支持，因此生成的`html`网页中的公式不能正常显示。

暂时的解决办法是，在Markdown编辑器中边界文件，书写数学公式（编辑器本身可以支持数学公式的渲染），然后生成同名的`.rst`（reStructuredText）文件，并在`index.rst`中指明使用这个`.rst`来生成网页，这样生成的网页中MathJax就可以正常显示数学公式了。



### Mermaid for Sphinx & MyST-parser

为了使得[MyST-Paser](https://myst-parser.readthedocs.io/en/latest/index.html)能够识别mermaid，并在生成的html中正常渲染图表，需要添加[sphinxcontrib-mermaid](https://pypi.org/project/sphinxcontrib-mermaid/)这个Python package。

```shell
pip install sphinxcontrib-mermaid
```

安装之后，需要在 `conf.py` 中如下设置：

```python
extensions = []
extensions.append('myst_parser')
extensions.append('sphinxcontrib.mermaid')
```


下载之后，需要如下编写mermaid的代码块。

【在`MyST-Parser`的`0.19.2`版本之前】，为了在sphinx中使用MyST-parser进行渲染，在Markdown文件中要写成\`\`\`{mermaid}\`\`\`，而不是\`\`\`mermaid\`\`\`（即要加上一对花括号使得MyST-parser能够识别）。但这样的问题是在Markdown编辑器（比如Typora，Obsidian等）里不能正常渲染，只有通过MyST-parser在sphinx中生成网页之后才能渲染。

下面的mermaid的code block在编辑器里面**不能**实时渲染，但在生成的html文件里渲染是正常的。

```{mermaid}
graph TB
	%% s=start  e=end  f=fork  n=normal

	s([开始])-->f1{{if条件}};

	%% 分支点2
	f1--true-->n1[if语句块]-->e([结束]);
	f1--false-->f2{{else if条件}};

	%% 分支点1
	f2--true-->n2[else if语句块]-->e;
	f2--false-->n3[else语句块]-->e;
```

下面的mermaid的code block在编辑器里面**可以**实时渲染，但在生成的html文件里不能正常渲染。

```mermaid
graph TB
	%% s=start  e=end  f=fork  n=normal
	s([开始])-->f1{{if条件}};

	%% 分支点1
	f1--true-->n1[if语句块]-->e([结束]);
	f1--false-->f2{{else if条件}};

	%% 分支点2
	f2--true-->n2[else if语句块]-->e;
	f2--false-->n3[else语句块]-->e;
```

**需要注意的是**，目前（2023-01-07）ReadTheDocs似乎在它的Python site-packages下面没有mermaid的module：[sphinxcontrib-mermaid](https://pypi.org/project/sphinxcontrib-mermaid/)。因此需要手动下载Python的mermaid的module，然后上传到repo里面，再通过添加system path的方法，使得ReadTheDocs的环境可以找到这个自定义的Python module。

可以参考repo里面我自己添加的说明 [sphinxcontrib_mermaid_v071/READM_Pyrad.txt](https://gitee.com/pyrad/pyradnotes/blob/master/source/pyextensions/sphinxcontrib_mermaid_v071/READM_Pyrad.txt)：

> This is actually Python package **sphinxcontrib-mermaid**.
> And this is downloaded by the following command.
>
> Why these files are extracted here and the folder renamed as **sphinxcontrib_mermaid_v071**?
> Because ReadTheDocs doesn't have Python package **sphinxcontrib-mermaid**.
> So I have to download it manually and then upload it to the git repo.
> These 3 files(autoclassdiag.py, exceptions.py, mermaid.py) theoratically should be placed in `<py-site-packages>/sphinxcontrib`.
> But ReadTheDocs already has the path `<py-site-packages>/sphinxcontrib`, so I can't place it there.
> Thus I place it here, and add this to the system path to let it be able to find it.
>
> Download command,
>
> ```shell
> pip download sphinxcontrib-mermaid -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -d "D:\Programs\MyPyPackages\SphinxMermaid_with_its_dependency"
> ```


【在`MyST-Parser`的`0.19.2`版本之后】，就不再需要给`mermaid`加上花括号了，而是直接在`conf.py`中做如下设置之后，就可以直接在html中正常渲染，这样在Obsidian、MarkText等编辑器中就可以按照正常的写法进行编辑了：

```python
extensions = ["myst_parser", "sphinxcontrib.mermaid"]
myst_fence_as_directive = ["mermaid"]
# optional to use directive options
myst_enable_extensions = ["attrs_block"]
```

如上设置之后，就可以在编辑器中直接如下书写：

```shell
graph LR
a --> b
```

关于 `MyST-Parser`的`0.19.2`版本的说明，参见[链接网页](https://myst-parser.readthedocs.io/en/latest/develop/_changelog.html#id3)。



[It is possible to have sphinx MyST rendering mermaid](https://stackoverflow.com/questions/67364913/it-is-possible-to-have-sphinx-myst-rendering-mermaid)





### Official Links

[Welcome - Sphinx](https://www.sphinx-doc.org/en/master/index.html)

[MyST-Parser - Use Markdown in Sphinx](https://www.sphinx-doc.org/en/master/usage/markdown.html)

[MyST-Parser Official](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html)



### References Links

[Sphinx 基础教程](https://blog.csdn.net/enjoyyl/article/details/97820201)



## Obsidian

### Intro

Obsidian不是开源软件，但个人可以免费使用它，商用用途需付费获得license。

### Links

[Obsidian Official Site](https://obsidian.md/)

[两年后，我还在用的 Obsidian 插件](https://zhuanlan.zhihu.com/p/570867991?utm_id=0)

### Releases

[Obsidian Releases on Github](https://github.com/obsidianmd/obsidian-releases)

### Use

在Windows平台下面，可以使用`Ctrl + P`打开命令面板。

### Plugins

因为墙的关系，下载Obsidian的插件需要翻墙。

这里从视频[由此开始 Obsidian 使用教程 3.高级功能与插件](https://www.bilibili.com/video/BV1DB4y1H7G7/?t=921&vd_source=05aabc7e72e595bed3d072985363efa7)中的链接得到百度网盘上这些插件的[分享链接](https://pan.baidu.com/s/148Ockd8JSxwSAsXkol_0Iw?pwd=td75)，保存到了我的网盘的全部文件>Softwares>ObsidianPluginsThemes这个目录下面。

如果要安装插件，需要

- 在Obsidian的设置中关闭安全模式。

- 然后把对应的插件文件夹（整个）拷贝到Obsidian对应的vault的`.obsidian/plugins`这个目录下。如果`plugins`目录不存在，就新建一个`plugins`名称的目录。

这里我按照上面两个步骤，把`obsidian-pandoc`这个插件目录从网盘下载下来，拷贝到了`D:/Gitee/pyradnotes/.obsidian/plugins`这个目录下面，然后重启Obsidian，通过`Ctrl + P`打开命令面板，就可以看到一`Pandoc Plugin:`开头的一系列功能选项了。

比如`Pandoc Plugin: Export as reStructuredText (RST)`，就可以根据当前的`.md`文件生成一个同名的`.rst`文件。

这里发现通过Obsidian的pandoc插件生成的`.rst`文件，和通过Typora生成的`.rst`文件，有一些差别，但总体不影响生成最终的html文件（sphinx docs）。


#### Plugin Quiet-Outline

[Github of obsidian plugin quiet-outline](https://github.com/guopenghui/obsidian-quiet-outline)

How to innstall

Download from github

-   Download the latest release.
-   Extract and put the three files (`main.js`, `style.css`, `manifest.json`) to folder `{{obsidian_vault}}/.obsidian/plugins/obsidian-quiet-outline`.


#### [Stardusten / ob-table-enhancer](https://github.com/Stardusten/ob-table-enhancer)

Manipulate markdown tables without touching the source code in Obsidian.

#### [Quorafind / Obsidian-Table-Generator](https://github.com/Quorafind/Obsidian-Table-Generator)

A plugin for generate markdown table quickly like Typora.


## MathJax

### Official

[mathjax.org](https://www.mathjax.org/)

[Sphinx Official Doc](https://www.sphinx-doc.org/en/master/)





### References

[MathJax的基本使用](https://www.cnblogs.com/mqingqing123/p/12711372.html)

[Latex reStructuredText 入门 math 数学公式写法](https://blog.csdn.net/neuldp/article/details/52192915)

[如何让Sphinx_doc支持MathJax公式](https://blog.csdn.net/weixin_43590796/article/details/123103215)

[MathJax Github Repo](https://github.com/MathJax/MathJax)

[A Sample Web showing Formulas Using MathJax](https://sphinx-hoverxref.readthedocs.io/en/latest/mathjax.html)

[Sphinx and Markdown](https://coderefinery.github.io/documentation/sphinx/)

[MathJax in Markdown](https://hiltmon.com/blog/2017/01/28/mathjax-in-markdown/)







## Clangd

### How to check clangd logs

```bash
$ clangd --check=/path/to/a/file/in/your/project.cc
```

### clangd avoid background indexing

https://github.com/clangd/clangd/issues/479


## Homebrew

### Introduction

[What is homebrew?](https://docs.brew.sh/Homebrew-on-Linux)



### Installation

查看官网安装指导[页面](https://docs.brew.sh/Installation)，并对照[Installation — Homebrew Documentation](https://docs.brew.sh/Installation#alternative-installs) 这一小节如下安装

```shell
# Make a directory named homebrew (of course other names can be used)
mkdir homebrew 
# Download the tarball and extract it to the directory just made
curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
```

为了绕开GFW，使用清华开源镜像来加速，可以参考清华开源镜像的说明以及如下博客页面

[homebrew | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/homebrew/)

[Homebrew 国内使用加速 - Cocowool - 博客园](https://www.cnblogs.com/cocowool/p/speedup-homebrew.html)

```shell
# Set some env vars in Linux
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
```

然后更新

```shell
brew update --force --quiet
chmod -R go-w "$(brew --prefix)/share/zsh"
```

之后就可以安装需要的package了，比如`gcc`

```shell
brew install gcc
```



## Z-Library

### Available links

2023-09-29

[https://singlelogin.se](https://singlelogin.se)
[https://singlelogin.re](https://singlelogin.re)
[https://singlelogin.site](https://singlelogin.site)

### Send mail to ask for a link

Send an mail to blackbox@zlib.se, then a link will be received.




## 使用百度秒传

### 步骤一

确保Chrome浏览器的扩展中心里安装了油猴脚本（Tampermonkey）

### 步骤二

安装脚本 [秒传链接提取](https://greasyfork.org/zh-CN/scripts/424574-%E7%A7%92%E4%BC%A0%E9%93%BE%E6%8E%A5%E6%8F%90%E5%8F%96)

### 步骤三

安装完成秒传链接提取之后，打开网页版百度网盘，出现了秒传连接按钮，把需要转存的秒传连接拷贝进去，注意文件名之间要手动去掉空格，然后点击下载即可。

### Reference

[秒传连接提取脚本 - 文档 & 教程](https://xtsat.github.io/rapid-upload-userscript-doc/document/Info/%E8%84%9A%E6%9C%AC%E8%AF%B4%E6%98%8E.html)

[秒传连接提取脚本 - Github页面](https://github.com/mengzonefire/rapid-upload-userscript)



## Looking for Books 查找书籍资源

[Zlibrary ISBN检索](https://find.looks.wang/isbn.htm)


## Software List（可用软件列表）

30+ 个常用开源软件，小妹吐血分享 - 傻大个黑科技的文章 - 知乎
https://zhuanlan.zhihu.com/p/657376197

1. [VLC](https://apps.microsoft.com/store/detail/vlc/XPDM1ZW6815MQM?hl=zh-cn&gl=cn)
2. [ShareX](https://apps.microsoft.com/store/detail/sharex/9NBLGGH4Z1SP?hl=zh-cn&gl=cn&rtc=1)
3. [OBS](https://apps.microsoft.com/store/detail/obs-studio/XPFFH613W8V6LV)
4. [Rufus](https://apps.microsoft.com/store/detail/rufus/9PC3H3V7Q9CH?hl=zh-cn&gl=cn)
5. [Lively Wallpaper](https://apps.microsoft.com/store/detail/lively-wallpaper/9NTM2QC6QWS7?hl=zh-cn&gl=cn)
6. [Rise Media Player](https://github.com/Rise-Software/Rise-Media-Player)
7. [Cider —— Apple Music 的替代品](https://apps.microsoft.com/store/detail/cider-beta/9p21xj9d9g66)
8. [KDE Connect——Phone Link 的替代品](https://apps.microsoft.com/store/detail/kde-connect/9N93MRMSXBF0?hl=zh-cn&gl=cn)
9. [GIMP——Adobe Photoshop 的免费替代品](https://apps.microsoft.com/store/detail/gimp/XPDM27W10192Q0)
10. [Audacity](https://apps.microsoft.com/store/detail/audacity/XP8K0J757HHRDW)
11. [Shotcut — Adobe Premiere Pro 的免费替代品](https://shotcut.org/)
12. [7-Zip](https://www.7-zip.org/), [NanaZip](https://apps.microsoft.com/store/detail/nanazip/9N8G7TSCL18R)
13. [LibreOffice — Microsoft Office 的免费替代品](https://www.libreoffice.org/)
14. [QuickLook](https://apps.microsoft.com/store/detail/quicklook/9NV4BS3L1H4S)
15. [File](https://github.com/files-community/Files)
16. [ScreenToGif](https://www.screentogif.com/)
17. [Brave Browser——Chrome、Edge 的开源替代品](https://apps.microsoft.com/store/detail/brave-browser/XP8C9QZMS2PC1T)
18. [Bitwarden](https://bitwarden.com/)
19. [Blender——Autodesk Maya 和 Cinema 4D 的免费替代品](https://www.blender.org/)
20. [Okular — 付费 PDF 编辑器的免费替代品](https://apps.microsoft.com/store/detail/okular/9N41MSQ1WNM8?hl=zh-cn&gl=cn&rtc=1)
21. [Krita — Adobe Illustrator 和 Adobe Animate 的免费替代品](https://krita.org/en/)
22. [HandBrake](https://handbrake.fr/)
23. [FreeCAD — AutoCAD 的免费替代品](https://www.freecad.org/)
24. [VeraCrypt](https://www.veracrypt.fr/en/Downloads.html)
25. [Joplin — OneNote 和 Evernote 的免费替代品](https://github.com/laurent22/joplin/)
26. [BleachBit — CCleaner 的开源替代品](https://www.bleachbit.org/)
27. [Clonezilla — Macrium Reflect 的免费替代品](https://clonezilla.org/)
28. [Mailspring](https://getmailspring.com/)
29. [Transmission](https://transmissionbt.com/)
30. [ExplorerPatcher](https://github.com/valinet/ExplorerPatcher)


## Fxxking GFW


### 航空公司

[Clash](https://docs.cfw.lbyczf.com/)

-   Clash：一个 Go 语言开发的多平台代理客户端，[Github(opens new window)](https://github.com/Dreamacro/clash)
-   ClashX：Clash 的 Mac 图形客户端，[Github(opens new window)](https://github.com/yichengchen/clashX)
-   ClashForAndroid：Clash 的 Android 图形客户端，[Github(opens new window)](https://github.com/Kr328/ClashForAndroid)
-   **Clash for Windows：本项目，Clash 的 Windows/macOS/Linux 图形客户端，[Github (opens new window)](https://github.com/Fndroid/clash_for_windows_pkg)**，使用文档详见：[https://docs.cfw.lbyczf.com/](https://docs.cfw.lbyczf.com/)

[ACL4SSR - https://acl4ssr-sub.github.io/](https://acl4ssr-sub.github.io/)

[Manjaro-KDE安装配置全攻略 - ayamir的文章 - 知乎](https://zhuanlan.zhihu.com/p/114296129)

### Clash.Meta

Surfing internet with sicence - Youtube [https://www.youtube.com/watch?v=nSYPpYIxL8o](https://www.youtube.com/watch?v=nSYPpYIxL8o)[](https://www.youtube.com/watch?v=nSYPpYIxL8o)

Clash.Meta [https://github.com/MetaCubeX/Clash.Meta/tree/Alpha](https://github.com/MetaCubeX/Clash.Meta/tree/Alpha)

clash verge [https://github.com/zzzgydi/clash-verge](https://github.com/zzzgydi/clash-verge)

X2ray [https://github.com/v2fly/v2ray-core](https://github.com/v2fly/v2ray-core)

xray [https://github.com/XTLS/Xray-core](https://github.com/XTLS/Xray-core)

sing-box [https://github.com/SagerNet/sing-box](https://github.com/SagerNet/sing-box)

hysteria [https://github.com/apernet/hysteria](https://github.com/apernet/hysteria)


### Steam++ (Watt Toolkit)

[Steam++ (Watt Tookit)](https://steampp.net/)：「Watt Toolkit」是一个开源跨 平台的多功能 Steam 工具箱。

[FastGithub下载及使用](https://zhuanlan.zhihu.com/p/428454772)

[steamcommunity 302 Ver.12.1.28](https://www.dogfight360.com/blog/686/)



### 修改host文件

此办法效果不怎么好，因为它们使用的是域名污染的伎俩，仅此志之。

- 首先查询DNS地址
  - 打开域名查找网站，比如`https://tool.chinaz.com/dns/`
  - 在A类型的查询中输入`github.com`
  - 找到TTL值最小（响应时间最短）的DNS，比如`20.205.243.166`

- 修改hosts文件

  - 文件是 `C:\Windows\System32\Drivers\etc\hosts`

  - 修改此文件需要管理员权限（以管理员打开编辑）

  - 在文件原有内容末尾，添加如下

    ```sh
    ### github fast visit
    20.205.243.166  github.com
    20.205.243.166  gist.github.com
    20.205.243.166  assets-cdn.github.com
    20.205.243.166  raw.githubusercontent.com
    20.205.243.166  gist.githubusercontent.com
    20.205.243.166  cloud.githubusercontent.com
    20.205.243.166  camo.githubusercontent.com
    20.205.243.166  avatars0.githubusercontent.com
    20.205.243.166 avatars1.githubusercontent.com
    20.205.243.166 avatars2.githubusercontent.com
    20.205.243.166 avatars3.githubusercontent.com
    20.205.243.166 avatars4.githubusercontent.com
    20.205.243.166 avatars5.githubusercontent.com
    20.205.243.166 avatars6.githubusercontent.com
    20.205.243.166 avatars7.githubusercontent.com
    20.205.243.166 avatars8.githubusercontent.com
    ```

- 打开`cmd`控制台

  - 输入`ipconfig /flushdns`来刷新




