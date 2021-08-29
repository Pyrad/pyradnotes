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

```mysql
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

```mysql
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

     一般和通配符```%```搭配使用

     通配符```%```表示0到多个字符

     通配符```_```表示单个任意字符

     如果需要转义（1）用'\\'即可（2）可以使用ESCAPE关键字指定

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



## 排序查询

### 基本语法

```mysql
SELECT 查询列表
FROM 表
【WHERE 筛选条件】
ORDER BY 排序字段/表达式 ASC/DESC;
```

1. 排序顺序

   ```ASC```是升序

   ```DESC```是降序

2. ```ORDER BY```子句可以支持：

   单个字段 | 别名 | 表达式 | 函数 | 多个字段

3. ```ORDER BY```子句放在查询语句的最后面（```LIMIT```子句除外）

### 示例

- 按单个字段排序

```mysql
SELECT * FROM employees ORDER BY salary DESC;
```

- 按添加筛选条件再排序

  查询部门编号>=90的员工信息，并按员工编号降序

```mysql
SELECT * 
FROM employees 
WHERE employee_id >= 90
ORDER BY employee_id DESC;
```

- 按表达式排序

  查询员工信息 按年薪降序

```mysql
SELECT *, salary * 12 * （1 + IFNULL(commission_pct, 0))
FROM employees
ORDER BY salary * 12 * （1 + IFNULL(commission_pct, 0)) DESC;
```

- 按别名排序

  查询员工信息 按年薪升序

```mysql
SELECT *, salary * 12 * （1 + IFNULL(commission_pct, 0)) AS InCome
FROM employees
ORDER BY InCome DESC;
```

- 按函数排序

  查询员工名，并且按名字的长度降序

```mysql
SELECT first_name, LENGTH(first_name) AS NameLen
FROM employees
ORDER BY NameLen DESC;
```

- 按多个字段排序

  查询员工信息，要求先按工资降序，再按employee_id升序

  注意，是用逗号```,```把多个排序条件连接起来

```mysql
SELECT *
FROM employees
ORDER BY salary DESC, employee_id ASC;
```



## 常见函数

### 好处

1. 隐藏实现细节
2. 提高代码重用性

### 语法（调用）

```mysql
SELECT 函数名(实参列表)
FROM 表
```

### 分类

1. 单行函数

   如：CONCAT，LENGTH，IFNULL，...

2. 分组函数

   做统计使用，又称统计函数、聚合函数、组函数

### 单行函数

#### 常见单行函数

| 字符函数 | 数学函数 | 日期函数    | 其他函数 | 控制函数 |
| :------- | :------- | :---------- | :------- | -------- |
| LENGTH   | ROUND    | NOW         | VERSION  | IF       |
| CONCAT   | CEIL     | CURDATE     | DATABASE | CASE     |
| SUBSTR   | FLOOR    | CURTIME     | USER     |          |
| INSTR    | TRUNCATE | YEAR        |          |          |
| TRIM     | MOD      | MONTH       |          |          |
| UPPER    |          | MONTHNAME   |          |          |
| LOWER    |          | DAY         |          |          |
| LPAD     |          | HOUR        |          |          |
| RPAD     |          | MINUTE      |          |          |
| REPLACE  |          | SECOND      |          |          |
|          |          | STR_TO_DATE |          |          |
|          |          | DATE_FORMAT |          |          |

#### 字符函数示例

- LENGTH 获取参数值的字节个数

```mysql
SELECT LENGTH('john');
SELECT LENGTH('张三丰hahaha');

# 查看内置变量（变量名包含字符char）
SHOW VARIABLES LIKE '%char%';
```

- CONCAT 拼接字符串

```mysql
SELECT CONCAT(last_name,'_',first_name) FullName FROM employees;
```

- UPPER，LOWER

```mysql
SELECT UPPER('john');
SELECT LOWER('joHn');

# 将姓变大写，名变小写，然后拼接
SELECT CONCAT(LOWER(last_name), '-', UPPER(first_name)) AS FullName
FROM employees
```

- SUBSTR、SUBSTRING

  索引是从1开始的

  语法：SUBSTR(字符串，起始索引【，长度】)

```mysql
# 截取从指定索引处后面所有字符
SELECT SUBSTR('李莫愁爱上了陆展元', 7) AS OutPut; # 结果是一行一列，'陆展元'

# 截取从指定索引处指定字符长度的字符
SELECT SUBSTR('李莫愁爱上了陆展元',1,3) AS OutPut; # 结果是一行一列，'李莫愁'

# 姓名中首字符大写，其他字符小写然后用'_'拼接，显示出来
SELECT CONCAT(UPPER(SUBSTR(last_name, 1, 1)), '_', LOWER(SUBSTR(last_name, 2)))
AS OUTPUT
FROM employees
```

- INSTR 返回子串第一次出现的索引，如果找不到返回0

  语法：INSTR(字符串，子字符串)

```mysql
SELECT INSTR('杨不殷六侠悔爱上了殷六侠','殷八侠') AS out_put;
```

- TRIM

  语法1：TRIM(字符串 )。该写法默认去掉空白符

  语法2：TRIM(需要去掉的字符 FROM 字符串)

```mysql
SELECT LENGTH(TRIM('    张翠山    ')) AS out_put;
SELECT TRIM('aa' FROM 'aaaaaaaaa张aaaaaaaaaaaa翠山aaaaaaaaaaaaaaaaaaaaaa') AS out_put;
```

- LPAD 用指定的字符实现左填充指定长度

  语法：LPAD(s1, len, s2)

   在字符串 s1 的开始处填充字符串 s2，使字符串长度达到 len

```mysql
SELECT LPAD('殷素素', 2, '*') AS out_put; # 输出殷素
```

- RPAD 用指定的字符实现右填充指定长度

  语法：RPAD(s1,len,s2)

  在字符串 s1 的结尾处添加字符串 s2，使字符串的长度达到 len

```mysql
SELECT RPAD('殷素素', 12, 'ab') AS out_put; # 输出殷素素ababababa
```

- REPLACE 替换

  语法：REPLACE(s, s1, s2)

  将字符串 s2 替代字符串 s 中的字符串 s1

```mysql
SELECT REPLACE('周芷若周芷若周芷若周芷若张无忌爱上了周芷若','周芷若','赵敏') AS out_put;
```



#### 数学函数示例

- ROUND

  语法：ROUND(x)

  返回离 x 最近的整数

```mysql
SELECT ROUND(-1.55); # -2
SELECT ROUND(1.567,2);
```

- CEIL 向上取整,返回>=该参数的最小整数

```mysql
SELECT CEIL(-1.02); # -1
```

- FLOOR 向下取整，返回<=该参数的最大整数

```mysql
SELECT FLOOR(-9.99); # -10
```

- TRUNCATE截断

  语法：TRUNCATE(x,y)

  返回数值 x 保留到小数点后 y 位的值（与 ROUND 最大的区别是不会进行四舍五入）

```mysql
SELECT TRUNCATE(1.69999,1); # 1.6
```

- MOD取余

```mysql
/*
mod(a,b) ：  a-a/b*b

mod(-10,-3):-10- (-10)/(-3)*（-3）=-1
*/
# 快速记忆：结果的符号和前面数的符号相同
SELECT MOD(10,3);  # 1
SELECT MOD(10,-3); # 1
SELECT MOD(-10,3); # -1
SELECT MOD(-10,-3);# -1
SELECT 10%3;
```



#### 日期函数示例

- NOW

  返回当前系统日期+时间

```mysql
SELECT NOW();
```

- CURDATE

  返回当前系统日期，不包含时间

```mysql
SELECT CURDATE();
```

- CURTIME

  返回当前时间，不包含日期

```mysql
SELECT CURTIME();
```

- YEAR，MONTH等

```mysql
#可以获取指定的部分，年、月、日、小时、分钟、秒
SELECT YEAR(NOW()) 年;
SELECT YEAR('1998-1-1') 年;

SELECT  YEAR(hiredate) 年 FROM employees;

SELECT MONTH(NOW()) 月;
SELECT MONTHNAME(NOW()) 月;
```

- STR_TO_DATE(string, format_mask)

  将字符通过指定的格式转换成日期

  就是给定一个字符串，告诉MySQL是以什么样的方式读取其中的年月日等信息

```mysql
SELECT STR_TO_DATE('1998-3-2','%Y-%c-%d') AS out_put;

#查询入职日期为1992--4-3的员工信息
SELECT * FROM employees WHERE hiredate = '1992-4-3';
SELECT * FROM employees WHERE hiredate = STR_TO_DATE('4-3 1992','%c-%d %Y');
```

- DATE_FORMAT 将日期转换成字符

  DATE_FORMAT(d,f)：按表达式 f的要求显示日期 d

```mysql
SELECT DATE_FORMAT(NOW(),'%y年%m月%d日') AS out_put; # 21年08月19日  
SELECT DATE_FORMAT(NOW(),'%Y年%m月%d日') AS out_put; # 2021年08月19日  

#查询有奖金的员工名和入职日期(xx月/xx日 xx年)
SELECT last_name, DATE_FORMAT(hiredate,'%m月/%d日 %y年') 入职日期
FROM employees
WHERE commission_pct IS NOT NULL;
```



#### 其他函数示例

```mysql
SELECT VERSION();
SELECT DATABASE();
SELECT USER();
```



#### 流程控制函数

- if函数

  IF(expr,v1,v2)

  如果表达式 expr 成立，返回结果 v1；否则，返回结果 v2。

```mysql
SELECT IF(10<5, '大', '小');

SELECT last_name, IF(commission_pct IS NULL,'HasComm','HasNotComm')
AS Reminder
FROM employees;
```

- CASE函数（一）

  语法

  ```mysql
  CASE expression
      WHEN condition1 THEN result1
      WHEN condition2 THEN result2
     ...
      WHEN conditionN THEN resultN
      ELSE result
  END
  ```

  CASE 表示函数开始，END 表示函数结束。

  如果 condition1 成立，则返回 result1；

   如果 condition2 成立，则返回 result2；

  当全部不成立则返回 result；

  而当有一个成立之后，后面的就不执行了。

  ```mysql
  /*
  案例：查询员工的工资，要求
  
  部门号=30，显示的工资为1.1倍
  部门号=40，显示的工资为1.2倍
  部门号=50，显示的工资为1.3倍
  其他部门，显示的工资为原工资
  */
  
  SELECT last_name,
  CASE department_id
    WHEN 30 THEN salary * 1.1
    WHEN 40 THEN salary * 1.2
    WHEN 50 THEN salary * 1.3
    ELSE salary
  END AS NewSalary
  FROM employees;
  ```



- CASE 函数（二）

  语法

  ```mysql
  CASE
      WHEN condition1 THEN result1/sentence1
      WHEN condition2 THEN result2/sentence1
     ...
      WHEN conditionN THEN resultN/sentenceN
      ELSE result/sentence
  END
  ```

  示例

  ```mysql
  /*
  案例：查询员工的工资的情况
  
  如果工资>20000,显示A级别
  如果工资>15000,显示B级别
  如果工资>10000，显示C级别
  否则，显示D级别
  */
  SELECT last_name,
  CASE
  WHEN salary > 20000 THEN 'A'
  WHEN salary > 15000 THEN 'B'
  WHEN salary > 10000 THEN 'C'
  ELSE 'D'
  END AS NewSalary
  FROM employees;
  ```



### 分组函数

#### 功能

用作统计使用，又称为聚合函数或统计函数或组函数

#### 分类

| 函数  | 作用     |
| ----- | -------- |
| SUM   | 求和     |
| AVG   | 求平均值 |
| MAX   | 求最大值 |
| MIN   | 求最小值 |
| COUNT | 计算个数 |

#### 特点

1. ```SUM```、```AVG```一般用于处理数值型
   ```MAX```、```MIN```、```COUNT```可以处理任何类型
   
2. 以上分组函数都忽略```NULL```值

3. 可以和```DISTINCT```搭配实现去重的运算

4. ```COUNT```函数的单独介绍

   一般使用```COUNT(*)```用作统计行数

5. 和分组函数一同查询的字段要求是```GROUP BY```后的字段

#### 示例

- 简单的使用

```mysql
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT MAX(salary) FROM employees;
SELECT COUNT(salary) FROM employees;

# 同时使用
SELECT SUM(salary) 和,
       AVG(salary) 平均,
       MAX(salary) 最高,
       MIN(salary) 最低,
       COUNT(salary) 个数
FROM employees;

SELECT SUM(salary) 和,
       ROUND(AVG(salary),2) 平均,
       MAX(salary) 最高,
       MIN(salary) 最低,
       COUNT(salary) 个数
FROM employees;
```

- 参数支持的类型

```mysql
# 返回0和0
SELECT SUM(last_name) ,AVG(last_name) FROM employees;
# 返回无意义的数值
SELECT SUM(hiredate) ,AVG(hiredate) FROM employees;
# 按照字符的ASCII码排序后得出最大和最小的字段
SELECT MAX(last_name),MIN(last_name) FROM employees;
# 按照时间排序后得出最大和最小的字段
SELECT MAX(hiredate),MIN(hiredate) FROM employees;
# 统计（非空的）个数
SELECT COUNT(commission_pct) FROM employees;
SELECT COUNT(last_name) FROM employees;
```

- 是否忽略```NULL```

```mysql
SELECT 
	SUM(commission_pct),
	AVG(commission_pct),
	SUM(commission_pct)/35,
	SUM(commission_pct)/107
FROM employees;

SELECT MAX(commission_pct), MIN(commission_pct) FROM employees;

SELECT COUNT(commission_pct) FROM employees;
SELECT commission_pct FROM employees;
```

- 和```DISTINCT```搭配

```mysql

SELECT SUM(DISTINCT salary), SUM(salary) FROM employees;

SELECT COUNT(DISTINCT salary), COUNT(salary) FROM employees;
```

- ```COUNT```函数

```mysql
# 以下三条语句返回同一个数值
SELECT COUNT(salary) FROM employees;
SELECT COUNT(*) FROM employees;
SELECT COUNT(1) FROM employees;
```

效率比较：

MYISAM存储引擎下  ，```COUNT(*)```的效率高

INNODB存储引擎下，```COUNT(*)```和```COUNT(1)```的效率差不多，比```COUNT(字段)```要高一些

- 和分组函数一同查询的字段有限制，否则表示的结果没有多大意义

```mysql
# 结果没有多大意义
/*
AVG(salary)  employee_id  
-----------  -------------
6461.682243            100
*/
SELECT AVG(salary),employee_id  FROM employees;
```



## 分组查询

### 语法

```mysql
SELECT 查询列表
FROM 表
【 WHERE 筛选条件 】
GROUP BY 分组的字段
【 HAVING 筛选条件 】
【 ORDER BY 排序的字段 】;
```

### 特点

1. 和分组函数一同查询的字段必须是```GROUP BY```后出现的字段

2. 筛选分为两类：分组前筛选和分组后筛选

|            | 针对的表           | 位置       | 连接的关键字 |
| ---------- | ------------------ | ---------- | ------------ |
| 分组前筛选 | 原始表             | GROUP BY前 | WHERE        |
| 分组后筛选 | GROUP BY后的结果集 | GROUP BY后 | HAVING       |

3. 分组可以按单个字段也可以按多个字段
4. 可以搭配着排序使用

问题1：分组函数做筛选能不能放在where后面
答：不能

问题2：where——group by——having

一般来讲，能用分组前筛选的，尽量使用分组前筛选，提高效率



### 示例

#### 简单分组

- 查询每个工种的员工平均工资

```mysql
SELECT job_id, AVG(salary)
FROM employees
GROUP BY job_id;
```

- 查询每个位置的部门个数

```mysql
SELECT location_id， COUNT(*)
FROM departments
GROUP BY location_id;
```



#### 实现分组前筛选

- 查询邮箱中包含a字符的 每个部门的最高工资

```mysql
SELECT department_id, MAX(salary)
FROM employees
WHERE email LIKE '%a%'
GROUP BY department_id;
```

- 查询有奖金的每个领导手下员工的平均工资

```mysql
SELECT manager_id, AVG(salary)
FROM employees
WHERE commission_pct IS NOT NULL
GROUP BY manager_id;
```



#### 实现分组后筛选

- 查询哪个部门的员工个数>5

```mysql
# 原始版本
SELECT department_id, COUNT(*)
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
# 美化版本
SELECT department_id, COUNT(*) AS dep_num
FROM employees
GROUP BY department_id
HAVING dep_num > 5;
```

- 每个工种有奖金的员工的最高工资>12000的工种编号和最高工资

```mysql
SELECT job_id, MAX(salary) AS max_sal
FROM employees
WHERE commission_pct IS NOT NULL
GROUP BY job_id
HAVING max_sal > 12000;
```

- 领导编号>102的每个领导手下的最低工资大于5000的领导编号和最低工资

```mysql
SELECT manager_id, MIN(salary) AS min_sal
FROM employees
WHERE manager_id > 102
GROUP BY manager_id
HAVING min_sal > 5000;
```

- 每个工种有奖金的员工的最高工资>6000的工种编号和最高工资,按最高工资升序

```mysql
SELECT job_id, MAX(salary) AS max_sal
FROM employees
WHERE commission_pct IS NOT NULL
GROUP BY job_id
HAVING max_sal > 6000
ORDER BY max_sal ASC;
```

- 按多个字段分组

  查询每个工种每个部门的最低工资,并按最低工资降序

```mysql
SELECT department_id, job_id, MIN(salary) AS min_sal
FROM employees
GROUP BY department_id, job_id
ORDER BY min_sal DESC;
```



## 连接查询

### 含义

即**多表查询**，当查询的字段来自于多个表时，用连接查询

### 笛卡尔积

表1有```M```行，表2有```N```行，查询结果为```M*N```行

原因：没有有效的连接条件

解决：添加有效的连接条件

### 分类

- 按年代分类

  SQL92标准：只支持内连接

  SQL99标准：支持内连接，外连接（左外+右外）以及交叉连接

- 按功能分类

  内连接：等值连接，非等值连接以及自连接

  外连接：左外连接，右外连接以及全外连接

  交叉连接

### SQL92标准的连接查询

#### 语法

```mysql
SELECT 表1字段1, 表1字段2, ... 表2字段1, 表2字段2, ...
FROM 表1, 表2, ...
WHERE 连接条件
【 AND 筛选条件 】
```

#### 等值连接

- 多表等值连接的结果为多表的交集部分
- ```N```表连接，至少需要```N-1```个连接条件
- 多表的顺序没有要求
- 一般需要为表起别名
- 可以搭配前面介绍的所有子句使用，比如排序、分组、筛选

##### 示例

- 查询女神名和对应的男神名

```mysql
SELECT beauty.name, boys.boyName
FROM beauty, boys
WHERE beauty.boyfriend_id = boys.id;
```

- 查询员工名和对应的部门名

```mysql
SELECT employees.first_name, departments.department_name
FROM employees, departments
WHERE employees.department_id = departments.department_id;
```



##### 给表起别名

- 提高语句的简洁度
- 区分多个重名的字段

如果为表起了别名，则查询的字段就不能使用原来的表名去限定

##### 示例

- 查询员工名、工种号、工种名

```mysql
# 两个表的顺序可以调换
SELECT E.first_name, E.job_id, J.job_title
FROM employees AS E, jobs AS J
WHERE E.job_id = J.job_id;
```

##### 添加筛选

- 查询有奖金的员工名、部门名

```mysql
SELECT E.first_name, D.department_name
FROM employees AS E, departments AS D
WHERE E.department_id = D.department_id
AND E.commission_pct IS NOT NULL;
```

- 查询城市名中第二个字符为o的部门名和城市名

```mysql
SELECT D.department_name, L.city
FROM departments AS D, locations AS L
WHERE D.location_id = L.location_id
AND L.city LIKE '_o%';
```



##### 添加分组

- 查询每个城市的部门个数

```mysql
SELECT D.department_name, COUNT(*) AS d_num
FROM departments AS D, locations AS L
WHERE D.location_id = L.location_id
GROUP BY D.location_id;
```

- 查询有奖金的每个部门的部门名和部门的领导编号和该部门的最低工资

```mysql
SELECT D.department_name, D.manager_id, MIN(salary) AS MinSal
FROM employees AS E, departments AS D
WHERE E.department_id = D.department_id
AND E.commission_pct IS NOT NULL
GROUP BY E.department_id;
```

##### 添加排序

- 查询每个工种的工种名和员工的个数，并且按员工个数降序

```mysql
SELECT J.job_id, J.job_title, COUNT(*) AS EmpNum
FROM employees AS E, jobs AS J
WHERE E.job_id = J.job_id
GROUP BY J.job_id
ORDER BY EmpNum DESC;
```



##### 三表连接

- 查询员工名、部门名和所在的城市

```mysql
SELECT E.first_name, D.department_name, L.city
FROM employees AS E, departments AS D, locations AS L
WHERE E.department_id = D.department_id
AND D.location_id = L.location_id;
```



#### 非等值连接

- 查询员工的工资和工资级别

```mysql
# 注意BETWEEN...AND...后面跟的值的大小顺序，是前面小后面大
SELECT E.salary, JG.grade_level
FROM employees AS E, job_grades AS JG
WHERE E.salary BETWEEN JG.lowest_sal AND JG.highest_sal;
```



#### 自连接

- 查询员工名和上级的名称

  即要查询的两个表实际是同一个表，使用同一张表的不同字段连接起来

```mysql
SELECT E0.first_name AS Ename, E1.first_name AS Mname
FROM employees AS E0, employees AS E1
WHERE E0.manager_id = E1.employee_id;
```





### SQL99语法连接查询

#### 语法

```mysql
SELECT 查询列表
FROM 表 AS 别名 【连接类型（ INNER/LEFT OUTER/RIGHT OUTER ）】
JOIN 表1 AS 别名1 ON 连接条件1
JOIN 表2 AS 别名2 ON 连接条件2
...
【 WHERE 分组前筛选条件 】
【 GROUP BY 分组 】
【 HAVING 分组后筛选条件 】
【 ORDER BY 排序列表 】
```

#### SQL92 vs. SQL99

- 功能：**SQL99**支持较多
- 可读性：**SQL99**实现连接条件和筛选条件的分离，可读性较高

结论：推荐使用**SQL99**

#### 分类

- **内连接**：```INNER```
- **外连接**
  - 左外连接```LEFT OUTER```
  - 右外连接```RIGHT OUTER```
  - 全外连接```FULL OUTER```
- **交叉连接**：```CROSS```



#### 内连接

##### 语法

```mysql
SELECT 查询列表
FROM 表 AS 别名 INNER
JOIN 表1 AS 别名1 ON 连接条件1
JOIN 表2 AS 别名2 ON 连接条件2
JOIN 表3 AS 别名3 ON 连接条件3
【 WHERE 分组前筛选条件 】
【 GROUP BY 分组 】
【 HAVING 分组后筛选条件 】
【 ORDER BY 排序列表 】
```

##### 分类

- 等值连接
- 非等值连接
- 自连接

##### 特点

- 可添加排序、分组和筛选
- ```INNER```可以省略
- 筛选条件放在```WHERE```后面，连接条件放在```ON```后面，提高分离性，便于阅读
- ```INNER JOIN```连接和SQL92语法中的等值连接效果是一样的，都是查询多表的交集



##### 等值连接

- 查询员工名、部门名

```mysql
SELECT E.first_name, D.department_name
FROM employees AS E
INNER JOIN departments AS D
ON E.department_id = D.department_id;
```

- 查询名字中包含e的员工名和工种名（添加筛选）

```mysql
SELECT E.first_name, J.job_title
FROM employees AS E
INNER JOIN jobs AS J
ON E.job_id = J.job_id
WHERE E.first_name LIKE '%e%';
```

- 查询部门个数>3的城市名和部门个数，（添加分组+筛选）

```mysql
SELECT L.city, COUNT(*) AS DepNum
FROM departments AS D
INNER JOIN locations AS L
ON D.location_id = L.location_id
GROUP BY L.city
HAVING DepNum > 3;
```

- 查询哪个部门的员工个数>3的部门名和员工个数，并按个数降序（添加排序）

```mysql
SELECT D.department_id, D.department_name, COUNT(*) AS EmpNum
FROM employees AS E
INNER JOIN departments AS D
ON E.department_id = D.department_id
GROUP BY D.department_id
HAVING EmpNum > 3
ORDER BY EmpNum DESC;
```

- 查询员工名、部门名、工种名，并按部门名降序（添加三表连接）

```mysql
SELECT E.first_name, D.department_name, J.job_title
FROM employees AS E
INNER JOIN departments AS D ON E.department_id = D.department_id
INNER JOIN jobs AS J ON E.job_id = J.job_id
ORDER BY D.department_name DESC;
```



##### 非等值连接

- 查询员工的工资级别

```mysql
SELECT E.first_name, E.salary, JG.grade_level
FROM employees AS E
INNER JOIN job_grades AS JG
ON E.salary BETWEEN JG.lowest_sal AND JG.highest_sal;
```

- 查询工资级别的个数>20的个数，并且按工资级别降序

```mysql
SELECT E.job_id, JG.grade_level, COUNT(*) AS JobGradeNum
FROM employees AS E
INNER JOIN job_grades AS JG
ON E.salary BETWEEN JG.lowest_sal AND JG.highest_sal
GROUP BY JG.grade_level
HAVING JobGradeNum > 20;
```



##### 自连接

- 查询员工的名字、上级的名字

```mysql
SELECT E.first_name AS Ename, M.first_name AS Mname
FROM employees AS E
INNER JOIN employees AS M
ON E.manager_id = M.employee_id;
```

- 查询姓名中包含字符k的员工的名字、上级的名字

```mysql
SELECT E.first_name AS Ename, M.first_name AS Mname
FROM employees AS E
INNER JOIN employees AS M
ON E.manager_id = M.employee_id
WHERE E.first_name LIKE '%k%';
```



#### 外连接

##### 应用

查询一个表中有，另一个表没有的记录

##### 特点

- **外连接**查询结果 = **内连接**结果 + **主表**中有而**从表**没有的记录

  外连接的查询结果包括**主表**中的所有记录

  如果**从表**中有和它匹配的，则显示匹配的值

  如果**从表**中没有和它匹配的，则显示```NULL```

- **左外连接**：```LEFT JOIN```**左边**的是**主表**

  **右外连接**：```RIGHTJOIN```**右边**的是**主表**

- **左外**和**右外**交换两个表的顺序，可以实现**同样**的效果 

- **全外连接** = **内连接**的结果 + 表1中有但表2没有的 + 表2中有但表1没有的

  **注意：MySQL不支持全外连接**



##### 示例

- 查询男朋友 不在男神表的的女神名

```mysql
SELECT BE.name, BO.boyName
FROM beauty AS BE
LEFT OUTER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
WHERE BO.boyName IS NULL;
```

- 查询哪个部门没有员工

```mysql
/* With LEFT JOIN */
SELECT D.department_id, D.department_name
FROM departments AS D
LEFT JOIN employees AS E
ON D.department_id = E.department_id
WHERE E.department_id IS NULL;

/* With RIGHT JOIN */
SELECT D.department_id, D.department_name
FROM employees AS E
RIGHT JOIN departments AS D
ON D.department_id = E.department_id
WHERE E.department_id IS NULL;
```

- 全外连接示例（**MySQL不支持全外连接**）

```mysql
SELECT BE.*, BO.*
FROM beauty AS BE
FULL OUTER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
```

- 交叉连接示例（就是笛卡尔积）

```mysql
SELECT BE.*, BO.*
FROM beauty AS BE
CROSS JOIN boys AS BO;
```



## 分页查询

### 应用场景

当要显示的数据，一页显示不全，需要**分页提交**SQL请求

### 语法

```mysql
SELECT 查询列表
FROM 表 AS 别名 【 连接类型 INNER/LEFT OUTER/RIGHT OUTER 】
JOIN 表1 AS 别名1 ON 连接条件1
JOIN 表2 AS 别名2 ON 连接条件2
...
【 WHERE 分组前筛选条件 】
【 GROUP BY 分组 】
【 HAVING 分组后筛选条件 】
【 ORDER BY 排序列表 】
【 LIMIT 【 offset, 】 size 】
```

- **offset**：要显示条目的起始索引（起始索引从0开始）
- **size**：要显示的条目个数

### 特点

- ```LIMIT```语句放在查询语句的最后

- 如果要显示的页数是 page，每页的条目数size

  ```mysql
  SELECT 查询列表
  FROM 表
  LIMIT (page-1)*size, size;
  ```

### 示例

- 查询前五条员工信息

```mysql
SELECT *
FROM employees
LIMIT 0, 5;

/* 如果起始索引是0，那么可以把这个offset省略，直接跟上后面的size（条目数） */
SELECT *
FROM employees
LIMIT 5;
```

- 查询第11条至第25条

```mysql
SELECT *
FROM employees
LIMIT 11, 15;
```

- 有奖金的员工信息，并且工资较高的前10名显示出来

```mysql
SELECT *
FROM employees
WHERE commission_pct IS NOT NULL
ORDER BY salary DESC
LIMIT 10;
```



## 子查询

### 含义

出现在其他语句中的```SELECT```语句，称为**子查询**或**内查询**

外部的查询语句，称为**主查询**或**外查询**

### 分类

#### 按子查询出现的位置

- ```SELECT```后面：只支持**标量子查询**
- ```FROM```后面：支持**表子查询**
- ```WHERE```或```HAVING```后面：支持**标量子查询**（单行单列）、**列子查询**（多行）以及**行子查询**（多列）
- ```EXISTS```后面：支持**表子查询**

#### 按结果集的行列数不同

- **标量子查询**（结果集只有**一行一列**）
- **列子查询**（结果集只有**一列多行**）
- **行子查询**（结果集有**一行多列**）
- **表子查询**（结果集一般为**多行多列**）

### ```WHERE```或```HAVING```后面

#### 支持三种子查询

- **标量子查询**（结果集只有**一行一列**）
- **列子查询**（结果集只有**一列多行**）
- **行子查询**（结果集有**一行多列**）

#### 特点

- 子查询放在小括号里

- 子查询一般放在条件的右侧

- 标量子查询一般搭配单行操作符使用```> < >= <= = <>```

  列子查询一般搭配多行操作符使用```IN ANY/SOME ALL```

- 子查询的执行优先于主查询而执行，主查询的条件用到了子查询的结果

#### 标量子查询示例

- 谁的工资比 Abel 高？

```mysql
SELECT EE.first_name, EE.salary
FROM employees AS EE
WHERE EE.salary > (
  SELECT salary
  FROM employees AS E 
  WHERE E.last_name = 'Abel'
);

/**
 * 注意，主查询里面的employees表也可以命名成同一个别名，
 * 但它和子查询里面的别名是不同的两个
 */
SELECT E.first_name, E.salary
FROM employees AS E
WHERE E.salary > (
  SELECT salary
  FROM employees AS E 
  WHERE E.last_name = 'Abel'
);
```

- 返回job_id与141号员工相同，salary比143号员工多的员工 姓名，job_id 和工资

```mysql
SELECT EE.first_name, EE.job_id, EE.salary
FROM employees AS EE
WHERE EE.job_id = (
  SELECT E.job_id
  FROM employees AS E
  WHERE E.employee_id = 141
) AND EE.salary > (
  SELECT E1.salary
  FROM employees AS E1
  WHERE E1.employee_id = 143
);
```

- 返回公司工资最少的员工的last_name，job_id和salary

```mysql
SELECT E.last_name, E.job_id, E.salary
FROM employees AS E
WHERE E.salary = (SELECT MIN(DISTINCT salary) FROM employees);

/* 也可以用LIMIT语句，但是LIMIT只会保留最终一项，但最低工资的人可能有多个 */
SELECT E.last_name, E.job_id, E.salary
FROM employees AS E
ORDER BY E.salary ASC
LIMIT 1;
```

- 查询最低工资大于50号部门最低工资的部门id和其最低工资

```mysql
/* 注意是求每个部门的最低工资 > 50号部门的最低工资 */
SELECT EE.department_id, MIN(EE.salary) AS MinSal
FROM employees AS EE
GROUP BY EE.department_id
HAVING MinSal > (
  SELECT MIN(E.salary)
  FROM employees AS E
  WHERE E.department_id = 50
)
ORDER BY MinSal ASC;
```



##### 列子查询（多行一列）示例

- 返回location_id是1400或1700的部门中的所有员工姓名

```mysql
SELECT E.first_name
FROM employees AS E
WHERE E.department_id IN (
  SELECT DISTINCT department_id
  FROM departments
  WHERE location_id IN (1400, 1700)
);

/*  或者也可以使用连接查询 */
SELECT E.first_name, D.location_id
FROM employees AS E
INNER JOIN departments AS D
ON E.department_id = D.department_id
WHERE D.location_id = 1400 OR D.location_id = 1700
```

- 返回其它工种中比job_id为‘IT_PROG’工种任一工资低的员工的员工号、姓名、job_id 以及salary

```mysql
/* 注意是ANY的考察，即只要低于其中之一即可 */
SELECT EE.first_name, EE.last_name, EE.employee_id, EE.job_id, EE.salary
FROM employees AS EE
WHERE EE.salary < ANY (
  SELECT E.salary
  FROM employees AS E
  WHERE E.job_id = 'IT_PROG'
) AND EE.job_id <> 'IT_PROG';
```

返回其它部门中比job_id为‘IT_PROG’部门所有工资都低的员工   的员工号、姓名、job_id 以及salary

```mysql
/* 注意是ALL的考察，即只要低于所有的 */
SELECT EE.first_name, EE.last_name, EE.employee_id, EE.job_id, EE.salary
FROM employees AS EE
WHERE EE.salary < ALL (
  SELECT E.salary
  FROM employees AS E
  WHERE E.job_id = 'IT_PROG'
) AND EE.job_id <> 'IT_PROG';
```



##### 行子查询（一行多列或多行多列）

- 查询员工编号最小并且工资最高的员工信息

```mysql
SELECT E.*
FROM employees AS E
WHERE E.employee_id = (
  SELECT MIN(E0.employee_id)
  FROM employees AS E0
) AND E.salary = (
  SELECT MAX(E1.salary)
  FROM employees AS E1
);
```



### ```SELECT```后面

在```SELECT```后面只支持标量子查询

- 查询每个部门的员工个数

```mysql
SELECT D.*,(
  SELECT COUNT(*)
  FROM employees AS E
  WHERE E.department_id = D.`department_id`
 ) DepNum
 FROM departments AS D;
 
/* 注意，下面的语句只能查出来有员工的department，但不能查出来没有员工的department */
SELECT E.department_id, COUNT(*) AS DepNum
FROM employees AS E
GROUP BY E.department_id
 
```

- 查询员工号=102的部门名

```mysql
SELECT (
  SELECT D.department_name
  FROM employees AS E
  INNER JOIN departments AS D
  ON E.department_id = D.department_id
  WHERE E.employee_id = 102
) depName;

/* 或者直接使用连接+筛选 */
SELECT D.department_name, E.employee_id
FROM employees AS E
INNER JOIN departments AS D
ON E.department_id = D.department_id
WHERE E.employee_id = 102;


```



### ```FROM```后面

**将子查询结果充当一张表，要求必须起别名**

- 查询每个部门的平均工资的工资等级

```mysql
SELECT AvgSalTab.AvgSal, JG.grade_level
FROM (SELECT AVG(E.salary) AS AvgSal
  FROM employees AS E
  GROUP BY E.department_id
  ORDER BY AvgSal) AS AvgSalTab
INNER JOIN job_grades AS JG
WHERE AvgSalTab.AvgSal BETWEEN JG.lowest_sal AND JG.highest_sal;

```



### ```EXISTS```后面（相关子查询）

#### 语法

```mysql
/* 结果返回1或0 */
SELECT EXISTS (完整的查询语句)

/* 例子 */
SELECT EXISTS(
SELECT employee_id
FROM employees
WHERE salary=300000) AS Result;
```

#### 示例

- 查询有员工的部门名

```mysql
/*
可以这样理解：
（1）首先是从department这个表开始，遍历每一条entry
（2）对于当前department的entry，执行EXIST后面的查询，即该条在department中的department_id是否在employee表中存在，如果存在返回1，否则返回0
（3）如果EXISTS子查询返回的是1，则保留该entry，进行department中的下一条entry；否则结果集中不保留该条目，继续进行department中的下一条entry
 */
SELECT D.department_name
FROM departments AS D
WHERE EXISTS(
  SELECT *
  FROM employees AS E
  WHERE D.department_id = E.department_id
);

/* 使用IN */
SELECT D.department_name
FROM departments AS D
WHERE D.department_id IN (
  SELECT DISTINCT E.department_id
  FROM employees AS E
);


/* 使用外连接查询 */
SELECT DISTINCT D.department_name
FROM departments AS D
LEFT OUTER JOIN employees AS E
ON D.department_id = E.department_id
WHERE E.employee_id IS NOT NULL
```

- 查询没有女朋友的男神信息

```mysql
SELECT *
FROM boys AS BO
WHERE NOT EXISTS(
  SELECT *
  FROM beauty AS BE
  WHERE BE.boyfriend_id = BO.id
);
```



## 联合查询

### 语法定义

```UNION```也叫联合、合并，就是将多条查询语句合并成一个结果

```mysql
查询语句1
UNION
查询语句2
UNION
查询语句3
UNION
...
```

### 应用场景

要查询的结果来自多个表，且多个表没有直接的连接关系，但查询的信息一致的时候

### 特点

- 要求多条查询语句的查询**列数是一致**的
- 要求多条查询语句的查询列的**类型和顺序最好一致**
- ```UNION```关键字默认是去重复的（即把结果中重复的行去掉），如果不想去掉重复的行，可以使用```UNION ALL```

### 示例

- 查询部门编号>90或邮箱包含a的员工信息

```mysql
SELECT * FROM employees AS E
WHERE E.email LIKE '%a%'
UNION
SELECT * FROM employees AS E
WHERE E.department_id > 90;
```

- 查询中国用户中男性的信息以及外国用户中年男性的用户信息

```mysql
SELECT id,cname FROM t_ca WHERE csex='男'
UNION ALL
SELECT t_id,tname FROM t_ua WHERE tGender='male';
```







# DML 数据管理（操作）语言

DML = Data Management Language

**就是表中记录的增删改**



## 三大类：增、删、改

- **插入语句**
- **修改语句**
- **删除语句**

注意：操作的对象都是表里面的**一行**或者**多行**



## 插入语句 ```INSERT```

**注意：就是插入一行或者多行的记录**

### 第一种插入方式

```mysql
INSERT INTO 表名(列名1, 列名2, ...) VALUES(值1, 值2, ...)
```

#### 几个要点

- **插入的值的类型要和列的类型一致或者兼容**

```mysql
INSERT INTO beauty(id, NAME, sex, borndate, phone, photo, boyfriend_id)
VALUES(13, 'Aragaki Yui', '女', '1992-05-02', 15210560360, NULL, 3);
```

- **不可为```NULL```的列必须插入值，可以为```NULL```的列有两种办法插入值。**
  - 对于可以为NULL的列，值可以写NULL插入NULL值
  - 对可以为NULL的列，可以省略列名和对应的值NULL，这样默认插入的值就是NULL

```mysql
# 对于可以为NULL的列，值可以写NULL插入NULL值
INSERT INTO beauty(id, NAME, sex, borndate, phone, photo, boyfriend_id)
VALUES(14, '唐艺昕', '女', '1990-4-23', '1898888888', NULL, 2);

# 对可以为NULL的列，可以省略列名和对应的值NULL，这样默认插入的值就是NULL
INSERT INTO beauty(id, NAME, sex, phone)
VALUES(15, '娜扎', '女', '1388888888');
```

- **列的顺序可以调换**

```mysql
INSERT INTO beauty(NAME, sex, id, phone)
VALUES('蒋欣', '女', 16, '15210560360');
```

- **列的个数和值的个数必须一致**

```mysql
INSERT INTO beauty(NAME, sex, id, phone)
VALUES('关晓彤', '女', 17, '110');
```

- **如果插入的时候不写列名，默认就是所有的列名，而且顺序和表中的顺序一致，后面的值也必须都写**

```mysql
INSERT INTO beauty
VALUES(18, 'Riho Yoshioka', '女', '1992-05-07', '15210560360', NULL, 1);
```

- **可以一次插入多行**
  - 注意，```VALUES```只写一次

```mysql
INSERT INTO beauty
VALUES(19, 'Satomi', '女', '1992-05-07', '15210560360', NULL, 2)
, (20, 'TingLiu', '女', '1992-05-07', '15210560360', NULL, 2)
, (21, 'Liudi', '女', '1992-05-07', '15210560360', NULL, 3);
```

- 可以利用子查询来插入子查询的结果

```mysql
INSERT INTO beauty(id, NAME, phone)
SELECT 23,'宋茜','11809866';

INSERT INTO beauty(id,NAME,phone)
SELECT id, boyname, '1234567'
FROM boys WHERE id<3;
```



### 第二种插入方式

```mysql
INSERT INTO 表名 SET 列名1=值1, 列名2=值2, ...
```

例子

```mysql
INSERT INTO beautySET id=22, NAME='刘涛', phone='999';
```



### 两种插入方式比较

- 第一种插入方式支持一次插入多行，第二种插入方式不支持
- 第一种插入方式支持子查询，第二种不支持





## 修改语句 ```UPDATE```

**注意：就是更新一行或者多行的记录**

### 语法

- 修改单表的记录

```mysql
UPDATE 表名 SET 列名1 = 值1, 列名2 = 值2, ...
WHERE 筛选条件
```

- 修改多表的记录

```mysql
# SQL99
UPDATE 表名1 AS 别名1
【 INNER | LEFT | RIGHT JOIN 】 表2 AS 别名2
ON 连接条件SET 列名1 = 值1, 列名2 = 值2, ...
WHERE 筛选条件

# SQL92
UPDATE 表1 AS 别名1, 表2 AS 别名2
SET 列名1 = 值1, 列名2 = 值2, ...
WHERE 连接条件AND 筛选条件
```



### 示例 - 修改单表

- 修改beauty表中姓唐的女神的电话为13899888899

```mysql
UPDATE beauty AS B SET phone='13899888899'
WHERE B.name LIKE '唐%';
```

- 修改boys表中id号为2的名称为张飞，魅力值 10

```mysql
UPDATE boys SET boyName = '张飞', userCP = 10
WHERE id = 2;
```



### 示例 - 修改多表

- 修改张无忌的女朋友的手机号为114，张无忌的魅力值为1000

```mysql
UPDATE beauty AS BE
INNER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
SET BE.phone = '114', BO.userCP = 1000
WHERE BO.boyName = '张无忌';
```

- 修改没有男朋友的女神的男朋友编号都为2号

```mysql
UPDATE beauty AS BE
LEFT OUTER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
SET BE.boyfriend_id = 2
WHERE BO.id IS NULL;
```



## 删除语句 ```DELETE```

**注意：就是删除一行或者多行的记录**



### 语法

#### 方式一：```DELETE```

- 单表中记录的删除

```mysql
DELETE FROM 表名 WHERE 筛选条件
```

- 多表中记录的删除

```mysql
DELETE 别名1, 别名2, 别名3, ...
FROM 表1 AS 别名1
【 INNER | LEFT | RIGHT JOIN 】表2 AS 别名2 ON 连接条件
【 INNER | LEFT | RIGHT JOIN 】 表3 AS 别名3 ON 连接条件
WHERE 筛选条件
```

##### 示例

- 删除单表中的记录：删除手机号以9结尾的女神信息

```mysql
DELETE FROM beauty
WHERE phone LIKE '%9';
```

- 删除多表中的记录：删除张无忌的女朋友的信息

```mysql
DELETE BE 
FROM beauty AS BE
INNER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
WHERE BE.boyfriend_id = 1;
```

- 删除黄晓明的信息以及他女朋友的信息

```mysql
DELETE BE, BO
FROM beauty AS BE
INNER JOIN boys AS BO
ON BE.boyfriend_id = BO.id
WHERE BE.boyfriend_id = 3;
```



#### 方式二：```TRUNCATE```

```mysql
TRUNCATE TABLE 表名;
```

注意：```TRUNCATE```只能删除整个表，不能加筛选条件



#### 两种删除方式比较

|                                | ```DELETE```             | ```TRUNCATE```      |
| ------------------------------ | ------------------------ | ------------------- |
| 可否加```WHERE```筛选条件      | 可以                     | 不可以              |
| 效率                           | 低                       | 高                  |
| 删除自增长列后再插入记录时的值 | 自增长列的值从断点处开始 | 自增长列的值从1开始 |
| 是否有返回值                   | 有                       | 无                  |
| 能否回滚                       | 可以                     | 不可能              |





# DDL 数据定义语言

DDL = Data Definition Language

就是库和表的管理



## 内容

- 库的管理：**创建、修改和删除**
- 表的管理：**创建、修改和删除**
- 对应的数据类型



## 库的管理

包括：创建、修改和删除

### 库的创建

```mysql
CREATE DATABASE 【 IF NOT EXISTS 】 库名;
```

注意：```IF NOT EXISTS```可以省略，加上它是为了防止创建已经已经存在的数据库

### 库的修改

- 重命名

```mysql
# 注意，这个重命名方法在MySQL中不支持
# 要重命名的话，需要先停止MySQL服务，然后再操作系统中修改数据库对应的名字，然后再重启服务
RENAME DATABASE books TO 新库名
```

- 修改库的字符集

```mysql
ALTER DATABASE Books CHARACTER SET gbk;
```

### 库的删除

```mysql
DROP DATABASE IF EXISTS 库名;
```



## 表的管理

包括：创建、修改和删除

### 表的创建

```mysql
CREATE TABLE 表名(
    列名 列的类型 【 (长度) 列级约束 】,
    列名 列的类型 【 (长度) 列级约束 】,
    列名 列的类型 【 (长度) 列级约束 】,
    ...
    列名 列的类型 【 (长度) 列级约束 】,
)
```

#### 示例

- 创建Book表

```mysql
CREATE TABLE Book(
  id INT,
  bName VARCHAR(20),
  price DOUBLE,
  authorId INT,
  publishData DATETIME
);
DESC Book;
```

- 创建author表

```mysql
CREATE TABLE author(
  id INT,
  au_name VARCHAR(20),
  nation VARCHAR(10)
)
DESC author;
```

### 表的修改

- 语法简要

```mysql
ALTER TABLE 表名
【 ADD | DROP | MODIFY | CHANGE 】 COLUMN 列名 【 列类型 约束 】
```

- 添加列

```mysql
ALTER TABLE 表名
ADD COLUMN 新列名 【 列类型 列级约束 】
```

- 修改列的类型或约束

```mysql
ALTER TABLE 表名
MODIFY COLUMN 列名 新类型 新约束

# 注意，如果要修改字段即列的字符集，MODIFY不起作用，需要用CHANGE COLUMN
```

- 修改列名

```mysql
ALTER TABLE 表名
CHANGE COLUMN 旧列名 新列名 【 列类型 约束 】

# 修改列的字符集
ALTER TABLE author 
CHANGE COLUMN 列名 不变列名 VARCHAR(20) CHARACTER SET utf8;
```

- 删除列

```mysql
ALTER TABLE 表名
DROP COLUMN 列名
```

- 修改表名

```mysql
ALTER TABLE 旧表名 RENAME TO 新表名;
```



### 表的删除

```mysql
DROP TABLE 【 IF EXISTS 】 表名
```



### 表的复制

#### 仅复制表的结构

即仅复制表的各个字段【列】，得到的新表里面没有数据记录，是空的

```mysql
CREATE TABLE 新表名 LIKE 旧表名;
```

#### 复制表的结构和数据

即不仅仅复制表的结构，还复制表的数据记录

- 复制全部数据记录

```mysql
CREATE TABLE 新表
SELECT * FROM 旧表; 
```

- 复制部分数据记录

```mysql
CREATE TABLE 新表
SELECT * FROM 旧表
WHERE 筛选条件
```

- 仅复制某些字段

```mysql
CREATE TABLE 新表
SELECT 列1，列2
FROM 旧表
WHERE 0;
```



### 创建表或库的惯用写法

- 创建库

```mysql
DROP DATABASE IF EXISTS 旧库名
CREATE DATABASE 新库名
```

- 创建表

```mysql
DROP TABLE IF EXISTS 旧表名
CREATE TABLE 新表名
```



## 常见数据类型

- 数值型
  - 整型
  - 小数（定点数、浮点数）
- 字符型
  - 短文本：```CAHR```，```VARCHAR```
  - 长文本：```TEXT```, ```BLOB```

- 日期型



### 数值型

#### 整型

- 分类

| 整型名称                | 占用字节数 |
| ----------------------- | ---------- |
| ```TINYINT```           | 1          |
| ```SMALLINT```          | 2          |
| ```MEDIUMINT```         | 3          |
| ```INT```/```INTEGER``` | 4          |
| ```BIGINT```            | 8          |

- 特点

1. 如果不设置有无符号，默认是**有符号**；如要设置无符号，需要添加```UNSIGNED```  关键字

2. 如果插入的数值超出整型范围，会报```out of range```  异常，并且插入的是临界值

3. 如果不设置长度（用来显示），会有默认长度

   长度代表显示的最大宽度；若不够会用```0```在左边填充，但必须搭配```ZEROFILL```一起使用

#### 小数

|  分类  |             语法              |
| :----: | :---------------------------: |
| 定点型 |  `DEC(M,D)`, `DECIMAL(M, D)`  |
| 浮点型 | `FLOAT(M, D)`, `DOUBLE(M, D)` |

- 特点

1. `M`表示整数部分+小数部分的（总）长度

   `D`表示小数部分的长度

   如果超过值的范围，则插入临界值

2. `M`和`D`都可以省略

   如果是`DECIMAL`，则`M`默认为10，`D`默认为0

   如果是`FLOAT`或`DOUBLE`，则根据插入数值的精度来决定显示精度

3. 定点型精度较高，适合要求数据精度要求较高（如货币）的运算

### 字符型

| 字符类型              | 用途                 |
| --------------------- | -------------------- |
| `CHAR`，`VARCHAR`     | 较短的文本           |
| `BINARY`，`VARBINARY` | 较短的二进制         |
| `ENUM`                | 保存枚举             |
| `SET`                 | 保存集合             |
| `TEXT`                | 保存较长的文本       |
| `BLOB`                | 保存较大的二进制文件 |

- `CHAR`和`VARCHAR`的比较

|           |            `CHAR`             |          `VARCHAR`           |
| :-------: | :---------------------------: | :--------------------------: |
|   写法    |           `CHAR(M)`           |         `VARCHAR(M)`         |
| `M`的含义 | 最大字符数，可以省略，默认为1 | 最大字符数，**不**可以省略， |
|   特点    |        固定长度的字符         |        可变长度的字符        |
| 空间耗费  |           比较耗费            |           比较节省           |
|   效率    |              高               |              低              |

- `ENUM`的例子

```mysql
CREATE TABLE tab_char(
	c1 ENUM('a','b','c')
);
INSERT INTO tab_char VALUES('a');
INSERT INTO tab_char VALUES('b');
INSERT INTO tab_char VALUES('c');
INSERT INTO tab_char VALUES('m'); # 报错，因为m不在枚举类型的值里面
INSERT INTO tab_char VALUES('A'); # 可以，因为不区分大小写
```

- `SET`的例子

```mysql
CREATE TABLE tab_set(
	s1 SET('a','b','c','d')
);
INSERT INTO tab_set VALUES('a');
INSERT INTO tab_set VALUES('A,B');
INSERT INTO tab_set VALUES('a,c,d');
```



### 日期型

| 日期类型    | 用途           |
| ----------- | -------------- |
| `DATE`      | 只保存日期     |
| `TIME`      | 只保存时间     |
| `YEAR`      | 只保存年份     |
| `DATETIME`  | 保存日期和时间 |
| `TIMESTAMP` | 保存日期和时间 |

- `DATETIME`和`TIMESTAMP`的比较

|              | `DATETIME`  | `TIMESTAMP` |
| ------------ | ----------- | ----------- |
| 占用字节     | 8           | 4           |
| 时间日期范围 | 1000 ~ 9999 | 1970 ~ 2038 |
| 受时区等影响 | 不受影响    | 受影响      |



## 常见约束



### 约束的含义和目的

是一种限制，用于限制表中的数据，保证表中数据的准确和可靠



### 语法

```mysql
CREATE TABLE 表名(
	字段名 字段类型 列级约束, # 有列级约束
    字段名 字段类型 列级约束,
    ...
	字段名 字段类型, # 无列级约束
    字段名 字段类型,
    ...
	表级约束
)
```



### 分类

- 有**六**大约束

| 约束类型      | 含义                                                         |
| ------------- | ------------------------------------------------------------ |
| `NOT NULL`    | 非空，保证该字段的值不能为`NULL`                             |
| `DEFAULT`     | 默认，保证该字段有默认值                                     |
| `UNIQUE`      | 唯一，保证该字段具有唯一性，可以为`NULL`（但只能有一个`NULL`） |
| `CHECK`       | 检查约束（MySQL不支持）                                      |
| `PRIMARY KEY` | 主键，保证该字段具有唯一性，并且非空                         |
| `FOREIGN KEY` | 外键，限制两个表的关系，保证该字段的值必须来自主表的关联列的值 |

其中`FOREIGN KEY`，在哪个表中添加，那个表就是**从表**，而引用的关联列所在的表是**主表**



### 添加时机

- 在创建表时
- 在修改表时



### 约束的添加分类

| 列/表级约束 | 是否支持                                   |
| ----------- | ------------------------------------------ |
| 列级约束    | 六大约束语法都支持，但**外键约束没有效果** |
| 表级约束    | 除了**非空**、**默认**，其他都支持         |



### 主键和唯一的对比

|                  | 主键`PRIMARY KEY`      | 唯一`UNIQUE`   |
| ---------------- | ---------------------- | -------------- |
| 是否保证唯一性   | 是                     | 是             |
| 是否允许为`NULL` | 否                     | 是             |
| 表中可否有多个   | 最多一个（字段是主键） | 可以有多个     |
| 是否允许组合     | 是（但不推荐）         | 是（但不推荐） |



### 外键的特点

- 外键关系是设置在**从表**中的
- 从表外键列的类型和主表关联列的类型要求**一致**或者**兼容**，名称可以不同
- 主表的关联列必须是一个**KEY**（一般为主键或唯一）
- 插入数据时，先插入主表，后插入从表；删除数据时，先删除从表，后删除主表



### 约束添加和删除示例

#### 创建表时添加约束

- 添加列级约束（只支持默认、非空、主键和唯一）

  语法：**直接在字段名和类型后面追加 约束类型即可**

```mysql
USE students;
DROP TABLE stuinfo;
CREATE TABLE stuinfo(
	id INT PRIMARY KEY,                                #主键
	stuName VARCHAR(20) NOT NULL UNIQUE,               #非空
	gender CHAR(1) CHECK(gender='男' OR gender ='女'),  #MySQL支持检查语法，但无效
	seat INT UNIQUE,                                   #唯一
	age INT DEFAULT 18,                                #默认约束
	majorId INT REFERENCES major(id)                   #外键，支持列级添加外键约束，但无效
);

# 创建上面从表所关联的主表
CREATE TABLE major(
	id INT PRIMARY KEY,
	majorName VARCHAR(20)
);

# 查看stuinfo中的所有索引，包括主键、外键和唯一
SHOW INDEX FROM stuinfo;
```



- 添加表级约束

  语法：在各个字段的最下面添加 **【`CONSTRAINT` 约束名】 约束类型（字段名）**

```mysql
DROP TABLE IF EXISTS stuinfo;
CREATE TABLE stuinfo(
	id INT,
	stuname VARCHAR(20),
	gender CHAR(1),
	seat INT,
	age INT,
	majorid INT,
	
	CONSTRAINT pk PRIMARY KEY(id),                                        # 主键
	CONSTRAINT uq UNIQUE(seat),                                           # 唯一键
	CONSTRAINT ck CHECK(gender ='男' OR gender  = '女'),                   # 检查
	CONSTRAINT fk_stuinfo_major FOREIGN KEY(majorid) REFERENCES major(id) # 外键
);

# 查看stuinfo中的所有索引，包括主键、外键和唯一
SHOW INDEX FROM stuinfo;
```



- 通用写法

```mysql
CREATE TABLE IF NOT EXISTS stuinfo(
	id INT PRIMARY KEY,
	stuname VARCHAR(20),
	sex CHAR(1),
	age INT DEFAULT 18,
	seat INT UNIQUE,
	majorid INT,
    
	CONSTRAINT fk_stuinfo_major FOREIGN KEY(majorid) REFERENCES major(id)
);
```



#### 修改表时添加约束

语法

```mysql
# 添加列级约束
ALTER TABLE 表名 MODIFY COLUMN 字段名 字段类型 新约束

# 添加表级约束
ALTER TABLE 表名 ADD 【 CONSTRAINT 约束名 】 约束类型(字段名) 【 外键引用 】
```



- 添加非空约束

```mysql
ALTER TABLE stuinfo MODIFY COLUMN stuname VARCHAR(20) NOT NULL;
```

- 添加默认约束

```mysql
ALTER TABLE stuinfo MODIFY COLUMN age INT DEFAULT 0;
```

- 添加主键

```mysql
# 列级
ALTER TABLE stuinfo MODIFY COLUMN id INT PRIMARY KEY;

# 表级
ALTER TABLE stuinfo ADD 【 CONSTRAINT pk 】 PRIMARY KEY(id);

# 注意，删除主键使用DROP PRIMARY KEY（并且先CHANGE COLUMN）
ALTER TABLE stuinfo CHANGE COLUMN id id INT;
ALTER TABLE stuinfo DROP PRIMARY KEY;
```

- 添加唯一键

```mysql
# 列级
ALTER TABLE stuinfo MODIFY COLUMN seat INT UNIQUE;

# 表级
ALTER TABLE stuinfo ADD 【 constraint st_uq 】 UNIQUE(seat)
```

- 添加外键

```mysql
ALTER TABLE stuinfo ADD CONSTRAINT fk_stu_major FOREIGN KEY(majorid) REFERENCES major(id);

```



### 修改表时删除约束

- 删除非空约束（非空只支持列级）

  即使用`MODIFY COLUMN`，后面约束用`NULL`

```mysql
ALTER TABLE stuinfo MODIFY COLUMN stuname VARCHAR(20) NULL;
```

- 删除默认约束（默认只支持列级）

  即使用`MODIFY COLUMN`，后面约束置空即可

```mysql
ALTER TABLE stuinfo MODIFY COLUMN age INT;
```

- 删除主键约束

  使用`DROP PRIMARY KEY`

```mysql
ALTER TABLE stuinfo DROP PRIMARY KEY;
```

- 删除唯一约束

  使用`DROP INDEX 列名`

```mysql
ALTER TABLE stuinfo DROP INDEX 列名;
```

- 删除外键约束

```mysql
ALTER TABLE stuinfo DROP FOREIGN KEY 外键约束名;

ALTER TABLE stuinfo DROP FOREIGN KEY fk_stuinfo_major;
```











# TCL 事务控制语言

TCL = Transaction Control Language



幻读一般就是针对插入（```INSERT```）的













```mysql

```









































```mysql
```



```sql


```



【2021-08-15】B站视频看到第100集

【2021-08-23】B站视频看到第124集（刚开始）

【2021-08-27】B站视频看到第152集（刚开始）



# DML 数据管理语言



DML = Data Management Language



# DDL 数据定义语言

DDL = Data Definition Language



# TCL 事务控制语言

TCL = Transaction Control Language