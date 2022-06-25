# Development Settings on Windows

主要记录在windows 7/10平台下安装terminal以及相对应的环境设置



# MSYS2 Setting Notes



## MSYS2 Installation

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

  



## MSYS2 Setup

### MSYS2 Packages Page

[Package page link](https://packages.msys2.org/queue)



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



### 安装`pip`

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



### 安装`man`

Package[页面](https://packages.msys2.org/package/man-pages-posix?repo=msys&variant=x86_64)

```bash
$ pacman -S man-pages-posix
```



### 安装`cgdb`

不使用`pacman -S cgdb`（看起来会导致python的版本降低）

在[Package Index](https://packages.msys2.org/queue)中搜索`cgdb`，点击搜索出来的结果进入对应的Package infor页面，在对应的页面中下载如下的文件

File：[https://mirror.msys2.org/msys/x86_64/cgdb-0.7.1-3-x86_64.pkg.tar.xz](https://mirror.msys2.org/msys/x86_64/cgdb-0.7.1-3-x86_64.pkg.tar.xz)

下载之后，解压tar ball，把对应的目录拷贝到`/home/Pyrad/procs`下面去，并把`cgdb`设置为alias

```bash
alias cgdb='/home/Pyrad/procs/cgdb/bin/cgdb'
```

安装之后，记得在`~/.cgdb/cgdbrc`文件中设定箭头的类型（[官方文档](http://cgdb.github.io/docs/cgdb.html)）



# Tabby

官网链接：[https://github.com/Eugeny/tabby](https://github.com/Eugeny/tabby)

## 安装

正常安装即可

## 设置

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

  - **TERM**：这项**十分重要**，不能随便乱写，否则会导致**退格键异常**（每按键Backspace一次，光标不能删除左边的字符，反而向右移动一格），这里填写`cygwin`即可。

  - Icon：这项目前还不清楚如何设置才能使tab显示图标（已经于2022-06-25解决，即用`html`标记的写法：`<img src="D:/procs/msys64/mingw64.ico">`）





pacman -Ss pip