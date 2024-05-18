# Debug Track

## 2024-05-18

今天就注意是看完了着一部分的内容：[NEP 13 — A Mechanism for Overriding Ufuncs](http://www.numpy.org/neps/nep-0013-ufunc-overrides.html)，它是 NumPy 中关于 method `__array_ufunc__` 的介绍和说明。

这篇文章（[NEP 13 — A Mechanism for Overriding Ufuncs](http://www.numpy.org/neps/nep-0013-ufunc-overrides.html)）的主要内容是：

1. `__array_ufunc__` 的概述

2. 实现的目的

   为什么要在一个 class 中，实现魔法函数 `__array_ufunc__`

   为了使得（允许）这个 class 的instance 可以和 `NumPy.ndarray` 进行类似乘法、加法等universal functions之类的运算。

   - 要实现的 `__array_ufunc__` 的signature必须如下，

     ```python
     def __array_ufunc__(self, ufunc, method, *inputs, **kwargs)
     ```

   - 类型转换（type cast hierarchy）是如何影响 `__array_ufunc__` 在实际中的使用机制的。

     根据类型转换的层次关系，`__array_ufunc__` 要根据情况返回不同的结果。

   - 通常情况下， 在 `__array_ufunc__` 的实现中，在将输入进行过滤等处理之后，
     就调用其所集成的父类的 `__array_ufunc__` 进行处理。

   - 如何关闭一个类的 ufunc 功能

     实现就是把 `__array_ufunc__` 置为 `None`：`__array_ufunc__ = None`

   - 一个实现了 `__array_ufunc__` 的类的instance，和一个实现了 Python二元操作符（比如 `+`，`*` 等）的类的instance，
     是以何种顺序、如何调用 `__array_ufunc__` 和 `__mul__` 、`__rmul__` 等魔法函数的。

   - 在定义了 `__array_ufunc__` 的类中，如何定义其他的Python二元操作符（比如 `+`，`*` 等），
     并使得它们能够按预期共同协作，运算得到预期结果。

   - NumPy ufunc、Python operator 以及 Python symbol的对应列表
     （[List of operators and NumPy Ufuncs](https://numpy.org/neps/nep-0013-ufunc-overrides.html#neps-ufunc-overrides-list-of-operators)）。

---

关于NumPy中所谓的 `ufunc` 的基本概念：[Universal functions basics - NumPy](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-basics)

`NumPy.ufunc`的reference page：[Universal functions (ufunc)](https://numpy.org/doc/stable/reference/ufuncs.html)

在Python中创建 `ufunc` 的简单例子：[How to Use NumPy’s ufuncs for Custom Operations](https://www.slingacademy.com/article/how-to-use-numpys-ufuncs-for-custom-operations/)

---

发现了 CuPy 的 ndarray 是用 **Cython** 实现的，定义在如下的源文件中

```shell
cupy/_core/core/ndarray.pyd
cupy/_core/core/ndarray.pyx
```

其中 `cupy/_core/core/ndarray.pyd` 的 Cython 的声明文件（看起来类似C的头文件），而 `cupy/_core/core/ndarray.pyx` 似乎是Cython 的定义文件（看起来类似C的源文件）。

---

NumPy 中的 NEP 是 **N**umPy **E**hancement **P**roposals，链接

- [NumPy NEPs Content - NumPy](https://numpy.org/neps/content.html)

- [NumPy Roadmap](https://numpy.org/neps/roadmap.html)

---

cornerstone 基石

proviso /prəˈvaɪzəʊ/ *n.* 附带条件；附文；限制性条款

acyclic /ˌeɪˈsaɪklɪk/ adj. 非循环的；[物] 非周期的

transitive /ˈtrænzətɪv; ˈtrænsətɪv/ adj.（动词）及物的；（关系）可递的，可迁的，传递的；n.及物动词

transitivity /ˌtrænzəˈtɪvəti; ˌtrænsəˈtɪvəti/ n. 传递性；动词的及物性；转移性

commutative /kəˈmjuːtətɪv/ adj. 交换的，交替的，（数学上）可交换的；（一般）代替的

coercion /kəʊˈɜːʃ(ə)n/ n. 强迫，胁迫；高压政治，威压

unilateral /ˌjuːnɪˈlætrəl/ adj. 单方的，单边的；单侧的，单面的；（父母）单系的；舌边音

reflexive /rɪˈfleksɪv/ adj. （词或词形）反身的；反射性的，本能反应的；（关系）自反的；考虑自身影响的；n. 反身词
