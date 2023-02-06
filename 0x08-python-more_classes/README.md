# <p align="center">Python - More Classes and Objects</p>

<img src="https://files.realpython.com/media/Object-Oriented-Programming-OOP-in-Python-3_Watermarked.0d29780806d5.jpg" width="100%">

## Description
### Classes and objects

You have already learned the basics of Python, now it's time to discover classes and objects. Classes and objects are a key concept in object-oriented programming (OOP).

### Classes

Classes are models for creating objects. They can contain variables (called properties) and functions (called methods). Properties describe the characteristics of objects, while methods describe the actions that objects can perform.  
  
Here is an example of a class for a car:

```python
class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def accelerate(self, added_speed):
        self.speed += added_speed
```

This class has a `__init__` method that is called when a new object of the class is created. The `accelerate` method adds a specified speed to the current speed of the car.

### Objects

Objects are instances of a class. You can create as many objects as you want from one class. Each object can have different values for its properties.  
  
Here is an example of how to create objects from the `Car` class:

```python
my_car = Car("Toyota", "red", 0)
your_car = Car("Honda", "blue", 0)
```

You can access the properties and methods of objects using the dot (`.`):

```python
print(my_car.brand) # Prints "Toyota"
my_car.accelerate(50)
print(my_car.speed) # Prints "50"
```

In summary, classes and objects allow you to model real-world things in code and use them in a more organized and efficient way.

## Resources
### Read or Watch:

- [Object Oriented Programming](https://intranet.hbtn.io/rltoken/NxSyny_ojf0m2yY1FxhvsA) (*Read everything until the paragraph “Inheritance” (excluded)*)
- [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/PgSxX0FFvkpyAjNyoU0qcg) (*Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The `__init__` Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “`__str__`- and `__repr__`-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”*)
- [Class and Instance Attributes](https://intranet.hbtn.io/rltoken/2Lv-3qPSpQfC1VI52d9LZA)
- [classmethods and staticmethods](https://intranet.hbtn.io/rltoken/18KAvV_Ife9t5o3HYXj9DQ)
- [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/uHYbs5bXkYo6KvTtT6K5Sg) (*Mainly the last part “Public instead of Private Attributes”*)
- [str vs repr](https://intranet.hbtn.io/rltoken/I0LZ2eMDlX6Fc-vrJvY5fA)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

---------------------

# Tasks

### [0. Simple Rectangle](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/0-rectangle.py)
Write an empty class `Rectangle` that defines a rectangle:

- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 0-main.py

#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

mathieu@ubuntu:~/$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
```
</details>

--------------------------

### [1. Real Definition Of a Rectangle](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/1-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 1-main.py

#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

mathieu@ubuntu:~/$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
```
</details>

---------------------

### [2. Area And Perimeter](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/2-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 2-main.py

#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

mathieu@ubuntu:~/$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
```
</details>

-------------------------

### [3. String Representation](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/3-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 3-main.py

#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

mathieu@ubuntu:~/$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
```
</details>

-------------------

### [4. Eval Is Magic](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/4-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 4-main.py

#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

mathieu@ubuntu:~/$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
```
</details>

-------------------------------

### [5. Detect Instance Deletion](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/5-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 5-main.py

#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

mathieu@ubuntu:~/$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
```
</details>

---------------------------

### [6. How Many Instances](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/6-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances:`
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 6-main.py

#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

mathieu@ubuntu:~/$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
```
</details>

-----------------------------------

### [7. Change Representation](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/7-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances:`
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol:`
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 7-main.py

#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

mathieu@ubuntu:~/$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
```
</details>

-------------------------

### [8. Compare Rectangles](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/8-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances:`
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol:`
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  - Returns `rect_1` if both have the same area value
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 8-main.py

#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

mathieu@ubuntu:~/$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
```
</details>

-----------------------

### [9. A Square Is a Rectangle](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/9-rectangle.py)
Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances:`
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol:`
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  - Returns `rect_1` if both have the same area value
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
- You are not allowed to import any module

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/$ cat 9-main.py

#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

mathieu@ubuntu:~/$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```
</details>

---------------------------

### [10. Class And Instance Attributes](https://medium.com/@mormth/classes-instances-and-attributes-in-python-e051b8d7fbc7)
Write a blog post describing how object and class attributes work.

- What’s a class attribute
- What’s an instance attribute
- What are all the ways to create them and what is the Pythonic way of doing it
- What are the differences between class and instance attributes
- What are the advantages and drawbacks of each of them
- How does Python deal with the object and class attributes using the `__dict__`
  
Your posts should have examples and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.
  
When done, please add all urls below (blog post, LinkedIn post, etc.)
  
Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

<a href="https://medium.com/@mormth/classes-instances-and-attributes-in-python-e051b8d7fbc7"><img src="https://cdn.pixabay.com/photo/2019/06/25/12/59/click-here-4298145_1280.png" width="10%"></a>

------------------------------

### [11. N Queens](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x08-python-more_classes/101-nqueens.py)
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
  
- Usage: `nqueens N`
  - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
- where N must be an integer greater or equal to `4`
  - If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
  - If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
- The program should print every possible solution to the problem
  - One solution per line
  - Format: see example
  - You don’t have to print the solutions in a specific order
- You are only allowed to import the `sys` module
  
Read: [Queen](https://intranet.hbtn.io/rltoken/dDicO6zMBxsIvGh5os96vw), [Backtracking](https://intranet.hbtn.io/rltoken/6Z2Yy69oesExpZ1-QVnvLw)

<details>
<summary>File Test</summary>
<br>

```python
mathieu@ubuntu:~/N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

mathieu@ubuntu:~/N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
</details>

--------------------------

## Author

- Mathieu Morel
