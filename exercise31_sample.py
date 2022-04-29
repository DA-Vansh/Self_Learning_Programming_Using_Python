print("""What is the day today?
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday """)

day = input(">")

print("Vansh works: Monday, Tuesday, and Wednesday")
print("Dave works: Thursday, Friday, and Saturday")
print("Kelly works: Monday, Tuesday, Wednesday, Thursday, and Friday")

print("""Whose will you choose to do the dishwasher?
1. Vansh or 2. Dave or 3. Kelly""")

turn = input(">")

if turn == "1" and day == "Monday":
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Vansh to do it?")
    print("2. Choose someone else.")

    choice_vansh = input(">")
    if choice_vansh == "1":
        print(f"Your choice was: {choice_vansh}. Vansh will do it after work, but you made him unhappy.")
    elif choice_vansh == "2":
        print(f"Your choice was: {choice_vansh}. You have to choose either Dave or Kelly.")
    else:
        print("Do it yourself.")

elif turn == "1" and day == "Tuesday":
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Vansh to do it?")
    print("2. Choose someone else.")

    choice_vansh = input(">")
    if choice_vansh == "1":
        print(f"Your choice was: {choice_vansh}. Vansh cursed you. He said he will not do it.")
    elif choice_vansh == "2":
        print(f"Your choice was: {choice_vansh}. You have to choose either Dave or Kelly.")
    else:
        print("Do it yourself.")

elif turn == "1" and day == "Wednesday":
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Vansh to do it?")
    print("2. Choose someone else.")

    choice_vansh = input(">")
    if choice_vansh == "1":
        print(f"Your choice was: {choice_vansh}. Vansh will do it.")
    elif choice_vansh == "2":
        print(f"Your choice was: {choice_vansh}. You have to choose either Dave or Kelly.")
    else:
        print("Do it yourself.")

elif turn == "1" and day == "Thursday":
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Vansh to do it?")
    print("2. Choose someone else.")

    choice_vansh = input(">")
    if choice_vansh == "1":
        print(f"Your choice was: {choice_vansh}. Vansh has a day off. He says f*** off.")
    elif choice_vansh == "2":
        print(f"Your choice was: {choice_vansh}. You have to choose either Dave or Kelly.")
    else:
        print("Do it yourself.")
    
elif turn == "1" and day == "Friday":
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Vansh to do it?")
    print("2. Choose someone else.")

    choice_vansh = input(">")
    if choice_vansh == "1":
        print(f"Your choice was: {choice_vansh}. Vansh will do it.")
    elif choice_vansh == "2":
        print(f"Your choice was: {choice_vansh}. You have to choose either Dave or Kelly.")
    else:
        print("Do it yourself.")

elif turn == "1" and day == "Saturday":
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Vansh to do it?")
    print("2. Choose someone else.")

    choice_vansh = input(">")
    if choice_vansh == "1":
        print(f"Your choice was: {choice_vansh}. Vansh will not do it. Its Saturday.")
    elif choice_vansh == "2":
        print(f"Your choice was: {choice_vansh}. You have to choose either Dave or Kelly.")
    else:
        print("Do it yourself.")

elif turn == "2" and day == 'Monday':
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Dave do it?")
    print("2. Choose someone else.")
    
    choice_dave = input(">")
    if choice_dave == "1":
        print(f"Your choice was: {choice_dave}. Dave will not do it. It's Monday for god's sake.")
    elif choice_dave == "2":
        print(f"Your choice was: {choice_dave}. See if Vansh or Kelly will do it.")
    else:
        print("Let it stink up the place.")

elif turn == "2" and day == 'Tuesday':
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Dave do it?")
    print("2. Choose someone else.")
    
    choice_dave = input(">")
    if choice_dave == "1":
        print(f"Your choice was: {choice_dave}. Dave will do it. He is feeling helpful today.")
    elif choice_dave == "2":
        print(f"Your choice was: {choice_dave}. See if Vansh or Kelly will do it.")
    else:
        print("Why dont you do it! After all you have been ordering around.")

elif turn == "2" and day == 'Wednesday':
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Dave do it?")
    print("2. Choose someone else.")
    
    choice_dave = input(">")
    if choice_dave == "1":
        print(f"Your choice was: {choice_dave}. It's his last day off for the week. Are you seriously thinking Dave will do dishwasher!")
    elif choice_dave == "2":
        print(f"Your choice was: {choice_dave}. See if Vansh or Kelly will do it.")
    else:
        print("No, No, its been a few days someone will have to do the dishwasher.")

elif turn == "2" and day == 'Thursday':
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Dave do it?")
    print("2. Choose someone else.")
    
    choice_dave = input(">")
    if choice_dave == "1":
        print(f"Your choice was: {choice_dave}. Dave will not do it. He has to work")
    elif choice_dave == "2":
        print(f"Your choice was: {choice_dave}. See if Vansh or Kelly will do it.")
    else:
        print("Let it stink up the place.")

elif turn == "2" and day == 'Friday':
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Dave do it?")
    print("2. Choose someone else.")
    
    choice_dave = input(">")
    if choice_dave == "1":
        print(f"Your choice was: {choice_dave}. Dave will do it. He is unhappy.")
    elif choice_dave == "2":
        print(f"Your choice was: {choice_dave}. See if Vansh or Kelly will do it.")
    else:
        print("I don't know who will do it.")

elif turn == "2" and day == 'Saturday':
    print("There are 2 options")
    print("Choose one:")
    print("1. Will Dave do it?")
    print("2. Choose someone else.")
    
    choice_dave = input(">")
    if choice_dave == "1":
        print(f"Your choice was: {choice_dave}. Dave say's, 'Don't even look at me or say anything!'")
    elif choice_dave == "2":
        print(f"Your choice was: {choice_dave}. See if Vansh or Kelly will do it.")
    else:
        print("Let Kelly do it. She has done nothing till now.")

elif turn == "3" and day == "Monday":
    print("Ther are 2 options.")
    print("Choose one:")
    print("1. Will Kelly do it?")
    print("2. Choose someone else.")

    choice_kelly = input(">")
    if choice_kelly == "1":
        print(f"Your choice was: {choice_kelly}.Kelly say's, 'Nope not happening.'")
    elif choice_kelly == "2":
        print(f"Your choice was: {choice_kelly}. Who. No one wants to do it.")
    else:
        print("I guess you will have to do it.")

elif turn == "3" and day == "Tuesday":
    print("Ther are 2 options.")
    print("Choose one:")
    print("1. Will Kelly do it?")
    print("2. Choose someone else.")

    choice_kelly = input(">")
    if choice_kelly == "1":
        print(f"Your choice was: {choice_kelly}.Kelly say's, 'Nope, I am working all week.'")
    elif choice_kelly == "2":
        print(f"Your choice was: {choice_kelly}. Who then? No one wants to do it.")
    else:
        print("Dave has agreed to do it")

elif turn == "3" and day == "Wednesday":
    print("Ther are 2 options.")
    print("Choose one:")
    print("1. Will Kelly do it?")
    print("2. Choose someone else.")

    choice_kelly = input(">")
    if choice_kelly == "1":
        print(f"Your choice was: {choice_kelly}.Kelly say's, 'Nope!!!!!!!'")
    elif choice_kelly == "2":
        print(f"Your choice was: {choice_kelly}. Find someone else")
    else:
        print("Vansh has already agreed to do it.")

elif turn == "3" and day == "Thursday":
    print("Ther are 2 options.")
    print("Choose one:")
    print("1. Will Kelly do it?")
    print("2. Choose someone else.")

    choice_kelly = input(">")
    if choice_kelly == "1":
        print(f"Your choice was: {choice_kelly}.Kelly say's, 'No.... How many time I have to tell you?'")
    elif choice_kelly == "2":
        print(f"Your choice was: {choice_kelly}. Vansh say's 'F*** off', Dave is not interested. So You have to do it Kelly!!")
    else:
        print("I guess you will have to do it.")

elif turn == "3" and day == "Friday":
    print("Ther are 2 options.")
    print("Choose one:")
    print("1. Will Kelly do it?")
    print("2. Choose someone else.")

    choice_kelly = input(">")
    if choice_kelly == "1":
        print(f"Your choice was: {choice_kelly}.Kelly say's, 'Nope not happening.'")
    elif choice_kelly == "2":
        print(f"Your choice was: {choice_kelly}. Vansh has agreed to do it anyway.")
    else:
        print("Let them stink.")

elif turn == "3" and day == "Saturday":
    print("Ther are 2 options.")
    print("Choose one:")
    print("1. Will Kelly do it?")
    print("2. Choose someone else.")

    choice_kelly = input(">")
    if choice_kelly == "1":
        print(f"Your choice was: {choice_kelly}.Kelly say's, 'Its Saturday, Hell NOOOO.'")
    elif choice_kelly == "2":
        print(f"Your choice was: {choice_kelly}. No one wants to do it.")
    else:
        print("Lets wait for Monday.") 

else:
    print("Great choice. No Chores for anyone. Let the place stink.")