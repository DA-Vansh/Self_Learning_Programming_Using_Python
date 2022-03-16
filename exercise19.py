#Here we have defined a function called cheese_and_crackers and we are passing 2 arguments cheese_count and box_of_crackers

def cheese_and_crackers(cheese_count, box_of_crackers):
    print (f"You have {cheese_count} cheeses!")
    print (f"You have {box_of_crackers} boxes of crackers!")
    print ("Man that's enough for the party.")
    print ("Get a blanket.\n")

print ("We can just give the function numbers directly:")
#Here we call, use, run the function cheese_and_crackers by passing values for the arguments
cheese_and_crackers(20, 30)

print ("OR, we can use variables from our script:")
#Here we create 2 variables and assigned them values
amount_of_cheese = 10
amount_of_crackers = 20
#Here we are passing the variables to call, use, or run the function cheese_and_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too:")
#Here we are passing int values by performing math for the arguments while using, running or calling the function
cheese_and_crackers(10+20, 5+6)

print ("And we can combine the two, variables, and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

