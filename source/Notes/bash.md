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

