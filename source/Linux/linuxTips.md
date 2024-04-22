
# Tips for Linux daily use

<!-- more -->

## helpmanual.io man pages and help text for unix commands

Linux命令查询网址：[https://helpmanual.io/](https://helpmanual.io/)


## 如果想提取同时包含两个关键词的行，可以用awk命令

```shell
awk '/KEY_WORD_1/&&/KEY_WORD_2/' <filename> 
```
比如，如果想在文件cdesigner.log中提取行，这些行同时含有关键词"/o"和"FAILED"，那么就可用命令：
```shell
awk '/\/o/&&/FAILED/' cdesigner.log
```
结果会在terminal中打印出来。
如果这两个关键词需要被精确匹配（比如只找work，而不是worker或者homework之类的），那么就用
```shell
awk '/\<KEY_WORD_1\>/&&/\<KEY_WORD_2\>/' <filename>
```



## Vim中搜索多个keyword

Go to search mode i.e. type '/' and then type \v followed by the words you want to search separated by ' | ' (pipe).
Example:

```vim
/\vword1|word2|word3
```
Go to search mode and type the words you want to search separated by '\| '.
Example:
```vim
/word1\|word2\|word3
```



## 要取消文件名扩展用

```shell
set noglob
```
要取消文件名扩展无匹配出错用
```shell
set nonomatch
```
要屏蔽出错信息用
```shell
(cmd >/dev/tty) >&/dev/null
```
要屏蔽信息用
```shell
cmd >&/dev/null
```



## 以递归的方式列出文件

```shell
find /path/to/search/ -print
find /path/to/search/ -ls
```
比如
```shell
find . -print
```
或者
```shell
find . -ls
```



## 结束后台进程

a. 列出后台进程：

```shell
jobs
```
b. 结束命令：
```shell
kill -9 %N（N是jobs列出的进程序号）
```



## Bash shell中变量自增的办法

```shell
# 1st
i=`expr $i + 1`;
# 2nd
let i+=1;
# 3rd
((i++));
# 4th
i=$[$i+1];
# 5th
i=$(( $i + 1 ))
```



## 取出指定文本的第10到15行：

```shell
sed -n '10,15p' FILENAME
```
取出指定的行(10~15, 23, 49, 169~221)
```shell
sed -n '10,15p;23,23p;49,49;169,221p' FILENAME
```



## sed 原地替换

```shell
sed -i 's/annotateCurrents/annotateDesign/g' test.txt
```



## 同时找出多种后缀结尾的文件并grep

```shell
find . -regex '.*\.tcl\|.*\.log' | xargs grep -rn "rtUseKeepoutWidth" > ~/find_result_useKeep.rpt
```



## 在vim中对第10至20行的文本按第5个字段以数值升序进行排序

```shell
:10,20!sort -n -k5
```



## linux中find的结果提供给数组使用

```shell
array=($(find . -name "*.txt"))
for i in "${array[@]}"; do echo $i; done
```



## 删除一个符号链接的方法：

```shell
rm -rf symbolic_name
```
注意不是`rm -rf symbolic_name/`

也就是说，如果要删除一个符号链接，如果是符号链接文件，直接删除即可，如果是符号链接文件夹，那么在后面就不可以带斜杠"/"



## 如果ps的时候中出现\<defunct\>，就是僵尸进程，需要kill掉其父进程来kill这个子进程，单独kill这个子进程是没有用的。命令是：

```shell
ps -e -o ppid,stat | grep Z | cut -d” ” -f2 | xargs kill -9
```



## alt+退格，删除最后一个单词



## shell脚本参数

`$0` ： ./test.sh,即命令本身，相当于c/c++中的argv[0]
`$1` ： -f,第一个参数.
`$2` ： `config.conf`
`$3, $4 ...` ：类推。
`$#` : 参数的个数，不包括命令本身，上例中`$#`为4.
`$@` ：参数本身的列表，也不包括命令本身，如上例为 `-f config.conf -v --prefix=/home`
`$*` ：和`$@`相同，但`$*` 和 `"$@"`(加引号)并不同，"`$*`"将所有的参数解释成一个字符串，而`"$@"`是一个参数数组。



## 判断字符串为空

```shell
if [ "$str" =  "" ] 
if [ x"$str" = x ]
if [ -z "$str" ] （-n 为非空）
```



## shell中if的正则匹配可以用如下变量来捕获

```shell
#!/bin/bash
ip="121.0"
if [[ $ip =~ ^([0-9]+)\.([0-9]+)$ ]];then
echo "match"
echo ${BASH_REMATCH[1]}
echo ${BASH_REMATCH[2]}
else
echo "Not match"
fi
```



## Csh中打印某个env

```shell
printenv LANG
```



## 几种快速清空文件内容的方法：

```shell
$ : > filename #其中的 : 是一个占位符, 不产生任何输出.
$ > filename
$ echo “” > filename
$ echo /dev/null > filename
$ echo > filename
$ cat /dev/null > filename
```


## 使用tar命令压缩和解压

### `tar` 命令常用选项的含义

- `tar`，含义是**T**ape **AR**chive。

命令格式：

```shell
tar [OPERATION_AND_OPTIONS] [ARCHIVE_NAME] [FILE_NAME(s)]
```

**Operations**：
- `-c`，`--create`，表示创建新的 `tar` 归档包文件
- `-x`，`--extract`，表示从归档包文件中抽取归档文件
- `-t`，`-list`，表示列出归档包文件中包含的文件

**Options**
- `-v`，`--verbose`，表示显示正在处理的文件（列表）
- `-f`，后面要跟上归档文件包的名称

Archive_Name：表示归档包文件名称

File_Names：表示要从归档包中抽取出的文件。如果省略，表示抽取包中所有文件。



### 解压 `tar.gz` 格式的压缩包

```shell
tar -zxf FILE_NAME.tar.gz
```

### 解压 `xz` 格式的压缩包

```shell
tar -Jxf FILE_NAME.tar.xz
```

这里 `-J` 表示使用 `xz` 命令来解压

### 解压 `bz2` 格式的压缩包

```shell
tar -jxf FILE_NAME.tar.gz
```

这里 `-j` 表示使用 `bzip2` 命令来解压



### 分步解压 `XZ` 格式的压缩包文件

```shell
xz -kd <FILE_NAME>
```
这里，k表示--keep，意思是解压之后不删除源文件包，d表示--decompress，意为解压
之后再用tar命令解压
```shell
tar xf <FILE_NAME>
```

### 分步解压 `.tar.bz2` 格式的压缩包文件

- 首先解压成一个 `.tar`格式的打包文件

  ```shell
  bzip2 -dk xxx.tar.bz2
  ```

  注意这里的`-d`表示decompress，而`-k`表示保留原先的`.bz2`文件。
  如果不添加`-k`选项，原先的`.bz2`文件，在解压之后会被自动删除。

  这个命令会生成一个对应的打包文件：`xxx.tar`

- 然后再使用`tar`命令提取打包文件即可。

  ```shell
  tar -xf xxx.tar
  ```


### tar 打包

```shell
tar -czf <TARGET>.tar.gz <FILES_TO_BE_COMPRESSED>
```



## 查看Linux版本

```shell
cat /proc/version
uname -a
uname -r
lsb_release -a
cat /etc/issue
cat /etc/redhat-release
```
查看是64位还是32位
```shell
getconf LONG_BIT or getconf WORD_BIT
file /bin/ls
```



## linux 下最大化窗口用Alt + F10，恢复原窗口大小，再次Alt + F10



## grep 显示匹配行之前或之后或者之前以及之后的选项：

显示匹配行，以及之后3行（共4行）。A-After

```shell
grep -A 3 "PATTERN" file.txt
```
显示匹配行，以及之前3行（共4行）。B-Before
```shell
grep -B 3 "PATTERN" file.txt
```
显示匹配行，以及之前3行和之后三行（共7行）
```shell
grep -C 3 "PATTERN" file.txt
```
`grep -l` 表示只显示文中有match pattern的文件名列表

递归搜索目录，并排除文件夹
```shell
grep -R --exclude-dir=node_modules "sa_family_t" <path_to_search>
```

只计算匹配的行数，用-c这个选项。
```shell
grep -c "<KEYWORD>" <path_to_file>
```

只计算不匹配的行数，用-vc这个选项。
```shell
grep -vc "<KEYWORD>" <path_to_file>
```

如果要grep一定行数范围内的（比如从5672行到13677行），可以用awk
```shell
awk '/string_to_search/ && NR >= 5672 && NR <= 13677' stack_execute.cpp
```

同时grep多个keyword
```shell
grep 'word1\|word2\|word3' /path/to/file
```



## cshell中的tee命令

在Cshell中把stderr和stdout的输出信息重定向到一个文件里，用>&，比如

```shell
xxx >& run.log
```
(This will force both standard output and standard error to go to the same place as the current standard output, effectively what you have with the bash redirection, 2>&1.)

如果要同时把stderr和stdout打印到屏幕上，并记到log里面，用 |&，比如
```shell
xxx |& tee run.log
```



## 目录中最旧和最新的文件：

```shell
find -type f -printf '%T+ %p\n' | sort | head -n 1
find -type f -printf '%T+ %p\n' | sort | tail -n 1
```



## find查找多个关键字文件：在-name之间用"-o"

```shell
find . -name "*.txt" -o -name "*.pdf"
```



## CGDB

设置source window中指向当前马上要执的代码行的箭头格式为长箭头格式

```shell
:set arrowstyle=long
```
设置source window中当前马上要执的代码行为block格式
```shell
:set selectedlinedisplay=block
```



## Check linux kernel version

```shell
uname -r
```



## Check CentOS version

```shell
lsb_release -d
```



## 查看当前目录下（深度为1）各个文件以及目录占用磁盘大小

```shell
du -h --max-depth=1 .
```



## Check fonts in Linux

字体列表

```bash
fc-list
```

中文字体

```bash
fc-list :lang=zh
```

查看字体详情

```bash
fc-match -v "FontName"
```



## User's RSS total memory on this Linux

```sh
ps --no-headers -eo user,rss | grep longc | \
	awk '{arr[$1]+=$2}; END {for (i in arr) {print i,arr[i]}}' | sort -nk2
```


## Linux rename multiple files

Use command `rename`

For example, if there a few files below,

```shell
myDbgFile_a.txt
myDbgFile_b.txt
myDbgFile_c.txt
```

If I'd like to change the name from "my" to "myTest" in each file name, I can use the following

```shell
rename my myTest *.txt
```

Here the 1st option `my` is the pattern I'd like to replace, and the 2nd option `myTest` is the string after replacement.

The 3rd option specifies the files waiting for replacement.

So after replacement, file names are,

```shell
myTestDbgFile_a.txt
myTestDbgFile_b.txt
myTestDbgFile_c.txt
```

## 重定向标准错误到/dev/null

重定向执行一个命令的标准错误（stderr）到`/dev/null`，并且把改命令的标准输出（stdout）返回到一个变量。

```shell
function test_redirect_to_dev_null() {
    errmsg=`which vim`
    echo "$? | $errmsg"

    errmsg=$(which vim)
    echo "$? | $errmsg"

    errmsg=`which vim 2>/dev/null`
    echo "$? | $errmsg"

    errmsg=$(which vim 2>/dev/null)
    echo "$? | $errmsg"

    errmsg=`which vimk 2>/dev/null`
    echo "$? | $errmsg"

    errmsg=$(which vimk 2>/dev/null)
    echo "$? | $errmsg"
}
```

这个函数的执行结果如下

```shell
0 | /usr/bin/vim
0 | /usr/bin/vim
0 | /usr/bin/vim
0 | /usr/bin/vim
1 |
1 |
```


## How to find zombie process?

https://askubuntu.com/questions/111422/how-to-find-zombie-process

```bash
$ ps aux | grep 'Z'
```

What you get is Zombies and anything else with a Z in it, so you will also get the grep:

```bash
USER       PID     %CPU %MEM  VSZ    RSS TTY      STAT START   TIME COMMAND
usera      13572   0.0  0.0   7628   992 pts/2    S+   19:40   0:00 grep --color=auto Z
usera      93572   0.0  0.0   0      0   ??       Z    19:40   0:00 something
```

Find the zombie's parent:

```bash
$ pstree -p -s 93572
```

Will give you:

```bash
init(1)---cnid_metad(1311)---cnid_dbd(5145)
```


## Ubuntu 安装tofrodos（类似dos2unix)

ubuntu下面没有dos2unix，需要安装`tofrodos`来使用`todos`和`fromdos`这两个命令

```shell
# install tofrodos
apt-get install tofrodos

# Use todos (change a file from unix style to window style)
todos <FILE>

# Use fromdos (change a file from window style to unix style)
fromdos <FILE>
```

## Exit code for GNU/Linux

[Exit & Error Codes in bash and Linux OS](https://www.adminschoice.com/exit-error-codes-in-bash-and-linux-os)

Linux OS Error Numbers, Error Codes and Meaning

Unix and Linux OS  shows  error code and error name at time time of failures  which may not be clear

The table below provides a quick reference to error numbers, error name and their meaning to help in troubleshooting.

| Error No.	| Error Name |Error description|
|:---------:|:----------:|:-----------------:|
| 1 | EPERM | Operation not permitted |
| 2 | ENOENT | No such file or directory |
| 3 | ESRCH | No such process |
| 4 | EINTR |Interrupted system call|
| 5 | EIO | I/O error |
| 6 | ENXIO | No such device or address |
| 7 | E2BIG | Arg list too long |
| 8 | ENOEXEC | Exec format error |
| 9 | EBADF | Bad file number |
| 10 | ECHILD | No child processes |
| 11 | EAGAIN | Try again |
| 12 | ENOMEM | Out of memory |
| 13 | EACCES | Permission denied |
| 14 | EFAULT | Bad address |
| 15 | ENOTBLK | Block device required |
| 16 | EBUSY | Device or resource busy |
| 17 | EEXIST | File exists |
| 18 | EXDEV | Cross-device link |
| 19 | ENODEV | No such device |
| 20 | ENOTDIR | Not a directory |
| 21 | EISDIR | Is a directory |
| 22 | EINVAL | Invalid argument |
| 23 | ENFILE | File table overflow |
| 24 | EMFILE | Too many open files |
| 25 | ENOTTY | Not a typewriter |
| 26 | ETXTBSY | Text file busy |
| 27 | EFBIG | File too large |
| 28 | ENOSPC | No space left on device |
| 29 | ESPIPE | Illegal seek |
| 30 | EROFS | Read-only file system |
| 31 | EMLINK | Too many links |
| 32 | EPIPE | Broken pipe |
| 33 | EDOM | Math argument out of domain of func |
| 34 | ERANGE | Math result not representable |
| 35 | EDEADLK | Resource deadlock would occur |
| 36 | ENAMETOOLONG | File name too long |
| 37 | ENOLCK | No record locks available |
| 38 | ENOSYS | Function not implemented |
| 39 | ENOTEMPTY | Directory not empty |
| 40 | ELOOP | Too many symbolic links encountered |
| 41 | EWOULDBLOCK | Operation would block |
| 42 | ENOMSG | No message of desired type |
| 43 | EIDRM | Identifier removed |
| 44 | ECHRNG | Channel number out of range |
| 45 | EL2NSYNC | Level 2 not synchronized |
| 46 | EL3HLT | Level 3 halted |
| 47 | EL3RST | Level 3 reset |
| 48 | ELNRNG | Link number out of range |
| 49 | EUNATCH | Protocol driver not attached |
| 50 | ENOCSI | No CSI structure available |
| 51 | EL2HLT | Level 2 halted |
| 52 | EBADE | Invalid exchange |
| 53 | EBADR | Invalid request descriptor |
| 54 | EXFULL | Exchange full |
| 55 | ENOANO | No anode |
| 56 | EBADRQC | Invalid request code |
| 57 | EBADSLT | Invalid slot |
| 58 | EDEADLOCK | File locking deadlock error |
| 59 | EBFONT | Bad font file format |
| 60 | ENOSTR | Device not a stream |
| 61 | ENODATA | No data available |
| 62 | ETIME | Timer expired |
| 63 | ENOSR | Out of streams resources |
| 64 | ENONET | Machine is not on the network |
| 65 | ENOPKG | Package not installed |
| 66 | EREMOTE | Object is remote |
| 67 | ENOLINK | Link has been severed |
| 68 | EADV | Advertise error |
| 69 | ESRMNT | Srmount error |
| 70 | ECOMM | Communication error on send |
| 71 | EPROTO | Protocol error |
| 72 | EMULTIHOP | Multihop attempted |
| 73 | EDOTDOT | RFS specific error |
| 74 | EBADMSG | Not a data message |
| 75 | EOVERFLOW | Value too large for defined data type |
| 76 | ENOTUNIQ | Name not unique on network |
| 77 | EBADFD | File descriptor in bad state |
| 78 | EREMCHG | Remote address changed |
| 79 | ELIBACC | Can not access a needed shared library |
| 80 | ELIBBAD | Accessing a corrupted shared library |
| 81 | ELIBSCN | .lib section in a.out corrupted |
| 82 | ELIBMAX | Attempting to link in too many shared libraries |
| 83 | ELIBEXEC | Cannot exec a shared library directly |
| 84 | EILSEQ | Illegal byte sequence |
| 85 | ERESTART | Interrupted system call should be restarted |
| 86 | ESTRPIPE | Streams pipe error |
| 87 | EUSERS | Too many users |
| 88 | ENOTSOCK | Socket operation on non-socket |
| 89 | EDESTADDRREQ | Destination address required |
| 90 | EMSGSIZE | Message too long |
| 91 | EPROTOTYPE | Protocol wrong type for socket |
| 92 | ENOPROTOOPT | Protocol not available |
| 93 | EPROTONOSUPPORT | Protocol not supported |
| 94 | ESOCKTNOSUPPORT | Socket type not supported |
| 95 | EOPNOTSUPP | Operation not supported on transport endpoint |
| 96 | EPFNOSUPPORT | Protocol family not supported |
| 97 | EAFNOSUPPORT | Address family not supported by protocol |
| 98 | EADDRINUSE | Address already in use |
| 99 | EADDRNOTAVAIL | Cannot assign requested address |
| 100 | ENETDOWN | Network is down |
| 101 | ENETUNREACH | Network is unreachable |
| 102 | ENETRESET | Network dropped connection because of reset |
| 103 | ECONNABORTED | Software caused connection abort |
| 104 | ECONNRESET | Connection reset by peer |
| 105 | ENOBUFS | No buffer space available |
| 106 | EISCONN | Transport endpoint is already connected |
| 107 | ENOTCONN | Transport endpoint is not connected |
| 108 | ESHUTDOWN | Cannot send after transport endpoint shutdown |
| 109 | ETOOMANYREFS | Too many references: cannot splice |
| 110 | ETIMEDOUT | Connection timed out |
| 111 | ECONNREFUSED | Connection refused |
| 112 | EHOSTDOWN | Host is down |
| 113 | EHOSTUNREACH | No route to host |
| 114 | EALREADY | Operation already in progress |
| 115 | EINPROGRESS | Operation now in progress |
| 116 | ESTALE | Stale NFS file handle |
| 117 | EUCLEAN | Structure needs cleaning |
| 118 | ENOTNAM | Not a XENIX named type file |
| 119 | ENAVAIL | No XENIX semaphores available |
| 120 | EISNAM | Is a named type file |
| 121 | EREMOTEIO | Remote I/O error |




## Patch file explained

[What is the format of a patch file? - Stack Overflow](https://stackoverflow.com/questions/987372/what-is-the-format-of-a-patch-file)

An example

```bash
diff -rBNu src.orig/java/org/apache/nutch/analysis/NutchAnalysisConstants.java src/java/org/apache/nutch/analysis/NutchAnalysisConstants.java
--- src.orig/java/org/apache/nutch/analysis/NutchAnalysisConstants.java 2009-03-10 11:34:01.000000000 -0700
+++ src/java/org/apache/nutch/analysis/NutchAnalysisConstants.java  2009-03-10 14:11:55.000000000 -0700
@@ -4,9 +4,12 @@

+  int CJK = 21;
+  int DIGIT = 22;

   int DEFAULT = 0;

   String[] tokenImage = {
     "<EOF>",
+    "\"OR\"",
     "<WORD>",
     "<ACRONYM>",
     "<SIGRAM>",
@@ -39,6 +42,8 @@
     "\"\\\"\"",
     "\":\"",
     "\"/\"",
+    "\"(\"",
+    "\")\"",
     "\".\"",
     "\"@\"",
     "\"\\\'\"",
```

- 例子文件是使用如下 `diff` 命令生成。

  ```shell
  diff -rBNu src.orig/java/org/apache/nutch/analysis/NutchAnalysisConstants.java src/java/org/apache/nutch/analysis/NutchAnalysisConstants.java
  ```

  一般来说，只用 `-u` 选项即可。
  
  这个选项的含义是：`-u` means to use the unified output format, which is only supported by GNU diff and GNU patch.
  
  ```shell
  diff -u a.java b.java
  ```

- 文件内容中
  
  - `---` 表示原始文件（命令行中做比较的第一个文件）
  
  - `+++` 表示新文件（命令行中做比较的第二个文件）

- `@@` 是 block headers，后面紧跟的就是两个文件的差异内容。

  - Block headers的格式为 `@@ -R,r +R,r @@`
  
  - `-R,r`表示原始文件中，和新文件对比有差异的行号范围。
  
  - `+R,r`表示新文件中，和原始文件对比有差异的行号范围。
  
  - 当**删除**了一行时，`+r` 中的 `r` 值，比 `-r` 中的 `r` 值**小**。
  
  - 当**增加**了一行时，`+r` 中的 `r` 值，比 `-r` 中的 `r` 值**大**。
  
  - 当**修改**了一行时，会给 `+r` 中的 `r` 值加 `0`，即值**不变**。

- `@@` block headers 后面跟随的是两个文件之间的差异

  - 以 `-` 起始的行，表示的是被删除的行。
  
  - 以 `+` 起始的行，表示的是新增加的行。
  
  - 没有 `-` 或 `+` 起始的行，表示的是不变的行。


## Shell read file line by line

```shell
fname="myfile.txt"
while IFS= read -r line; do
  echo "$line"
done < $fname
```

## maxdirsize

[What is maxdirsize](https://kb.netapp.com/onprem/ontap/os/What_is_maxdirsize)

Maxdirsize determines the number of files a directory can hold.

The default value of `maxdirsize` is 320M, which is 320\*1024\*1024=335544320.







```shell
Originally created in Pyrad Blog
title: LinuxTips
date: 2022-04-20 22:52:08
categories:
- linux related
tags: linux
```