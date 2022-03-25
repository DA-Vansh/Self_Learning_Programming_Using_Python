#Here I am going to create a formula for algebric equation (a+b)^2

def square_a(a):
    print(f"SQUARING {a} * {a}")
    return a * a

def square_b(b):
    print(f"SQUARING {b} * {b}")
    return b * b

def product(a,b):
    print(f"PRODUCT 2*({a} * {b})")
    return a * b

print ("What is the formula for (a + b)^2?")

step_1 = square_a(2)
step_2 = square_b(4)
step_3 = 2*product(2,4)

formula = step_1 + step_2 + step_3

print(f"The final output for the equation (a + b)2 is:", formula, f"And the formula is {step_1} added with {step_2} and lastly added with {step_3}")
