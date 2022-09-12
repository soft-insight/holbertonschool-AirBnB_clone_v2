![Logo](logo.png)
# 0x02. AirBnB clone - MySQL

## Description
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:\

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My object" and "How they are stored and persisted". This means that: from the console code (the shell itself) and from the front-end and RestAPI that we will build later, we will not have to pay attention (deal with) how objects are stored. _This abstraction will also allow changing the storage type easily without updating the code base_. The console will be a tool to validate this storage engine.

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Learning Objectives
* What is Unit testing and how to implement it in a large project
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
* How to create a MySQL database
* How to create a MySQL user and grant it privileges
* What ORM means
* How to map a Python Class to a MySQL table
* How to handle 2 different storage engines with the same codebase
* How to use environment variables

## Commands

| Command | Usage | Description |
| :-------- | :------- | :------------------------- |
| help | **(hbnb) >>>** help [command] | List available commands with "help" or detailed help with "help cmd". |
| EOF | **(hbnb) >>>** EOF | Quit Command to exit the Console |
| destroy | **(hbnb) >>>** destroy | Destroys an object based on class and UUID |
| show | **(hbnb) >>>** show | Shows an object based on class and UUID |
| all | **(hbnb) >>>** all | Shows all objects the program has access to, or all objects of a given class |
| update | **(hbnb) >>>** update | Updates existing attributes an object based on class name and UUID |
| quit | **(hbnb) >>>** quit | Quit Command to exit the Console |

## Execution

Clone the repository _https://github.com/soft-insight/holbertonschool-AirBnB_clone_v2_

**Execution in interactive mode:**
```
$ ./console.py
(hbnb) >>> help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) >>>
(hbnb) >>>
(hbnb) >>> quit
$
```
**Execution in non-interactive mode:**
```
$ echo "help" | ./console.py
(hbnb) >>>
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) >>>
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb) >>>
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) >>>
$
```

## Authors

* [Jaime Rodriguez](https://github.com/soft-insight)
* [Christian Oviedo](https://github.com/ch-ov)
