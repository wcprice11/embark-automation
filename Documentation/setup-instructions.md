# Setup
To start you will need to clone this repository to a folder on your computer. This can be done in terminal with `git clone "https://github.com/wcprice11/embark-automation"`.
From there you will need to make sure you have the necessary requirements:

## Python 
This test suite is written almost entirely in python.
Use the following if you aren't sure if python is installed on your system.

### **Windows**:

open command prompt and type:
`python`
If python is installed it should list the version and put you in a live python environment:
```
Python 3.10.5 (...)
Type "help, "copyright", "credits" or "license" for more information.
>>> 
```
You can type `exit()` to get back to the command line.

If python is not installed you will get an error message:
`python : The term 'python' is not recognized ...`

If this is the case, you can download and install python from [here](https://www.python.org/downloads/) (python.org).

Test again to make sure it is installed.

### **MacOS**
open a terminal and type:
`which python3` 
(Note the "3")

If this prints out a directory you're all set!

If python is not installed you will get an error message:
`python3 not found`

If this is the case, the recommended method of installing python is using `brew` using `brew install python`
If you do not have brew you can follow the instructions on the [brew homepage](https://brew.sh/)
Alternatively you can download python directly from [python.org](https://www.python.org/downloads/).

Once python is installed test again to make sure it is ready to go.

## Virtual Environment
A python virtual environment is also a good idea. You can use a virtual environment service create one manually by going to the project directory and running:

### **Windows**:
`python -m virtualenv venv`

### **MacOS**
`python3 -m virtualenv venv`

This will create a separate instance of python so any modules used here, won't show up in the normal installation.

You can activate it by running:

### **Windows**:
`.\venv\Scripts\activate`

### **MacOS**
`source ./venv/bin/activate`

Once the environment is activated it will display in your command line in parenthesis: `(venv) [your command line profile]`

When you are done using it you can deactivate it by typing `deactivate`

## Required modules

The modules needed for this project are all listed in the requirements.txt file.
You can automatically pass this to pip with:
`pip install -r requirements.txt`

Once this is finished running you should have all the requirements satisfied and be ready to test!