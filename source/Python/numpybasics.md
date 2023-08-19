# Numpy Basics

This is a file which shows basic usages of Numpy

## Checks if 2 floating number arrarys are equal

```python
nump.allclose(array_a, array_b)
```

## NumPy sort array of arrays

Use `np.lexsort` and `.T` method.

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
>>> np.lexsort(a.T)
array([1, 0, 3, 2], dtype=int64)
>>> a[np.lexsort(a.T)]
array([[  3,  19,  23,   7],
       [ 10,   0,   2,   9],
       [  2, 101,  25,  56],
       [  0,  84,  31, 100]])
```

