# my_file = open("c:\\Python33\\README.txt", 'r')
# contect = my_file.read()
# print(contect)
# my_file.close()
#
# my_file=open("c:\\Python33\\README.txt", 'r+')
# my_file.write("111")
#
# my_file = open("c:\\Python33\\README.txt", 'r')
# my_file.write("aaa")
# my_file.seek(0)
# print(contect)

try:
    my_file = open('1.txt', 'r')
    my_file.write('aaa')
except IOError as e:
    print("IO error...")
    print(e)

print('success')


try:
    f = open("c:\\Python33\\README.txt", 'r')
except IOError:
    print("Fatal Error")
finally:
    ("Error")

