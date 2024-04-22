# Lexer in Python
The lexer program for C Lite grammar in Python reads through the source code to find and pull out meaningful bits known as tokens. It recognizes various parts of the code like comments, names, numbers, and symbols, helping to sort out and understand the different pieces of the C Lite language. 

## Utils Folder
Utils folder contains all of the helpers to create the Lexer.
* tokenizer_class has the class for translating the code
* helpers has the helper/friend functions

## Main
Has minimal code. It is used to run the program, call the necessary toolkits to tokenize the input

## How to use it
This program has to be run from the console and make sure Python3 is installed on your machine.

### There are 2 ways of using it:
* You can always run the following command `python3 main.py --help` for MacOS/Linux or `python main.py --help` for Windows to see a guide of how to use it.
* Enter the input from CLI
    1. Open CMD for Windows or Terminal for MacOS/Linux
    2. Navigate to the correct directory with the use of the command `cd [directory]`
    3. When you are in the correct directory run the following command `python main.py --cli` or `python3 main.py --cli` on MacOS/Linux
    4. Enter the input line by line and make sure there is only one empty line on the end; nowhere else
    5. The output will be stored in the outputs folder
* Read input from file
    1. Open CMD for Windows or Terminal for MacOS/Linux
    2. Navigate to the correct directory with the use of the command `cd [directory]`
    3. Make sure that the file you want to tokenize is in the inputs folder. _there is already a test.c file to test it_
    3. When you are in the correct directory and the file is in the inputs folder run the following command `python main.py --file [name_of_the_file]` or `python3 main.py --file [name_of_the_file]` on MacOS/Linux


## About the Authors
This is a college project. There are only 2 participants Austin Kite and Filip Dimitrievski that are working on it. The project is for CPS450, a class in Central Michigan University and the professor is Dr. Qiyu Sun
