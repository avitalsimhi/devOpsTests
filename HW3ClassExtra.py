# 1
# כן, כיון שאין לו ערך ב- index 5

#2
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    print(colors[i])

#3
# יכול לגרום לשגיאה במידה והקובץ לא קיים

#4
# להוסיף try except מסוג IOerrorוכן הדפסה של השגיאה
# כדי לקבל את פרוט הבעיה בדוח הריצה

#5
import os
my_path = "c:\\users\\simchi\\test"
if not os.path.isdir(my_path):
   os.makedirs(my_path)
my_file = open(my_path+"\\name.txt", "w+")
my_file.write("Avital Simhi")
my_file.close()

#6
from docx import Document
document = Document()
document.save('test.docx')

#Extra:
document.add_paragraph("Avital Simhi")
document.save('test.docx')