#Exercise 1

print("Exercise 1\n") #prints Exercise 1

name = ['Zeke', 'Sameer', 'Elizah', 'Rosver', 'Monyl'] #a list of 5 names

print(name[0]) #prints the first name
print(name[1]) #prints the second name
print(name[2]) #prints the third name
print(name[3]) #prints the fourth name
print(name[4], "\n") #prints the fifth name and creates a new line

#Exercise 2

print("Exercise 2\n") #prints Exercise 2

name = ['Zeke', 'Sameer', 'Elizah', 'Rosver', 'Monyl'] #a list of 5 names

print("I hope you're good,",name[0]) #prints the message with the first name
print("I hope you're good,",name[1]) #prints the message with the second name
print("I hope you're good,",name[2]) #prints the message with the third name
print("I hope you're good,",name[3]) #prints the message with the fourth name
print("I hope you're good,",name[4], "\n") #prints the message with the fifth name and creates a new line

#Exercise 3

print("Exercise 3\n") #prints Exercise 3

transp = ['car', 'tricycle', 'motorcycle'] #list of 3 modes of transportation

print("I would like to own a ", transp[0]) #prints the message with the first mode of transportation
print("I would like to own a ", transp[1]) #prints the message with the second mode of transportation
print("I would like to own a ", transp[2], "\n") #prints the message with the third mode of transportation and creates a new line

#Exercise 4

print("Exercise 4\n") # prints Exercise 4

guest = ['Dahyun', 'Kendrick Lamar', 'KSI'] # list of 3 guests

print("Would you like to go to dinner with me,", guest[0], "?") #prints the invite to the first guest
print("Would you like to go to dinner with me,", guest[1], "?") #prints the invite to the second guest
print("Would you like to go to dinner with me,", guest[2], "?\n") #prints the invite to the third guest and creates a new line

#Exercise 5

print("Exercise 5\n") # prints Exercise 5

guest = ['Dahyun', 'Kendrick Lamar', 'KSI'] #list of 3 guiests

print("Would you like to go to dinner with me,", guest[0], "?") #prints the invite to the first guest
print("Would you like to go to dinner with me,", guest[1], "?") #prints the invite to the second guest
print("Would you like to go to dinner with me,", guest[2], "?\n") #prints the invite to the third guest and creates a new line

print(f"Oh no! {guest[2]} can't come.\n") #prints that the last guest can't come

popped_guests = guest.pop(2) #removes the second guest on the list

new = input("Who would you like to invite?: ") #asks the user to add a new guest

guest.append(new) #adds the guest the user input in the list

print("Would you like to go to dinner with me,", guest[0], "?") #prints the invite to the first guest
print("Would you like to go to dinner with me,", guest[1], "?") #prints the invite to the second guest
print("Would you like to go to dinner with me,", guest[2], "?\n") #prints the invite to the third guest and creates a new line

#Exercise 6

print("Exercise 6\n") #prints Exercise 6

guest = ['Dahyun', 'Kendrick Lamar', 'Sidemen'] #list of 3 guests

print("Oh no! My new dining table won't be able to arrive on time, sorry I can only invite two people!\n") #prints that only 2 guests can come

popped_guest = guest.pop(0) #removes the first guest

print(f"Sorry, {popped_guest}, I can't invite you anymore.\n") #says that the first removed guest cant come

print("You're still invited", guest[0]) #tells the first guest in the list that they can still come
print("You're still invited", guest[1], "\n") #tells the second guest in the list that they can still come

del guest[:] #removes everyone in the list

print(guest, "\n") #prints an empty list

#Exercise 7

print("Exercise 7\n") #prints Exercise 7

place = ['Seoul', 'Switzerland', 'Tokyo', 'Greece', 'Maldives'] #list of 5 places

print(place, "\n") #prints the list

print(sorted(place)) #prints the list in alphabetical order
print(place, "\n") #prints the original list

print(sorted(place, reverse=True)) # prints the list in reverse alphabetical order
print(place, "\n") # prints the original list

place.reverse() #permanently sorts the varibales in reverse alphabetical order
print(place, "\n") # prints the updated list

place.sort() # updates the list to be arranged in alphabetical order
print(place) # prints the updated list

place.sort(reverse=True) # updates the list to be arranged in reverse alphabetical order
print(place, "\n") # prints the updated list






