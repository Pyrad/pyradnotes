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


## GDB 查看当前加载的 symbol（binary）

Check the `main` function located in which symbol/binary

```gdb
info symbol main
```

reference: [https://visualgdb.com/gdbreference/commands/info_symbol](https://visualgdb.com/gdbreference/commands/info_symbol)




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


## 查看GDB当前加载的程序路径

[Show the location of the executable in GDB](https://stackoverflow.com/questions/71518645/show-the-location-of-the-executable-in-gdb)

```gdb
info file
```

## Learning GDB Notes

[https://blog.csdn.net/kafeiflynn/article/details/6712888](https://blog.csdn.net/kafeiflynn/article/details/6712888)

## GDB watch std::vector

[How to "watch" the size of a C++ std::vector in gdb? - StackOverflow](https://stackoverflow.com/questions/8249048/how-to-watch-the-size-of-a-c-stdvector-in-gdb)

假设 `vec` 是一个 `std::vector<int>`。

```gdb
(gdb) p vec._M_impl._M_finish
$2 = (int *) 0x0

(gdb) p &vec._M_impl._M_finish
$3 = (int **) 0x7fffffffd878

(gdb) watch *$3
Hardware watchpoint 2: *$3

(gdb) c

Hardware watchpoint 3: *$4

Old value = (int *) 0x0
New value = (int *) 0x604010

```

简而言之：

- 获得这个 `std::vector<int>` 的底层数组实现的尾部指针：`vec._M_impl._M_finish`

- 添加硬件断点，检测存储这个尾部指针的地址上，内容的变化，也就是这个尾部指针的值的变化。

- 继续执行程序，直到检测到这个尾部指针值的变化。



## GDB info command

[GDB中的info命令：一次全面的探索 - 泡沫o0的文章 - 知乎](https://zhuanlan.zhihu.com/p/661431501)

|命令 (Command)|用途 (Purpose)|使用场景 (Usage Scenario)|
|----------------|----------------|--------------------------|
| `info program` | Execution status of the program. |程序的执行状态（显式程序的加载地址、执行路径等）|
| `info source` | Information about the current source file. | 有关当前源文件的信息（包括文件名行数等） |
| `info locals` | All local variables of current stack frame or those matching REGEXPs. | 查看当前堆栈帧的所有局部变量 |
| `info breakpoints` | Status of specified breakpoints. | 查看指定断点的状态 |
| `info target` | Names of targets and files being debugged. |正在调试的目标和文件的名称 |
| `info threads` |Display currently known threads.|显示当前已知的线程（显示当前程序的线程信息：线程编号、状态等）|
| `info inferiors` | Print a list of inferiors being managed. |打印正在管理的下级列表（显示当前程序的进程信息：进程编号、状态等） |
|--- |---|---|
| info address | Describe where symbol SYM is stored. | 查看符号SYM的存储位置 |
| info all-registers | List of all registers and their contents, for selected stack frame. | 查看选定堆栈帧的所有寄存器及其内容 |
| info args |All argument variables of current stack frame or those matching REGEXPs.| 查看当前堆栈帧的所有参数变量 |
| info auto-load | Print current status of auto-loaded files. | 打印自动加载文件的当前状态 |
| info auxv | Display the inferior's auxiliary vector. | 显示下级的辅助向量 |
| info bookmarks | Status of user-settable bookmarks. | 查看用户设置的书签状态 |
| info checkpoints | IDs of currently known checkpoints. | 查看当前已知的检查点ID |
| info classes | All Objective-C classes, or those matching REGEXP. | 查看所有Objective-C类或匹配的类 |
| info common | Print out the values contained in a Fortran COMMON block. | 打印Fortran COMMON块中的值 |
| info copying | Conditions for redistributing copies of GDB. | GDB复制的分发条件 |
| info dcache | Print information on the dcache performance. | 打印dcache性能信息 |
| info display | Expressions to display when program stops. | 程序停止时要显示的表达式 |
| info exceptions | List all Ada exception names. | 列出所有Ada异常名称 |
| info extensions | All filename extensions associated with a source language. | 与源语言关联的所有文件名扩展名 |
| info files | Names of targets and files being debugged. | 正在调试的目标和文件的名称 |
| info float | Print the status of the floating point unit. | 打印浮点单元的状态 |
| info frame | All about the selected stack frame. | 有关选定堆栈帧的所有信息 |
| info frame-filter | List all registered Python frame-filters. | 列出所有注册的Python帧过滤器 |
| info functions | All function names or those matching REGEXPs. | 所有函数名称或匹配的函数名称 |
| info guile | Prefix command for Guile info displays. | Guile信息显示的前缀命令 |
| info handle | What debugger does when program gets various signals. | 程序收到各种信号时调试器的操作 |
| info line | Core addresses of the code for a source line. | 源代码行的核心地址 |
| info macro |Show the definition of MACRO.| 显示MACRO的定义 |
| info macros | Show the definitions of all macros at LINESPEC. | 显示LINESPEC处所有宏的定义 |
| info mem | Memory region attributes. | 内存区域属性 |
| info module | Print information about modules. | 打印模块信息 |
| info modules | All module names, or those matching REGEXP. | 所有模块名称或匹配的模块名称 |
| info os | Show OS data ARG. | 显示OS数据ARG |
| info pretty-printer | GDB command to list all registered pretty-printers. | GDB命令列出所有注册的pretty-printers |
| info probes | Show available static probes. | 显示可用的静态探针 |
| info proc | Show additional information about a process. | 显示有关进程的其他信息 |
| info record | Info record options. | 信息记录选项 |
| info registers | List of integer registers and their contents. | 查看整数寄存器及其内容的列表 |
| info scope | List the variables local to a scope. | 列出作用域内的局部变量 |
| info selectors | All Objective-C selectors, or those matching REGEXP. | 所有Objective-C选择器或匹配的选择器 |
| info set | Show all GDB settings. | 显示所有GDB设置 |
| info sharedlibrary | Status of loaded shared object libraries. | 已加载的共享对象库的状态 |
| info signals | What debugger does when program gets various signals. | 程序收到各种信号时调试器的操作 |
| info skip | Display the status of skips. | 显示跳过的状态 |
| info sources | All source files in the program or those matching REGEXP. | 程序中的所有源文件或匹配的源文件 |
| info stack | Backtrace of the stack, or innermost COUNT frames. | 堆栈的回溯或最内部的COUNT帧 |
| info static-tracepoint-markers | List target static tracepoints markers. | 列出目标静态跟踪点标记 |
| info symbol | Describe what symbol is at location ADDR. | 描述位于ADDR位置的符号 |
| info tasks | Provide information about all known Ada tasks. | 提供有关所有已知Ada任务的信息 |
| info terminal | Print inferior's saved terminal status. | 打印下级保存的终端状态 |
| info tracepoints | Status of specified tracepoints. | 查看指定跟踪点的状态 |
| info tvariables | Status of trace state variables and their values. | 跟踪状态变量及其值的状态 |
| info type-printers | GDB command to list all registered type-printers. | GDB命令列出所有注册的类型打印机 |
| info types | All type names, or those matching REGEXP. | 所有类型名称或匹配的类型名称 |
| info unwinder | GDB command to list unwinders. | GDB命令列出unwinders |
| info variables | All global and static variable names or those matching REGEXPs. | 所有全局和静态变量名称或匹配的变量名称 |
| info vector | Print the status of the vector unit. | 打印向量单元的状态 |
| info vtbl | Show the virtual function table for a C++ object. | 显示C++对象的虚函数表 |
| info warranty | Various kinds of warranty you do not have. | 您没有的各种保修 |
| info watchpoints | Status of specified watchpoints. | 查看指定监视点的状态 |
| info win | List of all displayed windows. | 列出所有显示的窗口 |
| info xmethod |GDB command to list registered xmethod matchers.| GDB命令列出注册的xmethod匹配器 |















