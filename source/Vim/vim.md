# Frequently Visited Vim Notes

## 只打印出来匹配的个数：

```powershell
:%s/XXX//gn
```

这样的话会在vim的状态栏中打印出来类似“6 matches on 6 lines”的提示信息

## windows下的`Ctrl+V`列操作

在windows下，把vim74目录里的`mswin.vim`中关于`Ctrl+V`的map那行命令给去掉

## 在一个文件中同时查找（高亮）两个关键词

```powershell
/\(KEY_WORD_1\)\|\(KEY_WORD_2\)
```

删除不包含关键字的行

```powershell
:g!/KEYWORD/d
```

## 删除某个范围内包含关键字的行

```powershell
:23,96g/KEYWORD/d
```

## 在Vim中去掉重复的行的命令是

```powershell
:%!sort -u
```

## 在vim里面逆序指定的行

```powershell
:1,200!tac
```

## 反转指定范围的行

```powershell
:<lineStart>, <lineEnd>g/^/m<ResultStartFromLineNum>
```

## 在vim中引用函数，比如用lineNumber做替换

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

## Replace certain words with consecutive numbers

```vim
:%s/x/\=printf("%d", line('.') - 10)
```

## 使用range来生成连续整数（[网页链接](https://vim.fandom.com/wiki/Making_a_list_of_numbers)），Eg.

```powershell
:for i in range(1,10) | put ='192.168.0.'.i | endfor
```

## 执行最近的一条命令

比如，上一条命令是vim script，那么可以使用`!vim`来执行上次执行的那条命令。

## 搜索

对之前打开过的文件进行搜索

```vim
:History
```

对之前搜索过的历史进行搜索

```vim
:History/
```

对之前执行过的命令进行搜索

```vim
:History:
```

## 在vim的搜索替换命令中，如果要将一个字符替换为换行符，那么要用下面的命令

```powershell
:%s/TO_REPLACE/^M/g
```

其中，`^M`是同时按下`Ctrl+V+M`三个键所输入的，注意，是同时。

## Vim frequently used commands

[link](http://blog.chinaunix.net/uid-20769502-id-112737.html)

[link2](https://www.zhihu.com/question/27478597/answer/36837839)

## 要打开vim中的函数列表，用命令

```powershell
:TlistToggle
```

在函数列表和正常的编辑区域之间切换，用`Ctrl+ww`，即按下`ctrl`，再敲击`w`两次。

## 在vim中直接插入当前日期和时间

- 在当前编辑界面进入插入模式（insert mode）
- `Ctrl + R`，然后输入`=strftime("%Y-%m-%d %H:%M:%S")`
- 回车。然后回插入类似以下的时间：`2017-01-05 18:15:05`

## vim折叠设置（转载）

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

## 捕获

注意，vi中pattern里的括号不需要转义，用于捕获的锚位括号需要加上转义斜线`\`

但是方括号在pattern里时需要加转义斜线的`\`

在替换部分，前面捕获的分别用`\1`，`\2`来引用

```powershell
s/rif_header_key_column.find(\(.\*\))/rif_header_key_column.find[\1]/gc
```

## 得到当前VIM的PID（进程号）

直接在vim的command模式下` :echo getpid()`

## 高亮（查找）重复的行

solution source [page](https://stackoverflow.com/questions/1268032/how-can-i-mark-highlight-duplicate-lines-in-vi-editor)

None of the answers above worked for me so this is what I do:

- Sort the file using `:sort`

- Execute command `:g/^\(.*\)$\n\1$/p`

## Disable 光标闪设置

```vim
" Disable all blinking:
:set guicursor+=a:blinkon0

" Remove previous setting:
:set guicursor-=a:blinkon0

" Restore default setting:
:set guicursor&
```

## Vim diff

启动命令

```bash
vimdiff <FILE_LEFT> <FILE_RIGHT>
```

或者

```bash
vim -d <FILE_LEFT> <FILE_RIGHT>
```

启动之后，两侧的文件滚动是同步的

`]c` 跳转到**下一个**差异点命令

`[c` 跳转到**上一个**差异点命令

文件合并命令

（注意，当前光标所在的文件是当前文件）

`dp` 把一个差异点中当前文件的内容复制到另一个文件里（是diff put的缩写）

`do` 把一个差异点中另一个文件的内容复制到当前文件里（是diff get的缩写，因为dg这个命令已经被占用，所以用了do）

打开/折叠

`zo` 打开折叠的文本行，意思是folding open（用字母z是因为它像被折叠的样子）

`zc` 重新折叠文本行，意思是folding close

## Vim colors

How to tell vim how many colors your terminal could be capable of?
`t_Co=256` tells Vim that your terminal is capable of using 256 colors (whether that is correct or not). termguicolors is a relative recent addition in Vim 8 and tells Vim that your terminal is capable of handling rgb colors (e.g. 16 Million colors, whether that is correct or not)

## Vim script

In non-interactive mode:

```bash
vim -s <cmds.file.vim> -es <file.to.modify>
```

If you are inside vim, just `:source <vim_script_file>`

## How to insert special code (unicode) in Vim

***3 steps to insert***

- `i` go to insert mode
- `Ctrl + v` go into ins-special-keys mode
- `u2713` insert the Unicode character CHECK MARK (U+2713). Here first char `u` tells it the following 4 chars are unicode

***Some powerline special glyphs***

`e0a0` stream

`e0a1` Line number

`e0a2` Lock

`e0a3` (Not sure)

`e0b0`, `e0b1`, `e0b2`, `e0b3`, `e0b4`, `e0b5`, `e0b6`, `e0b7`, `e0b8`, `e0b9`, `e0ba`

`e0bb`, `e0bc`, `e0be`, `e0bf`, `e0c0`, `e0c1`, `e0c2`, `e0c3`, `e0c4`, `e0c5`, `e0c6`

`e0c7`, `e0c8`, `e0ca`, `e0cc`, `e0cd`, `e0ce`, `e0ce`, `e0cf`, `e0d0`, `e0d1`, `e0d2`, `e0d4`

```vim
# original
'patched': {
        'lock': u'\uE0A2',
        'network': u'\uE0A2',
        'separator': u'\uE0B0',
        'separator_thin': u'\uE0B1'
},
# angly 1
'patched': {
        'lock': u'\uE0A2',
        'network': u'\uE0A2',
        'separator': u'\uE0B8',
        'separator_thin': u'\uE0B9'
},
# angly 2
'patched': {
    'lock': u'\uE0A2',
    'network': u'\uE0A2',
    'separator': u'\uE0BC',
    'separator_thin': u'\uE0BD'
},
# curvy
'patched': {
    'lock': u'\uE0A2',
    'network': u'\uE0A2',
    'separator': u'\uE0B4',
    'separator_thin': u'\uE0B5'
},
# flames (flamey)
'patched': {
    'lock': u'\uE0A2',
    'network': u'\uE0A2',
    'separator': u'\uE0C0',
    'separator_thin': u'\uE0C1'
},
# lego (blocky)
'patched': {
    'lock': u'\uE0A2',
    'network': u'\uE0A2',
    'separator': u'\uE0CE',
    'separator_thin': u'\uE0CF'
},
# pixelated blocks 2 (large) random fade (pixey)
'patched': {
    'lock': u'\uE0A2',
    'network': u'\uE0A2',
    'separator': u'\uE0C6',
    'separator_thin': u'\uE0C6'
}
```

## Vim to check if a plugin is loaded

https://vi.stackexchange.com/questions/10939/how-to-see-if-a-plugin-is-active

```vim
" Method 1
g:loaded_<plugin_name>

" Method 2
if exists("loaded_<plugin_name>")
" ...
endif
```

## VIM设置python3支持和检测python version

注意vim的版本（64or32）必须和python3的版本一致

python3的版本必须和vim中+python3/dyn所指明的python3版本一致，否则`echo has("python3")`只会返回`0`

https://www.jianshu.com/p/18f06d12348c

https://blog.zengrong.net/post/pyton_support_on_vim/

## Check shortcuts/key-mapping of Vim

```vim
:help index
```



## Check on which OS it is running

The best way is to use [`has()`](http://vimhelp.appspot.com/eval.txt.html#has()), with this function you can check for features of Vim; OS specific features from [`:help feature-list`](http://vimhelp.appspot.com/eval.txt.html#feature-list):

```vim
if has('unix')
	echo "On Unix!"
endif
```

[Detect OS in Vimscript](https://vi.stackexchange.com/questions/2572/detect-os-in-vimscript)


## Copy/Yank a single character

拷贝单个字符的操作：`yl`





## What's Vim paste mode?

[https://techexplorations.com/blog/kicad/blog-how-to-copy-text-into-vim/](https://techexplorations.com/blog/kicad/blog-how-to-copy-text-into-vim/)

If you are copying text for which the formatting should not change, beware that the above process can introduce changes to the formatting. For example, if you are copying Python code into a file using Vim, be prepared for the indentation to be altered, and therefore your program to not work as expected. In Python, code blocks like loops are denoted using text indentation.

To avoid this from happening, you can use Vim’s paste mode. When you enable paste mode, Vim will not auto-indent any text that you paste. To enable paste mode, follow this process:

In Vim, ensure you are command mode by hitting the Esc key.
- Type `:set paste` to enter command mode.
- Type `i` to enter paste mode. Notice the `– INSERT (paste) –` at the bottom of the Vim window.
- Paste your Python code into Vim. Indentation should be as in the original
- To exit paste mode, type `:set nopaste`. Notice the `– INSERT –` at the bottom of the Vim window. This means you are back to normal insert mode.


## Vim remove color codes from terminal

[Removing ANSI Color Codes from a text file in VI](https://superuser.com/questions/1445805/removing-ansi-color-codes-from-a-text-file-in-vi)


## Vim Reload current file

Just use `:e`

## Vim get current file name and path

Symbol `%` is a register in Vim, which stores the current file name

In normal mode, use `"%p` to paste the current file name to current cursor's position (or use `"%P` to paste before the cursor)

[Get the name of the current file](https://vim.fandom.com/wiki/Get_the_name_of_the_current_file#:~:text=In%20insert%20mode%2C%20type%20Ctrl,to%20create%20a%20similar%20name.)


## Vim Repeat finding next character in this line

Use `f` + `<char>` to move the the 1st occurrence of this line, then press `;` (semicolon) to jump to the 2nd occurrence, again for the next until none.

## Use vimgrep and quickfix window

```vim
:vimgrep /keyword_pattern/g % | cw
```

Here `keyword_pattern` is the word to search, and `%` is current file name, `cw` is used to open the quickfix windows

## Vim Official Home Page

官网：[https://www.vim.org/download.php](https://www.vim.org/download.php)


## Pass clangd args to YouCompleteMe

```vim
let g:ycm_clangd_args = ['--query-driver=' .. '/depot/gcc-7.3.0/bin/g++']
```

## Vim滚动屏幕（鼠标居中）

[Vim documentation: scroll (sourceforge.net)](https://vimdoc.sourceforge.net/htmldoc/scroll.html#zz)

`zz`：把鼠标所在的行调整到屏幕中间（居中）

但没有built-in的居中列的操作，所以需要使用`zL`和`zH`这两个滚动命令来近似实现。

`zL`：把屏幕向**左**移动半个屏幕宽度
`zH`：把屏幕向**右**移动半个屏幕宽度
