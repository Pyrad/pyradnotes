# CMake Notes



## `target_include_directories` 和 `include_directories` 的区别

[cmake：target_** 中的 PUBLIC，PRIVATE，INTERFACE](https://zhuanlan.zhihu.com/p/82244559)


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