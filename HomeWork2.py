# A:
y = 30
x = 50

if x > y:
    print("Big")
else:
    print("Small")

#B:
for i in range(5):
    print(i)

#C:
#עשיתי את זה שיעור שעבר לכן החלטתי לעשות בדרך אחרת כפי שלמדנו בשיעור הנוכחי
var = input("Enter number: ")
my_dictionary = {"1":"summer", "2":"winter", "3":"fall", "4":"spring"}
print(my_dictionary[var])

#D
# 1. 10
# 2. 10
count = 1
while count < 11:
    print(count)
    count = count + 1

#E
my_dictionary = {"Your age": 20, "First letter of your last name": "A", "Current shekels-dollar currency": 4.5, "Did you flew abroad": True, "Your apartment number":" 10"}
print(my_dictionary.values())
print(my_dictionary["Your age"] + my_dictionary["Current shekels-dollar currency"])

#F
my_phone = input("Enter your phone number: ")
print("phone number: " + my_phone)

#G
def printHello():
    print("hello")

def calculate():
    x = 5+3.2
    print(x)

#H
def printname(name):
    print(name)

def num(number):
    print(number / 2)

#I
def twonumbers(x, y):
    return x + y

def twostrings(str1, str2):
    print(str1 + " " + str2)

#J
import array as arr
a = arr.array("i",[3, 6, 9])
for x in a:
    print(x)

#K
for i in range(6):
    print("")
    for x in range(i):
        print("*" ,end="")

#L
pattern_size = 7
for t in range(pattern_size):
    pattern = list(" " * pattern_size)
    pattern[t] = "*"
    pattern[-(t+1)] = "*"
    print("".join(pattern))

#M:
def getnumber():
     number = input("Enter number: ")
     return number


def sum_digits():
    n = getnumber()
    sum_of_digits = 0
    for digit in str(n):
        sum_of_digits += int(digit)
    print(sum_of_digits)

if __name__ == '__main__':
    sum_digits()
