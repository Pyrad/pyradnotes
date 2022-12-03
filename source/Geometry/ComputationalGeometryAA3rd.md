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





## Usage

thought experiment

an elastic rubber band 橡皮筋

direct the line through *p* and *q*

to this end 为了这个目的（**formal** **:** as a way of dealing with or doing something）

rule out 排除，除去

windy river 弯曲的河流（不是多风的河流）

coinciding point 共点

in a sense 某种意义上



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



## Names

- output-sensitive algorithm





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

Brute-forced algorithm的时间复杂度是O(nlogn)，但实际情况，有可能只有很少的一些线段相交，并不必计算每个线段和其他线段的交点。

即，我们希望算法的复杂度依赖的不仅是输入点的个数，而且也是输出的交点的个数，这样的算法叫做***output-sensitive algorithm***。



可以利用的观察几何结果是：靠的比较近的线段是可能有交点的候选计算对象，而相离较远的线段是不需要计算交点的。

所以思路是，把所有线段向y轴做投影，得到投影线段有重叠的那些线段，就是需要计算交点的候选线段。

为什么没有投影重叠的线段就一定没有交点？这可以通过反证法得出，如果没有投影重叠的线段有交点，那么这个交点的y坐标值一定是介于两个线段的4个端点的y值之间，而这又说明这两条线段是有投影重叠的，因此矛盾，从而的证。



使用到的技术叫做：***plane sweep algorithm***。

***sweep line***：一条水平无限长的假想虚线

***status***：***sweep line***的“状态”指的是和它当前相交的**线段的集合**（**segments**）

***event point***：***sweep line***沿着垂直方向从上向下移动，但不是连续移动的，而是离散的，移动到的这些位置的点，叫做***event point***。这些***event point***，一部分是每条线段的upper end point（y值较大的点）和lower end point（y值较小的点），另一部分是线段的交点。

只有当***sweep line***移动到这些***event point***上的时候，算法才做相应的计算或调整，即更新***sweep line***的***status***，并计算（或测试）交点。

如果***event point***是一条线段的upper point，那么这条线段就是和***sweep line***相交，并且应该加入到***status***里面，同时要计算这条segment和***status***里面其他segments的交点（*后面会提到，只计算当前线段相邻的左右两条segments的交点，而不是计算和status里面所有线段的交点*），而且这个交点要放入到event point集合的适当位置，以便sweep line依次向下扫描时可以遍历到它。

如果***event point***是一条线段的lower point，那么这条线段就和***sweep line***不再相交（相离），就应该从status里面删除。

如果***event point***是两条线段的intersection point（这个intersection point是前面计算得到加入进来的），那么在该点之后，相邻的adjacent neighbor就会发生改变，所以就要测试（计算）这两条segments和它们各自左右相邻的segment的交点。



> Lemma 2.1 Let *si* and *sj* be two non-horizontal segments whose interiors intersect in a single point *p*, and assume there is no third segment passing through *p*. Then there is an event point above *p* where *si* and *sj* become adjacent and are tested for intersection.

因为根据前面遇到的event point是一条线段的upper point时的操作（计算adjacent segment之间的intersection point），这个引理主要想说明，如果两条都不是水平（也不共线）的线段，如果有交点，那么在这个交点的上方，一定有一个event point，在那个event point的时候，这两条线段变成adjacent，并且会被检查（计算）是否有交点。

这里暂时忽略了三种特殊情况：两条线段可能共线（重合），可能有水平的情况，以及有第三天线段穿过交点。



所以，简要叙述，***line sweeping algorithm***的答题思路如下

> Let’s briefly recap the overall approach. We imagine moving a horizontal sweep line ℓ downwards over the plane. The sweep line halts at certain event points; in our case these are the endpoints of the segments, which we know beforehand, and the intersection points, which are computed on the fly.
>
> While the sweep line moves we maintain the ordered sequence of segments intersected by it. When the sweep line halts at an event point the sequence of segments changes and, depending on the type of event point, we have to take several actions to update the status and detect intersections.

假设有一条水平扫描线，从上而下移动，每次移动到一个特殊的点（event point）。这样的event point有两种，一种是每条线段的upper point（end point），另一种是某两条线段的交点（intersection point）。前一种在计算之前就已知，而后一种是在扫描线移动过程中计算得出。

当扫描线移动时，维护一个有序的线段列表，列表中的每个线段是和扫描线相交的。当扫描线移动到下一个event point的时候，更新线段列表使其保持有序，同时根据event point的类型，更新状态（它是和扫描线相交的线段集合，每次操作有可能添加或删除一条线段）并检查某两条线段是否有交点。



sweep line遇到三种不同event point时对应的操作

- 如果event point是一条线段的upper point（end point），就要检查这个upper point所在的线段，和它左右两个相邻的线段是否有交点，如果有交点，那么这个交点就是一个新的event point。

  因为sweep line上方的event point都是已知的或已经计算过的，所以关注的是sweep line下方的交点。

- 如果event point是某两条线段的交点（intersection point），那么这两条线段在所维护的有序线段列表里面的位置就要交换，同时因为位置变化，它们各自相邻的线段也发生了变化（但只变化了一个，因为另一个仍然是它们自己中的一个），所以也要检查它们和各自新邻近的线段之间是否有交点，如果有并且是之前没有的event point，那么就有发现了一个或两个新的event point。

- 如果event point是一条线段的lower point（end point），那么这条线段原先左右两条线段就变成了直接相邻的线段，就要检查（计算）这两条线段是否有交点，同样的，如果有，就是新的event point。





