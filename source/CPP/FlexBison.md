# Flex & Bison

[Yacc介绍 - Sina Blog](http://blog.chinaunix.net/uid-8867796-id-358793.html)

# Flex & Bison by John Levine



## Chapter 1

lexical analysis (lexing/scanning)

- divides input to meaningful chunks (tokens)

syntax analysis (parsing)

- figures out how tokens relate to each other



YACC = Yet Another Compiler Compiler
Flex = Fast Lexical Analyzer Generator



### Lexical Analysis and Parsing


[Flex link](http://flex.sourceforge.net/)

[Bison link](http://www.gnu.org/software/bison/)

Flex & Bison (Linux) both depend on GNU m4 macroprocessor

Flex & Bison (Windows) are available in Cygwin.

A flex program basically consists of a list of regexps with instructions about
what to do when the input matches any of them, known as "actions".

基本上，flex就是一系列的正则表达式，跟上对应的action，表示对input如何处理。

flex把对应的正则表达式转为一种叫做DFA（Deterministic Finite Automation）的内部形式，以便提高处理速度。


### Regular Expressions and Scanning

#### Our First Flex Program

flex program 分三部分，由 `%%` 分开

- 第一部分是 declarations & option settings。

  在这一部分中，位于 `%{` 和 `%}` 中的C代码，会被逐字逐句地（verbatim）拷贝的生成的源代码文件中靠近开始的地方。

- 第二部分是 pattern 和 actions 的列表。

  在这部分中，格式是 pattern 跟上对应的C处理代码。

  pattern **必须** 是从行数开始；如果行首有空白的话，flex 会把任何以空白符起始的行原封不动地拷贝到生成的源代码中去。

  C处理代码可以是一行statement，或者是由 `{` 和 `}` 包起来的多行代码。
  
  另外的一个约定是， 如果 input 同时匹配多个 pattern ， 那么 `flex` 选择较早出现的那个作为匹配。
  
  如果使用双引号 （ `""` ） 把 pattern 括起来，就是告诉 `flex` 它是一个纯字符串，不需要以正则表达式的方式展开。
  
  如果一个 pattern 后面的 action 是空的（即空白，或者空的花括号 `{}` ），就表示遇到这样的 pattern 不做任何操作。
  
  在 action 中， 可以 return 一个预定义的 token （实质就是一个 int ），而且在 return 之前，可以把 匹配到的输入 `yytext` ，
  存储到 `yylval` 中，以便在调用 `yylex()` 的程序处对其引用。

- 第三部分是 C 代码，它会被直接拷贝到生成的scanner（程序）中。

在 `flex` 中， `yytext` 指向的是当前的pattern 匹配的input。

`flex` 默认赋予 scanner 函数的名字是 `yylex()` ，它默认会从 `stdin` 读入输入。



使用 `flex`

- 使用 `flex` 把 `lex` 代码转换为 C 代码。

  ```cpp
  flex fb1-1.l
  ```
  
  这个命令默认会生成一个叫做 `lex.yy.c` 的 C 代码文件。

- 然后使用 C 编译器，编译这个 C 代码文件，同时链接 `flex` library（ `-lfl` ）

  ```cpp
  cc lex.yy.c -lfl
  ```

  这个命令默认会生成一个叫做 `a.out` 的可执行程序（在Windows Cygwin下，名字是 `a.exe`）
  
  执行它，它从 stdin 接受输入，输入结束，以 `^D` （ `Ctrl` + `D` ）结束，得到如下结果。
  
  ```shell
  longc@LONGC-5520L ~/pyrad/flexBison
  $ ./a.exe
  The boy stood on the burning deck
  shelling peanuts by the peck
       2      12      63
  ```
  
  这里最后一行的 `2      12      63` 就是程序的输出结果。
  

#### Programs in Plain Flex

介绍了一个非常简单的，把英式单词转换为美式单词的 `flex` 程序。


#### Putting Flex and Bison Together


#### The Scanner as Coroutine

本节，提到了如何使用 `yylex()` ，从而不断地基于从其返回的 token ，做相应的处理。

这里还提到了 `flex` 和 `bison` 的由来和历史。

#### Grammars and Parsing


CFG = Context-Free Grammar （上下文无关文法）

根据一些规则（rule），解释器把一系列的 token 转化为 parse tree ，

计算机解释器处理的大多数语言的种类，属于 CFG，即上下文无关文法。

用来记录 CFG 的标准，就是 BNF（Backus-Naur Form  即巴科斯-诺尔范式）。

BNF 是由1960年代 Algol 60 委员会的两名成员的名字命名的。

计算机领域所称的 CFG，语言学家通常叫做 PSGs，或者 type-3，但它们是同一回事。

PSGs = Phrase-Structure Grammars （短语结构文法）

Type-3 language

BNF = Backus-Naur Form （巴科斯-诺尔范式）


```yacc
<exp> ::= <factor>
      | <exp> + <factor>
<factor> ::= NUMBER
      | <factor> * NUMBER
```

上面的例子里，每一行都是一条规则（rule），是用来创建 parse tree的一条分支的。

`::=` 可以读作 `is a` 或者 `becomes`。

`|` 符号可以读作 `or` ， 它同样是用来创建 parse tree的一条分支的另一种办法。

Rule 左边的名字，叫做 `symbol` 或 `term`。

按照惯例， 所有的 token 都被当做是 `symbol` ， 但有些 `symbol` 却不是 `token`。

也就是说， token 是 symbol 的子集（token 范围小，symbol 范围大）


#### Bison’s Rule Input Language

（特意地）Bison 被设计成和 flex 具有同样结构的三部分，即，

1. declarations

2. rules

3. C code

同样地，在第一部分中，位于 `%{` 和 `%}` 中的C代码，
会被逐字逐句地（verbatim）拷贝的生成的源代码文件中靠近开始的地方。

同样位于第一部分中的，还有 token 的声明，以 `%token` 开始。
这些指令，告诉 bison 这些名字在parser中被认为是 token。

第二部分中，是以简化版BNF形式列出的规则（rules）。

bison 规则中，使用的是单个分号 `;` 用来分隔不同的rule。

而在同一条rule中，symbol 和 action 之间，使用的是冒号 `:` （而不是 `::=` ）。

第一条rule的左边出现的 symbol，叫做 *start symbol* 。

一个 symbol 对应的值（value），在 action 中用 `$$` 表示。



