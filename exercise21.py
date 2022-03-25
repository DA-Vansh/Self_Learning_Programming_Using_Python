#Introduction of the word RETURN, to set variables to be a value from a function.

#Defining a function, add that has 2 arguments. Whenever, this function is called, it returns a task (a + b)
from re import I, sub


def add(a,b):
    #Let's Add the values that will be passed into the 2 arguments a & b
    print(f"ADDING {a} + {b}") 
    return a + b #Here our function is called with 2 arguments: a and b

#Defining a function, subtract, that has 2 arguments
def subtract(a,b):
    #Let's subtract the values that will be passed into the arguments: a and b
    print(f"SUBTRACTING {a} - {b}")
    return a - b #Here the function is called with 2 arguments: a and b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

    #Understanding what happens by defining a function above. Example. add
    #Step 1: Defined a function with arguments a,b
    #Step 2: When that function is called, Print the statement: ADDING a + b
    #Step 3: Perform the task assigned, i.e. we are adding a + b = c.
    #These steps repeat when ever the function add is called.

print("Let's do some math with just the functions.")

#Unloading the values in the place of the arguments and assigning them to a variable.

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for the extra credit, type it anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print(f"That becomes", what, "Can you do it by hand?")
print(f"Just checking, will this {what} value be printed here.")
