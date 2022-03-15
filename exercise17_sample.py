from sys import argv

#Here I am going to try and copy paste one file to another in few lines of code (logic)
script, x_in, y_out = argv

#Lets try to copy file x_in to y_out
#x_in = read or copy this variable
#y_out = write or paste into this variable

x = open(x_in, 'r') # The x variable is assigned the object x_in to read
y = open(y_out, 'w') #The y variable is assigned the object y_out to be written
#if we do this
#y.write(x) This will give a typeerror: saying that write() argument must be str(or string). This is because, x variable is assigned to object 'x_in' and not a string or str 

#Calling the write function to write the contents of x to y.
y.write(x.read())  #This argument  x.read() is a string or calling read function on variable x is string for the write function. 
#Hopefully this does it.
print ("Successfully copied.") 

x.close()
y.close()
