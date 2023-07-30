# BASH Tips



## BASH Color codes

```bash
cReset='\033[0m'
cPrefix='\033['

code_style_normal="0"
code_style_bold="1"
code_style_faint="2"
code_style_italics="3"
code_style_underline="4"

code_foreground="3"
code_light_foreground="9"
code_background="4"
code_light_background="10"

color_black="0m"
color_red="1m"
color_green="2m"
color_orange="3m"
color_blue="4m"
color_purple="5m"
color_cyan="6m"
color_gray="7m"
```



A script file to print different colors

```bash
### Show different kinds of colors

cReset='\033[0m'
cPrefix='\033['

code_style_normal="0"
code_style_bold="1"
code_style_faint="2"
code_style_italics="3"
code_style_underline="4"
slist=($code_style_normal $code_style_bold $code_style_faint \
         $code_style_italics $code_style_underline)
slist_str=("normal" "bold" "faint" "italics" "underline")
snum=${#slist[@]}


code_foreground="3"
code_light_foreground="9"
code_background="4"
code_light_background="10"
glist=($code_foreground $code_light_foreground $code_background $code_light_background)
glist_str=("fore" "light_fore" "back" "light_back")
gnum=${#glist[@]}

color_black="0m"
color_red="1m"
color_green="2m"
color_orange="3m"
color_blue="4m"
color_purple="5m"
color_cyan="6m"
color_gray="7m"
clist=($color_black $color_red $color_green $color_orange $color_blue \
         $color_purple $color_cyan $color_gray)
clist_str=("black" "red" "green" "orange" "blue" "purple" "cyan" "gray")
cnum=${#clist[@]}

for (( s = 0; s < snum; s++ )) do
   for (( g = 0; g < gnum; g++ )) do
      for (( c = 0; c < cnum; c++ )) do
         sstr="${slist_str[$s]}"
         gstr="${glist_str[$g]}"
         cstr="${clist_str[$c]}"

         scode="${slist[$s]}"
         gcode="${glist[$g]}"
         ccode="${clist[$c]}"

         msg="${sstr} + ${gstr} + ${cstr}"
         ccode="${cPrefix}${scode};${gcode}${ccode}"
         echo -e "$s-$g-$c ${ccode}${msg} ${cReset}"
      done
   done
done

```



## Bash array

```bash
# Syntax		Result
arr=()			# Create an empty array
arr=(1 2 3)		# Initialize array
${arr[2]}		# Retrieve third element
${arr[@]}		# Retrieve all elements
${!arr[@]}		# Retrieve array indices
${#arr[@]}		# Calculate array size
arr[0]=3		# Overwrite 1st element
arr+=(4)		# Append value(s)
str=$(ls)		# Save ls output as a string
arr=( $(ls) )	# Save ls output as an array of files
${arr[@]:s:n}	# Retrieve n elements starting at index s
```



## Function shell variables

All function parameters or arguments can be accessed via `$1, $2, $3,..., $N`.

`$0` always point to the shell script name.

`$*` or `$@` holds all parameters or arguments passed to the function.

`$#` holds the number of positional parameters passed to the function.


## Bash logical and, or

多个条件逻辑**与**

```bash
if [[ $test == "Monday" ]] && [[ $test == "Tuesday" ]]; then
	echo "Yes"
else
	echo "No"
fi
```


多个条件逻辑**或**

```bash
if [[ $test == "Monday" ]] || [[ $test == "Tuesday" ]]; then
	echo "Yes"
else
	echo "No"
fi
```

混合逻辑使用

```bash
if ([[ $test == "Monday" ]] || [[ $test == "Tuesday" ]]) &&  [[ $test2 ==  "AI" ]]; then
	echo "Yes"
else
	echo "No"
fi
```

## String starts with a value

需要注意的是，下面第4个条件测试中的`"Fly*"`，因为`*`在双引号里面，所以指的是`Fly*`这个字符串，`*`就不再被解释为任意字符的匹配，但如果`*`在双引号外面，那么`*`就会被解释为任意字符的匹配。

```bash
test="Fly001"
prefix="Fly"

# Output is: Starts with Fly
if [[ $test == "$prefix"* ]]; then
	echo "Starts with Fly"
else
	echo "Doesn't starts with Fly"
fi

# Output is: Starts with Fly
if [[ $test == "Fly"* ]]; then
	echo "Starts with Fly"
else
	echo "Doesn't starts with Fly"
fi

# Output is: Starts with Fly
if [[ $test == Fly* ]]; then
	echo "Starts with Fly"
else
	echo "Doesn't starts with Fly"
fi

# Output is: Doesn't starts with Fly
if [[ $test == "Fly*" ]]; then
	echo "Starts with Fly"
else
	echo "Doesn't starts with Fly"
fi

```

Outputs of the above 4 conditional tests are,

```bash
Output is: Starts with Fly
Output is: Starts with Fly
Output is: Starts with Fly
Output is: Doesn\'t starts with Fly
```


## `SECONDS` variable

[Advanced Bash-Scripting Guide - 9.1. Internal Variables](https://tldp.org/LDP/abs/html/internalvariables.html)

> `SECONDS` : The number of seconds the script has been running.

注意，`SECONDS`变量指的是脚本从开始运行到现在经过的时间，所以如果要求解某个耗时命令的elapsed time，就需要在该命令的前后各自记录当时的`SECONDS`，然后做两个值相减得到elapsed time。


## Spinner waiting for a process

等待一个进程的progress bar，参见文件 [Gitee/Pyrad - scripts/script_bash/wait_spinner.sh](https://gitee.com/pyrad/scripts/blob/master/script_bash/wait_spinner.sh)


## Separate a string and then print

看起来使用 `awk` 是比较简洁的办法

```shell
echo $PATH | awk -F: '{for (i = 1; i <= NF; ++i) print i, $i}'
```



