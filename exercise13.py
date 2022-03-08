#Here we are importing sys MODULES
from sys import argv

#Here we unpack 'argv' so that, rather than holding all he arguments, it gets assigned to four variables you can work with: script, first, second, and third.
# Pseudo code: Take whatever is in 'argv', unpack it, and assign it to all of these variables on the left in order.
script, first, second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
