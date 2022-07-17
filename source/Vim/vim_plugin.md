# Plugins of VIM



## coc.nvim

### 在VIM中查看coc.nvim的help文档

```vim
:h coc-nvim
```



### 设定存放extension,config等数据的目录

设定config home和data home（extension目录）

config home 变量：`coc_config_home`

data home 变量：`coc_data_home`

```vim
""Configure the directory which will be used to look for
""user's coc-settings.json, default:
"" Windows: ~/AppData/Local/nvim
"" Other: ~/.config/nvim`
let g:coc_config_home = 'D:/procs/VimVersion9/vimfiles/coc_nvim_files/config_home'

""Configure the directory which will be used to for data
""files(extensions, mru and so on), default:
""Windows: ~/AppData/Local/coc
""Other: ~/.config/coc`
let g:coc_data_home = 'D:/procs/VimVersion9/vimfiles/coc_nvim_files/data_home'
```



### 打开config文件

```vim
:CocConfig
```

该命令会打开一个名为`$coc_config_home/coc-settings.json`的目录，其中`$coc_config_home`见上面的设定，如果没有修改，默认在windows下是`~/AppData/Local/coc`。



### 自动补全

- 动补全默认是**自动开启**

- 末尾带有`~`符号的是snippet format的补全，需要用`Ctrl + N`（或`Ctrl + P`）选定，然后使用`Ctrl + Y`来展开（expand）

  - 当snippet expand被激活时，可以使用`Ctrl + J`和`Ctrl + K`来跳转到下一个或上一个占位符处（placeholder）。比如，如果选定并展开了`for`这个snippet，那么当前就会插入如下的一段代码

    ```cpp
    for (init-statement; condition; inc-expression) {
        statements
    }
    ```

    并且当前`init-statement`会被选择并处于插入模式（insert mode），写完初始条件之后，就可以使用`Ctrl + J`跳转到下一处（`condition`）并继续书写。如果需要跳转到上一处，使用`Ctrl + K`。

  - 变量`g:coc_snippet_prev`和`g:coc_snippet_next`可以用来调整跳转快捷键

  - 参考帮助文档中的`coc-snippets`小节查看更多

  - 







## vim-mark

GitHub [link](https://github.com/inkarkat/vim-mark)

Vim-script [link](https://www.vim.org/scripts/script.php?script_id=1238)



安装（注意，需要同时安装`vim-ingo-library`才能使用）

```vim
Plug 'inkarkat/vim-ingo-library'
Plug 'inkarkat/vim-mark'
```

vim中打开帮助文档

```vim
:h mark.txt
```





## tagbar

安装（注意，需要同时安装`ctags`才能使用）

注意，'majutsushi/tagbar'似乎不再维护了

```vim
# Plug 'majutsushi/tagbar'
Plug 'preservim/tagbar'
```

根据[preservim/**tagbar**](https://github.com/preservim/tagbar)说明，使用[universal-ctags/**ctags**](https://github.com/universal-ctags)，下载页面是[universal-ctags/**ctags-win32**](https://github.com/universal-ctags)，[release page](https://github.com/universal-ctags/ctags-win32/releases)，下载完成后直接解压到一个目录即可，然后再`vimrc`中设置`ctags`路径

```vim
""" ------------------------------------------------------
""" tagbar
""" ------------------------------------------------------
function s:setup_tagbar()
    nmap <F2> :TagbarToggle<CR>
    ""let g:tagbar_ctags_bin = '~/proc/ctags5.8/bin/ctags'
    ""let g:tagbar_ctags_bin = '/usr/bin/ctags'
    let g:tagbar_ctags_bin = 'D:/procs/ctags59/ctags.exe'
    let g:tagbar_width = 30
    let g:tagbar_left = 1
    " Set sort order to 0, it will list the tags in the
    " order where they appear in the source file, other
    " than alphabetic order
    let g:tagbar_sort = 0
    ""map <F3> :Tagbar<CR>
endfunction " End of function s:setup_tagbar
```





