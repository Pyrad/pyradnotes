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

