# Exercise 1

print("Exercise 1\n") #prints Exercise 1

info = { #makes a dictionary 
    'first_name' : 'Zach', #defines the variable first_name
    'last_name' : 'Tonacao', #defines the variable last_name
    'age' : 19, #defines the variable age
    'city' : 'Abu Dhabi' #defines the city
}

print(info['first_name']) #prints the value stored in 'first_name'
print(info['last_name']) #prints the value stored in 'last_name'
print(info['age']) #prints the value stored in 'age'
print(info['city']) #prints the value stored in 'city'

#Exercise 2

words = { #creates a dictionary
    'print' : 'displays the value of the variable', #defines the key 'print' with a value
    'input' : 'allows you to enter data in a program', #defines the key 'input' with a value
    'string' : 'is a group of characters or letters', #defines the key 'string' with a value
    'variable' : 'is represented by a letter or a string and is assigned to a value', #defines the key 'variable' with a value
    'constant' : 'is a variable whose value does not change' #defines the key 'constant' with a value
}

print("The function print",{words['print']}, "\n") #prints the definition of the key 'print'
print("The function input",{words['input']}, "\n") #prints the definition of the key 'input'
print("A string",{words['string']}, "\n") #prints the definition of the key 'string'
print("A variable",{words['variable']}, "\n") #prints the definition of the key 'variable'
print("A constant",{words['constant']}, "\n") #prints the definition of the key 'constant'

#Exercise 3D

words = { #makes a dicitonary 
    'print' : 'displays the value of the variable', #defines the key 'print' with a value
    'input' : 'allows you to enter data in a program', #defines the key 'input' with a value
    'string' : 'is a group of characters or letters', #defines the key 'string' with a value
    'variable' : 'is represented by a letter or a string and is assigned to a value',#defines the key 'variable' with a value
    'constant' : 'is a variable whose value does not change' #defines the key 'constant' with a value
}

for key, value in words.items(): #checks the key and value through the dictionary
    print(f"{key} {value}\n") #prints the key and value

#Exercise 4

river = { #makes a dictionary 
    'The Nile River' : 'Egypt', #defines the key 'Nile River' with a value
    'The Amazon River' : 'South America', #defines the key 'The Amazon River' with a value
    'The Ganges River' : 'India and Bangladesh' #defines the key 'The Ganges River' with a value

}
for key, value in river.items(): #runs through the items in the dictionary and passes the keys and values in the dictionary
    print(f"{key} runs through {value}\n") #prints the river and where it runs through

for key in river.items(): #runs through the items in the dictionary and passes the keys in the dictionary
    print({key}, "\n") #prints the rivers

for value in river.items(): #runs through the items in the dictionary and passes the values in the dicitionary
    print({value}, "\n") #prints the location of the rivers

#Exercise 5

dog = {'Husky' : 'Albert'} #makes a dictionary that consists of the pet and owner
cat = {'Siamese cat' : 'Tony'} #makes a dictionary that consists of the pet and owner
turtle = {'Asian Box turtle' : 'Vince'} #makes a dictionary that consists of the pet and owner

pet = [dog, cat, turtle] #creates a nested dictionary

for rawr in pet: #runs through each dictionary and prints the key and value in each dictionary
    print(rawr, "\n")

