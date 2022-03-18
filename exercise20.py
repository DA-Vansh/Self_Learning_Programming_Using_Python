import re
from sys import argv

#Here we are using argv to get2 input variables
script, input_file = argv

#Defining a print_all function
def print_all(f):       #Here we have passed a variable in print_all function
    print(f.read())     #Here whenever print_all function is called, the read() function is called on the variable f. 

def rewind(f):          #Another function
    f.seek(0)           #The seek function is dealing in bytes, not lines. The code seek(0) moves the file to the 0 byte(first byte) is the file.
def print_a_line(line_count, f):    #Another function with 2 variables
    print(line_count, f.readline())  #readline() is the code that scans each byte of the file until ot finds a \n character, then stops reading the file ti return what it found so far.

#Lets open the file object and assign it to the current file
current_file = open(input_file) #Here we are passing the file object we receive from the arg input_file and assigning to the variable currentfile.


## Here is where we start using most of the defined functions
print("First let's print the whole file.")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)
