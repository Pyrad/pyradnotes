# Vim Installation



## Install gVim on Windows platform

1. Download the source code from official website ([link](https://www.vim.org/download.php))

   Here is the ftp address for vim 9.0 version ([link: vim-9.0.tar.bz2](ftp://ftp.vim.org/pub/vim/unix/vim-9.0.tar.bz2))

2. Decompress the tar ball file, go to `vim90\src` folder

3. Read file `INSTALLpc.txt` file

4. Make sure current Windows OS is 64-bit, make sure the python installed is for 64-bit.

5. In MSYS2 terminal, use 64-bit version of make to build

   ```bash
   $ pwd
   /e/temp/vim90src/vim90/src
   $ make -f Make_ming.mak PYTHON3=D:/procs/python38 DYNAMIC_PYTHON3=yes PYTHON3_VER=38
   ```

   output message

   ```bash
   ... ...
   D:/procs/msys64/mingw64/bin/make.exe -C GvimExt -f Make_ming.mak CROSS=no CROSS_COMPILE= CXX='g++' STATIC_STDCPLUS=no
   make[1]: Entering directory 'E:/temp/vim90src/vim90/src/GvimExt'
   g++ -O2 -DFEAT_GETTEXT -DWINVER=0x0501 -D_WIN32_WINNT=0x0501 -c gvimext.cpp -o gvimext.o
   windres  --input-format=rc --output-format=coff -DMING gvimext_ming.rc -o gvimext.res
   g++ -shared -O2 -s -o gvimext.dll \
           -Wl,--enable-auto-image-base \
           -Wl,--enable-auto-import \
           -Wl,--whole-archive \
                   gvimext.o gvimext.res gvimext_ming.def \
           -Wl,--no-whole-archive \
                   -luuid -lgdi32
   make[1]: Leaving directory 'E:/temp/vim90src/vim90/src/GvimExt'
   ```

   

6. After build complete, `gvim.exe` will be created in current `src` folder

7. Remember to set environment variables,

   ```bash
   PYTHONHOME=D:\procs\python38
   PYTHONPATH=D:\procs\python38
   PYTHON38=D:\procs\python38
   ```

   and append the the following to `PATH` variable,

   ```bash
   %PYTHONHOME%
   %PYTHON38%\Scripts\
   %PYTHON38%\
   ```

8. 或者可以不用把新版本的python加到`PATH`环境变量中去，但是要在`$VIM\_vimr`中添加对应的变量设置，否则同样地`:echo has("python3")`永远返回`0`

   ```vim
   " ------------------------------------------------------
   " Python3 support
   " ------------------------------------------------------
   function s:setup_python3_dyn()
       let &pythonthreedll='D:/procs/python38/python38.dll'
       let &pythonthreehome='D:/procs/python38
   endfunction " End of function setup_python3_dyn
   
   """ ------------------------------------------------------
   """ Setup for the coc-nvim
   """ ------------------------------------------------------
   function s:setup_python3()
       let g:python3_host_prog='D:/procs/python38/python.exe'
   endfunction
   

8. After setting environment variables, check if the python3 is support in Vim

   ```vim
   :echo has("python3")
   ```

   Now it should return `1`, which means python3 is supported.

10. Re-visit file `INSTALLpc.txt` file to check how to add support for Lua, Ruby, Tcl and others.

11. In order to use `plug.vim`, download it and put it in folder `D:\procs\Vim9Compiled\vim90\runtime\autoload`, otherwise it can't be found.

9. 