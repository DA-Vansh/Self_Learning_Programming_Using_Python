import sys
script, input_encoding, error = sys.argv

#Creating a function "main" with 3 arguments
def main(language_file, encoding, errors):
    #Calling readline() function to read each line from the language_file and assign to variable 'line'.
    line = language_file.readline()
    #Intro Logic(if statement): You can test the truth of a variable and, based on that truth, run a piece of code or not run it. Here we are testing, 'if line' line variable has something. readline() function will read every line in the language_file untill it reaches the end of the file where if line simply tests for an empty string. As long as readline() reads something, this will be TRUE and hence the code will execute lines 10-11, when readline() reads empty string or nothing, this will be FALSE and skip lines 10-11.  
    if line:
        print_line(line, encoding, errors)  #Here I am calling a separate function to do the printing of 'line'. The function print_line is defined in line-13.
        return main(language_file, encoding, errors) #Calling function in itself is called Recursive Function. This is true and executable because of the 'if -statement' in line 9. This keeps the function from not looping forever, and hence this is allowed in Python.

#Defining the print_line function, which does actual encoding of each line from language.txt file.
def print_line(line, encoding, errors):
    next_lang = line.strip()                                    #This is simply stripping of the trailing \n on the line string.
    raw_bytes = next_lang.encode(encoding, errors=errors)       #In DBES, Decode Bytes, Encode Strings. Here, next_lang variable is a string, so to get raw bytes I must call .encode() on variable next_lang to encode the strings. I pass to encode() the encoding I want and how to handle the errors.
    cooked_string = raw_bytes.decode(encoding, errors=errors)   #In DBES, Decode Bytes, the variable, raw_bytes includes bytes, so I called .decode() onto it to get a Python String. This string should be same as next_lang variable.

    print(raw_bytes, "<==>", cooked_string)         #Print them both out to show what they look like.

languages = open("languages.txt", encoding = "utf-8")   #I am done defining the functions, this opens that language.txt file.

main(languages, input_encoding, error)      #this runs the main function with all the corrected parameters to get everything going and kick-start the loop.