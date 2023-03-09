## How to use clang-tidy

- Configure clang-tidy
  
  - One way is to use `.clang-tidy` (YAML/JSON format) in project directory
    
    - An example of `.clang-tidy` file
      
      ```yaml
      Checks: '-*,bugprone-*'
      CheckOptions:
          - key: bugprone-argument-comment.StricMode
          - value: 1
          - key: bugprone-exception-escape.FunctionsThatShouldNotThrow
          - value: WinMain,SDL_main
      ```
  
  - Another way is to use `-checks=*` to run all checks or `-checks=modernize-*` to run checks on only modern features.

- Make sure you have `compile_commands.json`
  
  - In CMake, use `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON`

- Use command below to check warnings or errors
  
  - `clang-tidy main.cpp -checks=* -p build`
  
  - `main.cpp` is the source file to check
  
  - `-p` option tells `clang-tidy` where to find the `compile_commands.json`




