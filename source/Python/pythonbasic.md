# Python Basics


## 数字转换为银行计数字符串

```python
value = 1000000
value_str = format(value, ",")
print(value_str)
```

结果为 `1,000,000`


## 使用Python查看CPU信息

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

另，可查看[cpuinfo.py](https://github.com/pydata/numexpr/blob/master/numexpr/cpuinfo.py)来查看相关的获取方法。

## Python时间

Python module：`from datetime import datetime`

当前时间：`cur_time = datetime.now()`

格式化当前时间为字符串：`cur_time_string = cur_time.strftime(%Y-%m-%d %H:%M:%S %A %U)`

三个module，`date`，`datetime`和`time`都支持使用函数`strftime`来获取格式化的时间字符串，`strftime()` and `strptime()` Behavior（详见Python doc）

|Directive|Meaning|Sample|
|:-----|:-----|:-----|
|`%Y` |年，以四位数表示|2013，2023 |
|`%m`|月，带`0`填充|01，02，12|
|`%d`|日，带`0`填充 |01，05，16，31|
|`%A`|星期 |Monday，Sunday|
|`%U`|本年第几周，带`0`填充，星期日为每周第一天 |02，04， 52，53|
|`%H`|小时，24小时计数|01，02，12，23|
|`%M`|分钟，带`0`填充 |02，15，33|
|`%S`|秒，带`0`填充|01，22，45|


## Python Boost-Python How-to

Refer to [How to expose...](https://wiki.python.org/moin/boost.python/HowTo)


## WeakValueDictionary

为什么WeakValueDictionary里面的对象在被`del`之后，有时候再去查询，发现它还在？

[WeakValueDictionary retaining reference to object with no more strong references](https://stackoverflow.com/questions/12023717/weakvaluedictionary-retaining-reference-to-object-with-no-more-strong-references)

简而言之，就是它只是标记了对象是可以被垃圾回收机制所回收的，但具体在什么时候回收，取决于垃圾回收机制。上面的回答里面，提到了如下的用法，它在interactive shell和作为script运行时，会得到不同的打印结果。

```python
from weakref import WeakValueDictionary

class Foo(object):
	pass

f = Foo()
d = WeakValueDictionary()
d['f'] = f

print dict(d)
del f
print dict(d)
```

在interactive shell的环境中运行时，实际上两次打印都会打印出来对象的信息，而在作为script运行时，第一次打印有对象的信息，而第二次打印`d`就是一个空的字典结构了（`f`被垃圾回收机制在某个时间点回收了）

## Python Get Memory Usage

[Python equivalent of PHP's memory_get_usage()?](https://stackoverflow.com/questions/897941/python-equivalent-of-phps-memory-get-usage)


## What does `sys.getrefcount()` return?

[Fun with Python's sys.getrefcount()](https://groverlab.org/hnbfpr/2017-06-22-fun-with-sys-getrefcount.html)

简而言之，一般情况下，`sys.getrefcount(obj)`返回当前`obj`的引用数量，但它的值比我们在代码中看到的要多，因为它内部也会创建对它的引用，一般这个返回的数值比我们看到的要多`3`。

但如果计算的是类似如`2`，`1`这类很常见的数字的时候，返回值可能会很大，因为Python内部就有很多对它们的引用。


## 脚本文件的名字和当前的行号

```python
from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())

print(frameinfo.filename, frameinfo.lineno)
```


## 长字符串多行表示

```python
msg = ( "Good "
	    "day "
	    "today")
print(msg)
print(type(msg))
```

上面打印的结果是

```python
<class 'str'>
Good day today
```



## 查看当前Python的环境

查看 `include` 目录

```powershell
python -c "import sysconfig; print(sysconfig.get_path('include'))"
```

查看`lib`目录

```powershell
python -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))"
```



## Python design patterns

[Python design patterns - https://python-patterns.guide](https://python-patterns.guide/)

## How to create a singleton class in Python

Refer to link [Creating a singleton in Python](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)

A singleton

```python
class OriginPoint(object):
    """A singleton class"""
    _data = None

    def __new__(cls):
        if cls._data is None:
            # Create one and only one instance
            cls._data = super(OriginPoint, cls).__new__(cls)
            # Initialize other attributes
            cls._data._dict = dict()
            cls._data._x = 0
            cls._data._y = 0
        return cls._data

    def __init__(self):
        # Don't do anything in __init__ as it's a singleton
        pass

    def __repr__(self):
        return f"x={self._x}, y={self._y}, dict={len(self._dict)}"
```

Validate to see if it's singleton

```python
p0 = OriginPoint()
p1 = OriginPoint()
print("Address of p0 is:", p0)
print("Address of p1 is:", p1)
print(p0 is p1)
```




## Python to create list and generator

```python
a_list = [i for i in range(10)]
a_itr = (i for i in range(10))
next_element_0 = next(a_itr, None)
next_element_1 = next(a_itr, None)
```

Here `next_element_0` is `0` and `next_element_1` is `1`.



## Build a python package with `setup.py` in CMake

[Build a python package with setup.py in CMake - StackOverflow](https://stackoverflow.com/questions/29232614/build-a-python-package-with-setup-py-in-cmake)

[Using CMake with setup.py](https://stackoverflow.com/questions/13298504/using-cmake-with-setup-py)

## Python的distutils模块介绍

[Python的Distutils模块](https://blog.csdn.net/weixin_36670529/article/details/102794001)