#1
for t in range(10):
    print(t + 1)

number = 1
while number < 11:
    print(number)
    number = number + 1

#2
x = int(input("Enter number: "))
if x > 0:
    print("+")
else:
    print("-")

#3
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x > y:
    print(x)
else:
    print(y)

#4
x = int(input("Enter your age: "))
y = int(input("Enter your height: "))
if x > 10 and y > 120:
    print("Welcome to the rollercoaster")
else:
    print("Sorry.. maybe next time")

#5
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x == y:
    print("equal")
else:
    print("not equal")

#6
#אולי להיכנס ללואה אין סופית

#7
def get_name(name):
   return "Your name " + name

def name():
    print(my_name=get_name("Avital"))

#8
x = int(input("Enter number: "))
if x>100:
    print("true")
else:
    print("false")