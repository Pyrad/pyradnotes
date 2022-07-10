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