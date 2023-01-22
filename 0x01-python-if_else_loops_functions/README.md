# Python - if/else, loops, functions

<img src="https://files.realpython.com/media/Conditional-Statements-in-Python_Watermarked.b6b7d30ff62b.jpg" width="100%">

## Resources
### Read or Watch:
- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
- [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn To Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Learn To Program 2 : Looping](https://www.youtube.com/watch?v=swQEbZ6ez1I&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=2)
- [Pycodestyle – Style Guide For Python Code](https://pypi.org/project/pycodestyle/)

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3 (version 3.8.5)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

-----------------------

# Tasks

#### [0. Positive Anything Is Better Than Negative Nothing](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/0-positive_or_negative.py)
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

- You can find the source code [here](https://github.com/hs-hq/0x01.py/blob/main/0-positive_or_negative_py)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
- The output of the program should be:
  - The number, followed by
    - if the number is greater than 0: `is positive`
    - if the number is 0: `is zero`
    - if the number is less than 0: `is negative`
  - followed by a new line

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
-4 is negative

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
0 is zero

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
-3 is negative

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
-10 is negative

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
10 is positive

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
-5 is negative

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
6 is positive

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
7 is positive

mathieu@ubuntu:~/$ ./0-positive_or_negative.py 
5 is positive
```
</details>

---------------------------

#### [1. The Last Digit](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/1-last_digit.py)
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

- You can find the source code [here](https://github.com/hs-hq/0x01.py/blob/main/1-last_digit_py)
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random.randint` do. **Please do not touch this code**. This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
  - The string `Last digit of`, followed by
  - the number, followed by
  - the string `is`, followed by the last digit of `number`, followed by
    - if the last digit is greater than 5: the string `and is greater than 5`
    - if the last digit is 0: the string `and is 0`
    - if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
  - followed by a new line

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0

mathieu@ubuntu:~/$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
```
</details>

--------------------------

#### [2. I Sometimes Suffer From Insomnia. And When I Can't Fall Asleep, I Play What I Call The Alphabet Game](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/2-print_alphabet.py)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyz
```
</details>

-------------------------

#### [3. When I Was Having That Alphabet Soup, I Never Thought That It Would Pay Off](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/3-print_alphabt.py)
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Print all the letters except `q` and `e`
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyz
```
</details>

----------------------

#### [4. Hexadecimal Printing](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/4-print_hexa.py)
Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
```
</details>

--------------------

#### [5. 00...99](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/5-print_comb2.py)
Write a program that prints numbers from `0` to `99`.

- Numbers must be separated by `,` , followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 `print` functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
```
</details>

--------------------------------

#### [6. Inventing Is a Combination Of Brains And Materials. The More Brains You Use, The Less Material You Need](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/6-print_comb3.py)
Write a program that prints all possible different combinations of two digits.

- Numbers must be separated by `,` , followed by a space
- The two digits must be different
- `01` and `10` are considered the same combination of the two digits `0` and `1`
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 `print` functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```
</details>

-------------------------------

#### [7. Islower](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/7-islower.py)
Write a function that checks for lowercase character.

- Prototype: `def islower(c):`
- Returns `True` if `c` is lowercase
- Returns `False` otherwise
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord) 
  
You don’t need to understand `__import__`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 7-main.py

#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

mathieu@ubuntu:~/$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
```
</details>

-------------------------

#### [8. To Uppercase](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/8-uppercase.py)
Write a function that prints a string in uppercase followed by a new line.

- Prototype: `def uppercase(str):`
- You can only use no more than 2 `print` functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use `str.upper()` and `str.isupper()`
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
  
You don’t need to understand `__import__`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 8-main.py

#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

mathieu@ubuntu:~/$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
```
</details>

-----------------------------

#### [9. There Are Only 3 Colors, 10 Digits, And 7 Notes; It's What We Do With Them That's Important](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/9-print_last_digit.py)
Write a function that prints the last digit of a number.

- Prototype: `def print_last_digit(number):`
- Returns the value of the last digit
- You are not allowed to import any module
  
You don’t need to understand `__import__`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 9-main.py

#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

mathieu@ubuntu:~/$ ./9-main.py
8044
```
</details>

----------------------

#### [10. a + b](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/10-add.py)
Write a function that adds two integers and returns the result.

- Prototype: `def add(a, b):`
- Returns the value of `a + b`
- You are not allowed to import any module
  
You don’t need to understand `__import__`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 10-main.py

#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

mathieu@ubuntu:~/$ ./10-main.py
3
98
98
```
</details>

--------------------

#### [11. a ^ b](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/11-pow.py)
Write a function that computes `a` to the power of `b` and return the value.

- Prototype: `def pow(a, b):`
- Returns the value of `a ^ b`
- You are not allowed to import any module  
  
You don’t need to understand `__import__`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 11-main.py

#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

mathieu@ubuntu:~/$ ./11-main.py
4
9604
1
0.0001
-1024
```
</details>

-----------------------

#### [12. Fizz Buzz](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/12-fizzbuzz.py)
Write a function that prints the numbers from 1 to 100 separated by a space.

- For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
- For numbers which are multiples of both three and five print `FizzBuzz`.
- Prototype: `def fizzbuzz():`
- Each element should be followed by a space
- You are not allowed to import any module  
  
You don’t need to understand `__import__`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 12-main.py

#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

mathieu@ubuntu:~/$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
```
</details>

-----------------------

#### [13. Smile In The Mirror](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/100-print_tebahpla.py)
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.

- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbA
```
</details>

----------------------------

#### [14. Remove At Position](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/101-remove_char_at.py)
Write a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).

- Prototype: `def remove_char_at(str, n):`
- You are not allowed to import any module  
  
You don’t need to understand `__import__`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 101-main.py

#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))

mathieu@ubuntu:~/$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
```
</details>

---------------------------

#### [15. ByteCode -> Python #2](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/102-magic_calculation.py)
Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:

<details>
<summary>File Test</summary>
<br>

```python
3           0 LOAD_FAST                0 (a)
            3 LOAD_FAST                1 (b)
            6 COMPARE_OP               0 (<)
            9 POP_JUMP_IF_FALSE       16

4          12 LOAD_FAST                2 (c)
           15 RETURN_VALUE

5     >>   16 LOAD_FAST                2 (c)
           19 LOAD_FAST                1 (b)
           22 COMPARE_OP               4 (>)
           25 POP_JUMP_IF_FALSE       36

6          28 LOAD_FAST                0 (a)
           31 LOAD_FAST                1 (b)
           34 BINARY_ADD
           35 RETURN_VALUE

7     >>   36 LOAD_FAST                0 (a)
           39 LOAD_FAST                1 (b)
           42 BINARY_MULTIPLY
           43 LOAD_FAST                2 (c)
           46 BINARY_SUBTRACT
           47 RETURN_VALUE
```
</details>

[tips - ByteCode](https://docs.python.org/3.4/library/dis.html)

--------------------------------

## Author

- Mathieu Morel
