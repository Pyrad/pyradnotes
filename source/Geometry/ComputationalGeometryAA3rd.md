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











