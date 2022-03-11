from sys import argv

#here we are using argv to get input for 2 variables
script, filename = argv

#Using the format 'f' command to get the output of the variable filename
print (f"We are going to erase {filename}")
print ("If you don't want that then, press CTRL-C (^C).")
print ("If you do what that then hit RETURN.")

input('?') #Asking using a question here and waiting for them to response

print ("Opening the file....")
target = open(filename, 'w')    #This will create an object file and that will be writable 'w'. The file object is assigned to the variable target.

print ("Truncating the file. Goodbye!")
target.truncate()               #We are calling a function on the variable target to truncate the file object in this case.

print ("Now I am going to ask for 3 lines.")
line1 = input("line 1: " )
line2 = input("line 2: " )
line3 = input("line 3: " )

print ("I am going to write these to the file.")

#Write function is user the open a file for write only (usually overwrite). In this case, we truncate the data in file so there is no overwriting.
target.write(line1)     
target.write("\n")      # This mean moving the cursor to the next  line so every line written is on a new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()          # We are calling the close function on the variable to close the file object associated with the variable target.

print ("Let us see our new updated file.")
target.open('exercise15_sample.txt', 'r')


