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
```





# DML 数据管理语言

DML = Data Management Language



# DDL 数据定义语言

DDL = Data Definition Language



# TCL 事务控制语言

TCL = Transaction Control Language