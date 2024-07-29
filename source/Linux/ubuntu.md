# Ubuntu Linux


## 国内配置镜像源

[Ubuntu 镜像源 - 阿里云](https://developer.aliyun.com/mirror/ubuntu) 中的配置步骤说明

### ubuntu 配置

#### ubuntu 24.04 (noble) 之前的配置

如果是较老版本的 Ubuntu，可以打开文件  `/etc/apt/sources.list` ， 把其中默认的，

```text
http://archive.ubuntu.com/
```

替换为

```text
http://mirrors.aliyun.com/
```

替换之后，便是如下的单行设置的办法

```text
# File /etc/apt/sources.list

deb https://mirrors.aliyun.com/ubuntu/ noble main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ noble-security main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble-security main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ noble-updates main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble-updates main restricted universe multiverse

# deb https://mirrors.aliyun.com/ubuntu/ noble-proposed main restricted universe multiverse
# deb-src https://mirrors.aliyun.com/ubuntu/ noble-proposed main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ noble-backports main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ noble-backports main restricted universe multiverse

```

#### ubuntu 24.04 (noble) 之后的配置

但是，如果是较新版本的 Ubuntu （24.04 LTS），文件 `/etc/apt/sources.list` 被移动到了 `/etc/apt/sources.list.d/` 目录下，并且重命名为了 `/etc/apt/sources.list.d/ubunut.sources`。

同时，设置格式也发生了变化，根据原始样例，最终可以修改如下

```shell
# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.

## Ubuntu distribution repository
##
## The following settings can be adjusted to configure which packages to use from Ubuntu.
## Mirror your choices (except for URIs and Suites) in the security section below to
## ensure timely security updates.
## 
## Types: Append deb-src to enable the fetching of source package.
## URIs: A URL to the repository (you may add multiple URLs)
## Suites: The following additional suites can be configured
##   <name>-updates   - Major bug fix updates produced after the final release of the
##                      distribution.
##   <name>-backports - software from this repository may not have been tested as
##                      extensively as that contained in the main release, although it includes
##                      newer versions of some applications which may provide useful features.
##                      Also, please note that software in backports WILL NOT receive any review
##                      or updates from the Ubuntu security team.
## Components: Aside from main, the following components can be added to the list
##   restricted  - Software that may not be under a free license, or protected by patents.
##   universe    - Community maintained packages. Software in this repository receives maintenance
##                 from volunteers in the Ubuntu community, or a 10 year security maintenance
##                 commitment from Canonical when an Ubuntu Pro subscription is attached.
##   multiverse  - Community maintained of restricted. Software from this repository is
##                 ENTIRELY UNSUPPORTED by the Ubuntu team, and may not be under a free 
##                 licence. Please satisfy yourself as to your rights to use the software.
##                 Also, please note that software in multiverse WILL NOT receive any
##                 review or updates from the Ubuntu security team.
##
## See the sources.list(5) manual page for further settings.
## See the sources.list(5) manual page for further settings. 
                                                  
#################################################################   
# Commented out by Pyrad at 2024-07-29 13:33                    
#################################################################  
# Types: deb                                                       
# URIs: http://archive.ubuntu.com/ubuntu/                     
# Suites: noble noble-updates noble-backports               
# Components: main universe restricted multiverse         
# Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg  
                                                                 
#################################################################   
# Commented out by Pyrad at 2024-07-29 13:33                      
#################################################################     
# ## Ubuntu security updates. Aside from URIs and Suites,              
# ## this should mirror your choices in the previous section.         
# Types: deb 
# URIs: http://security.ubuntu.com/ubuntu/
# Suites: noble-security
# Components: main universe restricted multiverse
# Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

Types: deb deb-src
URIs: http://mirrors.aliyun.com/ubuntu/
Suites: noble noble-updates noble-backports noble-security
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

可以看到，原先多行的设置命令，被压缩成了几行就完成了设定。


### Tcl/Tk Download

[Download Tcl/Tk Sources - Tcl Developer Xchange](https://tcl.tk/software/tcltk/download.html)

## Installing Compilers

[InstallingCompilers - Community Help Wiki - Ubuntu Documentation](https://help.ubuntu.com/community/InstallingCompilers)

```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential
gcc -v
make -v
```

## Other fundermental packages

```shell
sudo apt-get install flex bison cmake
sudo apt-get install tcl tk
sudo apt-get install locate
```

注意，使用 WSL Linux 下使用 `updatedb` ，可能会访问到 `/mnt/d` 这样的Windows文件目录，从而导致 hang（？），暂时不知道如何解决。