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