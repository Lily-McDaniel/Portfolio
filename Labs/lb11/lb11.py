age = 23
name = "Lily McDaniel"
print(name)

name = input("What's your name?")
print("Hi " + name)

first_name = input("What's your first name?")
last_name = input("What's your last name?")
full_name = first_name+" "+last_name
print("Good evening " +full_name)

first_name = input("What's your first name?")
last_name = input("What's your last name?")
full_name = first_name+" "+last_name
print("Good evening " +full_name)
fav_color = input("What's your favorite color?")
college = input("Which college do you attend?")
location = input("Where do you live?")
print("I love "+fav_color+" too!")
print("I bet "+college+" is awesome.")
print("Jealous. I love "+location+".")

first_name = input("What's your first name?")
last_name = input("What's your last name?")
full_name = first_name+" "+last_name
age = input("How old are you?")
dancing = input("How long have you been dancing?")
print("Hey, "+full_name+"! "+age+" is a great age."+" "+"I love to dance too. It's amazing that you've been at it for "+dancing+ " years now. Keep up the good work!")


'''
This program calculates the perimeter of a rectangle using input from the user.
'''

#Getting the length from the user
length = int(input("What is the length of the rectangle?"))
width = int(input("What is the width of the rectangle?"))

perimeter = 2 * (length + width)

print("The perimeter is " + str(perimeter))

#how to do math problems with variables
#int() around equation makes the answer an int without decimals
import math

r = int(input ("What is the radius of your circle?"))
h = int(input ("What is the height of your circle?"))
V = int(math.pi*(r**2)*h)
print("The volume of this cylinder is " + str(V));

#loops
x = 10
for i in range(4):
    x = x + 1
    print(x)

for dog in range(3):
    print("hi!")

#start inclusive, end exclusive
#0 1 2 3 4
for x in range(0,5):
    print(x)
#30 27 24 21 15 12
for x in range(30,12,-3)
    print(x)
