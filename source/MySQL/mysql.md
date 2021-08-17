# 数据库的好处

1. 可以持久化到本地
2. 结构化查询



# 数据库常见概念

1. DB：数据库，存储数据的容器
2. DBMS：数据库管理系统，又称为数据库软件或数据库产品，用于创建或管理DB
3. SQL：结构化查询语言，用于和数据库通信，主流的数据库软件通用的语言



# 数据存储数据的特点

1. 数据存放在表中，表放到库中
2. 库中可以有多张表，每张表有唯一的表名标识
3. 表有一个或多个列，列也叫“字段”，相当于属性
4. 表忠每行数据，相当于Java的对象



# 常见的数据库软件

MySQL

Oracle

DB2

SQL Server



# MySQL的优点

1. 开源免费成本低
2. 性能高，移植性好
3. 体积小，好安装



# MySQL的安装

属于C/S架构，需要先安装服务器（Server），使用前要启动服务



# MySQL 基本操作

启动服务/停止服务：

```shell
# windows command line中，使用管理员打开cmd
#启动服务
net start <服务名>
#暂停服务
net stop <服务名>

```

连接数据库

```shell
# 连接数据库
mysql -h localhost -P<PortNum> -u <root> -p<passward>
# 如果是连接本机，可以省略host和端口
mysql -u <root> -p<passward>
```

基本操作

```sql
# 查看所有database
show databases;

# 切换database
use <databases_name>;

# 查看当前库的所有表
show tables;

# 查看当前所在的database
SELECT database();

# 创建表
create table stuinfo(id int, name varchar(20));

# 查看表结构
desc <表名>;
desc stuinfo;
```



# MySQL语法规范

1. 不区分大小写，但建议关键字大写，表、列名用小写
2. 命令以分号结尾
3. 可以根据缩进或换行
4. 注释
   1. 单行注释，以"#"开头
   2. 单行注释，以"-- "开头（注意--后面有空格）
   3. 多行注释，以/* */把需要注释的地方包起来





# DQL 数据查询语言

DQL = Data Query Language



## 基础查询

### 基本语法

```sql
SELECT 查询列表 FROM 表名
```

查询列表可以是

（1）表中的字段

（2）常量

（3）表达式

（4）函数

查询的结果是一个虚拟的表格



### 示例

- 查询单个字段

```mysql
SELECT last_name FROM employees;
```

- 查询多个字段

```mysql
SELECT last_name, salary, email FROM employees;
SELECT * FROM empolyees;
```

- 可以使用着重号``，以表明是一个字段名，而不是关键字

```mysql
SELECT `NAME` FROM stuinfo
```

- 查询常量值

```mysql
# 如果查询字符型或日期型的常量值，必须用单引号引起来，数值型则不用
SELECT 100;
SELECT 'string'; #字符串单引号或双引号都可以
```

- 查询表达式

```mysql
SELECT 100%98;
```

- 查询函数

```mysql
# MySQL执行函数必须用SELECT，而且MySQL的语句都有返回值
SELECT VERSION();
```

- 使用别名

  （1）方便理解

  （2）【连接查询时】如果遇到多个同名的字段，可以区分

  其中```AS```可以省略（用空格代替），别名可以加双引号或单引号以防其中的某些字符串别认定为关键字

```mysql
SELECT 100%98 AS <NEW_NAME>;
SELECT last_name AS xing, first_name AS Ming FROM employee;
SELECT salary AS "out put" FROM employees;
```

- 去重复

  关键字是```DISTINCT```

```mysql
# 注意，不能对两个或多个字段使用DISTINCT，原因是每个字段的重复的行数可能不同
SELECT DISTINCT department_id FROM employees;
```

- +号的作用

  加号"+"在SQL中只当做运算符，如果要连接字符串,就用CONCAT函数

  - 两个都是数值型，做加法运算

  ```mysql
  SELECT 100 + 90; # --> 190
  ```

  - 其中一个为字符型，将其转换成数值型做运算

    如果转换成功，继续做加法；

    如果失败，字符型会被转换为0做计算

    如果其中一个为null，结果肯定是null     

  ```mysql
  SELECT '123' + 90; --> 213
  SELECT 'john' + 90; --> 90
  SELECT null + 90; --> null
  ```

- CONCAT函数

```mysql
# 员工的名和姓连接在一起
SELECT CONCAT(first_name, last_name) AS Ename FROM employees;

# 员工的名和姓连接在一起,用逗号隔开
SELECT CONCAT(first_name, ',', last_name) AS Ename FROM employees;

# 注意concat返回的是一个新的字段，这个字段可以重命名；
# 但里面的每个被连接的不能重命名
SELECT 
CONCAT(first_name, ',', last_name, ',', job_id, ',', IFNULL(commission_pct, 0)) 
AS CMP
FROM employees;
```

- IFNULL函数

  返回的是：如果第一个参数是原本是null，就用第二个参数值代替，否则不代替。

```mysql
# 如下函数选择commission_pct字段和IFNULL返回的新字段CMP，
# IFNULL返回的是：如果第一个参数是原本是null，就用0代替，否则不代替。
SELECT IFNULL(commission_pct, 0) AS CMP, commission_pct FROM employees;
```

- ISNULL函数

  判断某个字段是否为null，如是则返回1，否则返回0

```mysql
SELECT ISNULL(commission_pct, 0) AS CMP, commission_pct FROM employees;
```



## 条件查询

### 基本语法

```mysql
SELECT 查询列表 FROM 表名 WHERE 筛选条件
```

### 分类

1. 按照条件表达式筛选
   
   条件运算符 
   
   ```mysql
   >, <, =（等于）, !=, <>, >=, <=
   ```
   
   按逻辑表达式：主要用于连接表达式
   
   逻辑运算符
   
   ```mysql
   &&， ||， !， AND， OR， not
   ```
   
   
   
2. 模糊查询 

   - **LIKE**

     一般和通配符**```%```**搭配使用

     通配符**```%```**表示0到多个字符

     通配符```_```表示单个任意字符

     如果需要转义（1）用'\'即可（2）可以使用ESCAPE关键字指定

     MySQL5.5以上的版本不仅可以用于匹配字符，也可以匹配数值

   - **BETWEEN AND**

     提高了简洁度

     范围临界值是前小后大

     查询结果包含临界值

     两个临界值的类型要一致，或者能够隐式转换

   - **IN**

     需要用同样类型的列表

     用小括号包起来, 

     不支持通配符%

   - **IS NULL**

     ```=```或```<>```不能用于判断null值

     用```IS NULL```或```IS NOT NULL```来判断null值

   
   - **<=>**
   
     安全等于符号
   
     可以判断**NULL**值，也可判断普通类型的值



### 示例

```mysql
# 查询工资大于12000的员工信息
SELECT * FROM employees WHERE salary > 12000;

# 查询部门编号不等于90号的员工名和部门编号
SELECT last_name, department_id FROM employees WHERE department_id != 90;

# 查询工资在10000到20000之间的员工名,工资和奖金 
SELECT last_name, salary, commission_pct 
FROM employees
WHERE salary >= 10000 AND salary <= 20000;

# 部门编号不是在90到110之间,或工资高于15000的员工
SELECT *
FROM employees
WHERE department_id < 90 OR department_id > 110 OR salary > 15000;

# 查询员工名包含a的员工 （通配符用%）
SELECT * FROM employees WHERE last_name LIKE '%a%';

# 查询员工名第三和第五个字符为a的员工名和工资
SELECT last_name, salary FROM employees
WHERE last_name LIKE '__n_l%';

# 查询员工名第二个字符是下划线的员工
SELECT last_name FROM employees
WHERE last_name LIKE '_\_%';
# 使用ESCAPE关键字指定转义字符
SELECT last_name FROM employees
WHERE last_name LIKE '_k_%' ESCAPE 'k';

# 查询员工编号在100到120之间的员工信息
SELECT * FROM employees 
WHERE employee_id BETWEEN 100 AND 120;

# 查询员工的工种编号是：IT_PROG、AD_VP、AD_PRES中的一个员工名和工种编号
SELECT last_name, job_id
FROM employees
WHERE job_id IN('IT_PROG', 'AD_VP', 'AD_PRES');

# 查询没有奖金的员工名和奖金率
SELECT last_name, commission_pct
FROM employees
WHERE commission_pct IS NULL;
# 使用安全等于符号：<=>
SELECT last_name, commission_pct
FROM employees
WHERE commission_pct <=> NULL;

SELECT * FROM employees WHERE salary <=> 12000;

# 查询有奖金的员工名和奖金率
SELECT last_name, commission_pct
FROM employees
WHERE commission_pct IS NOT NULL;

# 查询工号为176的员工的姓名、部门号和年薪
SELECT 
	last_name, 
    department_id, 
    salary*12*(1+IFNULL(commission_pct, 0)) AS AnnualIncome
FROM employees;


# 一道面试题
# 下面两个语句的返回结果不同
# 原因是如果有null值，第一条可以查询出来，第二条不行
SELECT * FROM employees;
SELECT * FROM employees WHERE commission_pct LIKE "%%" AND last_name LIKE "%%";
```



```mysql
```



```sql


```



【2021-08-15】B站视频看到第100集

# DML 数据管理语言

DML = Data Management Language



# DDL 数据定义语言

DDL = Data Definition Language



# TCL 事务控制语言

TCL = Transaction Control Language