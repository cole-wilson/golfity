# golfity
a code golfing language built on the [cole-wilson/adicity](https://github.com/cole-wilson/adicity) language engine

Golfity uses one letter functions with $n$ number of arguments, which can further be more functions with more arguments, which can... etc.

Here is an example program: `a100I$g[#I\1\2\4]+!%I2?%I3Z2`. As you can see, it's incredibly short! This program implements the FizzBuzz program, which is a common code-golfing challenge. The expanded form is shown below:
```
"This is the expanded version...

a(100, I) { 					" loop 100 times, incrementing the I variable
    $( 							" print the following things with a trailing newline
        g([#I\1\2\4], 			" lookup value from array [#I (I to ASCII value), \1, \2, \4 (all predefined constants)] with the following value:
            +( 				    " addition of:
				!(%I2), 		" NOT (I mod 2)
				?(%I3){Z}{2} 	" if (I mod 3) then Z (undefined variable=0) or else 2
            )
		)
    )
}
" Note the extra () and {} usage, which is valid yet unnecessary.
```
## Install
`pip3 install golfity`


`golfity <filename>` or just use the REPL: `golfity`

## Functions
Golfity implements the following functions which you can use:

|character|arguments|description|
|---------|---------|-----------|
|`+`|2 (`a`, `b`)|addition: returns a+b|
|`-`|2 (`a`, `b`)|subtraction: returns a-b|
|`*`|2 (`a`, `b`)|multiplication: returns a\*b|
|`/`|2 (`a`, `b`)|division: returns a/b|
|`%`|2 (`a`, `b`)|modulus: returns a mod b|
|`^`|2 (`a`, `b`)|exponentiation: returns a^b|
|`k`|1 (`a`)|boolean cast: forces type into bool (which is 1 or 0)|
|`t`|2 (`a`, `b`)|greater than or equal to: returns a ≥ b|
|`x1`, `xbeef`, `x123`, etc.|0|literal hex integer|
|`-123.1231`, `8.123`, etc.|0|literal float|
|`123`, `-123`, `0`, etc.|0|literal integer|
|`"a string" (no escapes)`|0|literal string, which is parsed to an array (of ASCII values: see below)|
|`A`...`Z`|0|variable, defaults to [0]. for more than 26 variables use arrays|
|`h`|2 (`a`, `b`)|two element array shorthand, returns [a, b]|
|`[1, 2, 3]` etc.|as many up to ending `]`|returns array of arguments|
|`b`|2 (`A`, `B`: 2 block shorthand)|executes `A` then `B`|
|`c`|3 (`A`, `B`, `C`: 2 block shorthand)|executes `A` then `B` then `C`|
|`{`...`}`|as many up to ending `}`|executes all arguments in succession|
|`\``|0|debug dump, pretty print program|
|`~`|0|debugger breakpoint|
|`!`|1 (`a`)|logical NOT `a` (1 or 0 bool)|
|`|`|2 (`a`, `b`)|logical `a` OR `b`|
|`&`|2 (`a`, `b`)|logical `a` AND `b`|
|`=`|2 (`a`, `b`)|equality: `a` == `b`|
|`>`|2 (`a`, `b`)|more than: `a` > `b`|
|`$`|1 (`value`)|prints the array of ASCII glyphs with a trailing newline|
|`;`|1 (`value`)|same as above but no newline at the end|
|`#`|1 (`x`)|returns ASCII value of character (ord(x))|
|`:`|2 (`lower_bound`, `upper_bound`)|generate an array of integers (inclusive) from `lower_bound` to `upper_bound`|
|`?`|3 (`condition`, `if_yes`, `if_no`)|if statement|
|`@`|3 (`condition`, `counter`, `work`)|do work until condition is true, increment counter|
|`<`|1 (`type`)|get from `type` 0 (stdin), or get from argv (any other `type` value)|
|`i`|3 (`into`, `indices`, `value`)|insert `value` into `into` at `indice(s)`, returning new array|
|`\`|1 (`index`)|predefined constants: `\0`, `\1`, etc:<ol start=0><li>`Hello, World!`</li><li>`Fizz`</li><li>`Buzz`</li><li>`3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067`</li><li>`FizzBuzz`</li></ol>|
|`.`|1 (`variable`)|increment `variable` by 1|
|`_`|1 (`variable`)|decrement `variable` by 1|
|`a`|3 (`length`, `counter`, `work`)|do `work` `length` times incrementing `counter`|
|`d`|2 (`array`, `index`)|remove element `index` from `array`|
|`e`|3 (`array`, `indices`, `value`)|replace `array` value `indice(s)` with `value`|
|`f`|2 (`variable`, `function`)|set `variable` to `function`|
|`g`|2 (`array`, `indices`)|get `indice(s)` from `array`|
|`j`|2 (`array`, `joiner`)|join every element in `array` with `joiner` in between elements|
|`l`|3 (`array`, `var`, `work`)|do `work` for every value `var` in `array`|
|`m`|3 (`array`, `variable`, `func`)|map `func` onto every value `variable` in `array`|
|`n`|1 (`array`)|length of `array`|
|`o`|3 (`array`, `variable`, `func`)|filter out every value `variable` from `array` if not `func`|
|`p`|2 (`array`, `value`)|push `value` to `array`|
|`q`|2 (`array`, `value`)|prepend `value` to `array`|
|`r`|3 (`array`, `lookfor`, `replacewith`)|replace all `lookfor` in `array` with `replacewith`|
|`s`|2 (`variable`, `value`)|set var `variable` to `value`|
|`u`|1 (`upto`)|all value from 0 to `upto` inclusive (like `:` but lower bound is always zero)|
|`v`|0|skip iteration (continue)|
|`w`|2 (`array`, `search`)|where is `search` in `array`|
|`x`|0|stop iteration (break)|
|`y`|1 (`array`)|enumerate `array` with [index, value] pairs|
|`z`|2 (`arr1`, `arr2`)|zip arrays `arr1` and `arr2` together|

## arrays
Arrays are the only datatype. Integers are just arrays of length one, and booleans are just integers which are again just arrays.
You can access any index and if it is undefined it will return [0]. All arrays contain arrays, and every array is in an array, etc.
Adding arrays adds all value within them together, same with other operations. The "length" of an array is the highest index that has a non-default value.
Read `arrays.py` for more.
