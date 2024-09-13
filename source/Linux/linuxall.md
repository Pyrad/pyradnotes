# The Linux All

This is to keep all possible stuffs related Linux, if possible

## Issue `Cannot find the D-Bus session server`:

```shell
$ konsole
QDBusConnection: session D-Bus connection created before QCoreApplication. Application may misbehave.
unnamed app(4284): KUniqueApplication: Cannot find the D-Bus session server:  "Failed to connect to socket /tmp/dbus-aGE9cG1V4s: Connection refused" 

unnamed app(4283): KUniqueApplication: Pipe closed unexpectedly.
```

How-to-fix [cannot launch konsole from xterm](https://unix.stackexchange.com/questions/258143/cannot-launch-konsole-from-xterm)
```shell
export -n DBUS_SESSION_BUS_ADDRESS
```



## Issue `Qt: Session managment error: Could not open network socket`:
How-to-fix [Qt: Session Management Error](https://stackoverflow.com/questions/986964/qt-session-management-error)

```shell
rm -rf ~/.kde
export -n SESSION_MANAGER
```

Before `rm -rf ~/.kde`, make sure make backup for the kde config: `~/.kde/share/apps/konsole/konsoleui.rc`, there are some customized shortcuts in this file, backup it up first before deleting.



## Linux find files by dates

`find` files by dates

```shell
# Find regular files and show them, between 2 dates
find . -type f -newermt '01 jan 2009 00:00:00' -not -newermt '01 jan 2012 00:00:00' -ls
# Find symbolic files and show them,  between 2 dates
find . -type l -newermt '01 jan 2009 00:00:00' -not -newermt '01 jan 2012 00:00:00' -ls
# Find symbolic files and delete them,  between 2 dates
find . -type l -newermt '01 jan 2009 00:00:00' -not -newermt '01 jan 2012 00:00:00' -delete
```



## `ls` doesn't show colors in Cygwin terminals

Add the following, remember to set alias to `ls` (adding an option `--color=auto` is important)

```bash
### Check Current OS version
VERSTR_ALL=""
OS_INFO=""
if [[ -f /proc/version ]]; then
	# Noramlly `cat /proc/verison` returns a character string
	# E.g., 
	# MINGW64_NT-6.1-7601 version 3.1.7- ... (GCC) ) 2021-03-26 22:17 UTC
	# CYGWIN_NT-6.1-7601 version 3.2.0 ... (GCC) ) 2021-03-29 08:42 UTC
	VERSTR_ALL=`cat /proc/version`
	if [[ ${VERSTR_ALL:0:9} -eq "CYGWIN_NT" ]]; then
		### Check first 9 characters
		# echo "Current is Cygwin: $VERSTR_ALL"
		OS_INFO=${VERSTR_ALL:0:9}
	elif [[ ${VERSTR_ALL:0:10} -eq "MINGW64_NT" ]]; then
		### Check first 10 characters
		OS_INFO=${VERSTR_ALL:0:10}
	else
		OS_INFO="UNKWON"
	fi
fi

##############################################################################
### In Cygwin terminal, set the command ls for its colors, otherwise something 
### goes with its color display
##################################################################################
if [[ $OS_INFO -eq "CYGWIN_NT" ]]; then
	eval "`dircolors -b /etc/DIR_COLORS`"
	alias ls='ls --color=auto'
fi
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



## What is tty?

tty = **t**ele**ty**pewriter，中文翻译一般叫**电传打字机**。


## Bash multiple conditions and `[[` and `((` in if-condition

[Bash Multiple Conditions](https://stackoverflow.com/a/20263097)

If using `[[ ]]` for if-condition, then `-eq`, `-ne` and etc should be used, `==`, `!=` and etc are not valid in `[[]]`.

If trying to use `<`, `>`, ... arithematic operators, using `(())` for if-condition


## How to check libc version?

[How to check libc version?- StackOverflow](https://stackoverflow.com/questions/62732447/how-to-check-libc-version)

[Check glibc version for a particular gcc compiler- StackOverflow](https://stackoverflow.com/questions/9705660/check-glibc-version-for-a-particular-gcc-compiler)

[Check the actual glibc version used](https://unix.stackexchange.com/questions/537003/check-the-actual-glibc-version-used)

[What do the multiple GLIBC versions mean in the output of ldd?](https://unix.stackexchange.com/questions/458659/what-do-the-multiple-glibc-versions-mean-in-the-output-of-ldd)

### Method 1

[How to check libc version?- StackOverflow](https://stackoverflow.com/questions/62732447/how-to-check-libc-version)

Use `gcc` output

```shell
GCC_FEATURES=$(gcc -dM -E - <<< "#include <features.h>")

if grep -q __UCLIBC__ <<< "${GCC_FEATURES}"; then
    echo "uClibc"
    grep "#define __UCLIBC_MAJOR__" <<< "${GCC_FEATURES}"
    grep "#define __UCLIBC_MINOR__" <<< "${GCC_FEATURES}"
    grep "#define __UCLIBC_SUBLEVEL__" <<< "${GCC_FEATURES}"
elif grep -q __GLIBC__ <<< "${GCC_FEATURES}"; then
    echo "glibc"
    grep "#define __GLIBC__" <<< "${GCC_FEATURES}"
    grep "#define __GLIBC_MINOR__" <<< "${GCC_FEATURES}"
else
    echo "something else"
fi
```

The output should be one of 3 above.

### Method 2

[Check glibc version for a particular gcc compiler- StackOverflow](https://stackoverflow.com/questions/9705660/check-glibc-version-for-a-particular-gcc-compiler)

Check `/lib/libc.so` or `/lib64/libc.so`

First check what `libc.so` is used by `gcc`.

```shell
$ gcc -print-file-name=libc.so
/lib/../lib64/libc.so
```

Indeed, this file is a plain text,

```shell
$ file $(gcc -print-file-name=libc.so)
/lib/../lib64/libc.so: ASCII text

$ cat $(gcc -print-file-name=libc.so)
/* GNU ld script
   Use the shared library, but some functions are only in
   the static library, so try that secondarily.  */
OUTPUT_FORMAT(elf64-x86-64)
GROUP ( /lib64/libc.so.6 /usr/lib64/libc_nonshared.a  AS_NEEDED ( /lib64/ld-linux-x86-64.so.2 ) )
```

> On ELF platforms `/lib/x86_64-linux-gnu/libc.so.6` is a position-independent executable with a dynamic symbol table (like that of a shared library):

```shell
$ file /lib/x86_64-linux-gnu/libc.so.6
/lib/x86_64-linux-gnu/libc.so.6: symbolic link to libc-2.31.so

$ file $(readlink -f /lib/x86_64-linux-gnu/libc.so.6)
/usr/lib/x86_64-linux-gnu/libc-2.31.so: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1878e6b475720c7c51969e69ab2d276fae6d1dee, for GNU/Linux 3.2.0, stripped

$ /lib/x86_64-linux-gnu/libc.so.6
GNU C Library (Ubuntu GLIBC 2.31-0ubuntu9.9) stable release version 2.31.
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
Compiled by GNU CC version 9.4.0.
libc ABIs: UNIQUE IFUNC ABSOLUTE
For bug reporting instructions, please see:
<https://bugs.launchpad.net/ubuntu/+source/glibc/+bugs>.
```


### Method 3

[Check the actual glibc version used](https://unix.stackexchange.com/questions/537003/check-the-actual-glibc-version-used)

Use `strings`

```shell
strings /lib64/libc.so.6 | grep ^GLIBC_
```



## Ubuntu 18.04 编译安装新版本glibc

[Vscode更新不当人啦 - 天国滑行的文章 - 知乎](https://zhuanlan.zhihu.com/p/681393388)


## 编译silver searcher（ag）的时候遇到的multiple definition的问题

在编译安装silver searher的时候，可能会出现如下的多重定义的错误，

 ```shell
 /bin/ld: src/log.o:/<path-to-silver-searcher>/src/log.h:12:multiple definition of 'print_mtx';
 ```

这是一个bug，在[GitHub链接](https://github.com/ggreer/the_silver_searcher/issues/1378)上有讨论到。

同样在上面这个链接里面，有人提到，目前的workaround是，

```shell
make CFLAGS="-fcommon -D_GNU_SOURCE -lpthread"
```

经过尝试，发现可行。