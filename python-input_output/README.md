# Python - Input/Output

<img src="https://files.realpython.com/media/Basic-Input-Output-and-String-Formatting-in-Python_Watermarked.65ba5b535841.jpg" width="100%">

## Description
### Reading and Writing Files in Python
Python provides a number of functions for reading and writing data to and from files. This is an important aspect of data persistence and helps in storing data for later use.
  
Python's `open()` function is used to open a file for reading or writing. The function takes the name of the file to be opened and the mode in which the file should be opened (e.g., `'r'` for reading, `'w'` for writing, `'a'` for appending).

Here's an example of reading the contents of a file:

```python
with open("file.txt", "r") as f:
    contents = f.read()
    print(contents)
```

And here's an example of writing to a file:

```python
with open("file.txt", "w") as f:
    f.write("Hello, world!")
```

It's important to use the `with` statement when working with files, as it ensures that the file is properly closed, even if an exception is raised during the processing of the file.

### Predefined Clean-up Actions

In Python, when you use `with` to work with a file, you have the ability to specify predefined clean-up actions to be performed automatically. The `with` statement allows you to automatically close the file, even if an exception is raised during the processing of the file.
  
For example, here's how you can use the `with` statement to open a file and automatically close it after you're done working with it:

```python
with open("file.txt", "r") as f:
    contents = f.read()
    print(contents)
```

In this example, the file is automatically closed when the `with` block is exited, even if an exception is raised.

### JSON Encoder and Decoder

The `json` module in Python provides a way to encode and decode JSON data. The `json.dumps()` function is used to encode a Python object into a JSON-formatted string, and the `json.loads()` function is used to decode a JSON-formatted string into a Python object.
  
Here's an example of encoding a Python object into a JSON-formatted string:

```python
import json

python_obj = {'name': 'John Doe', 'age': 30}
json_data = json.dumps(python_obj)

print(json_data)
```

And here's an example of decoding a JSON-formatted string into a Python object:

```python
import json

json_data = '{"name": "John Doe", "age": 30}'
python_obj = json.loads(json_data)

print(python_obj)
```

## Resources
### Read or Watch:
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) (until “11.4 Binary Files” (included))
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com) (ch. 8 p 180-183 and ch. 14 p 326-333)

## Raquirements
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
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

--------------------------

# Tasks

### [0. Read File](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/0-read_file.py)
Write a function that reads a text file (`UTF8`) and prints it to stdout:

- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 0-main.py

#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

mathieu@ubuntu:~/$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!

mathieu@ubuntu:~/$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
```
</details>

----------------------------

### [1. Write To a File](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/1-write_file.py)
Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 1-main.py

#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

mathieu@ubuntu:~/$ ./1-main.py
24

mathieu@ubuntu:~/$ cat my_first_file.txt
This School is so cool!
```
</details>

----------------------

### [2. Append To a File](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/2-append_write.py)
Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

Prototype: `def append_write(filename="", text=""):`
If the file doesn’t exist, it should be created
You must use the `with` statement
You don’t need to manage `file permission` or `file doesn't exist` exceptions.
You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 2-main.py

#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

mathieu@ubuntu:~/$ cat file_append.txt
cat: file_append.txt: No such file or directory

mathieu@ubuntu:~/$ ./2-main.py
24

mathieu@ubuntu:~/$ cat file_append.txt
This School is so cool!

mathieu@ubuntu:~/$ ./2-main.py
24

mathieu@ubuntu:~/$ cat file_append.txt
This School is so cool!
This School is so cool!
```
</details>

-------------------------

### [3. To JSON String](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/3-to_json_string.py)
Write a function that returns the JSON representation of an object (string):

- Prototype: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 3-main.py

#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
```
</details>

----------------------------

### [4. From JSON String To Object](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/4-from_json_string.py)
Write a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 4-main.py

#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[JSONDecodeError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
```
</details>

-----------------------

### [5. Save Object To a File](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/5-save_to_json_file.py)
Write a function that writes an Object to a text file, using a JSON representation:

- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 5-main.py

#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./5-main.py
[TypeError] Object of type set is not JSON serializable

mathieu@ubuntu:~/$ cat my_list.json ; echo ""
[1, 2, 3]

mathieu@ubuntu:~/$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}

mathieu@ubuntu:~/$ cat my_set.json ; echo ""

```
</details>

--------------------------

### [6. Create Object From a JSON File](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/6-load_from_json_file.py)
Write a function that creates an Object from a “JSON file”:

- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat my_fake.json
{"is_active": true, 12 }

mathieu@ubuntu:~/$ cat 6-main.py

#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ cat my_list.json ; echo ""
[1, 2, 3]

mathieu@ubuntu:~/$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}

mathieu@ubuntu:~/$ cat my_fake.json ; echo ""
{"is_active": true, 12 }

mathieu@ubuntu:~/$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
```
</details>

------------------------------

### [7. Load, Add, Save](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/7-add_item.py)
Write a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function `save_to_json_file` from [5-save_to_json_file.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/5-save_to_json_file.py)
- You must use your function `load_from_json_file` from [6-load_from_json_file.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/6-load_from_json_file.py)
- The list must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat add_item.json
cat: add_item.json: No such file or directory

mathieu@ubuntu:~/$ ./7-add_item.py
mathieu@ubuntu:~/$ cat add_item.json ; echo ""
[]

mathieu@ubuntu:~/$ ./7-add_item.py Best School
mathieu@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School"]

mathieu@ubuntu:~/$ ./7-add_item.py 89 Python C
mathieu@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
```
</details>

-------------------------------

### [8. Class To JSON](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py)
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 8-my_class.py 

#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)


mathieu@ubuntu:~/$ cat 8-main.py 

#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

mathieu@ubuntu:~/$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}


mathieu@ubuntu:~/$ 
mathieu@ubuntu:~/$ cat 8-my_class_2.py 

#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)


mathieu@ubuntu:~/$ cat 8-main_2.py 

#!/usr/bin/python3
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

mathieu@ubuntu:~/$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
```
</details>

--------------------------------

### [9. Student To JSON](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/9-student.py)
Write a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py))
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 9-main.py 

#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))

mathieu@ubuntu:~/$ ./9-main.py 
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
```
</details>

---------------------------

### [10. Student To JSON With Filter](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/10-student.py)
Write a class `Student` that defines a student by: (based on `9-student.py`)

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py)):
  - If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
  - Otherwise, all attributes must be retrieved
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 10-main.py 

#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)

mathieu@ubuntu:~/$ ./10-main.py 
{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
{'age': 27, 'first_name': 'Bob'}
{'age': 27}
```
</details>

-----------------------------

### [11. Student To Disk And Reload](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/11-student.py)
Write a class `Student` that defines a student by: (based on [10-student.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/10-student.py))

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as [8-class_to_json.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/8-class_to_json.py)):
  - If `attrs` is a list of strings, only attributes name contain in this list must be retrieved.
  - Otherwise, all attributes must be retrieved
- Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
  - You can assume `json` will always be a dictionary
  - A dictionary key will be the public attribute name
  - A dictionary value will be the value of the public attribute
- You are not allowed to import any module
  
Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 11-main.py 

#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

mathieu@ubuntu:~/$ ./11-main.py student.json
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last_name": "Doe", "first_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23

mathieu@ubuntu:~/$ cat student.json ; echo ""
{"last_name": "Doe", "first_name": "John", "age": 23}
```
</details>

---------------------------

### [12. Pascal's Triangle](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/12-pascal_triangle.py)
**Technical interview preparation:**

- You are not allowed to google anything
- Whiteboard first
  
Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
  
- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 12-main.py

#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

mathieu@ubuntu:~/$ 
mathieu@ubuntu:~/$ ./12-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
</details>

--------------------------------

### [13. Search And Update](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/100-append_after.py)
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

- Prototype: `def append_after(filename="", search_string="", new_string=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 100-main.py

#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

mathieu@ubuntu:~/$ cat append_after_100.txt
At School,
Python is really important,
But it can be very hard if:
- You don't get all Pythonic tricks
- You don't have strong C knowledge.

mathieu@ubuntu:~/$ ./100-main.py
mathieu@ubuntu:~/$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
But it can be very hard if:
- You don't get all Pythonic tricks
"C is fun!"
- You don't have strong C knowledge.

mathieu@ubuntu:~/$ ./100-main.py
mathieu@ubuntu:~/$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
"C is fun!"
But it can be very hard if:
- You don't get all Pythonic tricks
"C is fun!"
"C is fun!"
- You don't have strong C knowledge.
```
</details>

--------------------------

### [14. Log Parsing](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0B-python-input_output/101-stats.py)
Write a script that reads `stdin` line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning:
  - Total file size: `File size: <total size>`
  - where is the sum of all previous (see input format above)
  - Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    - if a status code doesn’t appear, don’t print anything for this status code
    - format: `<status code>: <number>`
    - status codes should be printed in ascending order

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 101-generator.py

#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

mathieu@ubuntu:~/$ ./101-generator.py | ./101-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./101-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./101-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
```
</details>

-----------------------

## Author

- Mathieu Morel
