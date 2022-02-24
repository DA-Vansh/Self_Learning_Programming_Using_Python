types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
#y = "Those who know {binary} and those who {do_not}"
# If you this by mistake you output would be literal.

print (x)
print (y)

print (f"I said:", {x})
print (f"I also said:", {y})

hilarious = False #If you write FALSE then you will get a weird string in your output. 
joke_evaluation = "Isn't this joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ...."
e = "a string with right side."

print (w + e)
