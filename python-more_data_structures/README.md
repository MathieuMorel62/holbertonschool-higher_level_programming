# Python - More Data Structures: Set, Dictionary

<img src="https://files.realpython.com/media/Dictionaries-in-Python_Watermarked.3656a2293c00.jpg" width="100%">

## Description
### Set in Python

A set is a data type that contains unique and unordered elements. The elements of a set can be of any type, but they must be immutable (non-modifiable).

To create a set, you can use curly braces {} or the built-in `set()` function.

**Here's a basic example:**

```Python
# Creating an empty set
my_set = set()

# Creating a set with elements
my_set = {1, 2, 3, 4}
or
my_set = set([1, 2, 3, 4])
```

### Dictionary in Python

A dictionary is a data type that contains key-value pairs. The keys must be unique and immutable, while the values can be of any type.

To create a dictionary, you can use curly braces {} or the built-in `dict()` function.

**Here's a basic example:**

```python
# Creating an empty dictionary
my_dict = dict()

# Creating a dictionary with key-value pairs
my_dict = {'key1': 'value1', 'key2': 'value2'}
or
my_dict = dict(key1='value1', key2='value2')
```

It's important to note that dictionaries are unordered, so the order of elements may vary depending on the implementation.

## Resources
### Read or Watch:

- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, Filter, Reduce And Map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
- [Learn To Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

----------------------------------------

# Tasks

#### [0. Squared Simple](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/0-square_matrix_simple.py)
Write a function that computes the square value of all integers of a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
    - Same size as `matrix`
    - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, `map`, etc.

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 0-main.py

#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

mathieu@ubuntu:~/$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
</details>

------------------------------------------

#### [1. Search And Replace](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/1-search_replace.py)
Write a function that replaces all occurrences of an element by another in a new list.

- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 1-main.py

#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

mathieu@ubuntu:~/$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]`
```
</details>

------------------------------

#### [2. Unique Addition](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/2-uniq_add.py)
Write a function that adds all unique integers in a list (only once for each integer).

- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 2-main.py

#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

mathieu@ubuntu:~/$ ./2-main.py
Result: 15
```
</details>

-------------------

#### [3. Present In Both](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/3-common_elements.py)
Write a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 3-main.py

#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

mathieu@ubuntu:~/$ ./3-main.py
['C']`
```
</details>

--------------------------------

#### [4. Only Differents](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/4-only_diff_elements.py)
Write a function that returns a set of all elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 4-main.py

#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

mathieu@ubuntu:~/$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```
</details>

-----------------------------------

#### [5. Number Of Keys](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/5-number_keys.py)
Write a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 5-main.py

#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

mathieu@ubuntu:~/$ ./5-main.py
Number of keys: 3
```
</details>

----------------------------

#### [6. Print Sorted Dictionary](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/6-print_sorted_dictionary.py)
Write a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 6-main.py

#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

mathieu@ubuntu:~/$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```
</details>

---------------------------------

#### [7. Update Dictionary](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/7-update_dictionary.py)
Write a function that replaces or adds key/value in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string
- `value` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 7-main.py

#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

mathieu@ubuntu:~/$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```
</details>

--------------------------------

#### [8. Simple Delete By Key](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/8-simple_delete.py)
Write a function that deletes a key in a dictionary.

- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will be always a string
- If a key doesn’t exist, the dictionary won’t change
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 8-main.py

#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

mathieu@ubuntu:~/$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```
</details>

-----------------------------------

#### [9. Multiply By 2](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/9-multiply_by_2.py)
Write a function that returns a new dictionary with all values multiplied by 2

- Prototype: `def multiply_by_2(a_dictionary):`
- You can assume that all values are only integers
- Returns a new dictionary
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 9-main.py

#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

mathieu@ubuntu:~/$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```
</details>

------------------------------------

#### [10. Best Score](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/10-best_score.py)
Write a function that returns a key with the biggest integer value.

- Prototype: `def best_score(a_dictionary):`
- You can assume that all values are only integers
- If no score found, return `None`
- You can assume all students have a different score
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 10-main.py

#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

mathieu@ubuntu:~/$ ./10-main.py
Best score: Molly
Best score: None
```
</details>

------------------------------------

#### [11. Multiply By Using Map](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/11-multiply_list_map.py)
Write a function that returns a list with all values multiplied by a number without using any loops.

- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list:
    - Same length as `my_list`
    - Each value should be multiplied by `number`
- Initial list should not be modified
- You are not allowed to import any module
- You have to use `map`
- Your file should be max 3 lines

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 11-main.py

#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

mathieu@ubuntu:~/$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```
</details>

--------------------------

#### [12. Roman To Integer](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/12-roman_to_int.py)
**Technical interview preparation:**

- You are not allowed to google anything
- Whiteboard first
  
Create a function `def roman_to_int(roman_string):` that converts a [Roman numeral](https://en.wikipedia.org/wiki/Roman_numerals) to an integer.

- You can assume the number will be between 1 to 3999.
- `def roman_to_int(roman_string)` must return an integer
- If the `roman_string` is not a string or `None`, return 0

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 12-main.py

#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

mathieu@ubuntu:~/$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
```
</details>

-----------------------------

#### [13. Weighted Average!](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/100-weight_average.py)
Write a function that returns the weighted average of all integers tuple `(<score>, <weight>)`

- Prototype: `def weight_average(my_list=[]):`
- Returns `0` if the list is empty
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 100-main.py

#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

mathieu@ubuntu:~/$ ./100-main.py
Average: 2.80
```
</details>

---------------------------------

#### [14. Squared By Using Map](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/101-square_matrix_map.py)
Write a function that computes the square value of all integers of a matrix using `map`

- Prototype: `def square_matrix_map(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
    - Same size as `matrix`
    - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You have to use `map`
- You are not allowed to use `for` or `while`
- Your file should be max 3 lines

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 101-main.py

#!/usr/bin/python3
square_matrix_map = \
    __import__('101-square_matrix_map').square_matrix_map

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

mathieu@ubuntu:~/$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
</details>

-----------------------------

#### [15. Delete By Value](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x04-python-more_data_structures/102-complex_delete.py)
Write a function that deletes keys with a specific value in a dictionary.

- Prototype: def complex_delete(a_dictionary, value):
- If the value doesn’t exist, the dictionary won’t change
- All keys having the searched value have to be deleted
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 102-main.py

#!/usr/bin/python3
complex_delete = __import__('102-complex_delete').complex_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

mathieu@ubuntu:~/$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
```
</details>

--------------------------

## Author

- Mathieu Morel
