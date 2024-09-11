# Linux System



About Linux System Itself



## exec system call



按照 Advanced UNIX Programming 书中第5章的内容，exec其实是一族函数，总共6个，分别如下，

```cpp
execl
execv
execlp
execvp
execle
execve
```



它们名字的格式都是 `execAB`，其中

- `A` 是 `l` 或 `v`，分别表示参数要么就在调用中（list），要么在一个数组中（vector）。
- `B` 有三种情况，`p`，`e`，或者直接没有。`p` 表示要从环境变量中搜索程序，`e` 表示要使用特定的环境。



执行了`exec` 函数之后，新的程序会替换原有的程序，全局变量会被新的程序继承，因此这些全局变量仍然可以继续在新的程序中继续使用。



[Linux下Fork与Exec使用 - 知乎](https://zhuanlan.zhihu.com/p/659902392)

