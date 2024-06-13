
# Build NumPy from source

## Reference Links

### For development

[Building from source for NumPy development - NumPy](https://numpy.org/devdocs/building/index.html#building-from-source-for-numpy-development)

[Setting up and using your development environment](https://numpy.org/devdocs/dev/development_environment.html#setting-up-and-using-your-development-environment)

### Steps succeeded to create `compile_commands.json` on 2024-06-13

- 确保较高版本的`gcc/g++` 在 `PATH` 中，同时，确保对应的 `gcc/g++` 的lib在 `LD_LIBRARY_PATH` 中（不然gcc/g++无法正确找到动态链接库），2024年6月13日是 gcc 13即可
- 可以使用Python自带的虚拟环境 `venv` ，或者安装 `virtualenv` ，都可以，它只是在 numpy 源代码目录中切换到Python虚拟环境之后，使用对应的 `pip` 按照必须的package而已。
- 确保使用较高版本的 Python（2024年6月13日是Python 11.2即可）在 `PATH` 中，同时它的动态库也添加到 `LD_LIBRARY_PATH` 中
- 下载 numpy 源代码
   ```shell
   git clone https://github.com/numpy/numpy.git
   cd numpy
   git submodule update --init
   ```

- 然后（使用Python自带的虚拟环境 `venv` ）创建Python虚拟环境
   ```shell
   python -m venv myNumpyDevVEnv
   ```
   这会在当前的numpy源码目录下面，创建一个名字叫做 `myNumpyDevVEnv` 的目录。

- 然后切换进入（激活）虚拟环境

   ```shell
   source myNumpyDevVEnv/bin/activate
   ```

   此时，查看 `which pip` 和 `which python`，得到的路径应该是位于 `myNumpyDevVEnv/bin/activate` 下面的 `python` 和 `pip` 。

- 然后安装必须的Python package
   ```shell
   python -m pip install -r requirements/all_requirements.txt
   ```

- 之后如果只是想编译源码，然后安装到当前的Python虚拟环境中时，直接使用如下命令安装即可
   ```shell
   pip install .
   ```

   注意，在安装之前，可能需要设置环境变量 `CC`： `export CC=gcc`，因为前面把合适版本的 `gcc` 添加到了 `PATH` 中，那么此时 `gcc` 就是对应那个最新的 `gcc` 版本，这个命令会把 `CC` 变量也设定为这个版本的 `gcc` ，原因是 `meson` 编译时需要查看变量 `CC` ，否则版本太低会报错。

- 生成 `compile_commands.json`

   注意，本例使用如下命令调用 `meson` 即可
   ```shell
   meson setup.py build
   ```

   但 numpy 有定制版本的 `meson` （实际上是个脚本），必须使用这个脚本才能操作，所以，用到 `meson` 这个命令的地方，需要全部换成 `python vendored-meson/meson/meson.py`，（参考说明[Understanding Meson - Building from source - NumPy](https://numpy.org/devdocs/building/understanding_meson.html#understanding-meson)）所以上面的命令就要对应修改为：

   ```shell
   python vendored-meson/meson/meson.py setup.py build
   ```

   然后，就会在当前目录下面，生成一个叫做 `build` 的目录，它里面就有对应的 `compile_commands.json` 。

   然后只要在当前目录使用 `gvim` 打开源代码文件，在配置好 `clangd` 的情况下，`clangd` 默认就会去名字为 `build` 的目录下查找 `compile_commands.json` ，再做indexing。


### Just for usage

[Building from source to use NumPy - NumPy](https://numpy.org/devdocs/building/index.html#building-numpy-from-source)




# Numpy Basics

This is a file which shows basic usages of Numpy

## Checks if 2 floating number arrarys are equal

```python
nump.allclose(array_a, array_b)
```

## NumPy sort array of arrays

Use `np.lexsort` , `.T`  and `np.flipud` method.

```python
>>> import numpy as np
>>> a = np.array([[10, 0, 2, 9], [3, 19, 23, 7], [0, 84, 31, 100], [2, 101, 25, 56]])
>>> a
array([[ 10,   0,   2,   9],
       [  3,  19,  23,   7],
       [  0,  84,  31, 100],
       [  2, 101,  25,  56]])
>>> a.T
array([[ 10,   3,   0,   2],
       [  0,  19,  84, 101],
       [  2,  23,  31,  25],
       [  9,   7, 100,  56]])
>>> np.flipud(a.T)
array([[  9,   7, 100,  56],
       [  2,  23,  31,  25],
       [  0,  19,  84, 101],
       [ 10,   3,   0,   2]])
>>> np.lexsort(np.flipud(a.T))
array([2, 3, 1, 0], dtype=int64)
>>> a[np.lexsort(np.flipud(a.T))]
array([[  0,  84,  31, 100],
       [  2, 101,  25,  56],
       [  3,  19,  23,   7],
       [ 10,   0,   2,   9]])
```

