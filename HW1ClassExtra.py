from datetime import date, datetime
#1
print("Hello")
print("Avital Simhi")

#2
x = 10
y = 20
print(x+y)

#3
print("My Python version number : 3.8.3")

#4
string = "hello"
st = list()
for i in range(len(string)):
    st.append(string[i])
while len(st) > 0:
    print(st[-1], end="")
    st.pop()
print("")

#5
a = "hello"
print(len(a))

#6
now = datetime.now()
print("now =", now)

#7
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x > y:
    print(x)
elif y > x:
    print(y)

#8
x = 120
if x > 5 and x < 200:
    print("MATCH")
