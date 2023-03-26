
# Different ways to format a string in Python


[Python 3's f-Strings: An Improved String Formatting Syntax (Guide)](https://realpython.com/python-f-strings/)

[https://realpython.com/python-f-strings/](https://realpython.com/python-f-strings/)

## Old-school String formatting in Python

### Option 1 %-formatting

这种方式在python一开始就有。

在字符串中直接使用 `%` 来格式化单个变量
```python
>>> name = "Eric"
>>> "Hello, %s." % name
'Hello, Eric.'
```

在字符串中直接使用 `%` 来格式化多个变量
```python
>>> name = "Eric"
>>> age = 74
>>> "Hello, %s. You are %s." % (name, age)
'Hello Eric. You are 74.'
```

缺点：当需要格式化的字符串中有很多变量参数和长字符串时，变的不方便。


### Option 2 str.format() 函数

这种方式在python 2.6中加入。

可以按次序格式化参数
```python
>>> "Hello, {}. You are {}.".format(name, age)
'Hello, Eric. You are 74.'
```

可以通过索引格式化参数来改变出现的顺序
```python
>>> "Hello, {1}. You are {0}.".format(age, name)
'Hello, Eric. You are 74.'
```

还可以通过临时命名来传递需要格式化的参数
```python
>>> person = {'name': 'Eric', 'age': 74}
>>> "Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])
'Hello, Eric. You are 74.'
```

还能使用`**`来unpack一个字典参数
```python
>>> person = {'name': 'Eric', 'age': 74}
>>> "Hello, {name}. You are {age}.".format(**person)
'Hello, Eric. You are 74.'
```


缺点：和`%` 方式类似的，当需要格式化的字符串中有很多变量参数和长字符串时，变的不方便。


## f-Strings: A New and Improved Way to Format Strings in Python

在字符串前面加上`f`字符（大写的`F`也可以），然后在花括号中直接使用参数名
```python
>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
>>> F"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
```

除此之外，还能有其他方便的用法

- 数学计算
```python
>>> f"{2 * 37}"
'74'
```

- 调用函数
```python
>>> def to_lowercase(input):
...     return input.lower()

>>> name = "Eric Idle"
>>> f"{to_lowercase(name)} is funny."
'eric idle is funny.'
```

- 调用类的成员函数
```python
>>> f"{name.lower()} is funny."
'eric idle is funny.'
```

- 调用类的`__str__()`方法来格式化class object
	- 需要注意的是，f-string默认是使用类的`__str()__`方法
	- 如果要使用类的`__repr()__`方法，就需要在变量参数后面加上`!r`
```python
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

>>> new_comedian = Comedian("Eric", "Idle", "74")
>>> f"{new_comedian}"
'Eric Idle is 74.'

>>> f"{new_comedian}"
'Eric Idle is 74.'
>>> f"{new_comedian!r}"
'Eric Idle is 74. Surprise!'
```

- 组合多个字符串成为一个长字符串
	- 第一种办法是用圆括号`()`分隔多行
	- 第二种办法是使用反斜杠`\`分隔多行

```python
# 1st way
>>> name = "Eric"
>>> profession = "comedian"
>>> affiliation = "Monty Python"
>>> message = (
...     f"Hi {name}. "
...     f"You are a {profession}. "
...     f"You were in {affiliation}."
... )
>>> message
'Hi Eric. You are a comedian. You were in Monty Python.'
>>> type(message)
<class 'str'>

# 2nd way
>>> message = f"Hi {name}. " \
...           f"You are a {profession}. " \
...           f"You were in {affiliation}."
...
>>> message
'Hi Eric. You are a comedian. You were in Monty Python.'
>>> type(message)
<class 'str'>
```


## Python f-Strings: The Pesky Details

有一些需要注意的细节

- Quotation marks
	- 可以在花括号`{}`里面直接使用字符常量，而不是参数名，这样就直接显示常量字符
	- 要显示双引号`"`，就使用反斜杠`\`
	- 使用字典的时候，如果key是字符串，那么f-string就要使用双引号`"`，否则会出错
```python
>>> f"{'Eric Idle'}"
'Eric Idle'

>>> f'{"Eric Idle"}'
'Eric Idle'

>>> f"""Eric Idle"""
'Eric Idle'
 
>>> f'''Eric Idle'''
'Eric Idle'

>>> f"The \"comedian\" is {name}, aged {age}."
'The "comedian" is Eric Idle, aged 74.'

# Remember to use double quote instead of single quote
# for dictionaries
>>> comedian = {'name': 'Eric Idle', 'age': 74}
>>> f"The comedian is {comedian['name']}, aged {comedian['age']}."
The comedian is Eric Idle, aged 74.

>>> comedian = {'name': 'Eric Idle', 'age': 74}
>>> f'The comedian is {comedian['name']}, aged {comedian['age']}.'
  File "<stdin>", line 1
    f'The comedian is {comedian['name']}, aged {comedian['age']}.'
                                    ^
SyntaxError: invalid syntax
```

- 显示花括号
	- 要显示花括号，就要两个一起使用，才显示一个花括号
	- 写三个花括号，最后也只显示一个
	- 要显示两个花括号，需要写4个（依次类推）
```python
>>> f"{{70 + 4}}"
'{70 + 4}'

>>> f"{{{70 + 4}}}"
'{74}'

>>> f"{{{{70 + 4}}}}"
'{{70 + 4}}'
```


- 在f-string中表达式求值的部分，不能使用反斜杠`\`
	- 代替办法就是先求值，再使用求值之后的变量
```python
>>> f"{\"Eric Idle\"}"
  File "<stdin>", line 1
    f"{\"Eric Idle\"}"
                      ^
SyntaxError: f-string expression part cannot include a backslash

>>> name = "Eric Idle"
>>> f"{name}"
'Eric Idle'
```




















