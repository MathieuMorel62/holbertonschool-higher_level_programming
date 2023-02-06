# <p align="center">Python - Test-driven development</p>
<img src="https://files.realpython.com/media/Getting-Started-with-Testing-in-Python_Watermarked.9f22be97343d.jpg" width="100%">

## Description
### Introduction to Test-driven Development in Python
  
Test-driven Development (TDD) is a software development method that involves writing tests for your code before writing the code itself. It's an effective way to ensure that your code works as intended and meets requirements.
  
### Why use TDD with Python?

- TDD helps you design and write software in a more structured and efficient manner.
- It allows you to find and fix bugs more quickly and easily.
- It guarantees that your code remains functional even when you make future changes.

### How to implement TDD with Python?

1. Write a test that describes what your code should do.
2. Run the test and verify that it fails.
3. Write the code that makes the test pass.
4. Run the test again and verify that it passes.
5. Repeat this process for all necessary tests.

It's important to note that TDD is not just for bug fixing, but also for designing new features. It may seem a bit intimidating at first, but once you get used to it, you'll realize how useful it can be for writing higher quality code.

### Example

Here is an example of TDD in Python using the unittest module:

```python
import unittest

def sum(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, -1), -2)
        self.assertEqual(sum(3, 4), 7)

if __name__ == '__main__':
    unittest.main()
```

In this example, the `sum` function is tested using the `unittest` module. The tests are defined in the `TestSum` class and each test checks if the sum of two numbers is correct.

### Conclusion

TDD is a very useful software development method that can improve the quality of your code and speed up development. If you already use Python, it's easy to start using TDD with this language.

## Background Context
### Important notice on intranet checks for Python projects

Starting from today:

- Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. **But not in the implementation of them!**
- **Don’t trust the user**, always think about all possible edge cases

## Resources
### Read or Watch:

- [**Doctest — Test Interactive Python Examples**](https://intranet.hbtn.io/rltoken/Hmd_LI8NZ-F2ymDxue5HCg) (*until “26.2.3.7. Warnings” included*)
- [**Doctest – Testing Through Documentation**](https://intranet.hbtn.io/rltoken/fbFfGNFU07L2yD0D1uc-Xg)
- [**Unit Tests in Python**](https://intranet.hbtn.io/rltoken/LhbdUZYzqiP7cjxjE3rG3w)

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

-------------------------

# Tasks

### [0. Integers Addition](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/0-add_integer.py)
Write a function that adds 2 integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/0-add_integer.txt)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 0-main.py
  
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

mathieu@ubuntu:~/$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
  
mathieu@ubuntu:~/$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
  
mathieu@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
  
mathieu@ubuntu:~/$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
```
</details>

---------------------------

### [1. Divide a Matrix](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/2-matrix_divided.py)
Write a function that divides all elements of a matrix.

- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
- Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
- `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
- `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/2-matrix_divided.txt)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 2-main.py
  
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

mathieu@ubuntu:~/$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
  
mathieu@ubuntu:~/$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
```
</details>

----------------------------

### [2. Say My Name](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/3-say_my_name.py)
Write a function that prints `My name is <first name> <last name>`

- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/3-say_my_name.txt)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 3-main.py
  
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

mathieu@ubuntu:~/$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
  
mathieu@ubuntu:~/$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
```
</details>

-----------------------------

### [3. Print Square](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/4-print_square.py)
Write a function that prints a square with the character `#`.

- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
- if `size` is less than `0`, raise a ValueError exception with the message `size must be >= 0`
- if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/4-print_square.txt)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 4-main.py
  
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

mathieu@ubuntu:~/$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0

mathieu@ubuntu:~/$ python3 -m doctest -v ./tests/4-print_square.txt
  ```
  </details>
  
------------------------

### [4. Text Indentation](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/5-text_indentation.py)
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/5-text_indentation.txt)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 5-main.py
  
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

mathieu@ubuntu:~/$ ./5-main.py | cat -e
  
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresmathieu@ubuntu:~/$
mathieu@ubuntu:~/$ python3 -m doctest -v ./tests/5-text_indentation.txt
```
</details>
  
-------------------------

### [5. Max Integer - Unittest](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/6-max_integer.py)
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

- Your test file should be inside a folder `tests`
- You have to use the [unittest module](https://intranet.hbtn.io/rltoken/0a3DSCMIMni_V7pgq1myLQ)
- Your test file should be python files (extension: `.py`)
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
- [Test: Unittest](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/6-max_integer_test.py)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 6-max_integer.py
  
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

mathieu@ubuntu:~/$ cat 6-main.py
  
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))

mathieu@ubuntu:~/$ ./6-main.py
4
4

mathieu@ubuntu:~/$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK

mathieu@ubuntu:~/$ head -7 tests/6-max_integer_test.py 
  
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
```
</details>
  
-------------------------

### [6. Matrix Multiplication](https://github.com/MathieuMorel62/0x07-holbertonschool-higher_level_programming/blob/main/python-test_driven_development/100-matrix_mul.py)
Write a function that multiplies 2 matrices:

- Read: [Matrix multiplication - only Matrix product (two matrices)](https://intranet.hbtn.io/rltoken/efWuPFTQBfLSSnwTEAM9Fg)
- Prototype: `def matrix_mul(m_a, m_b):`
- `m_a` and `m_b` must be validated with these requirements in this order
- `m_a` and `m_b` must be an list of lists of integers or floats:
  - if `m_a` or `m_b` is not a list: raise a `TypeError` exception with the message `m_a must be a list` or `m_b must be a list`
  - if `m_a` or `m_b` is not a list of lists: raise a `TypeError` exception with the message `m_a must be a list of lists` or `m_b must be a list of lists`
  - if `m_a` or `m_b` is empty (it means: `= []` or `= [[]]`): raise a `ValueError` exception with the message `m_a can't be empty` or `m_b can't be empty`
  - if one element of those list of lists is not an integer or a float: raise a `TypeError` exception with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`
  - if `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raise a `TypeError` exception with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`
- If `m_a` and `m_b` can’t be multiplied: raise a `ValueError` exception with the message `m_a and m_b can't be multiplied`
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/100-matrix_mul.txt)
  
<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 100-main.py
  
#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

mathieu@ubuntu:~/$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
  
mathieu@ubuntu:~/$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
```
</details>
  
---------------------------

### [7. Lazy Matrix Multiplication](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/101-lazy_matrix_mul.py)
Write a function that multiplies 2 matrices by using the module [NumPy](https://intranet.hbtn.io/rltoken/F_2abrxZf-4QGrDmkwNhag)

To install it: `pip3 install numpy==1.15.0`

Prototype: `def lazy_matrix_mul(m_a, m_b):`
Test cases should be the same as `100-matrix_mul` but with new exception type/message
[Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x07-python-test_driven_development/tests/101-lazy_matrix_mul.txt)

<details>
<summary>File Test</summary>
<br>

```python
#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

mathieu@ubuntu:~/$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
```
</details>

------------------------
  
## Author
  
- Mathieu Morel
