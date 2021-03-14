#HW q1
n1 = float(input("Enter number:"))
n2 = float(input("Enter number:"))
n3 = float(input("Enter number:"))
print("Your original three numbers were ", n1, n2, n3)
def sum3 ():
    total = n1+n2+n3
    return total
def avg3 ():
    average = (sum3())/3
    return average
print("The sum of your three numbers is: ", sum3())
print("The average of your three numbers is: ", avg3())
print("Your original three numbers were ", n1, n2, n3,". The sum of your three numbers is ", sum3()," and the average is ", avg3(),".")

#HW advanced
numbers = []
l = int(input("How many numbers do you want to enter?"))
total = 0

for x in range(l):
    n = float(input("Enter your number here: "))
    numbers.append(n)

for add in numbers:
    total += add

for mult in numbers:
    avg = total/l

print("Your original numbers are ", numbers,". The sum of your numbers is ", total," and the average is ", avg)
