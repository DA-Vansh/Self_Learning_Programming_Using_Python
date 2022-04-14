from multiprocessing.spawn import old_main_modules


people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we couldn't take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's take the trucks.")
else:
    print("Fine, let's stay home then.")

new_people = 15
old_cars = 10
new_trucks = 50

if new_people > old_cars or new_people < old_cars:
    print("Doesn't matter we all can still fit in the old cars.")
else:
    print("Lets take the trucks then.")

if old_cars > new_people:
    print("We should take the cars.")
elif old_cars < new_people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if new_trucks > old_cars:
    print("That's too many trucks.")
elif new_trucks < old_cars:
    print("Maybe we couldn't take the trucks.")
else:
    print("We still can't decide.")

if new_people > new_trucks:
    print("Alright, let's take the trucks.")
else:
    print("Fine, let's stay home then.")