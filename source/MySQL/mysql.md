# MySQL 基本操作

启动服务/停止服务：

```shell
# windows command line中
net stop <mysql_name>
net start <mysql_name>
```

连接数据库

```shell
# 连接数据库
mysql -h localhost -P<PortNum> -u <root> -p<passward>
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
select database;

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



基本语法

```sql
SELECT 查询列表 from 表名
```

查询列表可以是

- 表中的字段
- 常量
- 表达式
- 函数

查询的结果是一个虚拟的表格

```sql
# 查询单个字段
SELECT last_name FROM employees;

# 查询多个字段
SELECT last_name,salary,email FROM employees;
SELECT * FROM empolyees;

# 可以使用着重号``，以表明是一个字段名，而不是关键字
SELECT `NAME` FROM stuinfo

# 查询常量值
SELECT 100;
SELECT 'string'; #字符串单引号或双引号都可以

# 查询表达式
SELECT 100%98;

# 查询函数
SELECT VERSION();

# 起别名
# （1）方便理解（2）【连接查询时】如果遇到多个同名的字段，可以区分
# 其中AS可以省略，别名可以加双引号或单引号以防其中的某些字符串别认定为关键字
SELECT 100%98 AS <NEW_NAME>;
SELECT last_name AS xing, first_name AS Ming FROM employee;

# 去重
SELECT DISTINCT department_id FROM employees;


/*去重*/
SELECT DISTINCT department_id FROM employees;

/*
如果要连接字符串,就用concat函数
加号"+"的作用：在SQL中只当做运算符
（1）两个都是数值型，做加法运算
SELECT 100 + 90; --> 190
（2）其中一个为字符型，将其转换成数值型做运算
     如果转换成功，继续做加法；如果失败，字符型会被转换为0做计算
     如果其中一个为null，结果肯定是null
     SELECT '123' + 90; --> 213
     select 'john' + 90; --> 90
     SELECT null + 90; --> null
*/
# 员工的名和姓连接在一起
SELECT concat(first_name, last_name) as Ename FROM employees;
# 员工的名和姓连接在一起,用逗号隔开
SELECT concat(first_name, ',', last_name) as Ename FROM employees;

# IFNULL函数
/*
如下函数选择commission_pct字段和ifnull返回的新字段CMP，
ifnull返回的是：如果第一个参数是原本是null，就用0代替，否则不代替。
 */
select ifnull(commission_pct, 0) as CMP, commission_pct from employees;
# 注意concat返回的是一个新的字段，这个字段可以重命名；
# 但里面的每个被连接的不能重命名
select concat(first_name, ',', last_name, ',', job_id, ',', ifnull(commission_pct, 0))  as CMP from employees;




/*** 条件查询 ***/
/*
 select 查询列表 from 表名 where 筛选条件

分类：
1. 按照条件表达式筛选
   条件运算符 >, <, =（等于）, !=, <>, >=, <=
2. 按逻辑表达式:主要用于连接表达式
   逻辑运算符: &&, ||, !, and, or, not
3. 模糊查询 
   like：一般和通配符%搭配使用,
         通配符%表示0到多个字符,
         通配符'_'表示单个任意字符,
         如果需要转义（1）用'\'即可（2）可以使用ESCAPE关键字指定
   between and:
		 提高了简洁度
         范围临界值是前小后大
         查询结果包含临界值
         两个临界值的类型要一致，或者能够隐式转换
   in: 需要用同样类型的列表, 
       用小括号包起来, 
       不支持通配符%
   is null:
       =或<>不能用于判断null值
       用IS NULL或IS NOT NULL来判断null值
       
   <=>
       安全等于符号，
       可以判断null值，也可判断普通类型的值
*/

# 查询工资大于12000的员工信息
select * from employees where salary > 12000;
# 查询部门编号不等于90号的员工名和部门编号
select last_name, department_id from employees where department_id != 90;

# 查询工资在10000到20000之间的员工名,工资和奖金 
select last_name, salary, commission_pct 
from employees
where salary >= 10000 and salary <= 20000;

# 部门编号不是在90到110之间,或工资高于15000的员工
select *
from employees
where department_id < 90 or department_id > 110 or salary > 15000;

# 查询员工名包含a的员工 （通配符用%）
select * from employees where last_name like '%a%';

# 查询员工名第三和第五个字符为a的员工名和工资
select last_name, salary from employees
where last_name like '__n_l%';

# 查询员工名第二个字符是下划线的员工
select last_name from employees
where last_name like '_\_%';
# 使用ESCAPE关键字指定转义字符
select last_name from employees
where last_name like '_k_%' escape 'k';

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

select * from employees where salary <=> 12000;

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
```





# DML 数据管理语言

DML = Data Management Language



# DDL 数据定义语言

DDL = Data Definition Language



# TCL 事务控制语言

TCL = Transaction Control Language