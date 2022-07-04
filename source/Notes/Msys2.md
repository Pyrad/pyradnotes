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



CMake FindBoost doc ([link](https://cmake.org/cmake/help/v3.9/module/FindBoost.html))

A possible workaround/solution mentioned by flynneva - [link](https://github.com/ros-perception/vision_opencv/issues/349)

Guide from MSYS2 - [link](https://www.msys2.org/docs/cmake/)

Another similar issue - [link](https://github.com/giotto-ai/giotto-tda/issues/115)

pacman cheatsheet - [link](https://devhints.io/pacman)

MSYS is an variable of CMake - [link](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)





