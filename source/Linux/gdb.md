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



## GDB save breakpoints

### Save current breakpoints as a file

```shell
save breakpoints my_bp_fname.brk
```

### Load a breakpoint file into current gdb sesseion

```shell
source my_bp_fname.brk
```

## Start GDB with a program and its arguments

`gcc` is the name of the program, and everything after it is the arguments, because `--args` is specified.

```shell
gdb --args gcc -O2 -c foo.c
```

## Run gdb without printing the front material

```shell
gdb --silent
gdb --quiet
gdb -q
```


## Run gdb with a core dump file

```shell
gdb <program_name> <core_dump_file>
```

## GDB uses a file as interactive input

If a program asks for user's input after launched, the user's input can be written into a file, and let `gdb` read that file as user's input, thus interactive input in `gdb` can be avoided.

For example, when running `corexec`, it might ask for user's confirmation and then continue,

```shell
If you wish to ignore this warning, type Y.
Typing anything else will terminate.
>
```


In this circumstances, you can type `Y`, and then hit `Enter` key to let it continue.

```shell
If you wish to ignore this warning, type Y.
Typing anything else will terminate.
> Y
```

But if the binary is attached into `gdb`, and then it asks for user's input. But there's no way to type that as `gdb` session doesn't know how to read it from `stdin`.

So write `Y` to a file (for example, `gdbStdin.in`), and start `gdb` as below,

```shell
corexec simp1_PBCSIMPLE_NDF.pjx 331 331 -color 1 -no_output < ./gdbStdin.in
```



## Print C++ macro in gdb

Links

[How do I print a #define constant in GDB](https://stackoverflow.com/questions/2934006/how-do-i-print-a-defined-constant-in-gdb)

[How to print #define value in gdb](https://stackoverflow.com/questions/26881742/how-to-print-define-value-in-gdb)


首先，需要在编译时使用 `-g3` 编译选项。

其次，才能在 `gdb` 中使用如下命令查看宏

```gdb
info macro <MACRO>
```

或者使用如下命令

```gdb
macro expand <MACRO>
```

最后，可以在`gdb`中使用命令 `help macro` 来查看和宏相关的信息。


## Print to log file

[Logging Output (Debugging with GDB) (sourceware.org)](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Logging-Output.html)

You may want to save the output of GDB commands to a file. There are several commands to control GDB’s logging.

```shell
set logging enabled [on|off]
```

Enable or disable logging.

```shell
set logging file file
```

Change the name of the current logfile. The default logfile is `gdb.txt`.

```shell
set logging overwrite [on|off]
```

By default, GDB will append to the logfile. Set `overwrite` if you want `set logging enabled on` to overwrite the logfile instead.

```shell
set logging redirect [on|off]
```

By default, GDB output will go to both the terminal and the logfile. Set `redirect` if you want output to go only to the log file.

```shell
set logging debugredirect [on|off]
```

By default, GDB debug output will go to both the terminal and the logfile. Set `debugredirect` if you want debug output to go only to the log file.

```shell
show logging
```

Show the current values of the logging settings.

You can also redirect the output of a GDB command to a shell command. See [pipe](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Shell-Commands.html#pipe).


## GDB Python Support

[GDB Python Support](https://devguide.python.org/advanced-tools/gdb/index.html)

## GDB Pretty Printer

[https://stackoverflow.com/questions/12574253/c-gdb-python-pretty-printing-tutorial](https://stackoverflow.com/questions/12574253/c-gdb-python-pretty-printing-tutorial)

[https://www.kurokatta.org/grumble/2018/05/gdb-pretty](https://www.kurokatta.org/grumble/2018/05/gdb-pretty)



## GDB tutorial

[RMS's gdb Debugger Tutorial](http://www.unknownroad.com/rtfm/gdbtut/)


## GDB Python

### Pretty Printer

为了使用STL的**pretty-printer**，需要把对应版本的gcc目录下面`libstdcxx`拷贝到某个专门给GDB使用的目录，然后在`~/.gdbinit`中加入对应的Python代码以便生效。

比如，把gcc-7.3.0中的`libstdcxx`拷贝到`~/scripts/python.utilities/PythonGdb`中：

```bash
cp -rf ${GCC_DIR}/python/libstdcxx/ ~/scripts/python.utilities/PythonGdb/libstdcxx
```

然后在`~/.gdbinit`中加入如下代码

```python
handle SIG35 noprint nostop

#------------------------------------------------------------
# Import the pretty-printer module from a local backup dir
#------------------------------------------------------------
python
import sys
sys.path.insert(0, '~/scripts/python.utilities/PythonGdb')
from libstdcxx.v6.printers import register_libstdcxx_printers
register_libstdcxx_printers(None)
end
```


### 查看编译GDB时的配置信息(Python)

可以使用`--configuration`参数进行查看

```bash
gdb --configuration
```

### gdb中执行Python script

编写Python script，**并且**以`.py`作为后缀。

然后在gdb中直接source即可

```gdb
(gdb) source myPyCmds.py
```

也可直接在gdb中键入命令`py`，进入Python prompt，输入Python代码结束之后，以`end`结尾并回车，即可执行输入的Python代码。

```gdb
(gdb) py
> import gdb
> val = gdb.Value(0)
> end
(gdb)
```


### 从gdb当前session中的variable创建对应的`gdb.Value` object

gdb提供了Python module `gdb`，可以直接import进来。

使用`gdb`这个module提供的API `parse_and_eval()`，参数是当前gdb session中的变量对应的名字（字符串），返回的值是一个`gdb.Value` object。

```python
cxx_var_name_str = "my_cxx_symbol"
val = gdb.parse_and_eval(cxx_var_name_str )
```

### GDB Pretty-Printer中显示错误的Python stack

在使用pretty-printer的时候，如果发生错误，可能只显示简短的异常信息，例如，

```gdb
(gdb) p uptr_var
$112 = Python Exception <type 'exceptions.TypeError'> expected string or buffer:
```

如果要查看更多信息，需要在gdb中设置`set pyathon print-stack [full|message]`：

```gdb
(gdb) set python print-stack full
```

然后就可以打印并查看更详细的错误信息，

```gdb
(gdb) p overflow_filter
$113 = Traceback (most recent call last):
  File "$TO_GDB_PYTHON_DIR/libstdcxx/v6/printers.py", line 144, in to_string
    if is_specialization_of(impl_type, '__uniq_ptr_impl'): # New implementation
  File "$TO_GDB_PYTHON_DIR/libstdcxx/v6/printers.py", line 108, in is_specialization_of
    return re.match('^std::(%s)?%s<.*>$' % (_versioned_namespace, template_name), type) is not None
  File "$PYTHON_DIR/lib/python2.6/re.py", line 137, in match
    return _compile(pattern, flags).match(string)
TypeError: expected string or buffer
```

可以在查看详细信息之后，把显示方式改回默认值：

```gdb
(gdb) set python print-stack message
```


### GDB Python Pretty-Printer中查看C++变量类型的操作

以`std::unique_ptr`对应的pretty printer为例。

在`$GCC_DIR/python/libstdcxx/v6/printers.py`中，对`std::unique_ptr`有如下对应的Python类处理代码。

```python
class UniquePointerPrinter:
  "Print a unique_ptr"

  def __init__ (self, typename, val):
    self.val = val

  def to_string (self):
    impl_type = self.val.type.fields()[0].type.tag
    if is_specialization_of(impl_type, '__uniq_ptr_impl'): # New implementation
      v = self.val['_M_t']['_M_t']['_M_head_impl']
    elif is_specialization_of(impl_type, 'tuple'):
      v = self.val['_M_t']['_M_head_impl']
    else:
      raise ValueError("Unsupported implementation for unique_ptr: %s" % self.val.type.fields()[0].type.tag)
    return 'std::unique_ptr<%s> containing %s' % (str(v.type.target()), str(v))
```

在函数`to_string()`中，

- `self.val`的类型是`gdb.Value`，它用来表示当前gdb session中一个对应的C/C++ object，这样以便在Python中访问。关于这个类，可以查看gnu gdb手册中*Extending GDB*这一章关于`gdb.Value`类和其上的成员的说明。

- `self.val.type`返回的是一个类型为`gdb.Type`的object。

- `self.val.type.fields()`返回的是一个Python `list` object，其中每个元素都是一个`gdb.Field`的object，可以查看手册中`gdb.Type`的说明。

- `self.val.type.fields()[0]`返回一个`gdb.Field` object

- `self.val.type.fields()[0].type`返回一个`gdb.Field` object上的`type`成员，它也是一个`gdb.Type`类型的对象。

- `self.val.type.fields()[0].type.tag`返回的是这个`gdb.Type`类型的`tag`（实际上就是一个字符串），手册中说它是*The tag name for this type. The tag name is the name after struct, union, or enum in C and C++*，也就是关键字`class`后面那个的名字。
  
  需要注意的是，有时候这个`tag`会返回一个`None`，在`std::unique_ptr`的pretty printer中我就遇到这个问题。这种情况下，我的临时办法是使用`self.val.type.fields()[0].type.name`，它返回的也是一个Python字符串，它类似于这样：`std::unique_ptr<XXXXX>::__tuple_type`。
  
  然后根据这个返回的名字字符串做判断。


