# A Tour of Go (Notes)

Notes for A Tour of Go ([link is here](https://go.dev/tour/welcome/1))

## 章节信息（欢迎使用Go[指南](https://tour.go-zh.org/list)）

### 前言

- [Chapter 1 Welcome](https://tour.go-zh.org/welcome)

  学习使用本指南：包括如何在不同的课程间切换以及运行代码。

- Exercise解答参考
  - [基础部分](https://www.jeddd.com/article/a-tour-of-go-exercises-basics.html)
  - [方法和接口部分](https://www.jeddd.com/article/a-tour-of-go-exercises-methods.html)
  - [并发部分](https://www.jeddd.com/article/a-tour-of-go-exercises-concurrency.html)

### 基础

- [Chapter 2 Packages, variables and functions](https://go.dev/tour/basics/1)

  Go 程序的基本结构。

- [Chapter 3 Flow control statements: for、if、else、switch and defer](https://tour.go-zh.org/flowcontrol)

  学习如何使用条件、循环、分支和推迟语句来控制代码的流程。

- [Chapter 4 More types: struct、slice and maps](https://tour.go-zh.org/moretypes)

  学习如何基于现有类型定义新的类型：本节课涵盖了结构体、数组、切片和映射。

### 方法和接口

学习如何为类型定义方法；如何定义接口；以及如何将所有内容贯通起来。

- [Chapter 5 Methods and interfaces](https://tour.go-zh.org/methods)

  本节课包含了方法和接口，可以用这种构造来定义对象及其行为。

### Generics

- [Chapter 6 Generics](https://go.dev/tour/generics/1)

### 并发

作为语言的核心部分，Go 提供了并发的特性。

这一部分概览了 goroutine 和 channel，以及如何使用它们来实现不同的并发模式。

- [Chapter 7 并发](https://tour.go-zh.org/concurrency)

Go 将并发结构作为核心语言的一部分提供。本节课程通过一些示例介绍并展示了它们的用法。



## Chapter 1 Welcome

### 本地网页版本的tour安装

离线版本使用如下命令安装

```powershell
go install golang.org/x/website/tour@latest
```

它会在`$GOPATH`这个环境变量所代表的目录中生成一个名为`tour`的binary，启动它即可打开本地网页版本的tour guide。



## Chapter 2 Packages, variables and functions

### 包 （Packages）

- Go程序都是由包（packages）组成的，通过关键字`import`导入包

- 包名按照惯例是导入路径（import path）的最后一个元素，比如`import math/rand`导入了`math/rand`这个包，那么这个包中的源代码就是以`package rand`语句开始的

- 程序入口是`main`这个包

- 多个包可以使用分组（factored）形式的导入语句，也可以简单地使用多个`import`语句导入

  ```go
  // 分组导入
  import (
      "fmt"
      "math"
  )
  
  // 也可以写成
  import("fmt"; "math")
  
  // 常规导入
  import "fmt"
  import "math"
  ```

  

- 导入一个包时，只能使用其中已经导出的名字（变量/函数），而所谓导出，指包中变量/函数名如果是大写字母开头，那么它是导出的，否则就不是导出的。

### 函数（functions）

- 以关键字`func`开头，然后跟上函数名，再跟上函数列表（用圆括号括起来）

- 返回值的类型在参数列表的后面

- 可有或无参数，注意go特殊的是参数类型在参数名称的后面

- 参数列表中，如果有两个或以上的参数类型相同时，可以只写最后一个形参的类型，前面其他的可省略

- 可以返回任意数量的返回值，同样的，参数类型列表也必须是同样的数目（并且用括号括起来）

- 返回值可以被命名，并和返回类型放在一起，这样`return`语句就可以省略后面的参数

  ```go
  // 函数
  func add(x int, y int) int {
      return x + y
  }
  
  // 省略连续相同类型形参的类型关键字
  func add(x, y int) int {
  	return x + y
  }
  
  // 返回两个返回值
  func swap(x, y string) (string, string) {
  	return y, x
  }
  
  // 命名返回值（return 省略后面的参数)
  func split(sum int) (x, y int) {
  	x = sum * 4 / 9
  	y = sum - x
  	return
  }
  ```




### 变量（variable）

- `var`用来声明一个变量或者一个变量列表，同样的，类型放在最后面

  - `var i int`（一般地声明）
  - `var i = 3`（如果直接在声明的时候初始化，其实还可以省略类型）

- 变量声明可以包含初始值，每个变量对应一个

- `:=`符号可以用在函数中（函数外面不可以），用来代替`var`声明，叫做简洁赋值语句（既赋值又声明）

- 基本类型

  - `bool`
  - `string`
  - `int int8 int16 in32 int64 uint unit8 uint16 uint32 uint64 uintptr`
  - `byte`（`uint8`的别称）
  - `rune`（`int32`的别称）
  - `float32 float64`
  - `complex64 complex128`
  - 像导入语句，基本类型也可以“分组”成一个语法块

- 没有明确初始值的变量声明会被赋予它们各自类型的**零值**

  - 数值类型的零值：0
  - 布尔类型为 `false`
  - 字符串为 `""`（空字符串）

- 类型转换

  - 表达式用`T(v)`把值`v`转换为类型`T`
  - 可以使用简洁形式`k := T(v)`，该表达式把`v`这个变量转换为类型`T`
  - go中的类型转换必须是显示的转换

- 变量的类型可以由右值推导出来

  - 如果右值是数值常量（即没有指定类型），你们新变量的类型就取决于常量的精度

- 常量

  - 声明和变量类似，但使用`const`关键字，当然可以声明在包里或函数里
  - 常量可以是：字符、字符串、布尔值或数值
  - 常量不能使用简洁赋值语句`:=`
  - 数值常量是高精度的**值**

- 

  ```go
  // 变量（列表）声明，实际上被赋予了各自的零值）
  var c, python, java bool
  
  // 变量声明对应初始值
  var i, j int = 1, 2
  
  // 简洁赋值
  k := 3
  c, python, java := true, false, "no!"
  
  // 分组的变量声明
  var (
     	ToBe   bool       = false
  	MaxInt uint64     = 1<<64 - 1
  	z      complex128 = cmplx.Sqrt(-5 + 12i)
  )
  
  // 类型转换
  var i int = 42
  var f float64 = float64(i)
  var u uint = uint(f)
  // 类型转换的简洁形式
  i := 42
  f := float64(i)
  u := uint(f)
  
  // 类型推导
  var i int
  j := i // j 也是一个 int
  // 根据数值常量的精度推导类型
  i := 42           // int
  f := 3.142        // float64
  g := 0.867 + 0.5i // complex128
  
  // 常量
  const World = "myWorld"
  const Truth = true
  ```




> Start 2022-May-9 20:41:35 Raycom 7F
>
> End 2022-May-9 21:46:28 Raycom 7F



## Chapter 3 Flow control statements: for, if, else, switch and defer

### for

- Go只有`for`这一种循环

- `for`循环由三部分组成，用分号隔开，但这三个部分不用小括号括起来

  - 初始化语句（类似C/C++中，可以省略）
  - 条件表达式
  - 后置语句（类似C/C++中，可以省略）

- 当`for`循环省略了初始化语句和后置语句，这时候就可以去掉分号，相当于Go中的`while`循环

- xxx

  ```go
  // 基本的for循环
  sum := 0
  for i := 0; i < 10; i++ {
  	sum += i
  }
  
  // 省略初始化语句和后置语句的for循环
  sum := 1
  for ; sum < 1000; {
  	sum += sum
  }
  
  // 省略初始化语句和后置语句的for循环，可以去掉分号
  sum := 1
  for sum < 1000 {
  	sum += sum
  }
  
  // 无限循环（死循环）
  for {
  }
  ```



> Started 2022-May-10 23:25
>
> End 2022-May-10 23:29



### if

- 和`for`循环类似，`if`后面的表达式不用小括号，但是更后面的执行语句块必须用大括号

- `if`语句可以在条件表达式前加一个简单语句（和表达式语句用分号`;`隔开），里面声明的变量仅在`if`语句块内有效

  ```go
  // 基本的if语句
  if x < 0 {
  	return sqrt(-x) + "i"
  } else {
      return x
  }
  
  // if表达式前面的简单语句，
  if v := math.Pow(x, n); v < lim {
  	return v
  }
  ```



### switch

- `switch`语句无需再每个case语句后面加上`break`，因为Go会自动提供`break`，以便自动结束分支执行

- `switch`的后面的变量同样不用小括号

- `switch`的后面的变量前面可以加入一个简单的语句，作用域仅限于该`switch`语句

- `switch`语句的case不仅限于常量或整数，其他类型也可以

- `switch`后面也可以不加条件，此时等价于`switch true`

  ```go
  // 基本的switch语句（例子1）
  switch os := runtime.GOOS; os {
  	case "darwin":
  		fmt.Println("OS X.")
  	case "linux":
  		fmt.Println("Linux.")
  	default:
  		// freebsd, openbsd,
  		// plan9, windows...
  		fmt.Printf("%s.\n", os)
  }
  
  // 基本的switch语句（例子2）
  today := time.Now().Weekday()
  	switch time.Saturday {
  	case today + 0:
  		fmt.Println("Today.")
  	case today + 1:
  		fmt.Println("Tomorrow.")
  	case today + 2:
  		fmt.Println("In two days.")
  	default:
  		fmt.Println("Too far away.")
  }
  ```

  

### defer

- `defer`后面**必须**跟的是函数，不能是简单的语句

- `defer`后面的函数会在`defer`所在的函数返回之后再执行，但是其参数会立即求值

- `defer`的函数会被依次压入堆栈，当外层函数返回后，`defere`的函数会按**后进先出**的顺序调用

  ```go
  // 最后打印出来的顺序是Hello, world!
  func print() {
      defer fmt.Println("world!")
      fmt.Println("Hello, ")
  }
  
  // defer的函数按照后进先出的顺序，在外层函数返回后被依次调用
  // 下面的打印结果是（->表示另起一行）:
  // counting->done->9->8->7->6->5->4->3->2->1->0
  
  func print() {
      fmt.Println("counting")
  	for i := 0; i < 10; i++ {
  		defer fmt.Println(i)
  	}
  	fmt.Println("done")
  }
  ```

  

## Chapter 4 More types: structs, slices, and maps

### Pointers（指针）

- Go是有指针的，和C一样，它保存值的内存地址

- `*T`是指向`T`类型值的指针，对应的零值是nil

- `&`操作符生成一个指向其操作数的指针

- `*`操作符表示指针的底层值（解引用）

- 和C不同，Go**没有指针的运算**

  ```go
  // 声明一个指针
  var p *int
  
  // &操作符
  i := 42
  p = &i
  
  // *操作符（解引用）
  fmt.Println(*p) // 读取p指针所对应的值
  *p = 21         // 通过p指针设置指向的值
  ```



### Struct（结构）

- 一个结构体就是一组字段（A `struct` is a collection of fields）

- 定义结构体，以关键字`type`开头，跟上结构体名字，再跟上关键字`struct`，后面是大括号括起来的一组字段（field）

- 结构体中的字段用点号`.`访问

- 注意，如果要在函数体外面初始化结构体，只能用以下办法

  - 一次性定义并全部赋值
  - 先声明变量，然后在某个函数内部进行赋值

- 如果有一个结构体指针（比如p指向一个结构体对象），那么字段也通过点号访问，

  - (*p).X ：完全的写法
  - p.X：简洁的写法（语言允许使用隐式间接引用）

- 分配结构体时，通过直接列出字段的值来分配一个结构体

  - `var v = Vertext{1, 2}`
  - `var v Vertex = Vertext{1, 2}`
  - `v := Vertex{1, 2}`
  - `var v Vertex`
    `v = Vertex{1, 2}`

- 可以只列出一部分字段的值，另一部分字段用字段名代替，表示使用其类型对应的零值
  -   `v := Vertex{X, 1}`  X字段的值默认为0(结构体定义见如下)
  -   `v := Vertex{}` X和Y的值默认为0(结构体定义见如下)

- 可以通过`&`前缀来直接返回一个结构体指针

  - `p := &Vertex{3, 4}`

  ```go
  // 结构体定义
  type Vertex struct {
  	X int
  	Y int
  }
  // 也可以如下，把相同类型的字段写到一起
  type Vertex struct {
  	X, Y int
  }
  
  // 定义结构体的文法几种办法
  var v Vertex = Vertex{1, 2}
  // 或者
  var v = Vertex{1, 2}
  // 或者
  v := Vertex{1, 2}
  // 先声明后赋值
  var v Vertex
  v = Vertex{1, 2}
  
  
  // 定义结构体的对象，并用点号访问
  v := Vertex{1, 2}
  v.X = 4
  fmt.Println(v.X)
  
  // 结构体指针访问字段
  p := &v
  p.X = 1e9
  
  // 
  var (
  	v1 = Vertex{1, 2}  // 创建一个 Vertex 类型的结构体
  	v2 = Vertex{X: 1}  // Y:0 被隐式地赋予
  	v3 = Vertex{}      // X:0 Y:0
  	p  = &Vertex{1, 2} // 创建一个 *Vertex 类型的结构体（指针）
  )
  ```




### Array（数组）

- 类型`[n]T`表示一个有n个T类型值的数组

  - `var a [10]int`

- 和C中一样，数组声明了之后，其长度不能改变

- 可以用花括号列出数组的初始值

  - `primes := [6]int{2, 3, 5, 7, 11, 13}`

  ```go
  // 数组定义
  var a [2]string
  a[0] = "Hello"
  a[1] = "World"
  
  // 数组定义2
  primes := [6]int{2, 3, 5, 7, 11, 13}
  fmt.Println(primes)
  ```

  

### Slice（切片）

- 切片给数组提供动态大小的、灵活的视角（dynamically-sized, flexible view into elements of an array）

- `[]T`表示一个元素类型为`T`的切片（slice），比如`var s []int`就声明了一个空的切片

- 数组名称后面加上方括号和上下界，可以创建一个对应的切片，比如`arr[low : high]`

- 上下界对应的是一个左闭右开的区间，包含第一个元素，但排除最后一个元素。

- 也可以直接使用简洁写法创建切片：`s := arr[0:7]`

- 切片不存储数据，修改切片对应的元素会修改其对应的底层数组中的元素，其他共享这个底层数组的切片也会看到相应的修改

- 切片常量（slice literal）的定义：`[n]T{value list}`

  - `n`是切片常量的长度
    - 这个值可以省略，省略的时候，切片的长度就由后面元素列表的长度决定
    - 如果`n`这个值没有省略，但比后面元素列表的长度大，那么切片的长度仍然是`n`，但不足的元素用相应类型的零值填充
    - 如果`n`这个值没有省略，但比后面元素列表的长度小，就会报错
  - `T`是切片中元素的类型
  - `value list`是元素列表
  - 例如：`[3]bool{true, true, false}`，`[]booll{true, true, false}`

- 切片的上界或下界是可以省略的

  - 切片下界默认为`0`
  - 切片上界默认为该切片的长度
  - 假如有数组`var arr [10]int`，以下切片是相同的
    - `a[0:10]`，`a[:10]`，`a[0:]`，`a[:]`

- 关于切片的**上界和下界的取值范围问题**

  - 下界：这个值必须是小于**切片的长度**
  - 上界：这个值可以一直大于切片的长度，但要**小于等于底层数组的长度减去切片的长度**

- 切片有**长度**和**容量**

  - **长度**：切片所包含的元素个数，表达式`len(s)`，`s`是一个切片
  - **容量**：从该切片的第一个元素开始，到其底层数组元素末尾的个数，`cap(s)`，`s`是一个切片

- 切片的**零值**是`nil`，它的长度和容量都是`0`，而且没有底层数组

- 使用`make`函数可以创建一个元素为零值的数组，并且返回一个引用它的切片

  - `a = make([]int, 5)` 只指定长度（5）
  - `b = make([]int, 0, 5)`同时指定长度（0）和容量（5）

- 切片的类型可以是任意的，甚至包含其他切片

  ```go
  // 切片的切片
  board := [][]string{
  	[]string{"_", "_", "_"},
  	[]string{"_", "_", "_"},
  	[]string{"_", "_", "_"},
  }
  ```

- `append`函数可以给切片追加元素

  - 函数原型`func append(s []T, vs ...T) []T`
  - 这里`s`是一个类型为`T`的切片，其余类型为`T`的值就会追加到该切片末尾
  - 返回的结果是包含原始切片所有元素（切片长度个数）加上新元素的切片（即引用了一个新数组）
  - 如果`s`引用的底层数组太小，Go会分配更大的数组，返回的切片引用这个新的大数组

- `for ... range`可以用来遍历**切片**或**映射**

  - 用`for`循环配合`range`遍历，每次迭代返回两个值，**当前元素的下标（索引）**和**当前元素的副本（值）**

  - 下标或值可以用下划线`_`代替而忽略

  - 可以只写一个变量，这时候代表的就只是索引了

  - ```go
    var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
    for i, v := range pow {
    	fmt.Printf("2**%d = %d\n", i, v)
    }
    ```

- 可以阅读文章，[Go 切片：用法和本质](https://blog.go-zh.org/go-slices-usage-and-internals)

  ```go
  // 切片的定义
  primes := [6]int{2, 3, 5, 7, 11, 13}
  var s []int = primes[1:4]
  fmt.Println(s) // [3, 5, 7]
  var t []int64
  fmt.Println(t)  // []
  k := primes[1 : 5]
  fmt.Println(k)  // [3, 5, 7, 11]
  
  // 修改切片导致底层数组元素变化
  names := [4]string{"John","Paul","George","Ringo",}
  a := names[0:2] // [John Paul]
  b := names[1:3] // [Paul George]
  b[0] = "XXX"
  fmt.Println(a) // [XXX George]
  fmt.Println(b) // [John XXX]
  fmt.Println(names) // [John XXX George Ringo]
  
  
  // Slice literal
  q := []int{2, 3, 5, 7, 11, 13}
  fmt.Println(q) // [2 3 5 7 11 13]
  k := [3]int32{1, 9}
  fmt.Println(k) // [1 9 0]
  r := []bool{true, false, true, true, false, true}
  fmt.Println(r) // [true false true true false true]
  s := []struct {
  	i int //注意，这里要新起一行，否则报错
  	b bool
  }{
  	{2, true},
  	{3, false},
  	{5, true},
  	{7, true},
  	{11, false},
  	{13, true},
  }
  fmt.Println(s) // [{2 true} {3 false} {5 true} {7 true} {11 false} {13 true}]
  
  // 切片的长度和容量，以及变化
  s := []int{2, 3, 5, 7, 11, 13} // s目前是一个切片常量，slice literal
  // 1. 截取切片使其长度为 0
  s = s[:0] // s为[]，长度为0，但容量为6，因为s是切片，指向的仍然是底层的数组
  // 2. 拓展其长度
  s = s[:4] 
  // 现在s为[2, 3, 5, 7]，长度为4，容量为6，
  // 因为s这个切片的第一个元素是底层数组的第一个元素，而底层数组的最后一个元素是13，所以容量为6
  // 3. 舍弃前两个值
  s = s[2:]
  // 现在s为[5, 7]，长度为2，容量为4
  // 长度为2容易理解，因为它是在上次切片[2,3,5,7]的基础上从第2个元素开始取值，直到原先切片的长度为止
  // 容量变成4是因为s这个切片的第一个元素现在是底层元数组的第2个元素（index 0 based）
  // 而它依然指向底层数组[2, 3, 5, 7, 11, 13]，而改底层数组的最后一个元素是13，所以容量变成了4
  // 容量的概念见前面所述
  // 4. 再扩展
  s = s[:4]
  // 原先的切片是[5, 7]，其长度是2，但容量是4
  // 所以":4"表示从第0个元素开始取，直到第4个元素为止（不包含）
  // 但原先的切片不是[5, 7]吗？怎么会有第4个元素？
  // 这是因为原先的切片仍然指向底层数组[2, 3, 5, 7, 11, 13]，只是从元素5开始，所以它依然可以取到元素11,13
  
  // append追加元素到切片
  var s []int // len=0 cap=0 []
  // 添加一个空切片
  s = append(s, 0) // len=1 cap=1 [0]
  // 这个切片会按需增长
  s = append(s, 1) // len=2 cap=2 [0 1]
  // 可以一次性添加多个元素
  s = append(s, 2, 3, 4) // len=5 cap=6 [0 1 2 3 4]
  
  k := []int{0,1,2,3,4} // [0,1,2,3,4]
  s0 := k[:3] // s0现在是切片[0,1,2]，长度是3，容量是5
  s0 = append(s0, 77, 88, 99) // 现在s0这个切片是[0,1,2,77,88,99]，它实际上指向了一个新的底层数组
  fmt.Printf("len=%d cap=%d %v\n", len(s0), cap(s0), s0) // len=6 cap=10
  s1 := s0[:cap(s0)] // 如果我们取到这个新底层数组的最后一个元素，就得到[0 1 2 77 88 99 0 0 0 0]
  // k这个切片还是引用原先的底层数组
  fmt.Printf("len=%d cap=%d %v\n", len(k), cap(k), k) // len=5 cap=5
  
  
  // for ... range 遍历切片/映射
  var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}
  for i, v := range pow {
  	fmt.Printf("2**%d = %d\n", i, v)
  }
  // 忽略下标或值
  for _, v := range pow {
  	fmt.Printf("value is %d\n", v)
  }
  for i, _ := range pow {
  	fmt.Printf("index is %d\n", i)
  }
  // 只有一个值时就是索引
  for i := range pow {
  	fmt.Printf("index is %d\n", i)
  }
  ```

  

### Map（映射）

- 就是键值对

- 映射的零值是`nil`，它无键无值

- 声明一个映射：`var <name> map[keyType]ValueType`

  - 比如`var m map[int]string`

- 可以用`make`函数创建映射

  - `make(map[keyType]ValueType)`

- 映射文法（定义）

  - 类似结构体，需要写键名，键和值直接用冒号`:`隔开

  - 如果top-level的类型只是一个类型名，可以在文法元素中省略，比如这里的Vertex

  ```go
    type Vertex struct {Lat, Long float64}
    var m = map[string]Vertex{
    	"Bell Labs": Vertex{40.68433, -74.39967,},
    	"Google": Vertex{37.42202, -122.08408,},
    }
    // 或者可以写成
    var m map[string]Vertex = map[string]Vertex{
    	"Bell Labs": Vertex{40.68433, -74.39967,},
    	"Google": Vertex{37.42202, -122.08408,},
    }
    // 或者可以写成
    var m = map[string]Vertex{
    	"Bell Labs": {40.68433, -74.39967,},
    	"Google": {37.42202, -122.08408,},
    }
  ```
  
- 映射元素的**增删查改**和**遍历**

  - **插入**元素，或者也可以修改元素：`m[key] = elem`
  
  - **获取**元素：`elem = m[key]`
  
  - **删除**元素：`delete(m, key)`
  
  - **检查键**是否存在（通过双赋值）：`elem, ok = m[key]`
    如果`key`在`m`中，`ok`为`true`，否则`ok`为`false`
    如果`key`不在`m`中，那么`elem`为该映射元素类型的零值
    如果`elem`或`ok`还未声明，那么可以使用短变量声明：`elem, ok := m[key]`
    
  - **遍历**可以使用`range`
  
    ```go
    mymap := make(map[int]string)
    for mykey, myval := range mymap {
    	fmt.Printf("%v: %v\n", mykey, myval)
    }
    ```
  
   ```go
  type Vertex struct {
  	Lat, Long float64
  }
  var m map[string]Vertex
  m = make(map[string]Vertex)
  m["Bell Labs"] = Vertex{40.68433, -74.39967,}
  fmt.Println(m["Bell Labs"])
  for mykey, myval := range m {
  	fmt.Printf("%v: %v\n", mykey, myval)
  }
  
   ```
  
  


### Function values（函数值）

- 函数也是值。它们可以像其它值一样传递。（有点像C++中的functor，或者函数指针）

- 函数值可以用作函数的参数或返回值。

  - 函数当做参数传递时，写的办法如下：
    `ArgName func(Arg0Type, Arg1Type, ...) returnType`

- 在这里也可以看到，函数里面也可以定义函数

- Go 函数可以是一个闭包。

  - 闭包是一个函数值，它引用了其函数体之外的变量。
  - 该函数可以访问并赋予其引用的变量的值，换句话说，该函数被这些变量“绑定”在一起。
  - 比如下面的函数`adder`，它返回的不是一个具体的值，而是一个闭包，它既引用了外部的变量，又操作该闭包里面的变量，而且各闭包里面的变量是属于各自的闭包的（不共享）

- xxx

- xxx

- xxx

  ```go
  // -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
  func compute(fn func(float64, float64) float64) float64 {
  	return fn(3, 4)
  }
  
  func compute2(fn func(float64, float64) float64) float64 {
  	myc := func(x, y float64) float64 { return x + y }
  	return fn(1, 2) + myc(3, 4)
  }
  
  func main() {
  	hypot := func(x, y float64) float64 {
  		return math.Sqrt(x*x + y*y)
  	}
  	fmt.Println(hypot(5, 12))
  
  	fmt.Println(compute(hypot))
  	fmt.Println(compute(math.Pow))
      
     	fmt.Println(compute2(hypot))
  }
  
  // -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
  
  func adder() func(int) int {
  	sum := 0
  	return func(x int) int {
  		sum += x
  		return sum
  	}
  }
  
  func main() {
  	pos, neg := adder(), adder()
  	for i := 0; i < 10; i++ {
  		fmt.Println(
  			pos(i),
  			neg(-2*i),
  		)
  	}
  }
  // Results
  // 0 0
  // 1 -2
  // 3 -6
  // 6 -12
  // 10 -20
  // 15 -30
  // 21 -42
  // 28 -56
  // 36 -72
  // 45 -90
  ```

  



## Chapter 5 Methods and interfaces

### Methods（方法）

- Go没有类，不能直接在`struct`里面定义类的方法，但还是可以定义结构体类型的方法

- 方法就是一类带特殊的 **接收者（receiver）** 参数的函数

- 基本可以理解为在`struct`外面为其定义方法

- 方法接收者在函数的参数列表里，位于`func`关键字和方法名之间

  - `func (v T) name(...) rType`
  - 一般的值接收者在方法内部不会改变原有的接收者（因为值传递），但指针接收者可以改变（见下）

- 下面的例子表明`Abs`有一个名字叫`v`，类型为`Vertex`的接收者，有名字`v`是因为在方法里面要使用这个变量

  ```go
  type Vertex struct {X, Y float64}
  // v Vertex是一个receiver，相当于形参，相当于给Vertex这个结构加上了一个方法
  func (v Vertex) Abs() float64 {
  	return math.Sqrt(v.X*v.X + v.Y*v.Y)
  }
  
  func main() {
  	v := Vertex{3, 4}
  	fmt.Println(v.Abs())
      k := Vertex{5, 6}
  	fmt.Println(k.Abs())
  }
  ```

- 类似地，可以给非结构体定义方法，但不能给内建类型声明方法

- 声明了方法的接收者类型必须在同一个包里面，不能给其他包内的类型定义方法

  - 就是接收者的类型定义和方法声明必须在同一包内；不能为内建类型声明方法

  ```go
  package main
  import("fmt"; "math")
  
  type MyFloat float64
  func (f MyFloat) Abs() float64 {
  	if f < 0 {
  		return float64(-f)
  	}
  	return float64(f)
  }
  func main() {
  	f := MyFloat(-math.Sqrt2)
  	fmt.Println(f.Abs())
  }
  ```

- 更有用的是**指针接收者（pointer receiver）**

  - 声明的时候在类型`T`前面加上`*`即可，其余和普通的值接收者相同：`func (v *T) name(...) rType`
  - 有用是因为可以修改指针接收者所引用的值

  ```go
  package main
  import("fmt"; "math")
  
  type Vertex struct {X, Y float64}
  
  func (v Vertex) Abs() float64 {
  	return math.Sqrt(v.X*v.X + v.Y*v.Y)
  }
  
  // 如果去掉这里的*号，那么最后的结果就是5，而不是50了，因为值接收者不改变原始的值（因为值传递）
  // 接收者是指针，那么方法被调用时，接收者既可以是值又可以是指针
  func (v *Vertex) Scale(f float64) {
  	v.X = v.X * f
  	v.Y = v.Y * f
  }
  
  func main() {
  	v := Vertex{3, 4}
  	v.Scale(10)
  	fmt.Println(v.Abs()) // 50
  }
  ```

- 方法与指针**重定向（indirection）**

  - 如果接收者是指针的话，对应的方法被调用是，接收者既可以是值又可以是指针
    （如果函数的参数是指针的话，那么它必须接收一个指针）
  - 如果接收者是值的话，对应的方法被调用是，接收者既可以是值又可以是指针
    （如果函数的参数是值的话，那么它必须接收值）
  - 总结起来就是：**接收者不管是值还是指针，被调用时，接收者既可以是值又可以是指针**

  ```go
  type Vertex struct {X, Y float64}
  // 接收者是值，那么方法被调用时，接收者既可以是值又可以是指针
  func (v Vertex) Abs() float64 {	return math.Sqrt(v.X*v.X + v.Y*v.Y)}
  // 接收者是指针，那么方法被调用时，接收者既可以是值又可以是指针
  func (v *Vertex) Scale(f float64) {
  	v.X = v.X * f
  	v.Y = v.Y * f
  }
  
  func main() {
  	v := Vertex{3, 4}
  	v.Scale(10)
  	fmt.Println(v.Abs()) // 50
      p := &v
      p.Scale(10)
      fmt.Println(v.Abs()) // 50
      
      k := Vertex{3, 4}
      s := &k
      fmt.Println(k.Abs()) // 5
      fmt.Println(s.Abs()) // 5
  }
  
  ```

- 为什么使用指针接收者？

  - 方法能够修改其接收者指向的值。
  - 可以在每次调用方法时避免复制该值（若值的类型为大型结构体时，会更加高效）

### Interfaces（接口）

- **接口类型** 是由一组方法签名定义的集合（An *interface type* is defined as a set of method signatures）

- 接口类型的变量可以保存任何实现了这些方法的值。

  - 就是说，如果要赋值给一个接口类型变量，那么它必须已经实现了接口类型里面的方法
  - 也就是说，如果要赋值给一个接口类型变量，它必须有一个对应的接收者的方法
  - 接口类型的变量可以调用其所声明的方法（已实现）

  ```go
  package main
  import ("fmt"; "math")
  type Abser interface { Abs() float64 }
  
  func main() {
  	var a Abser
  	f := MyFloat(-math.Sqrt2)
  	v := Vertex{3, 4}
  
  	a = f  // a MyFloat 实现了 Abser
  	a = &v // a *Vertex 实现了 Abser
  
  	// 下面一行，v 是一个 Vertex（而不是 *Vertex）
  	// 所以没有实现 Abser。
  	a = v
  
  	fmt.Println(a.Abs())
  }
  
  type MyFloat float64
  
  func (f MyFloat) Abs() float64 {
  	if f < 0 {	return float64(-f)	}
  	return float64(f)
  }
  
  type Vertex struct {X, Y float64}
  
  func (v *Vertex) Abs() float64 { return math.Sqrt(v.X*v.X + v.Y*v.Y) }
  ```

- 接口声明可以只是声明了该类型应该有的所有方法，而接口的实现方法，就是带有接收者的方法，它可以出现在任何包中，这样（隐式）接口和接口的实现二者分开了，解耦了。

  ```go
  package main
  import "fmt"
  
  type I interface {	M()	} // 一个接口类型
  type T struct {	S string } // 一个struct
  // 此方法表示类型 T 实现了接口 I，但我们无需显式声明此事。
  func (t T) M() { fmt.Println(t.S) }
  
  func main() {
  	var i I = T{"hello"}
  	i.M()
  }
  
  ```

- 接口也是值。它们可以像其它值一样传递

- 接口值可以用作函数的参数或返回值

- 在内部，接口值可以看做包含值和具体类型的元组：`(value, type)`

- 接口值保存了一个具体底层类型的具体值。

- 接口值调用方法时会执行其底层类型的同名方法。

  ```go
  package main
  import ("fmt"; "math")
  
  type I interface {	M()	} // 一个接口类型
  type T struct {	S string } // 一个struct
  
  func (t *T) M() { fmt.Println(t.S) }
  type F float64
  func (f F) M() { fmt.Println(f) }
  
  func main() {
  	var i I
  
  	i = &T{"Hello"}
  	describe(i) // (&{Hello}, *main.T)
  	i.M() // Hello
  
  	i = F(math.Pi)
  	describe(i) // (3.141592653589793, main.F)
  	i.M() // 3.141592653589793
  }
  
  func describe(i I) { fmt.Printf("(%v, %T)\n", i, i) }
  
  ```

- 即便接口内的具体值为 `nil`，方法仍然会被` nil` 接收者调用。

  - 比如说已经实现了一个指针接收者方法；现在赋值给一个接口的是一个空指针`nil`，那么接口的方法依然可以调用，而不会像其他语言中一样触发指针异常，但可以在接口内处理它

  ```go
  package main
  import ("fmt"; "math")
  
  type I interface {	M()	} // 一个接口类型
  type T struct {	S string } // 一个struct
  
  func (t *T) M() {
  	if t == nil {
  		fmt.Println("<nil>")
  		return
  	}
  	fmt.Println(t.S)
  }
  
  func main() {
  	var i I // 接口i目前本身是nil
  
  	var t *T // t现在的默认值是nil
  	i = t // 经过赋值，现在i实际上包含了nil，但它本身并不是nil
  	describe(i) // (<nil>, *main.T)
  	i.M() // <nil>
  
  	i = &T{"hello"}
  	describe(i) // (&{hello}, *main.T)
  	i.M() // hello
  }
  
  func describe(i I) { fmt.Printf("(%v, %T)\n", i, i) }
  
  
  ```

- nil 接口值既不保存值也不保存具体类型。

- 为 nil 接口调用方法会产生运行时错误，因为接口的元组内并未包含能够指明该调用哪个 **具体** 方法的类型。

  ```go
  package main
  import ("fmt"; "math")
  
  type I interface {	M()	}
  
  func main() {
  	var i I
  	describe(i) // (<nil>, <nil>)
  	i.M() // ! panic: runtime error: invalid memory address or nil pointer dereference
  }
  
  func describe(i I) { fmt.Printf("(%v, %T)\n", i, i) }
  ```

- 空接口

  - 指定了零个方法的接口值被称为 **空接口***：`interface {}`
  - 空接口可保存任何类型的值。（因为每个类型都至少实现了零个方法。）
  - 空接口被用来处理未知类型的值。例如，`fmt.Print` 可接受类型为 `interface{}` 的任意数量的参数。

  ```go
  package main
  import "fmt"
  
  func main() {
  	var i interface{}
  	describe(i) // (<nil>, <nil>)
  
  	i = 42
  	describe(i) // (42, int)
  
  	i = "hello"
  	describe(i) // (hello, string)
  }
  
  func describe(i I) { fmt.Printf("(%v, %T)\n", i, i) }
  ```

### Type assertions（类型断言）

- **类型断言**可以访问接口值底层具体值

  - `t := i.(T)`（即`retVal := interfaceValue.(typeName)`）

    该语句断言接口值`i`保存了具体类型`T`，并把底层类型为`T`的值赋予变量`t`

    如果接口值`i`没有保存类型`T`的值，就会触发恐慌（panic）

- **类型断言**也可以返回两个值：其底层值以及一个报告断言是否成功的布尔值。

  - `t, ok := i.(T)`（即`retVal, okVal := interfaceValue.(typeName)`）

    如果 `i` 保存了一个 `T`类型，那么 `t` 将会是其底层值，而 `ok` 为 `true`。

    否则，`ok` 将为 `false` 而 `t` 将为 `T` 类型的零值，程序并不会产生恐慌。

  ```go
  package main
  import "fmt"
  
  func main() {
  	var i interface{} = "hello"
  
  	s := i.(string)
  	fmt.Println(s) // hello
  
  	s, ok := i.(string)
  	fmt.Println(s, ok) // hello true
  
  	f, ok := i.(float64)
  	fmt.Println(f, ok) // 0 false
  
  	f = i.(float64) // 报错(panic)
  	fmt.Println(f)
  }
  ```

### Type switches（类型选择）

- **类型选择** 是一种按顺序从几个类型断言中选择分支的结构

- **类型选择**与一般的 `switch` 语句相似，不过类型选择中的 `case` 为类型（而非值）， 它们针对给定接口值所存储的值的类型进行比较

- **类型选择**中的声明与**类型断言** `i.(T)` 的语法相同，只是具体类型 `T` 被替换成了关键字 `type`

- 需要注意的是`i.(type)`只能在`switch`语句中使用，否则会报错

  ```go
  // 此选择语句判断接口值 i 保存的值类型是 T 还是 S
  // 在 T 或 S 的情况下，变量 v 会分别按 T 或 S 类型保存 i 拥有的值
  // 在默认（即没有匹配）的情况下，变量 v 与 i 的接口类型和值相同。
  switch v := i.(type) { // 注意这里的type是关键字
  case T:
      // v 的类型为 T
  case S:
      // v 的类型为 S
  default:
      // 没有匹配，v 与 i 的类型相同
  }
  ```

- xx

- xx

  ```go
  package main
  import "fmt"
  
  func do(i interface{}) {
  	switch v := i.(type) {
  	case int:
  		fmt.Printf("Twice %v is %v\n", v, v*2)
  	case string:
  		fmt.Printf("%q is %v bytes long\n", v, len(v))
  	default:
  		fmt.Printf("I don't know about type %T!\n", v)
  	}
  }
  
  func main() {
  	do(21) // Twice 21 is 42
  	do("hello") // "hello" is 5 bytes long
  	do(true) // I don't know about type bool!
  }
  ```

### Stringer

- `fmt`包中定义的`Stringer`是一个接口，实现它（对应接收者的方法）可以用字符串来描述自己的类型
  可以看到，这个接口规定了对应接收者的方法是一个名叫`String`的方法（无参数），返回的类型是`string`

  ```go
  type Stringer interface {
      String() string
  }
  ```

- 例子

  ```go
  package main
  import "fmt"
  
  type Person struct { Name string; Age  int }
  
  // 定义了Person为接收者的方法
  func (p Person) String() string { return fmt.Sprintf("%v (%v years)", p.Name, p.Age) }
  
  func main() {
  	a := Person{"Arthur Dent", 42}
  	z := Person{"Zaphod Beeblebrox", 9001}
  	fmt.Println(a, z)
  }
  
  ```

### Errors（错误）

- `error` 类型是一个内建接口（和 `fmt.Stringer` 类似），用来表示错误状态
  可以看到它需要给接收者实现一个名字叫 `Error`、返回值为 `string` 的方法

  ```go
  type error interface {
      Error() string
  }
  ```

- 通常函数会返回一个 `error` 值，调用的它的代码应当判断这个错误是否等于 `nil` 来进行错误处理。
  一般地，`error` 为 `nil` 时表示成功；非 `nil` 的 `error` 表示失败。

  ```go
  i, err := strconv.Atoi("42")
  if err != nil {
      fmt.Printf("couldn't convert number: %v\n", err)
      return
  }
  fmt.Println("Converted integer:", i)
  ```

### Reader

- `io` 包指定了 `io.Reader` 接口，它表示从数据流的末尾进行读取。

- `io.Reader` 接口有一个 `Read` 方法
  `Read` **用数据填充给定的字节切片**并**返回填充的字节数和错误值**
  在遇到数据流的结尾时，它会返回一个 `io.EOF` 错误

  ```go
  func (T) Read(b []byte) (n int, err error)
  ```

### Image（图像）

- [`image`](https://go-zh.org/pkg/image/#Image) 包定义了 `Image` 接口：
  **注意:** `Bounds` 方法的返回值 `Rectangle` 实际上是一个 [`image.Rectangle`](https://go-zh.org/pkg/image/#Rectangle)，它在 `image` 包中声明。

  ```go
  package image
  
  type Image interface {
      ColorModel() color.Model
      Bounds() Rectangle
      At(x, y int) color.Color
  }
  ```

















