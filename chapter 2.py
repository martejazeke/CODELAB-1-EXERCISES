# Exercise 1

print("Exercise 1\n") #prints Exercise 1

hello = ("Hi, how are you") #places "Hi, how are you" in the variable hello

print(hello) #prints "Hi, how are you"

hello = ("I'm good, yes.") #replaces the string earlier with "I'm good, yes."
print(hello,"\n") #prints "I'm good, yes."

#Exercise 2

print("Exercise 2\n") #prints "Exercise 2"

author = ("Albert Einstein") #places "Albert Einstein" in the variable author
quote = ("“Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid.”") #places the quote string in the variable quote

print(author, "once said", quote,"\n") #prints the string "Albert Einstein once said “Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid.”"

#Exercise 3

print("Exercise 3\n") #prints Exercise 3 

name = ("\tZeke\n") #places "Zeke" in the variable name and adds a tab space and a new line in the string

print(name) #default

print(name.lstrip()) #removes the whitespaces in the beginning of the string
print(name.rstrip()) #removes the spaces only from the right side of the string
print(name.strip(), "\n") #removes the trailing or leading spaces

#Exercise 4

print("Exercise 4\n") #prints "Exercise 4"

num = 26 #places the number in the variable 26

print("Zeke's favorite number is", num, "\n") #prints "Zeke's favorite number is 26, and creates a new line after the string."

#Exercise 5

print("Exercise 5\n") #prints Exercise 5

balance = 50 #the balance of the girl
usb = 6 #cost of one usb stick

total = balance//usb #to know how many USB sticks the girl can buy
how = total*usb #the total cost of all the USBs
change = balance - how #to know the change the girl will get

print("The girl can buy", total, "USB sticks and she will have", change, "as change.\n") #prints the total amount of USBs the girl can get and the change the girl will get.

