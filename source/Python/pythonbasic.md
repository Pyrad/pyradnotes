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
