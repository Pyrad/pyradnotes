# Learning GPU

## CUDA编程基础入门系列（持续更新）

B站视频网址：[CUDA编程基础入门系列 - 权双](https://www.bilibili.com/video/BV1sM4y1x7of?p=10&spm_id_from=pageDriver&vd_source=05aabc7e72e595bed3d072985363efa7)


第1集至第9集

CPU - Host
GPU - Device (CPU的协处理器)

主机代码和设备代码是写在一起的，由修饰符区分。

driver API
runtime API


核函数中只能使用 printf() 函数，无法使用 std::cout。

host端则是可以使用std::cout。

nvcc 把C++代码交给g++编译器处理，而它再处理纯cuda的代码。

kernel function 核函数

核函数在GPU上并行执行。

修饰符是 `__global__` 返回值必须是 `void`。

既要写主机代码，又要写设备代码。


核函数只能使用GPU内存（显存）

核函数无法使用变长参数

核函数无法使用静态变量

核函数无法使用函数指针

核函数有异步性


cuda代码 流程：
1. 主机代码
2. 核函数调用
3. 主机代码（内存同步、释放等）





线程块的个数，线程块中线程的个数

cudaDeviceSynchronize() -> 主机等待GPU执行完毕（host 和 device同步）




grid 网格，即核函数启动之后，所启动的所有的线程的总和

block 线程块，是逻辑划分，不是物理上的

thread 线程

<<<线程块个数, 线程块中线程个数>>>
<<<grid_size, block_size>>>

一维模型中的built-in variable
gridDim.x
blockDim.x

线程索引也是built-in variable
blockIdx.x，范围是 0 ~ gridDim.x - 1，表示线程在grid中的索引
threadIdx.x 范围是 0 ~ blockDim.x - 1，表示线程在block中的索引

在核函数中，这些built-in变量，这些都是预定义好的，直接取用即可
gridDim.x, blockDim.x
blockIdx.x, threadIdx.x

1个grid最多 2^31 - 1 个block

1个block最多 1024个线程


2024年5月15日23:10 观看至第10集第0分第30秒

