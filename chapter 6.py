#Exercise 1

print("Exercise 1\n") #prints Exercise 1

while True: #Executes while the statement is true
    
    ingr = input("Enter any ingridient to put on the pizza. Enter 'QUIT' if you want to stop adding toppings: ") #alows the user to input any topping or enter 'quit'
    
    if ingr == 'QUIT': #executes if the user enters 'QUIT'
        print("Enjoy your pizza!") #prints "Enjoy your pizza!"
        break #stops the code
    else: #Execute if the user doesn't enter 'QUIT'
        print(ingr, "has been added to your pizza.") #prints the ingridient the user had inputted in.
        continue #continues with the code until the user enters 'QUIT'  

#Exercise 2

print("\nExercise 2\n") #prints Exercise 2

while True: #Executes while the statement is true
    
    age = int(input("Hi! Welcome to the movie theatre, how old are you?: ")) #using the function int to only allow inputs that contain an integer
    
    if age < 3: #Executes if the user input is less than 3
        print(f"Wow, {age} years old? Here you go! Your ticket is free.") #prints the cost of the ticket
        break #ends the program
    elif age >= 3 and age <= 12: #Executes if the user input is less than or equal to 3 and less than or equal to 12
        print(f"Wow, {age} years old? Here you go! Your ticket costs $10.") #prints the cost of the ticket
        break #ends the program
    else: #Executes if the user input is greater than 12
        print(f"Wow, {age} years old? Here you go! Your ticket costs $15. ") #prints the cost of the ticket
        break #ends the program

"""#Exercise 3

print("\nExercise 3\n") #prints Exercise 3

while True: #Executes the program while it is true
    
    print("To infinity and beyond!") #prints 'To infinity and beyond'"""

#Exercise 4

print("\nExercise 4\n") #prints Exercise 4

sandwhich_orders = ['BLT', 'Egg', 'Club'] #creates a list with 3 sandwhiches
finished_sandwhiches = [] #creates an empty list

while sandwhich_orders: #while 
    
    sandwhich_now = sandwhich_orders.pop() #pops all the elements one by one
    print(f"I am now making your {sandwhich_now} sandwhich.") #prints the popped sandwhich in order
    finished_sandwhiches.append(sandwhich_now) #adds the popped sandwhiches to the empty list

print("\n\n") #prints new lines

for sandwhich in finished_sandwhiches: #runs through the list and selects the elements one by one
    print(f"I made you a {sandwhich} sandwhich") #prints each element one by one
    
#Exercise 5

print("\nExercise 5\n") #prints Exercise 5

sandwich_orders = [ #creates a list with 6 sandwhiches
    'pastrami', 'BLT', 'Egg', 'pastrami',
    'Club', 'pastrami']

finished_sandwiches = [] #creates an empty list

print("I'm sorry, we're all out of pastrami today.") #prints that pastrami is out of stock

while 'pastrami' in sandwich_orders: #checks if 'pastrami' is in the list
    
    sandwich_orders.remove('pastrami') #removes element with the word 'pastrami'

print("\n") #prints a new line

while sandwich_orders: 
    
    sandwich_now = sandwich_orders.pop() #pops all the elements one by one
    print(f"I'm working on your {sandwhich_now} sandwich.") #prints that the popped sandwhiches are being made
    finished_sandwiches.append(sandwich_now) #adds the popped sandwhiches in the empty list

print("\n") #prints a new line

for sandwich in finished_sandwiches: #runs through the list and selects each element
    
    print(f"I made a {sandwich} sandwich.") #prints each element one by one
    
    

    