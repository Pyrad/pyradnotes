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

def get_cpu_type():
    from win32com.client import GetObject
    root_winmgmts = GetObject("winmgmts:root\cimv2")
    cpus = root_winmgmts.ExecQuery("Select * from Win32_Processor")
    return cpus[0].Name


if __name__ == "__main__":
    print(f"Current machine's CPU is {get_cpu_type()}")
```
