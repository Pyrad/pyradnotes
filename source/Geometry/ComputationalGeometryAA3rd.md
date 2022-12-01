# Computational Geometry

**Algorithms and Applications, Third Edition**



## About the book

**Third Edition (March 2008)**

**[Mark de Berg](http://www.win.tue.nl/~mdberg/),** TU Eindhoven (the Netherlands)
**[Otfried Cheong](http://tclab.kaist.ac.kr/~otfried/),** KAIST (Korea)
**[Marc van Kreveld](http://www.cs.uu.nl/staff/marc.html), [Mark Overmars](http://www.cs.uu.nl/staff/markov.html),** Utrecht University (the Netherlands)



[Website URL](http://www.cs.uu.nl/geobook/)

Published by Springer

[Errata Page for 1st Edition](http://www.cs.uu.nl/geobook/errata1.html)

[Errata Page for 2nd Edition](http://www.cs.uu.nl/geobook/buglist2a.pdf)



## Resources

[*Handbook of Discrete and Computational Geometry, 3rd Edition, Online Page*](https://www.csun.edu/~ctoth/Handbook/HDCG3.html)





## Words

**asymptote** */ˈæsɪmˌtoʊt/* *n.* [数] 渐近线

**asymptotically**  */,æsimp'tɔtikli,-kəli/* *adj.* 渐近线的

**planar** */ˈpleɪnər/* *adj.* 平面的；二维的；平坦的

**polygonal** */pəˈlɪɡənl/* *adj.* [数] 多边形的；[数] 多角形的

**lexicographic** */ˌleksɪkəˈɡræfɪk/* *adj.* 词典编辑的；字典式的

**dent** */dent/* *v.* 使产生凹痕；损害，削弱；*n.* 凹痕；削减

**clutter** */ˈklʌtər/* *v.* 乱堆，塞满；使（脑子里）塞满（乱七八糟的事）；*n.* 杂乱的东西；杂乱

**radiosity** */ˌreɪdɪˈəʊsɪtɪ/* *n.* 光能传递；热辐射

**kinematic** */ˌkɪnəˈmætɪk/* *adj.* [力] 运动学上的，[力] 运动学的

**vegetation** */ˌvedʒəˈteɪʃn/* *n.* （总称）植物，植被；（植物的）生长；呆板单调的生活

**excavation** */ˌekskəˈveɪʃ(ə)n/* *n.* （对古物的）发掘，挖掘；发掘现场； 挖洞，开凿

**interpolate** */ɪnˈtɜːrpəleɪt/* *vt.* 篡改；插入新语句；*vi.* 插入；篡改

**interpolating** */ɪnˈtɜːrpəleɪtɪŋ/* *n.* 插值；内插；*v.* 窜改；加入（额外的事）







## Usage

thought experiment

an elastic rubber band 橡皮筋

direct the line through *p* and *q*





## Contents

- Preface
- 1 Computational Geometry (Introduction)
- 2 Line Segment Intersection (Thematic Map Overlay)
- 3 Polygon Triangulation (Guarding an Art Gallery)
- 4 Linear Programming (Manufacturing with Molds)
- 5 Orthogonal Range Searching (Querying a Database)
- 6 Point Location (Knowing Where You Are)
- 7 Voronoi Diagrams (The Post Office Problem)
- 8 Arrangements and Duality (Supersampling in Ray Tracing)
- 9 Delaunay Triangulations (Height Interpolation)
- 10 More Geometric Data Structures (Windowing)
- 11 Convex Hulls (Mixing Things)
- 12 Binary Space Partitions (The Painter’s Algorithm)
- 13 Robot Motion Planning (Getting Where You Want to Be)
- 14 Quadtrees (Non-Uniform Mesh Generation)
- 15 Visibility Graphs (Finding the Shortest Route)
- 16 Simplex Range Searching (Windowing Revisited)
- Bibliography
- Index



## Preface

序言要点

- 计算几何兴起与20世纪70年代（1970s），应用于计算机图形（CG）、地理信息系统（GIS）、机器人（robotics）等领域。
- 本书每章节基本独立，但初学者可以按顺序阅读前10章。
- 每章节只举例了容易理解和实现的算法（解决方案），并不是所有，而且提供的是高层次的论述，并不深入每个细节。
- 带星号（`*`）的章节作为扩展阅读，以及叫做 *Notes and Comments*的小节，可以通过其了解更多。
- 不需要应用领域的知识，只需要基本的数据结构和算法知识储备。
- 有网页可以找到[Errata Page](http://www.cs.uu.nl/geobook/)以及其他可用资源。



## 1 Computational Geometry - Introduction

校园中寻找最近电话亭（*Voronoi diagram*，第7章）

避障最短路径（*motion planning*，第13,15章）

多张地图定位问题（*overlay map*，第2章）

实际的应用

- Robotics
- Computer graphics
- CAD/CAM
- Geographic Information System



### 1.1 An Example: Convex Hulls

好的几何算法问题解决方案，本质上有两方面

- 理解几何问题的特性
- 对算法和数据结构的合理使用

本节举例，介绍了两种计算二维平面上凸体的轮廓的算法（二维平面凸体，planar convex hulls）



#### 1.1.1 第一种算法

第一种算法是时间复杂度较高的算法，文中称为 ***SlowConvexHull*** 算法。

**输入**：平面上点的集合 ***P***。

**输出**：一个点的序列 ***L***，表示点集合 ***P*** 的Convex Hull，点序是**顺时针**方向。

**算法简述**：

从集合 ***P*** 中取任意不同两点 *p* 和 *q*，组成一有向线段 *p* -> *q*，检查集合 ***P*** 中剩余的任意一点 *r*，如果任意一点 *r* 都位于有向线段 *p* -> *q* 的右侧，说明有向线段 *p* -> *q* 就是最终轮廓上的其中一条线段，将其加入集合 ***E*** 中。

穷举集合 ***P*** 中这样两个点 *p* 和 *q* 的组合，重复上述检查，直至最终遍历完成，得到一个线段集合 ***E***。

最后，从集合 ***E*** 中找出依次连接的线段，并组成一个点列表，按照**顺时针**方向排序。

**算法复杂度**：O(n^3)



对于伪代码中的几个的说明

- 诸如判断一个点在一条直线（线段）的左边或右边的操作，默认已经有现成的实现可以使用
- 从集合 ***E*** 中找出依次连接的有向线段的步骤是，首先从 ***E*** 中取任一有向线段 *e1*，以其头点（即 *p* -> *q* 线段的 *q* 点）为目标，从集合 ***E*** 中找出第二条有向线段 *e2*，其尾点（即 *p* -> *q* 线段的 *p* 点）为 *e1* 的头点，然后再以 *e2* 的头点搜索下一条有向线段，直到搜索到的这些线段 *e1*,  *e2*, *e3*, ..., *eN* 构成一条闭合的折线段。
- 关于算法复杂度是O(n^3)。从 *n* 个点中取两个点的组合是 *n!/ 2! (n-2)! = n(n-1)*，所以是O(n^2)，对每一条有向线段，查看剩余 *n-2* 个点是否在其右侧，这样时间复杂度就达到了O(n^3)。最后一步依次找出有向线段并按顺序连接，时间复杂度是O(n^2)，所以最终时间复杂度就是O(n^3)。



关于 ***degenerate case*** 或者叫做 ***degeneracy***

在判断一个点 *k* 是否在有向线段 *p* -> *q* 右侧时，点 *k* 是可能落在有向线段 *p* -> *q* 上的，针对这种退化情况，可以把它也当做是在有向线段右侧的一种（退化）情况。



关于 ***rounding error*** 导致的程序健壮性问题（robustness）

在实际情况中，因为使用的是浮点数计算，那么仍然是在判断一个点 *k* 是否在有向线段 *p* -> *q* 右侧时，可能产生微小的误差（rounding errors），导致最终计算出来的convex hull的点集合 ***E*** 有三种情况：

1. 要么不是真正意义上的convex hull（但仍然是非常接近实际情况的）
2. 要么最终的集合 ***E*** 中的有向线段不是一个闭合的折线段
3. 要么最终的集合 ***E*** 中的有向线段除了可以组成一个闭合的折线段外，还有额外剩余的几条有向线段

正是由于这种robust的问题，迫使我们需要寻找一种更为健壮和正确的算法。



#### 1.1.2 第二种算法

第二种算法是时间复杂度比第一种算法低，采用了所谓的 *incremental algorithm* 的方法，文中名为ConvexHull算法。

这种算法的总体思路是，将所有的点按照 *x* 坐标由大到小排序为 *p1*, *p2*, *p3*, ..., *pN*，因为前提是凸多边形，所以先按照从左向右的方向，找到这convex hull的上半部分边界 *upper hull*，即 *p1*, *u0*, *u1*, ..., *pN*（其中*u0*, *u1*, ... 都是集合中的点），再找到convex hull的下半部分边界 *lower hull*，即*p1*, *v0*, *v1*, ..., *pN*（其中*v0*, *v1*, ... 也都是集合中的点）。

这个所谓的 *incremental algorithm* 方法的关键步骤在于，如何在向已有的但不完整的*upper/lower hull* 添加一个点之后，更新这个不完整的*upper/lower hull*，使得其向左或向右延伸一段（最终到达最右或最左的点）。

换句话说，假如现已有*upper hull*的点是 *p1*, *p2*, ..., *p(i-1)*, 如何找到下一个点 *pi*，使得 *p1*, *p2*, ..., *pi* 是最终 *upper hull* 的一部分。

因为我们约定是按照顺时针方向来标记最终的convex hull的，所以，沿着convex hull的边界行走，一定是**“右转”**的。因此，可以按照此方法来确定如何加入上面提到的*pi*点，从而生成一条新的convex hull的一部分。

假设我们现在计算的是 *upper hull*，那么我们遍历的点一定是按照 *x* 坐标有小到大的顺序，那么当加入点 *pi* 时，点 *pi* 的 *x* 坐标就是目前的convex hull 点 *p1*, *p2*, ..., *p(i-1)* 里面 *x* 坐标最大的。

加入点 *pi* 后，此时点列为  *p1*, *p2*, ..., *p(i-1)*, *pi*。此时我们检查最后三个点 *p(i-2)*, *p(i-1)*, *pi*。

- 如果这三个点是**“右转”**的，那么新加入的点 *pi*，就是最终 upper convex hull的一部分（但有可能在加入之后的点以后，继续做调整从而删除点 *pi*）。

- 如果这三个点是**“左转”**的，那么因为目前 *pi* 的 *x* 坐标最大，它就一定是在目前遍历过的convex hull上，所以我们就需要从 *p(i-1)* 开始向后检查，每次删除最后3个点的中间的点（即每次的倒数第二个点），做重新调整。

  先删除 *p(i-1)* 这个点，然后检查此时的最后三个点，*p(i-3)*, *p(i-2)*, *pi*，如果它们组成了**“右转”**的折线，那么本次调整到此结束，然后继续加入下一个点 *p(i+1)*；如果它们组成了**“左转”**的折线，那么就需要再次删除中间点，即*p(i-2)*，然后继续检查时的最后三个点，*p(i-4)*, *p(i-3)*, *pi*，并重复上述步骤，直到最后三个点组成**“右转”**的折线（或者直到剩下最后2个点），本次调整才到此结束，然后继续加入下一个点 *p(i+1)*。

当针对上述两种情况做完调整之后，此时继续加入下一个点 *p(i+1)*，并重复上述步骤，直到加入最右边的点 *pN*，此时就得到了 *upper hull*。

寻找 *lower hull* 的incremental的步骤和上述类似。



第二种算法简述

**输入**：平面上点的集合 ***P***。

**输出**：一个点的序列 ***L***，表示点集合 ***P*** 的Convex Hull，点序是**顺时针**方向。

**算法简述**：

- 将集合 *P* 按 *x* 坐标排序为 *p1*, *p2*, ..., *pN*
- 把*p1*, *p2* 放入序列 ***L***，并且 *p1* 是第一个点， *p2* 是第二个点
- 变量 *i*，值从3到N，依次遍历加入序列 ***L1***，每次加入点 *pi*，检查最后三个点是否组成**“右转”**的折线段。如果是，继续遍历下一个值，否则删除当前序列 ***L1*** 的倒数第二个点，并继续检查最后三个点是否组成**“右转”**的折线段，以此类推，直到当前序列 ***L1*** 的最后三个点组成**“右转”**的折线段，才继续遍历下一个 *i* 值。
- 当变量 *i* 遍历完成时，就得到了convex hull的上半部分 upper hull的点序列是 ***L1*** 。
- 把*pN*, *p(N-1)* 放入序列 ***L2***，并且 *pN* 是第一个点， *p(N-1)* 是第二个点
- 变量 *j*，值从N-2到1，依次加入序列 ***L2***，和上面寻找upper hull的办法类似，仍然是确保每加入一点后，调整序列 ***L2***，使得其最后三点组成**“右转”**的折线段，然后才继续遍历下一个 *j* 值。
- 把序列 ***L2*** 的第一个和最后一个点去掉，避免重复点。
- 把序列  ***L1*** 和序列  ***L2*** 合并，即得到最终的点序列 ***L***。

时间复杂度：O(nlogn)



























