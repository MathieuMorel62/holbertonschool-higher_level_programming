# <p align=center>JavaScript - Web jQuery</p>
<img src="https://silvawebdesigns.com/wp-content/uploads/2020/09/jquery-detect-two-elements-colliding.jpg" width="100%">

## 🌟 JavaScript - Web jQuery 🌟

JavaScript Web jQuery is a project designed to help you leverage the power of jQuery, a popular and versatile JavaScript library that simplifies HTML document traversal, manipulation, event handling, and animation. By using jQuery 📚 combined with modern JavaScript techniques 💡, you'll be able to create interactive, dynamic websites 🌐 that engage and delight your users. This project serves as an excellent starting point for familiarizing yourself with jQuery in JavaScript and developing your skills 🔧 in this essential area of web development.

## 📚 Resources 📚
### Read or Watch:

- [What Is JavaScript ?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [Get And Set Content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
- [Manipulate CSS Classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
- [Manipulate DOM Elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
- [API](https://oscarotero.com/jquery/)
- [Introduction](https://jquery-tutorial.net/ajax/introduction/)
- [GET & POST Request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What Went Wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [JQuery](https://jquery.com)
- [JQuery API](https://api.jquery.com)
- [JQuery Ajax](https://learn.jquery.com/ajax/)

## 🔍 Requirements 🔍
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Chrome (version 57.0)
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant with the flag `--global $`: `semistandard *.js --global $`
- You must use JQuery version 3.x
- You are not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## ℹ️ More Info ℹ️
### Import JQuery

```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

----------------------

## ✅ Tasks ✅

### [0. No JQuery](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/0-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can’t use the JQuery API
    
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```
</details>

--------------------

### [1. With JQuery](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/1-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
  
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
  
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
```
</details>

-----------------------

### [2. Click And Turn Red](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/2-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
   
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
```
</details>

----------------------

### [3. Add `.red` Class](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/3-script.js)
Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`
  
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
   
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
```
</details>

--------------------

### [4. Toggle Classes](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/4-script.js)
Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

- The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
- If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
    
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
```
</details>

--------------------

### [5. List Of Elements](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/5-script.js)
Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:
    
- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
     
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
```
</details>

--------------------------

### [6. Change The Text](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/6-script.js)
Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
    
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
```
</details>

------------------------

### [7. Star Wars Character](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/7-script.js)
Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

- The name must be displayed in the HTML tag `DIV#character`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
   
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
```
</details>

---------------------

### [8. Star Wars Movies](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/8-script.js)
Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

- All movie titles must be list in the HTML tag `UL#list_movies`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
   
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
```
</details>

--------------------

### [9. Say Hello!](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/9-script.js)
Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.
  
- The translation of “hello” must be displayed in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Your script must work when it is imported from the `<head>` tag
    
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
</details>

--------------------

### [10. No jQuery - Document Loaded](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/100-script.js)
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can’t use the jQuery API
- Note: Your script must be imported from the `<head>` tag, not at the end of the HTML
     
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
</details>

----------------------

### [11. List, Add, Remove](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/101-script.js)
Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- When the user clicks on `DIV#add_item`: a new element is added to the list
- When the user clicks on `DIV#remove_item`: the last element is removed from the list
- When the user clicks on `DIV#clear_list`: all elements of the list are removed
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- You script must work when it imported from the `HEAD` tag
    
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
</details>

-----------------------

### [12. Say Hello To Everybody!](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/102-script.js)
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: `https://hellosalut.stefanbohacek.dev/?lang=`
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation must be fetched when the user clicks on `INPUT#btn_translate`
- The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- You script must work when imported from the `<head>` tag
    
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
</details>

--------------------------

### [13. And Press ENTER](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x13-javascript-web_jquery/103-script.js)
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: `https://hellosalut.stefanbohacek.dev/?lang=`
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
- The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- You script must work when imported from the `<head>` tag
     
Please test with this HTML file in your browser:

<details>
<summary>File Test</summary>
<br>
  
```html
mathieu@ubuntu:~/$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
```
</details>

-----------------------

## 👤 Author 👤

- Mathieu Morel
