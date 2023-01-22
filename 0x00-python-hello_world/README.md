# Python
<img src="https://yuyu-code.com/wp-content/uploads/2022/06/python-hello-world.jpg" width="100%">

## Author’s disclaimer
```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!
```

## Resources
### Read or Watch:

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
- [Using The Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction To Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
- [How To Use String Formatters In Python 3](https://intranet.hbtn.io/rltoken/dd7bIKsC3_0wb3Np_8URUA)
- [Learn To Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide For Python Code](https://pypi.org/project/pycodestyle/)

## Requirements
### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

## More Info
### Zen
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### Pycodestyle
`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)  

--------------------------------

# Tasks

#### [0. Run Python File](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/0-run)
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ cat main.py
#!/usr/bin/python3
print("Best School")

mathieu@ubuntu:~/py/$ export PYFILE=main.py
mathieu@ubuntu:~/py/$ ./0-run
Best School
```
</details>

-----------------------

#### [1. Run Inline](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/1-run_inline)
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ export PYCODE='print(f"Best School: {88+10}")'

mathieu@ubuntu:~/py/$ ./1-run_inline 
Best School: 98
```
</details>

-------------------------

#### [2. Hello, Print](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/2-print.py)
Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

- Use the function `print`

<details>
<summary> File Test </summary>
<br>

```shell
mathieu@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
```
</details>

--------------------

#### [3. Print Integer](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/3-print_number.py)
Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/main/3-print_number.py)
- The output of the script should be:
  - the number, followed by `Battery street`,
  - followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://intranet.hbtn.io/rltoken/dd7bIKsC3_0wb3Np_8URUA)

<details>
<summary> File Test </summary>
<br>

```shell
mathieu@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
```
</details> 
  
-----------------------------

#### [4. Print Float](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/4-print_float.py)
Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/main/4-print_float.py)
- The output of the program should be:
  - Float:, followed by the float with only 2 digits
  - followed by a new line
- You are not allowed to cast number to string
- You have to use f-strings

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
```
</details>

--------------------------

#### [5. Print String](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/5-print_string.py)
Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/main/5-print_string.py)
- The output of the program should be:
  - 3 times the value of `str`
  - followed by a new line
  - followed by the 9 first characters of `str`
  - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
```
</details>

-----------------------

#### [6. Play With Strings](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/6-concat.py)
Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/6-concat.py) to print `Welcome to Holberton School!`

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/main/6-concat.py)
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!

mathieu@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
```
</details>

----------------------------

#### [7. Copy - Cut - Paste](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/7-edges.py)
Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/7-edges.py)

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/main/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto

mathieu@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
```
</details>

--------------------

#### [8. Create a New Sentence](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/8-concat_edges.py)
Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/main/8-concat_edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python

mathieu@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
```
</details>

--------------------------

#### [9. Easter Egg](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/9-easter_egg.py)
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

<details>
<summary> File Test </summary>
<br>

```txt
mathieu@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
</details>

---------------------------

#### [10. Hello, Write](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/100-write.py)
Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.

- Use the function `write` from the `sys` module
- You are not allowed to use `print`
- Your script should print to `stderr`
- Your script should exit with the status code `1`

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19

mathieu@ubuntu:~/py/$ echo $?
1

mathieu@ubuntu:~/py/$ ./100-write.py 2> q
mathieu@ubuntu:~/py/$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
```
</details>

--------------------------

#### [11. Compile](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/101-compile)
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

<details>
<summary> File Test </summary>
<br>

```python
mathieu@ubuntu:~/py/$ cat main.py 
#!/usr/bin/python3
print("Best School")

mathieu@ubuntu:~/py/$ export PYFILE=main.py
mathieu@ubuntu:~/py/$ ./101-compile
Compiling main.py ...

mathieu@ubuntu:~/py/$ ls
101-compile  main.py  main.pyc

mathieu@ubuntu:~/py/$ cat main.pyc | zgrep -c "Best School"
1

mathieu@ubuntu:~/py/$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
```
</details>

-------------------------

#### [12. ByteCode -> Python #1](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x00-python-hello_world/102-magic_calculation.py)
Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

<details>
<summary> File Test </summary>
<br>

```python
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
</details>

Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)

-------------------------------

## Author

- Mathieu Morel
