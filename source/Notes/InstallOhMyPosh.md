# How to install oh-my-posh in windows

安装环境为windows 7

时间：2022年6月17日22:45:36



## 1. Install Tabby

链接：[Tabby](https://github.com/Eugeny/tabby)

选择下载最新的安装文件，比如当前（2022年6月17日）的：`tabby-1.0.179-setup-x64.exe`



## 2. Install Nerd Fonts

下载链接：[ryanoasis/nerd-fonts](https://github.com/ryanoasis/nerd-fonts/releases)

在`Assets`中选择一种或几种下载，然后安装到操作系统中。

以`Inconsolata`这个字体为例，下载`.zip`压缩包，解压后有多个文件，选择一种（比如`Inconsolata Nerd Font Complete Windows Compatible.otf`）直接安装



## 3. Install oh-my-posh

下载链接：[JanDeDobbeleer/oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh/releases)

对于windows平台，选择`install-amd64.exe`安装包下载，然后正常安装，比如安装到目录`D:\procs\OhMyPosh`，安装时会自动把`D:\procs\OhMyPosh\bin`这个路径添加到环境变量`PATH`中去，以便后面的`shell`可以找到`oh-my-posh`这个可执行程序。



## 4. Setup in Git-Bash

在`.bashrc`这个启动脚本中添加如下命令

```bash
THEME_DIR="/d/procs/OhMyPosh/themes"
THEME_NAME="paradox.omp.json"
eval "$(oh-my-posh --init --shell bash --config ${THEME_DIR}/${THEME_NAME})" 
```

其中在`THEME_DIR`这个目录下面有很多主题，可以选择一个(`THEME_NAME`)



## 5. Setup in Tabby

在系统的字体查看窗口里面找到在步骤`2`中安装的字体名字（比如`Inconsolata Nerd Font`），然后在Tabby的Setting > Appearance中把Font修改为对应的字体名字（比如`Inconsolata Nerd Font`）

重新启动Tabby，即可生效对应主题的终端`prompt`。



## Reference
[https://zhuanlan.zhihu.com/p/402739037](https://zhuanlan.zhihu.com/p/402739037)