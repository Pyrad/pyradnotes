# Install Boost library on windows



## Steps

1. Make sure `gcc` is the latest, otherwise some unexpected errors might occur.

   On Windows platform, you can install `msys2`, and after update it has all the latest `mingw64` tool chain for building use, which is convenient.

2. Download tar ball from [official website](https://www.boost.org/).

3. Decompress and run `bootstrap.bat`, it generates `b2.exe`

   For linux, run `bootstrap.sh` instead of `bootstrap.bat`

   ```bash
   .\bootstrap.bat
   ```

   

4. Run `b2.exe` with the following options

   ```bash
   .\b2.exe install \
   	    --build-type=complete \
   	    threading=multi \
   	    link=shared \
   	    address-model=64 \
   	    toolset=gcc \
   	    --prefix="D:\procs\boost_1_79_0"
   ```

   Note that `gcc` must have been set already before this, and `prefix` is where to copy the headers and libs to.

   For the day I ran this, `gcc` I used is from `msys2`and its version is `12.0`, the boost library is `1.79.0`.

5. After build with out errors, it should say the following

   ```bash
   ...updated 18043 targets...
   ```

6. If to compile only a few libraries, for example, `python`, `filesystem` and `regex`, these can be specified, and if doing so, other libraries won't be compiled

   ```bash
   .\b2.exe install \
      	--build-type=complete \
      	threading=multi \
      	link=shared \
      	address-model=64 \
      	toolset=gcc \
      	--with-python \
      	--with-filesystem \
      	--with-regex \
      	--prefix="D:\procs\boost_1_79_0"
   ```

7. If you have already compiled once by using `b2.exe install ...` for only a few libraries, as above, and now you want to compile more libraries, **but** without copying header files, remember to use `b2.exe stage ...` instead of `b2.exe install`, thus copying header files will be skipped, as this process takes quite a long time to finish copying.

   For example, I'd like to compile one more library `serialization` after  `python`, `filesystem` and `regex` are compiled, using the following.

   ```bash
   .\b2.exe stage \
        --build-type=complete \
        threading=multi \
        link=shared \
        address-model=64 \
        toolset=gcc \
        --with-serialization \
        --prefix="D:\procs\boost_1_79_0"
   ```








# Install Boost library on Linux



## Steps

1. Make sure `gcc` is installed

2. Download corresponding tar ball from  [official website](https://www.boost.org/).

   We need to pay attention, the `gcc` version should be somewhat applicable to this boost library version.  Otherwise some strange errors come up with compiling.

3. After decompress the tar ball, generate `b2` by using `bootstrap.sh`

   ```bash
   ./bootstrap.sh  --with-libraries=all --with-toolset=gcc
   ```

   

4. Create a directory for building (not to contaminate current source tree structure)

   ```bash
   # Give it a name you want
   # For example, here abs path is: /home/pyrad/swap/boost_1_69_0/PyradBuild
   mkdir PyradBuild
   ```

   

5. Use `b2` to compile, specify a build directory in current folder for generating build files (cache, scripts, ...)

   ```bash
   ./b2 toolset=gcc --build-dir=/home/pyrad/swap/boost_1_69_0/PyradBuild
   ```

   After it finishes, the following message will appear,

   ```bash
   The Boost C++ Libraries were successfully built!
   
   The following directory should be added to compiler include paths:
   
       /home/pyrad/procs/boost_1_72_0
   
   The following directory should be added to linker library paths:
   
       /home/pyrad/procs/boost_1_72_0/stage/lib
   ```

   ***Note***

   如果在上面的命令中指定了选项： `--build-type=complete`, 但没有指定`--layout=<versioned|tagged|system>`，那么编译的时候会报错，原因是在linux中，如果指定了`--build-type=complete`，那么就要加上`--layout=versioned`。但这样做会导致生成的`lib`目录中的库文件（`.so`，`.a`）会带有编译器版本，boost library版本等信息的字符串，如下

   ```bash
   ...
   libboost_math_c99-gcc9-mt-d-x64-1_69.so
   libboost_random-gcc9-mt-d-x64-1_69.so
   libboost_atomic-gcc9-mt-d-x64-1_69.so
   ...
   ```

   这样就会导致`cmake`的时候抱怨使用`find_package`不能找到boost library，实际上`cmake`是试图寻找以下这样的名字

   ```bash
   ...
   libboost_math_c99.so
   libboost_random.so
   libboost_atomic.so
   ...
   ```

   在linux中，`--layout`这个选项的默认值是`system`，即产生的库文件名称不带有编译器版本boost库版本等信息（如上）。

   

6. Install the libraries and header files to a path you specify

   ```bash
   ./b2 install --prefix=<SOME_USER_PATH>
   ```

   因为没有指定`--layout=versioned`，所以生成的目录结构如下

   ```bash
   boost_1_69_0/
   	|---include/
   	|     |---boost/
   	|          |---<all *.hpp headers>
   	|          |---<all_header_filer_folders>
   	|			  
   	|---lib/
   	     |---<all *.so files>
   	     |---<all *.a files>
   ```

   
7. 在Linux中，可能由于没有指明Python root目录，导致编译boost时没有能够编译出对应的`libboost_python38.so`这样的动态库，这样如果要编译的是Python的C extension，那么在编译时可能出现如下的错误：

   ```bash
   ...
   fatal error: pyconfig.h No such file or directory
   ```

   为了解决上面的问题，需要再次执行`./bootstrap.sh `，然后指明Python root的目录，如下：
   
   ```bash
   ./bootstrap.sh \
	   --with-python=/home/pyrad/procs/Python-3.8.3/bin/python3.8 \
	   --with-python-root=/home/pyrad/procs/Python-3.8.3 \
	   --prefix=/home/pyrad/procs/boost_1_73_0
   ```

   然后，重新**仅**编译`libboost_python38.so`这样的动态库（版本号根据具体情况不同）：

   ```bash
   ./b2 stage link=shared address-model=64 toolset=gcc --with-python
   ```

   上面命令执行完毕，会在当前编译目录下的`stage/lib`目录中，生成如下几个动态库：

   ```bash
   stage/lib/libboost_python38.so -> libboost_python38.so.1.73.0
   stage/lib/libboost_python38.so.1 -> libboost_python38.so.1.73.0
   stage/lib/libboost_python38.so.1.73 -> libboost_python38.so.1.73.0
   stage/lib/libboost_python38.so.1.73.0
   ```

   之后将这些`.so`动态库文件拷贝入`BOOST_ROOT/lib`中即可，这里的`BOOST_ROOT`是boost的安装目录。

# Reference

[MinGW编译boost库](https://blog.csdn.net/SUKHOI27SMK/article/details/122931498)
