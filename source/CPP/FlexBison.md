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
```

## Chapter 3 Using Bison

### How a Bison Parser Matches Its Input

```yacc
statement: NAME '=' expression

expression: NUMBER '+' NUMBER
            | NUMBER '−' NUMBER
```

在 Bison 中， 一条 rule 由冒号 `:` 分为两部分。

左侧部分（symbol）叫做 left-hand side of the rule ， 即 LHS

右侧部分（symbols）叫做 right-hand side of the rule ， 即 RHS

不同的rule，可以有相同的 left-hand side （LHS） symbol 。

符号 `|` 表示有两条或多条rule有相同的LHS symbol 。

在输入中出现的 symbols ，或由 lex 返回的 symbols ， 叫做 terminal symbols，或 tokens。

而出现在（Bison）rule左侧的LHS symbol，叫做 nonterminal symbol，或 nonterminals。

terminal symbol 和 nonterminal symbol **必须不相同** ，token 不能出现在rule的左侧。

一条 rule 可以直接或间接地引用它自身（递归），从而使得分析较长的语句比较高效。


### Shift/Reduce Parsing

> A bison parser works by looking for rules that might match the tokens seen so far.

Bison parser 是根据当前已经看到的 tokens ， 查询是否有匹配的 rule，并以此进行所谓的 shift 和 reduce。

Bison parser 每次读到一个 token，但没有组成一条完整的 rule 的时候，它就把这个 token
压入到内部维护的一个 stack 里面，然后切换到一个新的、反应刚读到的 token 的 state 上。

这个动作叫做 **shift** 。

当 Bison parser 读到了组成一条完整 rule 右侧（RHS）的所有 symbols 的时候，它就把这些 symbols
从 stack 中都 pop 出来，然后把这条 rule 左侧（LHS）的symbol 压入 stack，同时切换到一个新 state上。

这个动作叫做 **reduction** 。（因为它减少了stack上的item数量）

每当 reduce a rule 的时候，它就会执行rule对应的user code。


这里举例说明如下的表达式是如何被 parse 的。

```cpp
fred = 12 + 13
```

假设有如下的 rule ，

```yacc
statement: NAME '=' expression

expression: NUMBER '+' NUMBER
            | NUMBER '−' NUMBER
```

每次读到一个 token，就会向内部的 stack 中 shift 这个 token ，过程如下，

第一次，读到 token `fred` ， 它是一个 `NAME` ， 但是不能组成一个完整的 rule（RHS），
故向 stack 中压栈（shift），

```cpp
fred
```

第二次，读到 token `=` ，同样地，它和已经在栈中的 token 也不能组成一个完整的 rule（RHS），
故继续向 stack 中压栈（shift），此时栈的内容如下

```cpp
fred =
```

第三次，读到 token `12` ，它是一个 `NUMBER`，同样地，它和已经在栈中的 token 也不能组成一个完整的 rule（RHS），
故继续向 stack 中压栈（shift），此时栈的内容如下

```cpp
fred = 12
```

之后第四次重复了上述的压栈过程（shift），此时栈的内容如下，

```cpp
fred = 12 +
```

当第五次读到 token `13` 时，它自己本身也不是一个完整的rule（RHS），因此先把它压入栈（shift），
此时栈中的内容如下，

```cpp
fred = 12 + 13
```

而这个时候，栈中的内容 `12 + 13` 对应的是下面 rule 的右侧（RHS），

```yacc
expression: NUMBER '+' NUMBER
            | NUMBER '−' NUMBER
```

因此，这个时候就发生了 reduction ，token `12` ， `+` 和 `13` 从栈中弹出，然后使用这个 rule 的
左侧（LHS）的symbol，把它压入栈中，那么此时栈中的内容如下，

```cpp
fred = expression
```

而此时栈中的内容又组成了 rule `statement: NAME '=' expression` 的右侧（RHS）部分，因此又产生了
reduce，把 token `fred` ， `=` ，和 `expression` 再从栈中弹出，然后把这条 rule 的左侧（LHS）的
symbol （这里是 statement）压入栈中，此时栈中的内容如下，

```cpp
statement
```

而这个 symbol 正是开始时的 symbol （ *start symbol* ），因此根据语法，读入的所有输入就是合法的。


#### What Bison’s LALR(1) Parser Cannot Parse

Bison parser 的两种 parse 方法。

- LALR(1)

  Look Ahead Left to Right with a one-token lookahead

- GLR

  Generalized Left to Right


这一节介绍的是 LALR(1) ，第9章介绍 GLR。

LALR 不能 parse 的语法

- 同样的输入，匹配语法树中多个（节点）

- 需要多读入的 token 多于一个的情况。

关于上面提到的第二条，这里举例进行了说明。

比如有如下的 rule ，

```yacc
phrase   : cart_animal AND CART
         | work_animal AND PLOW

cart_animal: HORSE | GOAT

work_animal: HORSE | OX
```

如果有输入 `HORSE AND CART` ，看看会发生什么。

首先，bison parser 读入第一个 token `HORSE` ，因为是 LALR(1)，所以实际上 bison parser
还知道下一个 token 是 `AND`。

此时，当前的 token 是 `HORSE` ，有两条 rule 都符合（`cart_animal` 和 `work_animal`），
但 bison parser 不能区分出来它们，原因是，即使考虑到下一个token是 `AND` ，它们也都是
`HORSE AND` ，并不能区分出来有所不同。

而只有当再多读（考虑）下一个 token `CART` 的时候，bison parser 才能发现它符合第一条 rule
的右侧 `cart_animal AND CART`，从而反推出来 `HORSE` 应该是 `cart_animal` ，而不是 `work_animal`。

但这已经是额外多读了两个 token 了，并不是 LALR(1) 的工作方式（它每次只多读一个 token），所以这种
情况下 bison parser 就不能正确分析了。

为了使得 bison parser 能够区分，可以把第一条 rule 改成如下的形式，

```yacc
phrase   : cart_animal CART
         | work_animal PLOW

cart_animal: HORSE | GOAT

work_animal: HORSE | OX
```

此时输入也需要变成 `HORSE CART`。

这种情况下，bison parser 读入了第一个 token `HORSE`，如果仅仅靠这个 token ，
bison parser 是区分不出来它是 `cart_animal` 还是 `work_animal` 的。

但因为 bison parser 会多读一个 token `CART` ，所以它通过比较就会发现符合第一条 rule
的右侧 symbols `cart_animal CART`，因此就会把 `HORSE` 判定为 `cart_animal`。

栈中的变化，首先是把 `HORSE` 压入栈，此时它组成了rule `cart_animal: HORSE | GOAT` 的 RHS，
因此 `HORSE` 出栈， `cart_animal` 入栈。

再读第二个 token `CART`，它也先入栈，此时栈中的内容就是 `cart_animal CART` ，它符合第一条 rule
的右侧 `phrase   : cart_animal CART` ， 因此 `cart_animal` 和 `CART`都出栈，symbol `phrase` 入栈。



在第7章中，讨论了shift/reduce的更多细节。

关于parse的技术，可以参考 Dick Grune 的 [Parsing Techniques: A Practical Guide](http://www.cs.vu.nl/~dick/PTAPG.html)


### A Bison Parser

和 Flex 相同， bison specification 同样拥有三部分的结构，

- 第一部分是 definition section，定义的是 parser的控制信息，并且设置了parser工作时的环境（变量等）。

- 第二部分包含了 parser 的 rule 。

- 第三部分包含了C代码，这些C代码会被逐字逐句地拷贝到最终的C程序中去。


Bison parser 通过把代码片段，添加到一个标准的框架文件中去，从而生成一个 C 程序。

Bison 中的 rules 会被编译成状态机的数组，每个状态是匹配输入的 token。

每当发生 rule reduce的时候，action 的 `$N` 和 `@N` 被转换为 C 代码，位于函数 `yyparse()` 里面的 switch-case 语句中。


### Abstract Syntax Trees

AST = Abstract Syntax Tree

AST is basically a parse tree that omits the nodes for the uninteresting rules.

AST 基本就是 parse tree 里面，去掉不具备实际意义的node，得到的结果。


### An Improved Calculator That Creates ASTs

bison parser 可以允许 symbol（token 和 nonterminals）关联到一个值上，并且允许定义这个值的类型。

在 Bison specification 的第一部分（definition section），可以使用 `%union` 来定义一些类型，以供 symbol（token & nonterminals）使用。

比如这里定义两种类型 `a` 和 `d` ，分别表示一个 AST 的指针类型，和一个 `double` 类型。

```yacc
%union {
   struct ast *a;
   double d;
}
```

在定义了类型之后，就可以在声明 token 的时候，同时声明这个 token 的类型，这个类型的名称，要放在尖括号中 `< >` 。

但如果不需要使用这个 token 对应的值，那么就可以不需要声明它的类型。

比如，下面的例子中，声明了 `NUMBER` 这个 token 对应一个值，其值的类型是 `double`。而 `EOL` 只是被声明是 token，没有关联一个值。

```yacc
%token <d> NUMBER
%token EOL
```

注意，第一章中提到过，一个 symbol 对应的值（value），在 action 中用 `$$` 表示。

也要注意，如果一个 rule 没有指明显式的 action code，那么Bison parser 会赋予其默认的 action code，即

```cpp
$$ = $1;
```

在 bison 中， `$1` 表示的是 rule的右侧（RHS）出现的第`1`个symbol。

另外，如果不使用一个 nonterminal symbol 的值，那么这个 nonterminal symbol 也可以**不声明**。


#### Literal Character Tokens

单个的char，可以在 lex 中直接当做 token 返回，它对应的 token number 实际上就是它自己的ASCII值。

比如 `"+"` ， 就可以直接返回（`yytext[0]`）。



在声明了 token 的类型之后，在 `flex` 中如果要使用一个输入的匹配 `yylval`，那么就得使用到和 C中`union`一样的语法。

比如，因为已经在 yacc 中声明了 token `NUMBER` 是一个 `<d>` ，即浮点类型，那么 `flex` 在处理时，如果要取得对应的值，
并把这个值设置到 `yylval` 中时，就需要使用 `yylval` 了（bison中可以不用这样写），然后才能返回这个 token `NUMBER`。

```lex
[0-9]+"."[0-9]*{EXP}? | "."?[0-9]+{EXP}? {
											yylval.d = atof(yytext); return NUMBER;
										 }
```

#### Building the AST Calculator

Flex 的输出名字默认是 `lex.yy.c` ，如果要指定新的名字，就需要使用 `-o` 选项，如下，

```shell
flex -oMyLexName.c OriginalLex.l
```

Bison 和 Flex 结合起来编译，可以写成 Mikefile 步骤如下

```makefile
fb3_1: fb3_1.l fb3_1.y fb3_1.h
	bison -d fb3_1.y
	flex -ofb3_1.lex.c fb3_1.l
	cc -o $@ fb3_1.tab.c fb3_1.lex.c fb3_1funcs.c
```

### Shift/Reduce Conflicts and Operator Precedence

这节主要说明的是 Bison 如何处理 shift/reduce conflict。

假如有如下的 rule，

```yacc
%type <a> exp

%%
/* ... */

exp: exp '+' exp { $$ = newast('+', $1,$3); }
	| exp '-' exp { $$ = newast('-', $1,$3);}
	| exp '*' exp { $$ = newast('*', $1,$3); }
	| exp '/' exp { $$ = newast('/', $1,$3); }
	| '|' exp { $$ = newast('|', $2, NULL); }
	| '(' exp ')' { $$ = $2; }
	| '-' exp { $$ = newast('M', $2, NULL); }
	| NUMBER { $$ = newnum($1); }
	;
%%
```

当输入是 `2+3*4` 时，分析如下。

- 首先读入 token `2` ，压入栈（shift），此时它符合最后一条 rule 。

  因此发生 reduce，把刚压入栈的 `2` 弹出，然后压入 nonterminal symbol `exp`。

- 再读入 token `+` ，压入栈（shift），此时没有符合的 rule 。

- 再读入 token `3` ，压入栈（shift），此时 `3` 这个 token 符合最后一条 rule
  （即 `exp: NUMBER {$$ = newnum($1); }`），所以reduce，弹出 `3` ， 压入
  nonterminal symbol `exp`。此时栈中的内容是 `exp + exp`。

到这时候，bison parser 就会产生 shift/reduce conflict。

原因是，因为使用的是 LALR(1) ，此时它已经知道下一个 token 是 `*` 了。

那么此时，它可以直接按照 rule

```yacc
exp: exp '+' exp { $$ = newast('+', $1,$3); }
```

产生reduce，或者，读入下一个 token （即 `*` ），再把 `*` 压入栈，并且等到下次再
遇到 `exp` 的时候，根据 rule

```yacc
exp: exp '*' exp { $$ = newast('*', $1,$3); }
```

再在那时候产生 reduce。

产生这样 reduce/shift 问题的原因是：没有告诉 bison 关于操作符的 **precedence** 和 **associativity** 。

