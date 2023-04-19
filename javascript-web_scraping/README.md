# <p align=center>JavaScript - Web scraping</p>

<img src="https://www.bestproxyreviews.com/wp-content/uploads/2020/09/web-scraping-with-javascript.jpg" width="100%">

## 🌟 JavaScript Web Scraping 🌟

JavaScript Web Scraping is a project designed to help you extract and manipulate data from websites in a simple and efficient way. By using modern JavaScript techniques 💡 and popular libraries such as `axios` ⚡️, `node-fetch` 📦, and `request` 📡, you'll be able to retrieve information from various web sources 🌐 and process them as structured data 📂. This project provides an excellent starting point for familiarizing yourself with web scraping in JavaScript and developing your skills 🔧 in this field.

## 📚 Resources 📚
### Read or Watch:

- [ Working With JSON Data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The Workflow Of Accessing The Attributes Of a Simply-Created JSON Object By Jimmy Tran From Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [Request Module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## 🔍 Requirements 🔍
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## ℹ️ More Info ℹ️
### Install Node 10

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install Semi-Standard
[Documentation](https://github.com/standard/semistandard)

```bash
$ sudo npm install semistandard --global
```

### Install `Request` Module And Use It
[Documentation](https://github.com/request/request)

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

---------------------

## ✅ Tasks ✅

### [0. Readme](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/0-readme.js)
Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the error object

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ cat cisfun
C is super fun!
  
mathieu@ubuntu:~/$ ./0-readme.js cisfun
C is super fun!

mathieu@ubuntu:~/$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```
</details>

-------------------

### [1. Write Me](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/1-writeme.js)
Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in `utf-8`
- If an error occurred during while writing, print the error object

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./1-writeme.js my_file.txt "Python is cool"
mathieu@ubuntu:~/$ cat my_file.txt ; echo ""
Python is cool
```
</details>

-----------------

### [2. Status Code](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12javascript-web_scraping/2-statuscode.js)
Write a script that display the status code of a `GET` request.

- The first argument is the URL to request (`GET`)
- The status code must be printed like this: `code: <status code>`
- You must use the module `request`

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
  
mathieu@ubuntu:~/$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
```
</details>

--------------------

### [3. Star Wars Movie Title](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/3-starwars_title.js)
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID
- You must use the [Star wars API](https://swapi-api.hbtn.io) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`
- You must use the module `request`

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./3-starwars_title.js 1
A New Hope
  
mathieu@ubuntu:~/$ ./3-starwars_title.js 5
Attack of the Clones
```
</details>

---------------------

### [4. Star Wars Wedge Antilles](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/4-starwars_count.js)
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

- The first argument is the API URL of the [Star wars API](https://swapi-api.hbtn.io): `https://swapi-api.hbtn.io/api/films/`
- Wedge Antilles is character ID `18` - your script **must** use this ID for filtering the result of the API
- You must use the module `request`

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
3
```
</details>

-------------------

### [5. Loripsum](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/5-request_store.js)
Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be UTF-8 encoded
- You must use the module `request`

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./5-request_store.js http://loripsum.net/api loripsum
mathieu@ubuntu:~/$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>
```
</details>

----------------

### [6. How Many Completed?](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/6-completed_tasks.js)
Write a script that computes the number of tasks completed by user id.

- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
- Only print users with completed task
- You must use the module `request`

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
```
</details>

-------------------

### [7. Who Was Playing In This Movie?](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/100-starwars_characters.js)
Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name by line
- You must use the [Star wars API](https://swapi-api.hbtn.io)
- You must use the module `request`

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
```
</details>

----------------

### [8. Right Order](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x12-javascript-web_scraping/101-starwars_characters.js)
Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name by line **in the same order of the list “characters” in the `/films/` response**
- You must use the [Star wars API](https://swapi-api.hbtn.io)
- You must use the module `request`

<details>
<summary>File Test</summary>
<br>

```js
mathieu@ubuntu:~/$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```
</details>

------------------

## 👤 Author 👤

- Mathieu Morel
