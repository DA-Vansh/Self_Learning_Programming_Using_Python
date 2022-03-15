from sys import argv
#Hte os.path module is always the path module suitable for the operating system Python is running on, and therefore usable for local paths.
from os.path import exists # Here we are importing another command or module called exists. This returns True if a file exists, based on its name in a string as an argument. It returns False if not.

#Here we are using argv to get input of 3 variables
script, from_file, to_file = argv

#Print command using the format method to output the value of the variables assigned using argv
print (f"Copying from {from_file} to {to_file}")

#We could do these two on one line, how?
in_file = open(from_file)   #Here we are using the open function to pass the parameter from_file and assigning to the variable in_file

#Read all the contents in the 'from_file' and assign to variable 'indata'
indata = in_file.read()     #Here we are calling the read function on the variable in_file to read the file assigned to the variable in_file

print (f"The input file is {len(indata)} bytes long")   #len() is a built-in function in Python. Gives length of the given string, array, tuple, dictionary, and in this case file.

print (f"Does the output file exist? {exists(to_file)}")    #Here we have used the exists( ) function to obtain a True or False answer.
print ("Ready, hit RETURN to continue, CTRL-C to abort.")   #Giving the user the option to continue or abort
input() # Waiting for Users response.

out_file = open(to_file, 'w')
out_file.write(indata) #calling the write function for in_file over the variable out_file. Using this logic we copied the in_file to out_file.

print ("Alright, all done")

#Closing both files. You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
out_file.close()
in_file.close()



