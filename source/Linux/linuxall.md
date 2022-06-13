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