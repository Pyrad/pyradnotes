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

**thematic** */θɪˈmætɪk/* *adj.* 主题的，主旋律的；题目的；语干的

**precipitation** */prɪˌsɪpɪˈteɪʃ(ə)n/* *n.* 降水（如雨，雪，冰雹）；沉淀，淀析；仓促，鲁莽，轻率；坠落

**grizzly** */ˈɡrɪzli/* *adj.* 灰色的；*n.* 灰熊

**lemma** */ˈlemə/* *n.* 引理；辅助定理；论点；膜

**recap** */ˈriːkæp/* *v.* 扼要重述，摘要说明；翻新胎面；*n.* 扼要的重述，概述；翻新的轮胎

**treat** */triːt/* *v.* 处理，探讨，论述；

**deciduous** */dɪˈsɪdʒuəs/* *adj.* 落叶性的，脱落性的；非永久性的

**cyclic** */ˈsaɪklɪk/* *adj.* 环的；循环的；周期的



## Usage

thought experiment

an elastic rubber band 橡皮筋

direct the line through *p* and *q*

to this end 为了这个目的（**formal** **:** as a way of dealing with or doing something）

rule out 排除，除去

windy river 弯曲的河流（不是多风的河流）

coinciding point 共点

in a sense 某种意义上

incident to 由...产生（这里incident是 *adj.*）

hold for 适用



> Define the *y*-interval of a segment to be its orthogonal projection onto the *y*-axis.
>
> 把一条线段在 *y* 轴上的正交投影，叫做它的 *y*-interval



> they are far apart in the y-direction
>
> 它们在y方向上相距足够远



> We denote the *event queue* by Q
>
> 我们把event queue记作**Q**



> This horizontal sweeping line is sloping just a tiny bit upward
>
> 这条横向的扫描线翘起来一点点



> We need an operation that removes the next event that will occur from Q, and returns it so that **it can be treated**.
>
> 需要一个从队列Q里面删除下个event（point）的操作，并且返回它，以便（对它进行）处理。





## Names

- Graham’s scan
- output-sensitive algorithm

- planar graph
- planar subdivisions



## Maths

$e'$ ：$e$ prime（或 $e$ dash）

$e''$ ：$e$ double prime（或 $e$ double dash）



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

**（这个算法实际上是Andrew对Graham’s scan的一种改进算法）**

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



对于该算法的几点说明

- 在排序时，如果 *x* 坐标相同，可以按照 lexicographic 的办法排序，即先按照 *x* 坐标排序，如果 *x* 坐标相同，就再按照 *y* 坐标排序（仅对 *x* 坐标相同的点的情况下）。
- 在上面判断最后三点是否组成**“右转”**的折线段时，如果这三点共线，仍然把这种情况归为**”左转“**的情况，从而触发删除三点里面中间点的操作处理。
- 因为使用的是floating point calculation，并且依然存在rounding error，所以最后的点列表，有一定概率并不是实际上真正的convex hull的点列表（比如有三个点靠的很近以至于是一个左转的折线段，但被计算为右转了），但这种结果是可以接受的。



#### 1.1.3 计算convex hull的时间复杂度

> Theorem 1.1 The convex hull of a set of n points in the plane can be computed in O(nlogn) time.

关于第二种算法正确性的证明，文中采用了数学归纳法。

以upper hull为例，假如现已有点列 {*p1*, *p2*, ..., *p(i-1)*}，准备加入点 *pi*。根据算法，点列{*p1*, *p2*, ..., *p(i-1)*}中最后三点一定是组成**“右转”**的折线段（即除了这些点，到目前最大的点为止，其他点都在这些点的下方）。我们把此时的upper hull点列叫做 old chain。

在加入点 *pi* 之后，按照字典序（lexicographic），最小的点是 *p1*，最大的点是 *pi*，经过调整，此时的upper hull我们叫做new chain（而且new chain的最后一个点一定是*pi*）。

可以断言的是old chain一定是在new chain的下方（有可能点*pi*就是old chain的延伸，但是在算法中，这种共线的情况被当做是左转而被排除掉了）。

按照算法，我们需要证明的是，到目前为止，除了{*p1*, *p2*, ..., *pi*}，所有的点都在new chain的下方。

假如有一个点位于new chain的上方，那么这个点就必须介于 *p(i-1)* 和 *pi*之间，因为在加入 *pi* 之前，所有的点都位于old chain的下方。但这又是矛盾的，因为 *p(i-1)* 和 *pi* 之间没有其它点，因为所有点已经是按照字典序排列过了的。

因此归纳出来，到目前为止，除了{*p1*, *p2*, ..., *pi*}，所有的点都在new chain的下方。算法正确性得到证明。



关于时间复杂度的证明。

对于upper hull，按字典序排序，时间复杂度是O(nlogn)。

for循环是线性的，关键在于其里面用于检查右转折线段和删除中间点的while循环的执行次数。

这个while循环首先可以肯定至少执行一次（检查右转折线段），而额外执行的次数，是为了删除每次得到的序列最后三点的中间点，而因为所有点只会被加入序列一次，所以，每个点最多也只会被删除一次，那么这个for循环里面的while循环执行的上限就是O(n)。

所以，带有while循环的这个for循环，时间复杂度是O(n)，而不是O(n^2)。

因此计算upper hull的时间复杂度就是O(nlogn)。

对于lower hull也是类似的。所以加起来，整个算法的时间复杂度就是O(nlogn)。



### 1.2 Degeneracies and Robustness

提出算法的三个步骤（阶段）

- 首先，排除次要因素的干扰，因为这些因素是细节问题，不影响算法的整体思路。
- 其次，再考虑前面可能出现的退化情况（边界条件，特殊和极端情况等问题），调整算法细节以便处理。
- 最后，实现细节。比如原子操作，如何遍历等等。



比如，在convex hull的算法中，我们可以先假设没有三个共线的点，没有两个点的 *x* 坐标是相同的。

symbolic perturbation schemes指在设计和实现阶段忽略了special case，但在实际应用过程当中算法仍然正确的方法。



在实现细节的阶段，使用实数（浮点数）计算可能导致假设在某种情况下失效的问题，这是算法健壮性的体现。就像前面第二种算法中提到的，最终的output也许不是真正意义上的真实结果，但也是十分接近真实的结果，在这种情况下，需要预期这种情况可能的后果，并避免有次可能产生的crash问题等等。

使用现有的arithmetic library是其中一种办法，如果不能达到我们所需要的要求，就需要自己实现一些特定情况下的处理。



### 1.3 Application Domains

这一节主要介绍了Computational Geometry的几种应用领域，已经每个领域要解决的问题。

- Computer graphics
- Robotics
- Geographic information systems
- CAD/CAM
- Other applications domains （比如 molecular modeling，pattern recognition等）



### 1.4 Notes and Comments

本节主要是对本章内容的一些延伸以及参考书籍资料等出处说明，提到了本章算法的来源，其发展的简要历史，以及相似算法的研究情况。

比如，本章所讨论的convex hull问题是Computational Geometry的经典问题，而本章第二种算法，其实是Graham’s scan算法，是Andrew基于最早的Graham提出的算法的改进。

还有其他的一些算法，时间复杂度也是O(nlogn)。







## 2 Line Segment Intersection - Thematic Map Overlay

引言部分，以旅游为例，讲述了在实际当中，可能需要查看包含不同信息类型的地图，从而找到所需的信息。

在GIS领域中，***layer*** 是指包含某一种信息的地图（map），而需要将多种类型的地图进行交叉引用的合并结果，叫做 ***overlay***。

比如，一个layer（map）只包含城市名的信息，另一个layer（map）只包含河流的信息，还有一个layer（map）只包含了铁路轨道的信息，诸如此类等等。

当查看了城市信息的layer（map）之后，想要得知如何前往，就需要和另一个包含道路信息的layer（map）重叠查看，就是overlay。

GIS中，在overlay上，不同信息有交叉的地方（比如查看河流和道路的重叠情况），有时是一个交叉点，有时是一个交叉的区域。



### 2.1 Line Segment Intersection

本节要解决的问题是，给定二维平面上一个有 *n* 个线段的集合，找出所有的交点。

> given a set S of n closed segments in the plane, report all intersection points among the segments in S.

其中线段的端点碰到其他的线段，也算作交点。

Brute-forced algorithm的时间复杂度是O(n^2)，但实际情况，有可能只有很少的一些线段相交，并不必计算每个线段和其他线段的交点。

即，我们希望算法的复杂度依赖的不仅是输入点的个数，而且也是输出的交点的个数，这样的算法叫做***output-sensitive algorithm***。



可以利用的观察几何结果是：靠的比较近的线段是可能有交点的候选计算对象，而相离较远的线段是不需要计算交点的。

所以思路是，把所有线段向y轴做投影，得到投影线段有重叠的那些线段，就是需要计算交点的候选线段。

为什么没有投影重叠的线段就一定没有交点？这可以通过反证法得出，如果没有投影重叠的线段有交点，那么这个交点的y坐标值一定是介于两个线段的4个端点的y值之间，而这又说明这两条线段是有投影重叠的，因此矛盾，从而的证。



使用到的技术叫做：***plane sweep algorithm***。

***sweep line***：一条水平无限长的假想虚线

***status***：***sweep line***的“状态”指的是和它当前相交的**线段的集合**（**segments**）

***event point***：***sweep line***沿着垂直方向从上向下移动，但不是连续移动的，而是离散的，移动到的这些位置的点，叫做***event point***。这些***event point***，一部分是每条线段的upper end point（y值较大的点）和lower end point（y值较小的点），另一部分是线段之间的交点。

只有当***sweep line***移动到这些***event point***上的时候，算法才做相应的计算或调整，即更新***sweep line***的***status***，并测试线段之间有无交点（如有，就计算交点）。

- 如果***event point***是一条线段的**upper point**，那么这条线段就是和***sweep line***相交，并且应该加入到***status***里面，同时要计算这条segment和***status***里面其他segments的交点（*后面会提到，只计算当前线段相邻的左右两条segments的交点，而不是计算和status里面所有线段的交点*），而且这个交点（如果有）要放入到event point集合的适当位置，以便sweep line依次向下扫描时可以遍历到它。

- 如果***event point***是一条线段的**lower point**，那么这条线段就和***sweep line***不再相交（即变为相离），就应该从status里面删除。而且这也会导致**status**里面原先不直接相邻的两条线段，现在变成了直接相邻了，那就要计算这两条相邻线段之间有无交点（如果有，依然要放入event point集合里面去）

- 如果***event point***是两条线段的**intersection point**（这个intersection point是前面计算得到加入进来的），那么在该点之后，相邻的adjacent neighbor就会发生改变，所以就要测试（计算）这两条segments和它们各自左右相邻的segment的交点。



> Lemma 2.1 Let *si* and *sj* be two non-horizontal segments whose interiors intersect in a single point *p*, and assume there is no third segment passing through *p*. Then there is an event point above *p* where *si* and *sj* become adjacent and are tested for intersection.

因为根据前面遇到的event point是一条线段的upper point时的操作（计算adjacent segment之间的intersection point），这个引理主要想说明，如果两条都不是水平（也不共线）的线段，如果有交点，那么在这个交点的上方，一定有一个event point，在那个event point的时候，这两条线段变成adjacent，并且会被检查（计算）是否有交点。

这里**暂时忽略**了三种特殊情况：两条线段可能共线（重合），可能有水平的情况，以及有第三天线段穿过交点。



所以，简要叙述，***line sweeping algorithm***的大体思路如下

> Let’s briefly recap the overall approach. We imagine moving a horizontal sweep line ℓ downwards over the plane. The sweep line halts at certain event points; in our case these are the endpoints of the segments, which we know beforehand, and the intersection points, which are computed on the fly.
>
> While the sweep line moves we maintain the ordered sequence of segments intersected by it. When the sweep line halts at an event point the sequence of segments changes and, depending on the type of event point, we have to take several actions to update the status and detect intersections.

假设有一条水平扫描线，从上而下移动，每次移动到一个特殊的点（event point）。这样的event point有两种，一种是每条线段的upper point（end point），另一种是某两条线段的交点（intersection point）。前一种在计算之前就已知，而后一种是在扫描线移动过程中计算得出。

当扫描线移动时，维护一个有序的线段列表，列表中的每个线段是和扫描线相交的。当扫描线移动到下一个event point的时候，更新线段列表使其保持有序，同时根据event point的类型，更新状态（它是和扫描线相交的线段集合，每次操作有可能添加或删除一条线段）并检查某两条线段是否有交点。



sweep line遇到三种不同event point时对应的操作

- 如果**event point**是一条线段的**upper point**（end point），就要检查这个upper point所在的线段，和它左右两个相邻的线段是否有交点，如果有交点，那么这个交点就是一个新的event point。当然，upper point所在的线段要放入status中去。

  因为sweep line上方的event point都是已知的或已经计算过的，所以关注的是sweep line下方的交点。

- 如果**event point**是某两条线段的**交点**（intersection point），那么这两条线段在所维护的有序线段列表（status）里面的位置就要交换，同时因为位置变化，它们各自相邻的线段也发生了变化（但只变化了一个，因为另一个仍然是它们自己中的一个），所以也要检查它们和各自新邻近的线段之间是否有交点，如果有并且是之前没有的event point，那么就有发现了一个或两个新的event point。

- 如果**event point**是一条线段的**lower point**（end point），那么这条线段原先左右两条线段就变成了直接相邻的线段，就要检查（计算）这两条线段是否有交点，同样的，如果有，就是新的event point。当然，这个lower point所在的线段要从status里面移除出去。





算法当中需要的两个数据结构

- **event queue**（记作 ***Q***）

  **需要支持删除一个点（event point）的操作**，并返回这个点以便对其处理。

  （如果两个点有相通的y坐标，返回x坐标较小的一个。这个实际上说明，如果一个线段是水平时，当水平的sweep line扫描到这条线段时，upper point是其左边的点，lower point右边的点，即sweep line先遇到的event point是左边的点。）

  **需要支持插入一个点（event point）的操作**，因为新的intersection point是在sweep line移动过程中计算得出。

  同时，允许两个event point是共点的（coincide，比如两条线段的upper point可能是同一个点），但把它们当做是同一个点，所以需要支持查看一个event point是否在***Q***中已经存在。

  根据上述特点，采用平衡二叉搜索树（**Balanced Binary Search Tree**，BST），并定义点（event point） *p* < *q* 的“小于”操作符（`<`）为

  （1）如果 *p* 和 *q* 的y坐标相同，那么 *p* 的x坐标小于*q* 的x坐标

  （2）如果 *p* 和 *q* 的y坐标不相同，那么 *p* 的y坐标小于*q* 的y坐标

  需要删除一个点的操作的原因是，sweep line向下移动时，需要event point的顺序，移动到下一个event point上，而这是二叉树删除一个节点并返回的操作（同时二叉搜索树会重新平衡并排序）

  需要插入一个点的操作的原因是，当sweep line移动到不是intersection point的event point的时候，要计算相邻两条线段之间的intersection point，如果有就要插入BST，所以这是BST的插入节点的操作。

- **status**（记作 ***J***）

  这个所谓的状态，是指当前和水平的sweep line相交的**线段**的**有序**集合。

  对于给定的一条线段，为了计算它和相邻线段的相交情况，它必须是可以动态调整的，即：

  （1）当sweep line遇到一条线段的upper end point的时候，该线段需要放入status，并且需要查看此时它和左右相邻的两条线段的相交情况，如果有交点就需要计算出来，并放入**event queue**里

  （2）当sweep line遇到一条线段的lower end point的时候，该线段需要从status中移除，同时它原先左右相邻的两条线段现在变为直接相邻，那么也要再次查看并计算这两条线段是否有交点，如果有，同样放入**event queue**里

  （3）当sweep line遇到的event point是intersection point的时候，那么就需要交换这两条相交的线段在status中的位置，同时在status中，它们各自分别有一条相邻的线段发生了变化，同样需要再查看并计算交点，如果有交点，同样放入**event queue**里

  同样根据上面的特点，也采用平衡二叉搜索树（**Balanced Binary Search Tree**，BST），但这里的BST里面，只有叶子节点是存储了线段的信息，而树中间的每个节点（interior nodes），存储的都是其左子树里面最右边（叶）节点的线段信息。

  虽然中间的节点也可以存储线段信息，但为了方便陈述算法，所以中间节点都是用来引导寻找最终叶节点的导引信息（values to guide the search），而不是最终的线段数据信息（data item）。



***FindIntersections***算法简述

**输入**：平面上线段的集合 ***S***。

**输出**：交点的集合 ***L***，这些交点都在集合 ***S*** 中的某些线段上，同时每个交点还有其对应的线段信息，表示该交点位于哪（几）条线段上。

**算法简述**：

首先，初始化一个空的event queue，记作 ***Q***。然后把集合 ***S*** 里线段的end points都插入到 ***Q*** 中，当一个end point是线段的upper point时，要同时带上其所在的线段的信息（属于那条线段）。

然后，初始化一个空的status 数据结构，记作 ***J***。

之后，依次遍历 ***Q***，每次从 ***Q*** 中返回下一个event point *p*（同时 *p* 从 ***Q*** 中被移除），然后根据event point *p*，调用对 *p* 的处理函数***HandleEventPoint(p)***（如下）。这个遍历的终止条件是 ***Q*** 为空。（即这是一个while循环，而在遍历过程中可能有新event point加入 ***Q*** ）

**算法复杂度**：

O((n+k)logn)，其中，n是输入线段个数，k是输出个数

或者更具体地，O((n+I)logn)，其中，n是输入线段个数，I是交点个数



***HandleEventPoint(p)*** 步骤简述

- 输入是点 *p*

- 记 upper end point为 *p* 的线段集合为 ***U(p)***，这些线段是和点 *p* 对应存储的。如果线段是水平的，它的upper end point是左边的端点。

- 在status ***J*** 中找到所有包含点 *p* 的线段，它们都是相邻的，记 ***L(p)*** 是lower endpoint为 *p* 的线段集合，记 ***C(p)*** 是线段中间包含点 *p* 的线段集合（即点 *p* 是它们之间某两条或几条线段的交点）。

- 如果 ***L(p)*** ∪ ***U(p)*** ∪***C(p)*** 至少有一条线段，就说明点 *p* 是一个交点

  - 报告这个结构，并同时报告它所在的线段（在***L(p)***， ***U(p)*** 和 ***C(p)*** 中）

- 从status ***J*** 中删除***L(p)*** ∪***C(p)*** （即它们的并集）

- 向status ***J*** 中添加***U(p)*** ∪***C(p)*** （即它们的并集），并且插入的这些线段的顺序是，按照它们和sweep line在 *p* 稍下方一点位置相交的顺序。如果有线段是水平的，那么它要排在其他线段的最后面。

- 从上面的两个步骤可以得到，删除了***C(p)*** 又添加了***C(p)*** ，那么***C(p)*** 中的线段在status ***J*** 中的顺序逆序了。

- 如果***U(p)*** ∪***C(p)*** （即它们的并集）为空集

  - 把 status ***J*** 中，在 *p* 点左右两边的线段记为 *sl* 和 *sr*，调用寻找event point的函数***FindNewEvent(sl, sr, p)***

    如果 *sl* 或 *sr* 不存在，就忽略此步骤。

- 如果***U(p)*** ∪***C(p)*** （即它们的并集）不是空集

  - 把既在 ***U(p)*** ∪***C(p)*** 中又在status ***J*** 中，最左边的线段记作 *s1*，把在status ***J*** 中 *s1* 左边的线段记作 *sl*，然后调用寻找event point的函数***FindNewEvent(sl, s1, p)***。

    如果 *sl* 不存在，就忽略此步骤。

  - 把既在 ***U(p)*** ∪***C(p)*** 中又在status ***J*** 中，最右边的线段记作 *s2*，把在status ***J*** 中 *s1* 右边的线段记作 *sr*，然后调用寻找event point的函数***FindNewEvent(s2, sr, p)***

    如果 *sr* 不存在，就忽略此步骤。



***FindNewEvent(sl, sr, p)*** 步骤简述

- 如果线段 *sl* 和 *sr* 在sweep line的下方相交，或者就在sweep line上相交并且在当前event point *p* 的右边，那么这个新的交点就是在 ***Q*** 中还没出现的新的event point
  - 把这个新的交点加入到 ***Q*** 中



Lemma 2.2 和Lemma 2.3 分别是这个算法的正确性，以及算法的时间复杂度的证明。

根据这两个引理，得出Theorem 2.4。

>  Lemma 2.2 Algorithm FINDINTERSECTIONS computes all intersection points and the segments that contain it correctly.
>
> Lemma 2.3 The running time of Algorithm FINDINTERSECTIONS for a set S of n line segments in the plane is O(nlogn+I logn), where I is the number of intersection points of segments in S.
>
> Theorem 2.4 Let S be a set of n line segments in the plane. All intersection points in S, with for each intersection point the segments involved in it, can be reported in O(nlogn+I logn) time and O(n) space, where I is the number of intersection points.



### 2.2 The Doubly-Connected Edge List

引出了**可平面图**（planar graph, or planar embedding graph）的概念，引出可平面图的点（vertex）、线（edge）、面（face）。

同时引出了我们需要的应用，即确定哪个面（face）是包含所给定的一个点（given point）的。

引出了数据结构 ***doubly-connected edge list***，即 ***doubly-connected edge list*** 包含了一个平面细分（subdivision）上的face，edge，vertex的记录（record），并且除了几何和拓扑信息外，可能还有一些其他额外的信息，这个额外的信息叫做 ***information attribute*** （例如，一个face可能代表的是一种植被的覆盖，那么这个植被的种类就可以是这个额外的信息）。

这个 ***doubly-connected edge list*** 数据结构上的几何与拓扑信息，需要允许我们支持以下的一些操作

- 逆时针遍历这些face的edges，同时也能容易地反方向（顺时针）遍历。（这就要求edge直接有指向前一个和后一个的指针）

- 因为一个edge是两个face的边界，所以edge上需要有两个指针来指向这两个face

- 为了更方便表示当前描述的edge是哪个face的edge，可以把一条edge拆解为两条 ***half-edge***

  - 这两条half-edge是不同face的，而且每个half-edge都有唯一的指向前一个half-edge和执行后一个half-edge的指针
  - 而这同样意味着，一条half-edge只属于同一个face
  - 对于同一条edge的两条half-edge，我们把它们叫做 ***twins***
  - 我们把half-edge定义为有方向的，沿着half-edge走，face就在它的左边，所以这个方向是**逆时针**
  - 把half-edge定义为一个向量，origin（起点）是v，终点（destination）是w。所以它的twin half-edge的起点就是w，而终点是v。
  - 根据上面的定义，为了访问face的边界，可以只存储一个指向half-edge的指针，这样就可以沿着逆时针方向遍历这个face的所有half-edge了。

- 为了在表示洞（hole）时，仍然有沿着half-edge走时，face还在它的左边，就把洞的half-edge的方向定义为顺时针。

  而且，为了表示洞，需要需要有两个指向half-edge的指针，一个逆时针表示包含洞的face的边界，一个顺时针表示洞本身。

- 还可以存储多个half-edge的指针，而且这些指针沿着这些edge遍历起来的时候，没有重复的edge，这就是isolated island的形式（为了简化期间，书中暂时不作讨论）

**总结起来**，doubly-connected edge list数据结构有三种记录数据（record）

- vertex record

  它用来记录每个vertex（记作v）的坐标Coordinate(v)，并且它还有一个指针$IncidentEdge(v)$指向一条half-edge，而且这条half-edge的起点就是v

- face record

  一个face（记作$f$）

  - 存储一个指针$OuterComponent(f)$，指向的是outer boundary的half-edge。（如果face是unbound，即open edges的话，这个指针就是空？）
  - 还存储一个指针$InnerComponent(f)$，指向的是inner boundary的half-edge，这是用来表示洞的

- half-edge record

  一个half-edge（记作$e$）

  - 存储一个指针$Origin(e)$指向它的起点（origin）
  - 存储一个指针$Twin(e)$指向它的twin half-edge
  - 存储一个指针$IncidentFace(e)$，表示它绑定（bound）的face
  - 存储一个指向它前面half-edge的指针$Prev(e)$
  - 存储一个指向它后面half-edge的指针$Next(e)$

  没有必要存储它的终点（destination），因为可以通过$Origin(Twin(e))$得到。

本节还画了vertex，edge，half-edge，face以及上面提到的各种record的示意图，如下。

（图暂时省略，图位于第32页，页码是41）

这里也提到了，有时候有些record在一些应用中不是必须的（比如river和road构成的face，在某些应用中没有太多意义），所以在实现的时候可以适当忽略，以便在算法实现中更方便地调整其他数据。



### 2.3 Computing the Overlay of Two Subdivisions

简而言之，计算两个subdivision的overlay，就是根据两个subdivision的doubly-connected edge list（记作S1和S2），计算出一个新的doubly-connected edge list表示的subdivision（记作$O(S_1, S_2)$ ）。

（此处的图为，Figure 2.4，Overlaying two subdivisions）

这个overlay，可以看做是S1的edges被S2的edges所切割，而S1中的大部分edge其实可以在新生成的doubly-connected edge list中来复用，仅那些被S2的edges所真正切割到的S1的edges，才需要在新生成的$O(S_1, S_2)$ 被更新。

为了计算overlay结果，要把两个doubly-connected edge list（S1和S2），拷贝到一个新的doubly-connected edge list中去。拷贝的结果当然不是一个合法的doubly-connected edge list，因为它不能代表一个平面的细分（subdivision）。overlay算法的任务就是，把这个不合法的doubly-connected edge list，通过计算两个network edges之间的交点，并把两个doubly-connected edge list的部分区域连接起来，从而最终得到一个合法的doubly-connected edge list，即结果$O(S_1, S_2)$ 。

下面首先讨论的是，最终的overlay结果$O(S_1, S_2)$ 中的vertex和half-edge records，是如何被计算出来的。（关于新生成的face record，因为比较复杂，稍后再讨论）

计算$O(S_1, S_2)$ 的办法，利用了前面提到的计算line segments交点的plane sweep algorithm。算法操作的对象是，包含了S1和S2中所有line segment的线段集合（一个新的线段集合拷贝）。

在plane sweep algorithm中，需要两个数据结构，分别是event point的集合Q，以及status structure J。

Q是用来存储event point的（BST实现），而J是用来存储和sweep line相交的那些line segment的集合的（是有序的，在plane上是从左向右依次和sweep line相交的，也是BST实现的）。

除了这个两个数据结构之外，还需要维护一个doubly-connected edge list的数据结构$D$，它的初始值是从S1和S2拷贝而来，也就是说它的初始值是包含了S1和S2的所有line segment的集合。而随着sweep line的向下移动，$D$会随之而更新，最终变成一个合理的doubly-connected edge list。

如果一个$D$中的edge和sweep line相交而要被放入status J中时，我们需要用指针把放入J中的edge和它来自于$D$中的哪个half-edge record联系起来，这样当遇到一个intersection point时，我们就能够方便地找到$D$中的哪一个half-edge record（或哪一部分）需要被更新和调整。

在sweep line向下扫描的过程中，sweep line上面是已经计算好的最终overlay结果的一部分，是不再变化的。



当遇到一个event point时候的处理：当event point是来自原先同一个subdivision的edges时，那么这个event point是可以被复用的；但如果event point是来自原先两个subdivision的不同edges时，那么我们就需要更新数据结构$D$，更新（加入或删除）某些edges，以便把两个subdivision通过新的intersection point而连接起来。



这里通过举例，说明了一个subdivision中的一条edge，是如何和另一个subdivision中的其他几个edge相交，然后做处理的。这个过程比较tedious，但是不难（difficult）

（图为Figure 2.5，图位于第35页，页码是44）

这里主要结合图形，说明了在新生成了两条edge（对应的是两队half-edge pair）之后，如何调整它们以及周围的edge的Next()和Prev()指针。

值得说明的是，这个例子中，一条edge恰好经过的是另一个subdivision的一个vertex，因此，在调整新产生的edge的prev和next的时候，是按照clockwise的转向，找到第一个相邻的edge作为Next()指针所指向的edge，而按照anti-clockwise的转向，找到其第一个相邻的edge作为Prev()指针所指向的edge。这个可以结合图的说明清晰容易地看到。



除了更新生成的新half-edge pair，还要找到$O(S_1, S_2)$ 中每个face $f$ 的 $OuterComponent(f)$ （指向一个表示outer boundary的half-edge）和$InnerComponent(f)$ （指向一个或几个half-edge的指针，表示一个或多个洞）。还要给每个edge的$IncidentFace()$设定合理的指针指向face record。最后，每个$face$还要用原先两个subdivision中包含这个$face$的face name来给它做label。



如何判断一个half-edges组成的boundary是outer boundary，还是表示hole的inner boundary？

选定leftmost的vertex（in case of ties，choose lowest of leftmost），因为沿着half-edge的走向是clockwise的就是outer boundary，所以计算这个vertex前后两个相邻的（有序的）half-edge的夹角，如果是小于$90°$，那么就是outer vertex的half-edge，如果是大于$90°$，就是inner boundary的half-edge。这个特性仅适用于leftmost（或lowest of leftmost if ties）的vertex。

（这里的图位于第36页，页码是45）



通过一个图的例子，说明了如何确定一个face $f$是由一个或几个cycle组成的。如果是多个cycles组成，一般有几个洞的cycle（half-edges是顺时针的）和一个outer cycle（for outer boundary）组成，而且一个洞要通过对应的数据结构（比如class上的成员变量）连接到另一个洞或outer boundary上，这样才能表明这些cycles组成的是同一个face $f$。



> Lemma 2.5 Each connected component of the graph $G$ corresponds exactly to the set of cycles incident to one face.

关于这个lemma的证明，没看懂。

总之，他想说明的是，一个face上的洞，是和这同一个face上的其他洞相连的，或者是和这个face对应的$OuterComponent(f)$ 相连接，而这些相连接的洞（实际上就是$InnerComponent(f)$ ？）和$OuterComponent(f)$ 就组成了这个face $f$。



如果构建graph $G$？

构建graph $G$，实际上是把这些$InnerComponent(f)$（即洞）和$OuterComponent(f)$ 直接合理地用书中所谓的“arc”连接起来。

对于每个表示洞的cycle的leftmost的vertex $v$，如果有一条half-edge $e$，是这个vertex $v$ 左边第一个邻近的half-edge，那么就在这两个node直接就用一条arc连接起来。

为了快速（有效）地找到这些node，每个half-edge的record上有指针指向这些node，表示这些node在这个graph $G$ 的哪个cycle上。

而找到一条vertex左边的、相邻的第一个half-edge，是在plane sweep algorithm中sweep line向下扫描时得出的，而且这个相邻的左边第一个half-edge，是位于另外一个cycle上的。

（这里用来说明的图，位于第37页，页码是46）



最后一件事情是，在overlay结果 $O(S_1, S_2)$ 中，每个face $f$ 都要找到它原先分别在 $S_1$ 和 $S_2$ 中的label。

假如一个vertex $v$ 是来自 $S_1$ 的一条edge $e_1$ 和 $S_2$ 的一条edge $e_2$ 的相交得到新的点，那么可以从edge $e_1$ 和 $e_2$ 的 $IncidentFace(f)$ 得到各自在原先 $S_1$ 和 $S_2$ 中的label name。

但如果vertex $v$ 本身就是来自 $S_1$ 的一个点（或者$S_2$ 的一个点），那么我们首先能得知它来自 $S_1$ 的哪个face（因为能从 $v$ 对应的half-edge的 $IncidentFace(f)$ 上得到。其次，就需要找到在 $S_2$ 上的哪个face包含这个vertex $v$。

书中在此处没有展开解释，只说明了仍然使用本章介绍共的plane sweep algorithm就可以找到，而且也不用再次调用这个plane sweep algorithm，而是在原先扫描的过程中，就可以找到。





### 2.7 References

- [库拉托夫斯基定理](https://baike.baidu.com/item/%E5%BA%93%E6%8B%89%E6%89%98%E5%A4%AB%E6%96%AF%E5%9F%BA%E5%AE%9A%E7%90%86/2748841?fr=aladdin)
- [可平面图（planar graph）](https://baike.baidu.com/item/%E5%8F%AF%E5%B9%B3%E9%9D%A2%E5%9B%BE/19138688?fr=aladdin)
- [Geometry Symbol Names](https://www.rapidtables.com/math/symbols/Geometry_Symbols.html)
- 

