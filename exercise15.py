from sys import argv

#Here we are using argv to get input for 2 variables
script, filename = argv

#We are assigning the variable txt (filename) by using the open function and calling the parameter 'filename' which from our previous argument will consist of filename, eg: exercise15_sample.txt
txt = open(filename)                        # This will create a file object, and unless you use print(txt.read()), it will not show you the contents of the file.  
print (f"Here is your file {filename}:")    #using the format syntax to print the value of the variable (filename)
print (txt.read())                          #Here we are calling a function on txt called read().

print ("Type the file name again:")         # This is a basic print function where it will print the string ending with ':'
file_again = input('>')                     # Here the variable file_again will be assigned the input value that user enters.

txt_again = open(file_again)                # Same concept as above. We are assigning the variable txt_again (filename) by using the open function and calling the parameter 'file_again' which from our previous argument will consist of filename, eg: exercise15_sample.txt

print (txt_again.read())


