# CMake Notes



## `target_include_directories` 和 `include_directories` 的区别

[cmake：target_** 中的 PUBLIC，PRIVATE，INTERFACE](https://zhuanlan.zhihu.com/p/82244559)

## 查询系统相关信息

[cmake_host_system_information](https://cmake.org/cmake/help/latest/command/cmake_host_system_information.html)




## 只拷贝文件到binary目录

[Copy file from source directory to binary directory using CMake](https://stackoverflow.com/questions/34799916/copy-file-from-source-directory-to-binary-directory-using-cmake)

- Method 1: Using `configure_file(<input> <output> COPYONLY)`
- Method 2: Uising `file(COPY ...)` and `add_custom_command`
```cmake
add_custom_command(
TARGET foo POST_BUILD
COMMAND ${CMAKE_COMMAND} -E copy
        ${CMAKE_SOURCE_DIR}/test/input.txt
        ${CMAKE_CURRENT_BINARY_DIR}/input.txt
)
```


## 编译库是添加-fPIC选项的方式及验证

网页地址：[编译库是添加-fPIC选项的方式及验证](https://blog.csdn.net/m0_37876242/article/details/121786076)


## 改变编译出来的`.so`或`.dll` library的前缀或后缀

网页地址：[How do you rename a library filename in CMake?](https://stackoverflow.com/questions/31038963/how-do-you-rename-a-library-filename-in-cmake)

By default, the library filename will be `libnew_thing.so`
```cmake
add_library(new_thing ${NEW_THING_SRCS})
```

This changes the filename to `new_thing.so`

```cmake
set_target_properties(new_thing PROPERTIES PREFIX "")
```


## MSYS2 CMake path prefix is in Windows format (C:/) but needs MSYS2/\*nix style (/c/) to link

[MSYS2 CMake path prefix is in Windows format (C:/) but needs MSYS2/*nix style (/c/) to link](https://stackoverflow.com/questions/54767375/msys2-cmake-path-prefix-is-in-windows-format-c-but-needs-msys2-nix-style)

```cmake
    cmake_minimum_required(VERSION 3.12)

    project(sample CXX)

    # Find GTK+ headers/libs with PkgConfig
    find_package(PkgConfig REQUIRED)
    pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

    # Generated paths starting with "C:" need to be converted to /c/ to work with MSYS2
    # TODO remove this or do it some way better at some point in the future
    if(MSYS OR MINGW)
        string(REGEX REPLACE "C:" "/c/" GTK3_INCLUDE_DIRS "${GTK3_INCLUDE_DIRS}")
    endif(MSYS OR MINGW)

    include_directories(${GTK3_INCLUDE_DIRS})
    link_directories(${GTK3_LIBRARY_DIRS})

    add_definitions(${GTK3_CFLAGS_OTHER})

    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/natives)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib/natives)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

    add_executable(sample src/main.cpp)

    target_link_libraries(sample ${GTK3_LIBRARIES})
```


## Turn on `-DBoost_DEBUG=ON` for cmake to print out more information about errors

[cmake v3.15.3 cannot find boost v1.71.0](https://stackoverflow.com/questions/57870032/cmake-v3-15-3-cannot-find-boost-v1-71-0)

## CMake Workshop

[Detecting your environment](https://enccs.github.io/cmake-workshop/environment/)



## CMake 正确链接动态库

[CMake如何做到正确链接动态库so？ - Lion Long的回答 - 知乎](https://www.zhihu.com/question/489682173/answer/2873091122)




## 使用 CMake 和 setuptools，把二者结合起来，编译 C extension 的参考文章：

[使用CMake扩展setuptools](https://cloud.tencent.com/developer/information/%E4%BD%BF%E7%94%A8CMake%E6%89%A9%E5%B1%95setuptools%E3%80%82%E6%9C%AA%E5%AE%89%E8%A3%85%E7%94%9F%E6%88%90%E6%89%A9%E5%B1%95)


## Some links to build Python extension modules

[Recommendations for Python module inclusion](https://discourse.cmake.org/t/recommendations-for-python-module-inlusion/2612)

[Creating a python package (deb/rpm) from cmake](https://stackoverflow.com/questions/70017740/creating-a-python-package-deb-rpm-from-cmake)

[Building Python submodules from C++ extensions via cmake](https://stackoverflow.com/questions/61956365/building-python-submodules-from-c-extensions-via-cmake)

[A simple example of using cmake to build a Windows DLL](https://stackoverflow.com/questions/24872225/a-simple-example-of-using-cmake-to-build-a-windows-dll)

[GenerateExportHeader](https://cmake.org/cmake/help/v3.0/module/GenerateExportHeader.html)


## Hacking CPP

[Cheat Sheets & Infographics - https://hackingcpp.com](https://hackingcpp.com/cpp/cheat_sheets.html)




