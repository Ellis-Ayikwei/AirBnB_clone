#  AirBnB clone - The console

The AirBnb clone is a simple copy of the AirBnB website. It is a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The Console
The console is a command line interpreter that will take in commands used to manage various data and objects on the storeage engine for the backend part of the website. It should be able to ;

- manage and manipulate data models and object (create, update, destroy, etc) objects
- retrieve, store and persist objects to a file (JSON file)
- operate on objects (count, compute stats, etc...)
- Update attributes of an object

## To start and use the console:

- Clone this repo: git clone "https://github.com/Alphajay1/AirBnB_clone.git"
- Enter AirBnb_clone directory: cd AirBnB_clone

- To Run the console(interactively): enter ./console.py

- A prompt (hbnb) is displayed for input, then enter command. Example::memo:
- (hbnb) show <user> : Prints the string representation of an instance based on the class name and id.
- (h- bnb) EOF : exits console
- (hbnb) create <class> : Create an object (prints its id)
- (hbnb) all or all <class> : Show all objects, or all instances of a class
- To Run hbnb(non-interactively): echo "<command>" | ./console.py. Example::memo:

- echo "help" | ./console.py
- It shows the lists of commands available. If you include a command you want help on, the output is more verbose and restricted to details of that command, when available.
- echo "count place" | ./console.py
- Retrieves the number of instances of a given class : place

## A look of some examples, usage and behaviour on the terminal when run interactively:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
## But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## File Descriptions

- console.py - the console contains the entry point of the command interpreter. List of commands this console current supports:

- `EOF` - exits console
- `quit` - exits console
- `<emptyline>` - overwrites default emptyline method and does nothing
- `create` - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id
- `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
- `show` - Prints the string representation of an instance based on the class name and id.
- `all` - Prints all string representation of all instances based or not on the class name.
- `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
- `count` - Retrieve the number of instances of a given class.
- `models/` directory contains classes used for this project:
- base_model.py - The BaseModel class from which future classes will be derived

## Authors
Ayako James.
Ellis Armah Ayikwei.

## License
Public Domain. No copy write protection.
