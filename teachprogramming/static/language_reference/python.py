"""
Python  # VER: title
www.python.org  # VER: download
Python 3 or higher  # VER: download
http://docs.python.org/py3k/  # VER: help
"""


def hello_world():
    print("Hello World")  # VER: hello_world


def read_line_from_console():
    username = raw_input()  # VER: read_line_from_console


def comment():
    #This is a comment  # VER: comment
    pass


def define_variables():
    count = 0            # VER: define_variables
    username = "Betty"   # VER: define_variables
    distance = 3.14      # VER: define_variables
    email_errors = True  # VER: define_variables


def define_constats():
    GRAVITY = 9.81  # VER: define_constants


def arithmetic():
    xpos = xpos + 1                  # VER: arithmetic
    distance = 3 / 4                 # VER: arithmetic
    total_cost = item_price * quant  # VER: arithmetic
    remainder = 14 % 11              # VER: arithmetic
    count += 1                       # VER: arithmetic


def if_statement():
    if count >= 5 and username == "Jim":  # VER: if
        print("Yes")                      # VER: if
    elif username == "admin":             # VER: if
        print("Admin")                    # VER: if
    else:                                 # VER: if
        print("No")                       # VER: if


def if_statement_more():
    # Not or # VER: more_if INCOMPLETE
    pass


def for_loop():
    for i in range(0, len(username)):  # VER: for_loop
        print(username[i])             # VER: for_loop


def while_loop():
    count = 0                         # VER: while_loop
    while count < 10:                 # VER: while_loop
        print("Count is %s") % count  # VER: while_loop
        count = count + 2             # VER: while_loop


def for_each_loop():
    names = ("Bob", "Ben", "Bill", "Borris", "Bin")  # VER: for_each_loop
    for name in names:                               # VER: for_each_loop
        print name                                   # VER: for_each_loop


def file_write():
    line_to_write = "Append to end of file"     # VER: file_write
    with open("out.txt", 'a') as file:          # VER: file_write
        file.write(line_to_write + "\n")        # VER: file_write
                                                # VER: file_write
    # Alternate way of writing file             # VER: file_write
    file = open("out.txt", 'a')                 # VER: file_write
    file.write(line_to_write + "\n")            # VER: file_write
    file.close()                                # VER: file_write


def file_read():
    line_count = 0                                          # VER: file_read
    with open("in.txt", 'r') as file:                       # VER: file_read
        for line in file:                                   # VER: file_read
            print("Line " + str(line_count) + ": " + line)  # VER: file_read
            line_count += 1                                 # VER: file_read
                                                            # VER: file_read
    # Alternate way of reading file                         # VER: file_read
    file = open("in.txt", 'r')                              # VER: file_read
    for line in file:                                       # VER: file_read
        print("Line " + str(line_count) + ": " + line)      # VER: file_read
        line_count += 1                                     # VER: file_read
    file.close()                                            # VER: file_read


def string_concatination():
    fullname = forename + " " + surname                     # VER: string_concatination
    fullname = "%s %s" % (forename, surname)  # Alternate   # VER: string_concatination


def conert_string_to_interger_and_back():
    sum = int("5") + int(input())           # VER: conert_string_to_interger_and_back
    print(str(sum))                         # VER: conert_string_to_interger_and_back
    #Python has a cool string formatter     # VER: conert_string_to_interger_and_back
    print("The number is %s then %s" % sum, 27)  # VER: conert_string_to_interger_and_back


def function():
    def say_hello():        # VER: function
        print("Hello")      # VER: function
        print("Goodbye")    # VER: function


def function_with_return_value():
    def biggest(a, b):  # VER: function_with_return_value
        if a > b:       # VER: function_with_return_value
            return a    # VER: function_with_return_value
        else:           # VER: function_with_return_value
            return b    # VER: function_with_return_value

#Everything is a reference

names = []
names.insert(0,"Bob")
names.insert(1,"Foo")
names.insert(2,"Rah")
for name in names:
  print(name)
print ("array size is %s" % len(names))
grid = {}  #Not really a 2D array (it's a hash)
for x in range(10): #Fill the grid with 0's
  for y in range(10):
    grid[(x,y)] = 0
grid[(5,5)] = 1
list = []
list.append("Bill")
list.append("Ben")
list.append("Bob")
list.remove("Ben")
list.pop()
list.insert(0,"Kim")
for name in list:
  print(name)
print("list size is %s" % len(list))
dict = {}
dict["Joe"] = 77
dict["Jane"] = 51
for key in dict.keys():
  print("Key: %s Value: %s" % (key,dict[key]))

#todo add contains
try:
  #thing that may error
except:
  #what to do if things go wrong
csv_line_test = "Jane,09/09/1989,Female,Blue"
line_split = csv_line_test.split(",")
import random

new_num = random.randint(0, 100)
new_fraction = random.random()
todo
class Star:
  x = 0
  y = 0
  speed = 0
...
s = Star()
s.x = 100
from datetime import date

class Student:
  forename = ""
  surname  = ""
  dob      = date.today()

students = []
filename = "c:\\test.csv"

with open(filename, 'r') as file:
  for line in file:
    line_split = line.split(",")
    new_student = Student()
    new_student.forname = line_split[0]
    new_student.surname = line_split[1]
    new_student.date    = line_split[2] #rrr
    students.append(new_student)
print("Loaded %s students" % len(students))
from time import sleep
sleep(1)
