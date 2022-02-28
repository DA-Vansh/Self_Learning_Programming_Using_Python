#creating a variable called formatter
formatter = "{} {} {} {}"

print (formatter.format('1','2','3','4')) #This converts int to string
print (formatter.format(1,2,3,4)) #This keeps them as int.
print (formatter.format('One', 'Two', 'Three', 'Four'))
print (formatter.format(True, False, False, True)) 
print (formatter.format("True", "False", "False", "True"))
print (formatter.format(formatter, formatter, formatter, formatter)) #Here or at any other position if you declare 3 values instead of 4 you will get IndexError: Replacement index 3 out of range for positional args tuple
print (formatter.format(formatter,'', formatter,'', formatter,'', formatter)) #The output of this syntax is a thinker, but I am glad I added it. My goal was to space out the output between curly braces, but that didn't happen.
print (formatter.format("This is", 
"driving me",
'crazy',
"with different ways of syntaxing."))
