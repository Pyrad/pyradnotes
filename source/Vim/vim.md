# Frequently Visited Vim Notes

1. 只打印出来匹配的个数：

   ```powershell
   :%s/XXX//gn
   ```

   这样的话会在vim的状态栏中打印出来类似“6 matches on 6 lines”的提示信息

   

2. windows下的`Ctrl+V`列操作

   在windows下，把vim74目录里的`mswin.vim`中关于`Ctrl+V`的map那行命令给去掉

   

3. 在一个文件中同时查找（高亮）两个关键词

   ```powershell
   /\(KEY_WORD_1\)\|\(KEY_WORD_2\)
   ```

   删除不包含关键字的行

   ```powershell
   :g!/KEYWORD/d
   ```

   

4. 删除某个范围内包含关键字的行

   ```powershell
   :23,96g/KEYWORD/d
   ```

   

5. 在Vim中去掉重复的行的命令是

   ```powershell
   :%!sort -u
   ```

   

6. 在vim里面逆序指定的行

   ```powershell
   :1,200!tac
   ```

   

7. 反转指定范围的行

   ```powershell
   :<lineStart>, <lineEnd>g/^/m<ResultStartFromLineNum>
   ```

   

8. 在vim中引用函数，比如用lineNumber做替换

   ```powershell
   :%s/x/\=printf("%d", line('.'))
   ```

   比如如下命令

   ```powershell
   :48,91s/\(\S\+\)/\=printf("printf(\"the value of %16s is %%d\\n\", %s)", submatch(1), submatch(1))
   ```

   它会把如下的字符串

   `NPY_INT`

   替换成

   `printf("the value of     NPY_INT is %d\n", NPY_INT)`

   

   再比如，把某个关键字替换成连续递增的整数：

   ```powershell
   :%s/x/\=printf("%d", line('.') - 10)
   ```

   其中10就是要替换的第一个关键字所在的行的行号

 

9. 使用range来生成连续整数（[网页链接](https://vim.fandom.com/wiki/Making_a_list_of_numbers)），Eg.

   ```powershell
   :for i in range(1,10) | put ='192.168.0.'.i | endfor
   ```

   

10. 执行最近的一条命令

    比如，上一条命令是vim script，那么可以使用`!vim`来执行上次执行的那条命令。



11. 在vim的搜索替换命令中，如果要将一个字符替换为换行符，那么要用下面的命令

    ```powershell
    :%s/TO_REPLACE/^M/g
    ```

    其中，`^M`是同时按下`Ctrl+V+M`三个键所输入的，注意，是同时。



12. 要打开vim中的函数列表，用命令

    ```powershell
    :TlistToggle
    ```

    在函数列表和正常的编辑区域之间切换，用`Ctrl+ww`，即按下`ctrl`，再敲击`w`两次。

    

13. 在vim中直接插入当前日期和时间
    - 在当前编辑界面进入插入模式（insert mode）
    - `Ctrl + R`，然后输入`=strftime("%Y-%m-%d %H:%M:%S")`
    - 回车。然后回插入类似以下的时间：`2017-01-05 18:15:05`



14. vim折叠设置（转载）

    ```powershell
    set foldmethod=indent "set default foldmethod
    ```

    **`"zi`** 打开关闭折叠

    **`zm`**   关闭折叠

    **`zr`**   打开

    **`zc`**   折叠当前行

    **`zd`**   删除折叠

    **`"zv`** 查看此行

    **`zM`** 关闭所有

    **`zR`** 打开所有

    **`zo`** 打开当前折叠

    **`zD`** 删除所有折叠 

    






15. 捕获

    注意，vi中pattern里的括号不需要转义，用于捕获的锚位括号需要加上转义斜线`\`

    但是方括号在pattern里时需要加转义斜线的`\`

    在替换部分，前面捕获的分别用`\1`，`\2`来引用

    ```powershell
    s/rif_header_key_column.find(\(.\*\))/rif_header_key_column.find[\1]/gc
    ```



16. 得到当前VIM的PID（进程号）

    直接在vim的command模式下` :echo getpid()`

 

17. 高亮（查找）重复的行

    solution source [page](https://stackoverflow.com/questions/1268032/how-can-i-mark-highlight-duplicate-lines-in-vi-editor)

    None of the answers above worked for me so this is what I do:

    - Sort the file using `:sort`

    - Execute command `:g/^\(.*\)$\n\1$/p`

 

18. Disable 光标闪设置

    ```powershell
    " Disable all blinking:
    :set guicursor+=a:blinkon0
    
    " Remove previous setting:
    :set guicursor-=a:blinkon0
    
    " Restore default setting:
    :set guicursor&
    ```

    

 



 
