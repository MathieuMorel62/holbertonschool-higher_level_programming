# Python - Inheritance

<img src="https://files.realpython.com/media/Inheritance-vs-Composition-in-Python_Watermarked_1.aec726368a97.jpg" width="100%">

## Description
### Introduction to Inheritance in Python
Inheritance is an important concept in object-oriented programming (OOP). It allows for creating a new class based on an existing class by using a portion or all of its code. The derived class is referred to as a subclass or child class, while the original class is referred to as a parent class or superclass.
  
Inheritance in Python is a simple and powerful process that can help you avoid unnecessary code repetition and organize your code more efficiently.

### Syntax of Inheritance in Python

To declare a subclass in Python, you use the class keyword followed by the name of the subclass, and indicate the name of the superclass in parentheses after the name of the subclass. Here is a simple example:

```python
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def __str__(self):
    return f"{self.name} is a {self.species}"

class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="Dog")
    self.breed = breed

  def __str__(self):
    return f"{self.name} is a {self.breed} {self.species}"
```

In this example, the `Dog` class inherits from the `Animal` class. We added an `__init__` method to the `Dog` class to initialize the breed of each `Dog` object, as well as a `__str__` method to display the `Dog` object as a string.

### Using Inheritance in Python

Now that we have defined the `Dog` class, we can create objects from it in the same way we create objects from any other class.

```python
dog1 = Dog("Max", "Labrador")
print(dog1)
# Output: Max is a Labrador Dog

dog2 = Dog("Rocky", "Bulldog")
print(dog2)
# Output: Rocky is a Bulldog Dog
```

As you can see, the `Dog` class inherits the `__str__` method from the `Animal` class, but we also redefined this method to include the breed of each `Dog` object.

### Summary

Inheritance in Python is a simple and powerful way to create derived classes from existing classes. It helps to organize code and reduce redundant code, making it easier to maintain and debug.

## Resources
### Read or Watch:
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://hub.packtpub.com/inheritance-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

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
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Documentation
- Do not use the words `import` or `from` inside your comments, the checker will think you are trying to import some modules

-----------------------

# TASKS

### [0. Lookup](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/0-lookup.py)
Write a function that returns the list of available attributes and methods of an object:

- Prototype: `def lookup(obj)`:
- Returns a `list` object
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 0-main.py

#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

mathieu@ubuntu:~/$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```
</details>

-------------------

### [My List](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/1-my_list.py)
Write a class `MyList` that inherits from `list`:

- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type `int`
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/tests/1-my_list.txt)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 1-main.py

#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

mathieu@ubuntu:~/$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```
</details>

-----------------------

### [2. Exact Same Object](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/2-is_same_class.py)
Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

- Prototype: `def is_same_class(obj, a_class):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 2-main.py

#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

mathieu@ubuntu:~/$ ./2-main.py
1 is an instance of the class int
```
</details>

---------------------------------

### [3. Same Class Or Inherit From](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/3-is_kind_of_class.py)
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

- Prototype: `def is_kind_of_class(obj, a_class):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 3-main.py

#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

mathieu@ubuntu:~/$ ./3-main.py
1 comes from int
1 comes from object
```
</details>

----------------------------

### [4. Only Sub Class Of](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/4-inherits_from.py)
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

- Prototype: `def inherits_from(obj, a_class):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 4-main.py

#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

mathieu@ubuntu:~/$ ./4-main.py
True inherited from class int
True inherited from class object
```
</details>

-----------------------------

### [5. Geometry Module](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/5-base_geometry.py)
Write an empty class `BaseGeometry`.

- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 5-main.py

#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

mathieu@ubuntu:~/$ ./5-main.py
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```
</details>

--------------------------

### [6. Improve Geometry](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/6-base_geometry.py)
Write a class `BaseGeometry` (based on [5-base_geometry.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/5-base_geometry.py)).

- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 6-main.py

#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./6-main.py
[Exception] area() is not implemented
```
</details>

--------------------------

### [7. Integer Validator](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py)
Write a class `BaseGeometry` (based on [6-base_geometry.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/6-base_geometry.py)).

- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- Public instance method: `def integer_validator(self, name, value):` that validates `value`:
  - you can assume `name` is always a string
  - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
  - if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
- You are not allowed to import any module
- [Test: text files](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/tests/7-base_geometry.txt)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 7-main.py

#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```
</details>

--------------------------

### [8. Rectangle](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/8-rectangle.py)
Write a class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py)).

- Instantiation with `width` and `height`: `def __init__(self, width, height):`
  - `width` and `height` must be private. No getter or setter
  - `width` and `height` must be positive integers, validated by `integer_validator`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 8-main.py

#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./8-main.py
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
```
</details>

-----------------------------------------

### [9. Full Rectangle](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py)
Write a class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/7-base_geometry.py)). (task based on [8-rectangle.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/8-rectangle.py))

- Instantiation with `width` and `height`: `def __init__(self, width, height):`:
  - `width` and `height` must be private. No getter or setter
  - `width` and `height` must be positive integers validated by `integer_validator`
- the `area()` method must be implemented
- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 9-main.py

#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

mathieu@ubuntu:~/$ ./9-main.py
[Rectangle] 3/5
15
```
</details>

-------------------------------

### [10. Square #1](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/10-square.py)
Write a class `Square` that inherits from `Rectangle` ([9-rectangle.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py)):

- Instantiation with `size`: `def __init__(self, size):`:
  - `size` must be private. No getter or setter
  - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method must be implemented

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 10-main.py

#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

mathieu@ubuntu:~/$ ./10-main.py
[Rectangle] 13/13
169
```
</details>

-----------------------------

### [11. Square #2](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/11-square.py)
Write a class `Square` that inherits from `Rectangle` ([9-rectangle.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/9-rectangle.py)). (task based on [10-square.py](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/10-square.py)).

- Instantiation with `size`: `def __init__(self, size):`:
  - `size` must be private. No getter or setter
  - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method must be implemented
- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 11-main.py

#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

mathieu@ubuntu:~/$ ./11-main.py
[Square] 13/13
169
```
</details>

-------------------------

### [12. My Integer](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/100-my_int.py)
Write a class `MyInt` that inherits from `int`:

- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 100-main.py

#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

mathieu@ubuntu:~/$ ./100-main.py
3
False
True
```
</details>

---------------------------

### [13. Can I ?](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0A-python-inheritance/101-add_attribute.py)
Write a function that adds a new attribute to an object if it’s possible:

- Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
- You are not allowed to use `try/except`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 101-main.py

#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./101-main.py
John
[TypeError] can't add new attribute
```
</details>

---------------------

## Author

- Mathieu Morel
