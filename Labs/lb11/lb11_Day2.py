#day 2 python

num = int(input("Input a number:"))
if num > 5:
     print("Greater than 5!")
else:
    print("End")

#conditionals & flow charts
#if and else should be in the same line
num = int(input("Input a number"))
if num >= 5:
     print("Greater than or equal to 5!")
else:
    print("This number is less than 5")

num = int(input("Input your age: "))
if num >= 21:
     print("Congrats! You can drive, vote, and drink!")
elif num >= 18:
    print("You can drive and vote, but no drinking!")
elif num >= 16:
    print("Awesome! You can drive, but no drinking or voting")
else:
    print("Sorry. You cannot drive, vote, or drink yet.")

age = int(input("what is your age?"))
if 0 < age < 16:
    print("You are too young to drive.")
#checkin
#Version 1
order = input("Did you order food?")
if order == "yes":
    print("Great!")
else:
    print("NO?! So who is cooking?")
#Version 2
order = input("Did you order food?")
if order == "yes" or order == "Yes" or order == "YES":
    q1 = int(input("What is the cost of the food order?"))
    q2 = int(input("How many people are splitting the order?"))
    print("The cost per person is ",q1/q2)
else:
    print("NO?! So who is cooking?")

#dice roll game
import random

rolls = int(input("How many rolls do you want to play?"))
points = 0

for i in range(rolls):
    x = random.randint(1,6)
    guess = int(input("Take a guess 1-6:"))
    if guess == x:
        print("Your guess was", guess)
        print("The correct roll was", x)
        print("You earned 6 points")
        points += 6
    else:
        print("Your guess was", guess)
        print("The correct roll was", x)
        print("You lost 1 point")
        points -= 1

print("Final score =", points)

#count
count = 0
while count < 5:
    print("hi!")
    count += 1
print("Good bye!")

# version 1
pw = 'simonsnyc'
userPw = input("Please input your password: ")

while userPw != pw:
    print("Wrong password. Try again.")
    userPw = input("Please input your password: ")
print("Correct. You may enter...")'''

# version 2
pw = 'simonsnyc'
userPw = input("Please input your password: ")
guess = 1
while guess<3 and userPw != pw:
    print("Wrong password. Try again.")
    userPw = input("Please input your password: ")
    guess += 1
    if guess==3:
        print("No more chances.")
    elif pw==userPw:
        print("Correct. You may enter...")

# version 3
pw = 'simonsnyc'
userPw = input("Please input your password: ")

guess = 1

while guess < 3 and userPw.lower() != pw:
    print("Wrong password. Try again.")
    userPw = input("Please input your password: ")
    guess += 1

if userPw.lower() == pw:
    print("Correct. You may enter...")
else:
    print("Too many tries. Try again later.")

#professors answers
#Version 1
PW = "simonsnyc"
guess = input("What's the Password? ")

while guess != PW:
  print ("Wrong!, Guess Again!")
  guess = input("What's the Password? ")
print ("Correct! You may enter...")


#Version 2 - stops after 3 times
PW = "simonsnyc"
guess = input("What's the Password? ")
num_guesses = 0
while guess != PW and num_guesses < 2:
  print ("Wrong!, Guess Again!")
  num_guesses = num_guesses + 1
  guess = input("What's the Password? ")

if guess == PW:
  print ("Correct! You may enter...")
else:
  print ("Sorry, you're locked out!")

#Version 3 - isn't case sensitive
PW = "simonsnyc"
guess = input("What's the Password? ")
num_guesses = 0
while guess.lower() != PW.lower() and num_guesses < 2:
  print ("Wrong!, Guess Again!")
  num_guesses = num_guesses + 1
  guess = input("What's the Password? ")

if guess.lower() == PW.lower():
  print ("Correct! You may enter...")
else:
  print ("Sorry, you're locked out!")

#list
fruits=["apple","strawberries","blackberries"]
print(fruits)
# will print out:
#['apple', 'strawberries', 'blackberries']
#[0,1,2]
fruits=["apple","strawberries","blackberries"]
print(fruits[0:2])
# will print ['apple', 'strawberries'] because 0:2 is up to 2 - not including 2
#lists
list = [1,2,4,8]
list.append(16)
list.insert(0,0.25)
list.remove(2)
list.remove(8)
print(list)
#Output [0.25, 1, 4, 16]

sum = 0
for x in [1.95,4.50,0.99,5.99]:
    sum += x
print(sum)

#check in for lists
prices = []
names = []
quantity = []
q1 = int(input("how many prices do you want to add?"))
sum = 0

for x in range(q1):
    n = input("Enter name: ")
    p = float(input("Enter price: "))
    q = float(input("Enter quantity: "))
    prices.append(p)
    names.append(n)
    quantity.append(q)
    sum += p*q
print("Prices:", prices)
print("Names: ", names)
print("Quantity: ", quantity)
print("Total Price =",sum)
#output ex:
Prices: [3.0, 4.0]
Names:  ['apple', 'orange']
Quantity:  [7.0, 2.0]
Total Price = 29.0
#functions
def happybday(name):
    print("Happy Birthday "+name+"!!!")
happybday("Cersei")
happybday("Jamie")
#function - have the user input their name
def happybday(name):
    print("Happy Birthday "+name+"!!!")
name = input("What is your name?")
happybday(name)
#functions with multiple inputs
def find_rect_area(w,l):
    area = w*l
    (print("Calculating Area..."))
    return area

answer = find_rect_area(4,7)
print(answer)
#overview of function syntax
def mult_function(x,y):
    z = x *y
    print("I heart math")
    return z - return value

mult_function(5,4)

#check in done by me:
n1 = float(input("Enter number:"))
n2 = float(input("Enter number:"))
n3 = float(input("Enter number:"))

def sum (x,y,z):
    w=x+y+z
    print("The sum of your three numbers is: ",w)
    return w
sum(n1,n2,n3)

def avg (x,y,z):
    a=(x+y+z)/3
    print("The average of your three numbers is: ",a)
    return a
avg(n1,n2,n3)

#HW q1
n1 = float(input("Enter number:"))
n2 = float(input("Enter number:"))
n3 = float(input("Enter number:"))
print("Your original three numbers were ", n1, n2, n3)
def sum (x,y,z):
    w = x+y+z
    return w
w = sum(n1,n2,n3)

def avg (x,y,z):
    a = (x+y+z)/3
    return a

a = avg(n1,n2,n3)
print("The sum of your numbers is ", w," and the average is ", a,".")

#HW advanced
numbers = []
l = int(input("How many numbers do you have?"))
total = 0

for x in range(l):
    n = float(input("Enter your number here: "))
    numbers.append(n)
print("Your original three numbers were ", numbers)

for add in numbers:
    total += add
print("The sum of your list is: ",total)

for mult in numbers:
    avg = total/l
print("The average of your list is: ", avg)
