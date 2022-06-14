# GDB

This is to keep all possible stuffs related to GDB

1. 打印一个函数里面的static variable

    ```gdb
    (gdb) p 'longc_perf_test::longc_perf_cnt_7()::cnt'
    ```
    这里`longc_perf_test`是`namespace`，`longc_perf_cnt_7()`是函数，`cnt`是函数`longc_perf_cnt_7()`中的`static`变量，注意单引号必须加上

2. 查看一个变量的类型: 

    [https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_109.html](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_node/gdb_109.html)

    ```gdb
    whatis variable_name
    
    ptype variable_name
    ```

3. 查看gdb是否在编译时期设置了python support

    ```shell
    gdb --configuration
    ```

4. 如何加载core dump文件

    [http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF](http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF)

5. Gdbinit file example

    [https://gist.github.com/CocoaBeans/1879270](https://gist.github.com/CocoaBeans/1879270)
