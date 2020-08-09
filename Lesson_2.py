# import sys
# print("Python version")
# print(sys.version)
#
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
#
#
# from math import pi
# r = float(input("Input the radius of the circle : "))
# print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
#
#
# for x in range(7):
#     print(x)
#
# for x in range(7,10):
#     print(x)
#
# for x in range(7,10,2):
#     print(x)
#
password = '12345'
user_password = input('Please enter password')
while password != user_password:
    user_password = input('Wrong password! Please re-enter password')
else:
    print('Password correct!')

# count =0
# while 1>0:
#     print(x)
#     count =+1
#     if count>=5:
#         break

for x in range(5):
    if x == 3:
        break
    print(x)

for x in range(5):
    if x == 3:
        continue
    print(x)

