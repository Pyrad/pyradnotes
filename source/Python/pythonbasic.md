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