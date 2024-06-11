# Python Virtual Environment

Python 虚拟开发环境

## venv

Python 标准库中自带一个虚拟开发环境的模块，`venv`，它支持轻量级的虚拟环境。

个人理解，这里所谓的虚拟开发环境，指的就是通过 `pip` 安装那些package的时候，会安装到指定的目录下面，而这个目录是跟随project不同而不同的。

意思就是说，可以做到一个 project 就有一个虚拟开发环境对应的package 安装目录，里面安装的模块都是只对本project可见的，其他project看不到。

所以就需要创建、删除以及激活特定的虚拟开发环境，以便使用这个项目独有的那些安装包模块。

但是，使用的Python解释器，是在创建这个虚拟开发环境时所调用的那个Python版本，这个信息会写入到虚拟开发环境中的一个配置文件中（`pyvenv.cfg`），而切换到那个虚拟开发环境中时，使用的Python解释器就是那个对应版本的Python。

### 参考链接

Python 3 中自带的 venv：[venv - Creation of virtual environments](https://docs.python.org/3/library/venv.html)

创建、删除和激活 venv：[Install packages in a virtual environment using pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)

### 创建虚拟开发环境

Linux下

```shell
python -m venv /path/to/new/virtual/environment/myvenv01
```

Windows下，

```powershell
c:\> python -m venv c:\path\to\new\virtual\environment\myvenv01
```

上面的 `python` 是 `PATH` 变量中的，也可以指定特定路径下的 python。

这个命令会生成一个叫做 `myvenv01` 的目录。

一般情况下，给一个project创建虚拟开发环境，按照约定会把这个虚拟开发环境目录的名称命名为 `.venv` ，目的是为了从避免被git等版本管理所追踪。


### 激活虚拟开发环境

Linux

```shell
source .venv/bin/activate
```

Windows,

```powershell
.venv\Scripts\activate
```

为了确认已经切换到了虚拟开发环境，可以查看 `python` 的路径：

Linux下：

```shell
which python
```

输出的结果类似如下：

```shell
.venv/bin/python
```

Windows

```powershell
Get-Command python
```

输出的结果类似如下：

```powershell
.venv\Scripts\python
```

### 暂停虚拟开发环境

如果要暂时离开虚拟开发环境，或者切换到另外的虚拟开发环境，只需要执行：

```shell
deactivate
```

### 重启虚拟开发环境

和前面提到的激活开发环境一样，使用同样的命令即可重新开启对应的虚拟开发环境，参考前面的命令即可。
