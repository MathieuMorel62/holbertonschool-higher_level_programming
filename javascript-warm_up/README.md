# <p align=center>JavaScript - Warm up</p>

<img src="https://camo.githubusercontent.com/bdd38b0c65d47c7cba62b60617adffedb3a48d1ac6e77501b990fffb1e52815c/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f333230302f312a4f463078454d6b5742762d36397a766d4e73365244512e676966" width="100%">

## Description to JavaScript and Node.js
### JavScript

**JavaScript** is a high-level, interpreted, and object-oriented programming language initially designed to add interactivity to web pages. Today, it is widely used in web and mobile development, as well as various other platforms.
  
Here are some key features of **JavaScript**:
  
- `Dynamic`: JavaScript enables the creation of interactive and responsive web pages by modifying content and styles on the fly.
- `Object-oriented`: JavaScript uses objects to model data and functionality, making it easier to reuse and organize code.
- `Compatibility`: JavaScript is supported by all modern browsers and works on most devices.
- `Scalability`: With popular libraries and frameworks like React, Angular, and Vue.js, JavaScript can be used to create complex and scalable web applications.

## Node.js

**Node.js** is an open-source runtime environment for JavaScript that enables server-side JavaScript execution. It is built on Chrome's JavaScript V8 engine and uses an event-driven model and non-blocking I/O architecture, making it particularly suitable for real-time and high-throughput applications.
  
The main features of **Node.js** are:
  
- `Performance`: With its event-driven execution model, Node.js is capable of handling a large number of simultaneous connections with low latency.
- `Modularity`: Node.js uses a module system to organize code into small, reusable units, making it easier to manage large-scale projects.
- `Ecosystem`: The npm (Node Package Manager) is one of the largest open-source library ecosystems, offering modules for almost any imaginable task.
- `Versatility`: Node.js can be used to create a variety of applications, ranging from web servers and RESTful APIs to desktop applications and command-line tools.
  
By combining JavaScript and Node.js, developers can create complete web and mobile applications using a single programming language for both front-end and back-end, making maintenance and development more manageable.

Here's a simple "Hello, Holberton School!" example in JavaScript and Node.js:
  
```javascript
console.log("Hello, Holberton School!"); 

#output: Hello, Holberton School!
```

## Resources
### Read or Watch:

- [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
- [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
- [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Module patterns](http://darrenderidder.github.io/talks/ModulePatterns/#/)
- [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
- [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`

## More Info
### Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install Semi-Standard
[Documentation](https://github.com/standard/semistandard)

```bash
$ sudo npm install semistandard --global
```

------------------

## Tasks

### [0. First Constant, First Print](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/0-javascript_is_amazing.js)
Write a script that prints “JavaScript is amazing”:

- You must create a constant variable called `myVar` with the value “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./0-javascript_is_amazing.js 
JavaScript is amazing
```
</details>

--------------

### [1. 3 Languages](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/1-multi_languages.js)
Write a script that prints 3 lines:

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
```
</details>

----------------

### [2. Arguments](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/2-arguments.js)
Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print “No argument”
- If only one argument is passed to the script, print “Argument found”
- Otherwise, print “Arguments found”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
  
Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv)

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./2-arguments.js 
No argument
  
mathieu@ubuntu:~/$ ./2-arguments.js Best
Argument found
  
mathieu@ubuntu:~/$ ./2-arguments.js Best School
Arguments found
```
</details>

-----------------

### [3. Value Of My Argument](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/3-value_argument.js)
Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print “No argument”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./3-value_argument.js 
No argument
  
mathieu@ubuntu:~/$ ./3-value_argument.js School
School
```
</details>

------------------

### [4. Create a Sentence](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/4-concat.js)
Write a script that prints two arguments passed to it, in the following format: “ is ”

- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./4-concat.js c cool
c is cool
  
mathieu@ubuntu:~/$ ./4-concat.js c 
c is undefined
  
mathieu@ubuntu:~/$ ./4-concat.js
undefined is undefined
```
</details>

-----------------

### [5. An Integer](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/5-to_integer.js)
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print “Not a number”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./5-to_integer.js 
Not a number
  
mathieu@ubuntu:~/$ ./5-to_integer.js 89
My number: 89
  
mathieu@ubuntu:~/$ ./5-to_integer.js "89"
My number: 89
  
mathieu@ubuntu:~/$ ./5-to_integer.js 89.89
My number: 89
  
mathieu@ubuntu:~/$ ./5-to_integer.js School
Not a number
```
</details>

----------------

### [6. Loop To Languages](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/6-multi_languages_loop.js)
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop (`while`, `for`, etc.)

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
```
</details>

------------------

### [7. I Love C](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/7-multi_c.js)
Write a script that prints x times “C is fun”

- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print “Missing number of occurrences”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (`while`, `for`, etc.)

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./7-multi_c.js 2
C is fun
C is fun
  
mathieu@ubuntu:~/$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
  
mathieu@ubuntu:~/$ ./7-multi_c.js 
Missing number of occurrences

mathieu@ubuntu:~/$ ./7-multi_c.js -3
```
</details>

------------

### [8. Square](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/8-square.js)
Write a script that prints a square

- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print “Missing size”
- You must use the character `X` to print the square
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop (`while`, `for`, etc.)

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./8-square.js
Missing size
  
mathieu@ubuntu:~/$ ./8-square.js School
Missing size
  
mathieu@ubuntu:~/$ ./8-square.js 2
XX
XX
  
mathieu@ubuntu:~/$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
  
mathieu@ubuntu:~/$ ./8-square.js -3
```
</details>

---------------

### [9. Add](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/9-add.js)
Write a script that prints the addition of 2 integers

- The first argument is the first integer
- The second argument is the second integer
- You have to define a function with this prototype: `function add(a, b)`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./9-add.js 
NaN
  
mathieu@ubuntu:~/$ ./9-add.js 1
NaN
  
mathieu@ubuntu:~/$ ./9-add.js 1 7
8
  
mathieu@ubuntu:~/$ ./9-add.js 13 89
102
```
</details>

------------------

### [10. Factorial](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/10-factorial.js)
Write a script that computes and prints a factorial

- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- You must do it recursively
- You must use a function
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./10-factorial.js 
1
  
mathieu@ubuntu:~/$ ./10-factorial.js 3
6
  
mathieu@ubuntu:~/$ ./10-factorial.js 89
1.6507955160908452e+136
  
mathieu@ubuntu:~/$ ./10-factorial.js 333
Infinity
```
</details>

------------------

### [11. Second Biggest!](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/11-second_biggest.js)
Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer
- If no argument passed, print `0`
- If the number of arguments is 1, print `0`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ ./11-second_biggest.js 
0
  
mathieu@ubuntu:~/$ ./11-second_biggest.js 1
0
  
mathieu@ubuntu:~/$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```
</details>

--------------

### [12. Object](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/12-object.js)
Update this script to replace the value `12` with `89`:

- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

  
mathieu@ubuntu:~/$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```
</details>

---------------

### [13. Add File](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/13-add.js)
Write a function that returns the addition of 2 integers.

- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`

[Tip](http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
  
  
mathieu@ubuntu:~/$ ./13-main.js
8
```
</details>

---------------------

### [14. Const Or Not Const](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/100-let_me_const.js)
Write a file that modifies the value of `myVar` to `333`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
  
  
mathieu@ubuntu:~/$ ./100-main.js
333
```
</details>

Do you get it? Tweet! Post! Talk about it!
  
Hint: Scope
  
**This exercise doesn’t pass `semistandard`** so don’t worry about it.

------------------

### [15. Call Me Moby](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/101-call_me_moby.js)
Write a function that executes `x` times a function.

- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
  
  
mathieu@ubuntu:~/$ ./101-main.js
C is fun
C is fun
C is fun
```
</details>

----------------

### [16. Add Me Maybe](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/102-add_me_maybe.js)
Write a function that increments and calls a function.

- The function must be visible from outside
- Prototype: `function (number, theFunction)`
- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
  
  
mathieu@ubuntu:~/$ ./102-main.js
New value: 5
```
</details>

-------------------

### [17. Increment Object](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x10-javascript-warm_up/103-object_fct.js)
Update this script by adding a new function `incr` that increments the integer `value`.

- You are not allowed to use `var`

<details>
<summary>Test File</summary>
<br>
  
```javascript
mathieu@ubuntu:~/$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);


mathieu@ubuntu:~/$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
```
</details>

-----------------

## Author

- Mathieu Morel
