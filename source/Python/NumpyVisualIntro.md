# NumPy Notes

This is the note for article [A Visual Intro to NumPy and Data Representation](https://jalammar.github.io/visual-numpy/), by [Jay Alammar](https://jalammar.github.io/about/)

Chinese version can be found at [**Numpy和数据展示的可视化介绍**](http://www.junphy.com/wordpress/index.php/2019/10/24/visual-numpy/)



Also, it takes some notes for another article [NumPy Illustrated: The Visual Guide to NumPy](https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d), and the a Chinese version of it can be found at [**图解 | NumPy可视化指南**](https://www.yanxishe.com/TextTranslation/3198), another version is at [**一图胜千言，超形象图解NumPy教程！**](https://zhuanlan.zhihu.com/p/504917890)



[Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

[Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)



# NumPy Illustrated: The Visual Guide to NumPy





## 1. Vectors, the 1D Arrays

### 初始化**Numpy array**用到的函数

|        函数        |                             参数                             |
| :----------------: | :----------------------------------------------------------: |
| `np.array(pylist)` |            使用Python list来初始化一个Numpy array            |
|    `np.zeros()`    |               `shape, dtype=float, order='C'`                |
|    `np.ones()`     |                `shape, dtype=None, order='C'`                |
|    `np.empty()`    |               `shape, dtype=float, order='C'`                |
|    `np.full()`     |          `shape, fill_value, dtype=None, order='C'`          |
| `np.zeros_like()`  |      `a, dtype=None, order='K', subok=True, shape=None`      |
|  `np.ones_like()`  |      `a, dtype=None, order='K', subok=True, shape=None`      |
| `np.empty_like()`  |  `prototype, dtype=None, order='K', subok=True, shape=None`  |
|  `np.full_like()`  | `a, fill_value, dtype=None, order='K', subok=True, shape=None` |



### 使用单调序列初始化Numpy array

|      函数       |                             参数                             |
| :-------------: | :----------------------------------------------------------: |
|  `np.arange()`  |             `[start,] stop[, step,], dtype=None`             |
| `np.linspace()` | `start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0` |



### 创建随机数组

- 旧式创建方法（deprecated）

| 函数                | 参数                                   |
| ------------------- | -------------------------------------- |
| `np.random.randint` | `low, high=None, size=None, dtype=int` |
| `np.random.rand`    | `d0, d1, ..., dn`                      |
| `np.random.uniform` | `low=0.0, high=1.0, size=None`         |

- 新式创建方法

**首先创建对象**：`rng = np.random.default_rng()`

| 函数           | 参数                                                        |
| -------------- | ----------------------------------------------------------- |
| `rng.integers` | `low, high=None, size=None, dtype=np.int64, endpoint=False` |
| `rng.random`   | `size=None, dtype=np.float64, out=None`                     |
| `rng.uniform`  | `low=0.0, high=1.0, size=None`                              |





## 2. Vector indexing

### 基本索引操作

可以指定单个索引，索引范围，反向索引，以及数组索引

定义数组

```python
>>> a = np.arange(1, 6)
>>> a
array([1, 2, 3, 4, 5])
```

操作及效果

|   索引操作   |        结果        |            效果            |
| :----------: | :----------------: | :------------------------: |
|    `a[1]`    |        `2`         |          返回view          |
|   `a[2:4]`   |  `array([3, 4])`   |          返回view          |
|   `a[-2:]`   |  `array([4, 5])`   |          返回view          |
|   `a[::2]`   | `array([1, 3, 5])` |          返回view          |
| `a[[1,3,4]]` | `array([2, 4, 5])` | fancy indexing，返回新数组 |

Python list vs Numpy list

|        Python List        |        Numpy List         |
| :-----------------------: | :-----------------------: |
|      `a = [1, 2, 3]`      | `a = np.array([1, 2, 3])` |
|   `b = a` **(no copy)**   |    b = a **(no copy)**    |
|   `c = a[:]` **(copy)**   | `c = a[:]` **(no copy)**  |
| `d = a.copy()` **(copy)** | `d = a.copy()` **(copy)** |



### Boolean索引

定义数组：`a = np.array([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])`

逻辑比较（返回一个Boolean数组）

```python
>>> a > 5
array([False, False, False, False, False,  True,  True,  True, False,
       False, False, False, False])
```

`any`和`all`函数

```python
>>> np.any(a > 5)
True

>>> np.all(a > 5)
False
```

利用Boolean数组索引

```python
>>> a[a > 5]
array([6, 7, 6])

>>> a[(a >= 3) & (a <= 5)]
array([3, 4, 5, 5, 4, 3])
```



`np.where`和`np.clip`函数

|     函数     |                             参数                             | 作用                                                         |
| :----------: | :----------------------------------------------------------: | ------------------------------------------------------------ |
| `np.where()` | `condition, [x, y]`<br />`condition `: array_like, bool<br/> | If `condition` is `true`, yield `x`, otherwise yield `y`.<br /> If `x` or `y` 都没有指定，返回原先数组中的值 |
| `np.clip()`  |            `a, a_min, a_max, out=None, **kwargs`             | 指定值的范围`[a_min, a_max]`，<br />小于`a_min`的赋值为`a_min`，大于`a_max`的赋值`a_max` |



## 3. Vector operations

### 基本操作：vector之间的加减乘除整除

```python
# 定义两个数组
>>> a = np.array([4, 8])
>>> b = np.array([2, 5])
# 加
>>> a + b
array([ 6, 13])
# 减
>>> a - b
array([2, 3])
# 乘
>>> a * b
array([ 8, 40])
# 除
>>> a / b
array([2. , 1.6])
# 整除
>>> a // b
array([2, 1], dtype=int32)
# 乘方
>>> a ** b
array([   16, 32768], dtype=int32)
```



### 基本操作：vector与scalar之间的加减乘除整除

```python
# 定义数组
>>> c = np.array([1, 2])
# 加
>>> c + 3
array([4, 5])
# 减
>>> c - 3
array([-2, -1])
# 乘
>>> c * 3
array([3, 6])
# 除
>>> c / 3
array([0.33333333, 0.66666667])
# 整除
>>> c // 2
array([0, 1], dtype=int32)
# 乘方
>>> c ** 2
array([1, 4], dtype=int32)
```



### 截断近似函数

`np.floor`向下取整（round to negative infinity, -$\infty$）

```python
>>> np.floor([1.1, 1.5, 1.9, 2.5])
array([1., 1., 1., 2.])
```

`np.ceil`向上取整（round to negative infinity, +$\infty$）

```python
>>> np.ceil([1.1, 1.5, 1.9, 2.5])
array([2., 2., 2., 3.])
```

`np.round`向最近的整数截断（around to nearest integer）

```python
>>> np.round([1.1, 1.5, 1.9, 2.5])
array([1., 2., 2., 2.])
```

### 一些数学函数

```python
# 开方
>>> np.sqrt([4, 9])
array([2., 3.])
# 以e为底的幂乘
>>> np.exp([1, 2])
array([2.71828183, 7.3890561 ])
# 以e为底的对数（the logrithm of np.e to base e）
>>> np.log([np.e, np.e**2])
array([1., 2.])
# 点积
>>> np.dot([1,2], [3,4])
11
# 点积的另一种写法
>>> np.array([1,2]) @ np.array([3,4])
11
# 叉积
>>> np.cross([2, 0, 0], [0, 3, 0])
array([0, 0, 6])
# 正弦
>>> np.sin([np.pi, np.pi/2])
array([1.2246468e-16, 1.0000000e+00])
# 反正弦
>>> np.arcsin([0, 1])
array([0.        , 1.57079633])
# 平方和的开方
>>> np.hypot([3,5], [4,12])
array([ 5., 13.])
```

一些三角函数

| 三角函数 | 反三角函数 | 双曲函数 | 反双曲函数 |
| :------: | :--------: | :------: | :--------: |
|  `sin`   |  `arcsin`  |  `sinh`  | `arcsinh`  |
|  `cos`   |  `arccos`  |  `cosh`  | `arccosh`  |
|  `tan`   |  `arctan`  |  `tanh`  | `arctanh`  |



双曲正弦函数：$\sinh{x}$


$$
\sinh{x} = \frac{e^x - e^{-x}}{2}
$$


双曲余弦函数：$\cosh{x}$
$$
\cosh{x} = \frac{e^x + e^{-x}}{2}
$$


双曲正切函数：$\tanh{x}$
$$
\tanh{x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$

### 基本的统计函数

```python
# 最大值
>>> np.max([1, 2, 3])
3
# 最大值
>>> np.array([1, 2, 3]).max()
3
# 最大值的索引
>>> np.array([1, 2, 3]).argmax()
2
# 最小值
>>> np.array([1, 2, 3]).min()
1
# 最小值的索引
>>> np.array([1, 2, 3]).argmin()
0
# 求和
>>> np.array([1, 2, 3]).sum()
6
# 求平均
>>> np.array([1, 2, 3]).mean()
2.0
# 标准差
>>> np.array([1, 2, 3]).var()
0.6666666666666666
# 方差
>>> np.array([1, 2, 3]).std()
0.816496580927726
```

### 排序函数

|       Python List        | Numpy Arrays |           Effect           |
| :----------------------: | :----------: | :------------------------: |
|        `a.sort()`        |  `a.sort()`  |       sort in place        |
|       `sorted(a)`        | `np.sort(a)` | return a new sorted array  |
|     `a.sort(key=f)`      |      -       |       sort with key        |
| `a.sort(reversed=False)` |      -       | ascending/descending order |

