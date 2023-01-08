#Exercise 1 

print("Exercise 1\n")

song = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!" #stores the string in the variable

print(song) #prints the string

#Exercise 2

print("Exercise 2\n")

import sys

print("The version of python you're using is", sys.version)

print("Here is the version's info: ", sys.version_info, "\n")

#Exercise 3

print("Exercise 3\n")

import datetime

now = datetime.datetime.now()

print("The date today is", now.strftime("%m-%d-%Y"), "and the time is now ", now.strftime("%H: %M: %S\n")) 

#Exercise 4 

print("Exercise 4\n")

hi = "Hello"
no = "Hell no"
yes = "Yesser!"

print(hi, no, yes, "\n")

#Exercise 5

print("Exercise 5\n")

rad = int(input("Enter the radius of your circle: "))

area = 3.14159*(rad**2)

print("The area of the circle is", area)
