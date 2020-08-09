#1, 2
try:
    a = 1/0
except:
    print("Error")

#3
# yes

#4
#All exepation

#5
#because this exepation will bring partial information

#6
# IOError - handler input/output errors
# ZeroDivisionError - handler division by zero

#7 + 8
my_file = open('C:\\Users\\simchi\\words.txt', 'w+')
my_file.write("Avital Simhi")
my_file.close()

# 9
my_file1 = open('C:\\Users\\simchi\\words.txt')
contect = my_file1.read()
print(contect)
my_file1.close()


# 10
my_file2 = open('C:\\Users\\simchi\\hebrew.txt', 'w+')
my_file2.write("אביטל שמחי")
my_file2.close()
my_file2 = open('C:\\Users\\simchi\\hebrew.txt')
contect = my_file2.read()
print(contect)
my_file2.close()

#11
from PIL import Image
img = Image.new('RGB', (60, 30), color='red')
img.save('c:\\Users\\simchi\\image.png')
