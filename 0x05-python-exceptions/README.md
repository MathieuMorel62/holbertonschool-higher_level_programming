# Python - Exceptions

<img src="https://files.realpython.com/media/Python_Exceptions_Watermark.47f814fbeced.jpg" width="100%">

## Description
### Exceptions In Python
Exceptions in Python are like alarm signals that indicate that there was an error during the execution of your program. For example, trying to divide a number by zero will cause an exception. To handle these exceptions, we use the keywords `try`, `except`, and `finally` in our code.

**Here's a basic example:**

```python
try:
   # code that may cause an exception
except ExceptionType:
   # code to handle the exception
finally:
   # code to be executed regardless of whether an exception occurred
```

- The `try` block is used to execute a portion of code that might cause an exception.  
- The `except` block is used to handle the exception that occurs.
- The `finally` block is used to execute a portion of code that should be executed regardless of whether an exception occurred.

By using exceptions, you can prevent your program from abruptly stopping in case of an error and instead handle these errors in an appropriate manner. This can improve the reliability and robustness of your code.

## Resources
### Read or Watch:

- [Errors And Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn To Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4) (starting at minute 7)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc``

----------------------------------

# Tasks

#### [0. Safe List Printing](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/0-safe_print_list.py)
Write a function that prints `x` elements of a list.

- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- Returns the real number of elements printed
- You have to use `try: / except:`
- You are not allowed to import any module
- You are not allowed to use `len()``

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 0-main.py

#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

mathieu@ubuntu:~/$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```
</details>

----------------------------

#### [1. Safe Printing Of An Integers List](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/1-safe_print_integer.py)
Write a function that prints an integer with `"{:d}".format()`.

- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
- Otherwise, returns `False`
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print as integer
- You are not allowed to import any module
- You are not allowed to use `type()``

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 1-main.py

#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

mathieu@ubuntu:~/$ ./1-main.py
89
-89
School is not an integer
```
</details>

--------------------------------

#### [2. Print And Count Integers](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/2-safe_print_list_integers.py)
Write a function that prints the first `x` elements of a list and only integers.

- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- `x` represents the number of elements to access in `my_list`
- `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print an integer
- You are not allowed to import any module
- You are not allowed to use `len()``

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 2-main.py

#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

mathieu@ubuntu:~/$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```
</details>

-----------------------------------

#### [3. Integers Division With Debug](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/3-safe_print_division.py)
Write a function that divides 2 integers and prints the result.

- Prototype: `def safe_print_division(a, b):`
- You can assume that `a` and `b` are integers
- The result of the division should print on the `finally:` section preceded by `Inside result:`
- Returns the value of the division, otherwise: `None`
- You have to use `try: / except: / finally:`
- You have to use `"{}".format()` to print the result
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 3-main.py

#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

mathieu@ubuntu:~/$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```
</details>

-------------------------------

#### [4. Divide a List](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/4-list_division.py)
Write a function that divides element by element 2 lists.

- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
- `list_length` can be bigger than the length of both lists
- Returns a new list (length = `list_length`) with all divisions
- If 2 elements can’t be divided, the division result should be equal to `0`
- If an element is not an integer or float:
    - print: `wrong type`
- If the division can’t be done (`/0`):
    - print: `division by 0`
- If `my_list_1` or `my_list_2` is too short
    - print: `out of range`
- You have to use `try: / except: / finally:`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 4-main.py

#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

mathieu@ubuntu:~/$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
```
</details>

----------------------------

#### [5. Raise Exception](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/5-raise_exception.py)
Write a function that raises a type exception.

- Prototype: `def raise_exception():`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 5-main.py

#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

mathieu@ubuntu:~/$ ./5-main.py
Exception raised
```
</details>

----------------------------

#### [6. Raise a Message](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/6-raise_exception_msg.py)
Write a function that raises a name exception with a message.

- Prototype: `def raise_exception_msg(message=""):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 6-main.py

#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

mathieu@ubuntu:~/$ ./6-main.py
C is fun
```
</details>

------------------------

#### [7. Safe Integer Print With Error Message](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/100-safe_print_integer_err.py)
Write a function that prints an integer.

- Prototype: `def safe_print_integer_err(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if `value` has been correctly printed (it means the `value` is an integer)
- Otherwise, returns `False` and prints in `stderr` the error precede by `Exception:`
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print as integer
- You are not allowed to use `type()`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 100-main.py

#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

mathieu@ubuntu:~/$ ./100-main.py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
School is not an integer

mathieu@ubuntu:~/$ ./100-main.py 2> /dev/null
89
-89
School is not an integer
```
</details>

-----------------------------------

#### [8. Safe Function](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/101-safe_function.py)
Write a function that executes a function safely.

- Prototype: `def safe_function(fct, *args):`
- You can assume `fct` will be always a pointer to a function
- Returns the result of the function,
- Otherwise, returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception:`
- You have to use `try: / except:``

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 101-main.py

#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

mathieu@ubuntu:~/$ ./101-main.py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None

mathieu@ubuntu:~/$ ./101-main.py 2> /dev/null
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None
```
</details>

---------------------------------

#### [9. ByteCode -> Python #4](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x05-python-exceptions/102-magic_calculation.py)
Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

<details>
<summary>File Test</summary>
<br>

```python
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
</details>

- Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)

-------------------------------

## Author

- Mathieu Morel
