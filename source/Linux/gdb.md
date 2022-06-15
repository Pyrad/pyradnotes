# GDB

This is to keep all possible stuffs related to GDB

## 打印函数里面的static variable

```gdb
(gdb) p 'longc_perf_test::longc_perf_cnt_7()::cnt'
```

这里`longc_perf_test`是`namespace`，`longc_perf_cnt_7()`是函数，`cnt`是函数`longc_perf_cnt_7()`中的`static`变量，注意单引号必须加上



## 查看变量的类型:

[https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_109.html](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_109.html)

```gdb
whatis variable_name

ptype variable_name
```



## 查看gdb是否在编译时期设置了python support

```shell
gdb --configuration
```



## 如何加载core dump文件

[http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF](http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF)



## Gdbinit file example

[https://gist.github.com/CocoaBeans/1879270](https://gist.github.com/CocoaBeans/1879270)



## 加载需要读入stdin的程序

- 开两个terminal，一个运行程序，直到运行到等待stdin的时候阻塞，另一个terminal在此时用gdb通过pid加载进程，然后再在等待stdin的terminal中输入

- Write the desired input to a file "input.txt", then redirect in gdb

  ```shell
  (gdb) r program-arg-list < input.txt
  ```

  [https://github.com/cgdb/cgdb/issues/36](https://github.com/cgdb/cgdb/issues/36)

- 
