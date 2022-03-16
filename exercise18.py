# this one is like your scripts with argv
def print_two (*args):                                          #Here we are telling Python to make a function using def for "define" and give the function a name (print_two). We passed *argv parameter and ended the line using ':'
# After the colon (:), all the lines that are indented four spaces will become attached to print_two. The below indented line is the one that unpacks the arguments, the same as with your script.
    arg1, arg2 = args
    print (f"arg1 : {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print (f"arg1: {arg1}, arg2: {arg2}")

# This one just takes one argument
def print_one(arg1):
    print (f"arg1: {arg1}")

# This one takes no arguments
def print_none():
    print ("I got nothing.")

#Passing the arguments for all the defined functions.
print_two("Vansh", "Shah")
print_two_again("Vansh", "Shah")
print_one("First!")
print_none()

#***#NOTE:What does * in *args do? That tells Python to take all the arguments to the function and then put them in args list. It's like argv that you've been using but for functions.  