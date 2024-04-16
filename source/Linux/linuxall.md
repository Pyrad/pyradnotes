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






