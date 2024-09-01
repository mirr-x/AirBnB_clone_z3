# AirBnB Clone - MySQL

![blabla](https://i.ibb.co/ncJ1H6Z/65f4a1dd9c51265f49d0.png)

Welcome to the AirBnB clone project! This project involves building a command interpreter to manage AirBnB objects, creating a simple flow of serialization/deserialization, and implementing a file storage engine.

## Project Overview

The primary goal of this project is to create a command interpreter that allows users to:

- Create new objects (e.g., User, State, City, Place)
- Retrieve objects from a file or database
- Perform operations on objects (e.g., count, compute stats)
- Update attributes of an object
- Destroy an object

## Objectives

- What is Unit testing and how to implement it in a large project
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
- How to create a MySQL database
- How to create a MySQL user and grant it privileges
- What ORM means
- How to map a Python Class to a MySQL table
- How to handle 2 different storage engines with the same codebase
- How to use environment variables

## Project Phase at Last Modification

- Understanding and building a web framework with Flask
- What is a route, how to define routes, and handle variables in routes
- What is a template, how to create dynamic templates and render them in Flask

## HolbertonBnB Stack

### Classes

AirBnB clone implements the following classes:

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review
- Storage

The above classes are handled by one of either two abstracted storage engines, depending on the call - FileStorage or DBStorage.

### FileStorage

The default mode.

In FileStorage mode, every time the backend is initialized, HolbertonBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file [`file.json`](command:_github.copilot.openSymbolFromReferences?%5B%22file.json%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A192%7D%7D%5D%5D "Go to definition"). As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the [`file.json`](command:_github.copilot.openSymbolFromReferences?%5B%22file.json%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A192%7D%7D%5D%5D "Go to definition").

### DBStorage

Run by setting the environmental variables `HBNB_TYPE_STORAGE=db`.

In DBStorage mode, every time the backend is initialized, HolbertonBnB instantiates an instance of DBStorage called storage. The storage object is loaded/re-loaded from the MySQL database specified in the environmental variable `HBNB_MYSQL_DB`, using the user `HBNB_MYSQL_USER`, password `HBNB_MYSQL_PWD`, and host `HBNB_MYSQL_HOST`. As class instances are created, updated, or deleted, the storage object is used to register changes in the corresponding MySQL database. Connection and querying is achieved using SQLAlchemy.

Note that the databases specified for DBStorage to connect to must already be defined on the MySQL server. This repository includes scripts [`setup_mysql_dev.sql`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2Fsetup_mysql_dev.sql%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/mirr/Desktop/amir/github/alx/AirBnB_clone_z2/setup_mysql_dev.sql") and [`setup_mysql_test.sql`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2Fsetup_mysql_test.sql%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/mirr/Desktop/amir/github/alx/AirBnB_clone_z2/setup_mysql_test.sql") to set up `hbnb_dev_db` and `hbnb_test_db` databases in a MySQL server, respectively.

## Console

The console is a command line interpreter that permits management of the backend of HolbertonBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file [`console.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2Fconsole.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/mirr/Desktop/amir/github/alx/AirBnB_clone_z2/console.py") at the command line.

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the file [`console.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2Fconsole.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/mirr/Desktop/amir/github/alx/AirBnB_clone_z2/console.py") by itself:

```bash
$ ./console.py
```

Remember, the console can be run with storage instantiated in either FileStorage or DBStorage mode. The above examples instantiate FileStorage by default, but DBStorage can be instantiated like so:

```bash
$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

The console functions identically regardless of the storage mode.

While running in interactive mode, the console displays a prompt for input:

```bash
$ ./console.py
(hbnb)
```

To quit the console, enter the command [`quit`](command:_github.copilot.openSymbolFromReferences?%5B%22quit%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A37%2C%22character%22%3A40%7D%7D%5D%5D "Go to definition"), or input an EOF signal (ctrl-D).

```bash
$ ./console.py
(hbnb) quit
$
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HolbertonBnB console supports the following commands:

- **create**
  - Usage: [`create <class> <param 1 name>=<param 1 value> <param 2 name>=<param 2 value> ...`](command:_github.copilot.openSymbolFromReferences?%5B%22create%20%3Cclass%3E%20%3Cparam%201%20name%3E%3D%3Cparam%201%20value%3E%20%3Cparam%202%20name%3E%3D%3Cparam%202%20value%3E%20...%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A8%2C%22character%22%3A39%7D%7D%5D%5D "Go to definition")
  - Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file [`file.json`](command:_github.copilot.openSymbolFromReferences?%5B%22file.json%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A192%7D%7D%5D%5D "Go to definition"). When passing parameter key/value pairs, any underscores contained in value strings are replaced by spaces.

```bash
$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb)
(hbnb) create State name="California"
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T21:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "BaseModel", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}, {'id': 'd80e0344-63eb-434a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name': 'California'}}
```

- **show**
  - Usage: [`show <class> <id>`](command:_github.copilot.openSymbolFromReferences?%5B%22show%20%3Cclass%3E%20%3Cid%3E%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A37%2C%22character%22%3A46%7D%7D%5D%5D "Go to definition") or `<class>.show(<id>)`
  - Prints the string representation of a class instance based on a given id.

```bash
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-ac3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
(hbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-ac3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828), 'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
```

- **destroy**
  - Usage: [`destroy <class> <id>`](command:_github.copilot.openSymbolFromReferences?%5B%22destroy%20%3Cclass%3E%20%3Cid%3E%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A37%2C%22character%22%3A25%7D%7D%5D%5D "Go to definition") or `<class>.destroy(<id>)`
  - Deletes a class instance based on a given id.

```bash
$ ./console.py
(hbnb) create State
d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) create Place
3e-8329-4f47-9947-dca80c03d3ed
(hbnb)
(hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) Place.destroy(03486a3e-8329-4f47-9947-dca80c03d3ed)
(hbnb) quit
$ cat file.json ; echo ""
{}
```

- **all**
  - Usage: [`all`](command:_github.copilot.openSymbolFromReferences?%5B%22all%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A37%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") or [`all <class>`](command:_github.copilot.openSymbolFromReferences?%5B%22all%20%3Cclass%3E%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A37%2C%22character%22%3A5%7D%7D%5D%5D "Go to definition") or `<class>.all()`
  - Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.

```bash
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb) create User
b742dbc3-f4bf-425e-b1d4-165f52c6ff81
(hbnb) create User
8f2d75c8-fb82-48e1-8ae5-2544c909a9fe
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[BaseModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
(hbnb) User.all()
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetime(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[User] (b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}"]
(hbnb)
(hbnb) all
["[User] (8f2d75c8-fb82-48e1-8ae5-2544c909a9fe) {'updated_at': datetime.datetime(2019, 2, 17, 21, 44, 44, 428413), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 44, 428413), 'id': '8f2d75c8-fb82-48e1-8ae5-2544c909a9fe'}", "[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.datetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[User] (b742dbc3-f4bf-425e-b1d4-165f52c6ff81) {'updated_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 974608), 'created_at': datetime.datetime(2019, 2, 17, 21, 44, 15, 974608), 'id': 'b742dbc3-f4bf-425e-b1d4-165f52c6ff81'}", "[BaseModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17, 21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
```

- **count**
  - Usage: [`count <class>`](command:_github.copilot.openSymbolFromReferences?%5B%22count%20%3Cclass%3E%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A12%2C%22character%22%3A39%7D%7D%5D%5D "Go to definition") or `<class>.count()`
  - Retrieves the number of instances of a given class.

```bash
$ ./console.py
(hbnb) create Place
12c73223-f3d3-4dec-9629-bd19c8fadd8a
(hbnb) create Place
aa229cbb-5b19-4c32-8562-f90a3437d301
(hbnb) create City
22a51611-17bd-4d8f-ba1b-3bf07d327208
(hbnb)
(hbnb) count Place
2
(hbnb) city.count()
1
(hbnb)
```

- **update**
  - Usage: [`update <class> <id> <attribute name> "<attribute value>"`](command:_github.copilot.openSymbolFromReferences?%5B%22update%20%3Cclass%3E%20%3Cid%3E%20%3Cattribute%20name%3E%20%5C%22%3Cattribute%20value%3E%5C%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22path%22%3A%22%2Fhome%2Fmirr%2FDesktop%2Famir%2Fgithub%2Falx%2FAirBnB_clone_z2%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A37%2C%22character%22%3A52%7D%7D%5D%5D "Go to definition")
  - Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at).

```bash
$ ./console.py
(hbnb) create User
6f348019-0499-420f-8eec-ef0fdc863c02
(hbnb)
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton" 
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': datetime.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-ef0fdc863c02'}
(hbnb)
```

## Testing

Unittests for the HolbertonBnB project are defined in the `tests` folder. To run the entire test suite simultaneously, execute the following command:

```bash
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```bash
$ python3 unittest -m tests/test_console.py
```

## Contributors

- mirr

## License

This project is licensed under the [MIT License](LICENSE).
