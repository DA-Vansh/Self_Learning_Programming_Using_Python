print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines \t tabs.')

poem = """
\t The lovely wprld
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------------------")
print(poem)
print("--------------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

#Here we have defined the function with 1 parameter called started
def secret_formula(started):
    jelly_beans = started*500       #Under the function we have defined 3 variables
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates    #return defines 3 values for 3 variables this function outputs when you call it.

start_point = 10000 #Creating a new variable with value of 10000
any_beans, jars, crates = secret_formula(start_point) #We are passing 3 arguments for the function and assigning the value of the variable start_point to the parameter "started".

#remember this is anothere way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with an f"" string
print(f"We'd have {any_beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point/10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))