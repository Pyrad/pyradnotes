# GDB

This is to keep all possible stuffs related to GDB

## 打印函数里面的static variable

```bash
(gdb) p 'longc_perf_test::longc_perf_cnt_7()::cnt'
```

这里`longc_perf_test`是`namespace`，`longc_perf_cnt_7()`是函数，`cnt`是函数`longc_perf_cnt_7()`中的`static`变量，注意单引号必须加上



## 查看变量的类型:

[https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_109.html](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_109.html)

```bash
whatis variable_name

ptype variable_name
```



## 查看gdb是否在编译时期设置了python support

```bash
(gdb) gdb --configuration
```



## 如何加载core dump文件

[http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF](http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF)



## Gdbinit file example

[https://gist.github.com/CocoaBeans/1879270](https://gist.github.com/CocoaBeans/1879270)



## 加载需要读入stdin的程序

- 开两个terminal，一个运行程序，直到运行到等待stdin的时候阻塞，另一个terminal在此时用gdb通过pid加载进程，然后再在等待stdin的terminal中输入

- Write the desired input to a file "input.txt", then redirect in gdb

  ```bash
  (gdb) r program-arg-list < input.txt
  ```

  [https://github.com/cgdb/cgdb/issues/36](https://github.com/cgdb/cgdb/issues/36)



## GDB 查看所加载程序的参数

```bash
(gdb) show args
```



## GDB check vtable from a pointer/reference to base class object

```bash
(gdb) run
#Starting program: /home/bazis/test

Program received signal SIGTRAP, Trace/breakpoint trap.
main (argc=1, argv=0xbffff064) at test.cpp:23
23 delete pObject;

(gdb) print pObject
$1 = (BaseClass *) 0x804b008

(gdb) info vtbl pObject
vtable for 'BaseClass' @ 0x80486c8 (subobject @ 0x804b008):
[0]: 0x80485f4 <ChildClass::Test()>

(gdb) info symbol 0x80486c8
vtable for ChildClass + 8 in section .rodata of /home/bazis/test
```



## GDB Prints char* to a file

https://stackoverflow.com/questions/14609577/print-character-array-to-file-in-gdb

```bash
(gdb) pi open("myoutput_data.log","w").write(gdb.execute("print jclGlobals->pydata.source",to_string=True))
```



https://stackoverflow.com/questions/233328/how-do-i-print-the-full-value-of-a-long-string-in-gdb

This is even better, because it honors the newline/carriage return chars instead of escaping them

```bash
call (void)puts(your_string)
```



## Print length of char*

需要把`strlen`的返回值做一次转换，如下

```bash
(gdb) call strlen(charArr)
'__strlen_sse2_pminub' has unknown return type; cast the call to its declared return type
(gdb) call (int)strlen(charArr)
$6 = 5156
```



## Create std::string in GDB

[link](https://stackoverflow.com/questions/7429462/creating-c-string-in-gdb)

可以在GDB里面生成一个堆上的变量，然后赋值

```shell
(gdb) call malloc(sizeof(std::string))
$1 = (void*) 0x91a6a0
(gdb) call((std::string*)0x91a6a0)->basic_string()
(gdb) call((std::string*)0x91a6a0)->assign("Hello, World")
$2= (..., _M_p = 0x91a6f8"Hello, World"}}
(gdb) call SomeFunctionThatTakesAConstStringRef(*(const std::string*)0x91a6a0)
```



## Watch array element changes

[GDB watch point](https://undo.io/resources/gdb-watchpoint/watchpoints-more-than-watch-and-continue/)

使用 `watch` 命令来观察一个数组当中某个元素值的变化，并在变化的时候添加断点。

```shell
watch -l array_name[array_index]
```

这里`array_name`就是数组的名字，`array_index`是某个元素的索引，可以是变量名。

选项`-l`告诉编译器对变量名（或表达式）去求值（evaluate）。

