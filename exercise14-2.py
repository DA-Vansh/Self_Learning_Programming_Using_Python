from sys import argv

script, name, last_name = argv
prompt = ':'

print (f"Hello, {name} {last_name}, what are we planning to learn in this {script}.")
print ("What is new in this script?")

print (f"We are going to learn about variables, {name}. Can you identity what argument is assigned to the variable prompt?")
var_prompt = input(prompt)

print (f"In this {script}, we will also learn how to unpack variables using the module 'argv'.")
print ("What does argv stands for?")
argu = input(prompt)

print (f"""
So, {name}, in this {script}
we have a lot of area to cover. We are learning about 
assigning variables like {var_prompt}, and understanding the functionality 
of {argu} abreviated as 'argv' module.
""")