# Install Boost library (on windows)



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



## Reference

[MinGW编译boost库](https://blog.csdn.net/SUKHOI27SMK/article/details/122931498)