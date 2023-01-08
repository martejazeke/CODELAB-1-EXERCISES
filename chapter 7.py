#Exercise 1

print("\nExercise 1\n") #prints Exercise 1

def display_message(): #defines the function
    
    msg = "Im learning how to use the define function." #places the message in a variable
    
    print(msg) #prints the message
    
display_message() #calls the function

#Exercise 2 

print("\nExercise 2\n") #prints Exercise 2

def favorite_book(title): #defines the function with a parameter 'title'
    
    print(f"{title} is one of my favorite books.") #prints the parameter in a sentence.
    
favorite_book('Romeo and Juliet') #calls the function with an argument

#Exercise 3 

print("\nExercise 3\n") #prints Exercise 3

def make_shirt(size, message): #defines the function with 2 parameter
    
    print(f"I am going to make a {size} t-shirt") #states the size of the shirt being made
    print(f"It will say {message}\n") #states what the shirt will say
    
make_shirt('Large', 'I love python') #calls the function and uses positional arguments
make_shirt(size = 'Medium', message = 'I love python') #calls the function and uses keyword arguments

#Exercise 4 

print("\nExercise 4\n") #prints Exercise 4

def make_shirt(size = 'Large', message = 'I love Python'): #makes a function with default values
    
    print(f"I am going to make a {size} shirt.") #states that it will make a large shirt
    print(f"It will say {message}.\n") #states that the shirt will say I love Python
    
make_shirt() #calls teh function as is
make_shirt(size = 'medium') #calls the function and replaces the value for the argument 'size' with the use of keyword arguments
make_shirt('Extra Large', 'It must be nice') #calls the function and uses positional arguments

#Exercise 5

print("\nExercise 5\n") #prints Exercise 5

def describe_city(city, country = 'United Arab Emirates'): #makes a function and has one parameter and another parameter with a default value
    
    print(f"{city.title()} is located in {country.title()}.\n") #prints the city and the country with proper capitalization
    
describe_city('abu dhabi') #calls the function and adds a value using positional arguments
describe_city(city = 'Manila', country = 'philippines') #calls the function and replaces the values using keyword arguments
describe_city('dubai') #calls the function and adds the value using positional arguments