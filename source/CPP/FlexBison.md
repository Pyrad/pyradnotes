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


## Chapter 2 Using Flex

### Regular Expressions

这一节主要介绍了用于正则表达式中的metalanguage，即用于匹配字符的特殊字符标识。

^ -> circumflex

virtue n. 高尚的道德，德行；美德，

punctuation n. 标点符号，标点符号用法

#### Regular Expression Examples

一个用来匹配 Fortan-style 的数字的正则表达式

```flex
[-+]?([0-9]*\.?[0-9]+|[0-9]+\.)(E(+|-)?[0-9]+)?
```

#### How Flex Handles Ambiguous Patterns

flex 解决 conflict 的两个办法

- 当输入匹配时，取最长的匹配

- 当有相同匹配时，取最先出现的匹配

#### Context-Dependent Tokens

Flex 提供了叫 start state 的状态，用来解决和上下文相关的 token 匹配问题。


### File I/O in Flex Scanners

（这一节讲的主要是flex如何读入文件，而不是标准输入）

flex scanner 默认的输入是 `stdin` （标准输入），由变量 `yyin` 标识。

如果要改变这个默认输入，比如使其从文件中读入字符，可以对 `yyin` 变量进行赋值。

比如讲打开文件的指针赋值给 `yyin` 。

```cpp
yyin = fopen(argv[1], "r")
```

如果程序中对 `yyin` 没有赋值，那么 `yylex()` 函数会默认将其赋值到 `stdin` 。

这里看起来 `perror()` 也是 flex library 里面提供的函数。

lex scanner 扫描到 `yyin` 的结尾时，会调用函数 `yywrap()`。

这个做法原先的目的是，如果有下一个需要读入的文件， `yywrap()` 可以用来调整 `yyin` ，
然后返回 `0` ， 以便继续扫描。

如果没有下一个文件，当前已经读到了结尾，那么它就返回 `1` ，告诉 lex scanner 扫描已经结束。

这个机制目前看起来已经没有用了，但 flex 和 lex 仍然保留了这个机制。

目前的 flex 版本中，可以使用 `%option noyywrap` 来告诉 scanner 不需要调用函数 `yywrap()`。


### Reading Several Files

如果要连续读入（扫描）多个文件，flex 提供了函数 `yyrestart()` 。

这个函数的参数是文件指针，需要在 `yylex()` 之前调用。


```cpp
for (int i = 0; i < argc; i++) {
   // ...
   FILE *f = fopen(argv[i], "r");
   yyrestart(f);
   yylex();
   fclose(f);
   // ...
}
```

flex 也通过了 `YY_NEW_FILE` ，它相当于是 `yyrestart(yyin)` 。


### The I/O Structure of a Flex Scanner

flex 默认的输入是 `stdin` ，默认的输出是 `stdout` 。但它们都可以被更改。

#### Input to a Flex Scanner

最早的 lex 是从 `yyin` 中逐个字符读入进行扫描的。

Flex scanner 从 `stdin` 和文件读入的区别是，从文件中读入可以一次读入一大块，
但从 `stdin` 交互式读入时，它一次读入一个字符。

flex 有一个用来描述单个输入的数据结构 `YY_BUFFER_STATE` ，它通常包含一个文件指针，
以及其他一些变量和标识。

通常这个文件指针是和要读入的文件相关联的，但也可以直接创建一个没有关联到文件的 `YY_BUFFER_STATE` ，
从而直接扫描内存的中的字符串。

典型的使用过程，

- 使用函数 `yy_create_buffer` 创建一个 `YY_BUFFER_STATE` 结构，可以和文件相关联或不关联。

- 使用函数 `yy_switch_to_buffer` 告诉 scanner 使用刚才创建的 buffer 来扫描。

- 使用 `yylex()` 或其他（比如 `yyparse()` ） 调用扫描器开始扫描。

```cpp
YY_BUFFER_STATE bp;
extern FILE* yyin;

// ... whatever the program does before the first call to the scanner
if (!yyin)
   yyin = stdin; // default input is stdin

// YY_BUF_SIZE defined by flex, typically 16K
bp = yy_create_buffer(yyin, YY_BUF_SIZE );

// tell it to use the buffer we just made
yy_switch_to_buffer(bp);

// or yyparse() or whatever calls the scanner
yylex();
```

如果是扫描多个文件，还是要用到函数 `yyrestart()` 。
（还要创建对应个` YY_BUFFER_STATE` 结构？然后再 scan？）

还有其他的函数用来创建被扫描的buffer

- `yy_scan_string("string")` ： 扫描以 `\0` 字符结尾的字符串。

- `yy_scan_buffer(char *bas, size)` ： 扫描已知长度的buffer。

`YY_BUFFER_STATE` 使用 `yy_create_buffer()` 创建，
使用完毕时候可以使用 `yy_delete_buffer()` 来销毁。


允许重定义宏 `YY_INPUT` 提供了管理输入的最大灵活性。

```cpp
#define YY_INPUT(buf,result,max_size) ...
```

机制是，当 scanner 的 input buffer 为空时， `YYINPUT` 就会被调用。
`buf` 是（字符）缓冲区， `max_size` 是其长度， `result` 是读入的字符放置的位置（？）。

Flex 还提到了两个宏 `inptu()` 和 `unput()`。

- `input()` 是从输入流冲返回下一个字符。

- `unput(c)` 是把一个字符放回到输入流中去。


总结，三种管理输入层次

- 直接设置 `yyin` 来扫描文件

- 创建 ` YY_BUFFER_STATE` 来扫描

- 重定义 `YY_INPUT`。


#### Flex Scanner Output

早期版本的 lex 的行为，会在scanner 的结束处加入类似如下的规则，
用来匹配input中没有匹配到其他pattern的字符串，然后拷贝到输出里去。

```flex
. ECHO;

#define ECHO fwrite(yytext, yyleng, 1, yyout)
```

因为这样写容易出现bug，所以 flex 提供了 `%option nodefault` ，避免
加入这样一条默认的rule。

在这种情况下，如果其他的rule没有覆盖所有可能出现的情况， flex 就会报错。


### Start States and Nested Input Files

本节讲解了一个例子， 说明了如何创建、切换和销毁 `YY_BUFFER_STATE` ，
并利用它来读取扫描嵌套的 `#include<XXX>` 这样的文件。

在这个例子中，介绍了如何切换 `YY_BUFFER_STATE` ，并保留之前已经读到的内容，
并不使用 `yyrestart()` 重新开始扫描的技术。


以 `%x` 开始的行定义的是一个 start state 。

flex 默认会定义一个叫做 `INITIAL` 的 start state 。

在rule部分，用尖括号 `<` `>` 括起来的 start state ，后面跟上要匹配的pattern，
表示只有在这种 start state 的情况下，这种 pattern才能被匹配到。如下，

```cpp
%x IFILE
<IFILE>[^ \t\n\">]+ { /* ... */ }
```

`%x` 表示 exclusive start state，表示只有这种状态下的pattern才能被匹配到。

`%s` 表示 inclusive start state，表示其他状态下的pattern都能被匹配到。

在 action code 里面，有一个 `BEGIN` 的宏，用来切换 start state 。


`yylineno` 是 flex 提供的一个用来记录当前行号的 int 变量。
它通过 `%option yylineno` 来声明，flex 据此定义一个叫做 `yylineno` 的变量，用来维护行号。

它的效果是，每当 scanner 读到一个换行符的时候，这个变量就自增 `1` ；如果 scanner 有所谓的
"backs up over a newline" ， 这个变量自减 `1` 。

flex 提供的宏 `yytermnate()` 返回一个值 `YY_NULL` ，它实际上是值 `0` 。
Bison parser 把它当做是输入的终结标识。


`<<EOF>>` 是一个特殊的 pattern ，扫描到文件结尾时，会匹配到它。

### Symbol Tables and a Concordance Generator

这一节提到的 **symbol table** ，概念和编译器中的 symbol table 是相同的。

它是用来记录输入中的名字的。

这节提到了一个叫做 **concordance** 的概念，它实际上就是用来记录输入中每个word出现的行号（以及文件名）。

**concordance** 叫关键字似乎比较合适。


#### Managing Symbol Tables

本节主要介绍了一个如何建立 symbol table 的例子，通过这个例子说明了 flex scanner 用到的一些特性。

本节提到了 `yylineno` 这个 option。

`yylineno` 是 flex 提供的一个用来记录当前行号的 int 变量。
它通过 `%option yylineno` 来声明，flex 据此定义一个叫做 `yylineno` 的变量，用来维护行号。

它的效果是，每当 scanner 读到一个换行符的时候，这个变量就自增 `1` ；如果 scanner 有所谓的
"backs up over a newline" ， 这个变量自减 `1` 。

但是如果是读入类似 `#include` 这样的形式，那么仍然需要手动把 `yylineno` 设置为 `1`
（ `#include` 开始时），或设置为之前保存的值（`#include` 结束时）。

提到另外一个 option 是 `case-insensitive` ， 它表示 flex 不区分输入的大小写，不过它也不会修改输入。

本节例子里面提到的 symbol table ，其实就是一个 `symbol` 数据结构的数组，每个元素包含名字（指针），
以及一个reference的列表。


本节的例子中，还提到了一个叫做 `hashing with linear probing` 的技术。

它是通过计算hash的办法，首先把一个字符串转换为一个数组的索引，然后查看是否是要搜索的元素。
如果不是，就从此处开始，依次向后查找。

### C Language Cross-Reference

本节讲述了另外一个例子，其中包含了本章中所学到的 flex 的技术。


在 lex 文件的 declaration 部分，似乎可以对pattern起名字，以便后续使用。
比如，例子里面给如下三个pattern起了名字，

```flex
UCN (\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8})
EXP ([Ee][-+]?[0-9]+)
ILEN ([Uu](L|l|LL|ll)?|(L|l|LL|ll)[Uu]?)
`

