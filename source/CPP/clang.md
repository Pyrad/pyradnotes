## How to use clang-tidy

- Make sure you have `compile_commands.json`
  
  - In CMake, use `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON`

- Use command below to check warnings or errors
  
  - `clang-tidy main.cpp -checks=* -p build`
  
  - `main.cpp` is the source file to check
  
  - `-p` option tells `clang-tidy` where to find the `compile_commands.json`




