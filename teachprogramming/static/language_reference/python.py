"""
Python  # VER: title
www.python.org  # VER: download
Python 3 or higher  # VER: download
http://docs.python.org/py3k/  # VER: help
"""


def hello_world():
    print("Hello World")  # VER: hello_world


def read_line_from_console():
    input = lambda: None
    username = input()  # VER: read_line_from_console


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
    xpos = 0
    item_price = 0
    quant = 0
    count = 0

    xpos = xpos + 1                  # VER: arithmetic
    distance = 3 / 4                 # VER: arithmetic
    total_cost = item_price * quant  # VER: arithmetic
    remainder = 14 % 11              # VER: arithmetic
    count += 1                       # VER: arithmetic


def if_statement():
    username = 'bob'
    count = 3

    if count >= 5 and username == "Jim":  # VER: if_statement
        print("Yes")                      # VER: if_statement
    elif username == "admin":             # VER: if_statement
        print("Admin")                    # VER: if_statement
    else:                                 # VER: if_statement
        print("No")                       # VER: if_statement


def if_statement_more():
    # Not or # VER: more_if INCOMPLETE
    pass


def for_loop():
    username = 'bob'                    # VER: for_loop
    for i in range(0, len(username)):   # VER: for_loop
        print(username[i])              # VER: for_loop


def while_loop():
    count = 0                         # VER: while_loop
    while count < 10:                 # VER: while_loop
        print("Count is {0}".format(count))  # VER: while_loop
        count = count + 2             # VER: while_loop


def until_loop():
    """
    Not implemented in python
    """
    pass


def for_each_loop():
    names = ("Bob", "Ben", "Bill", "Borris", "Bin")  # VER: for_each_loop
    for name in names:                               # VER: for_each_loop
        print(name)                                  # VER: for_each_loop


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
    #file = open("in.txt", 'r')                              # VER: file_read
    #for line in file:                                       # VER: file_read
    #    print("Line " + str(line_count) + ": " + line)      # VER: file_read
    #    line_count += 1                                     # VER: file_read
    #file.close()                                            # VER: file_read


def string_concatination():
    forename = 'bob'
    surname = 'jones'
    fullname = forename + " " + surname                     # VER: string_concatination
    fullname = "%s %s" % (forename, surname)  # Alternate   # VER: string_concatination
    print(fullname)


def convert_string_to_interger_and_back():
    sum = 5 + int('5')                      # VER: conert_string_to_interger_and_back
    print(str(sum))                         # VER: conert_string_to_interger_and_back


def convert_double_to_string_and_back():
    pass


def _function():
    def say_hello():        # VER: function
        print("Hello")      # VER: function
        print("Goodbye")    # VER: function
    say_hello()             # VER: function


def function_with_return_value():
    def biggest(a, b):      # VER: function_with_return_value
        if a > b:           # VER: function_with_return_value
            return a        # VER: function_with_return_value
        else:               # VER: function_with_return_value
            return b        # VER: function_with_return_value
    print(biggest(1, 2))    # VER: function_with_return_value


def define_fixed_array():
    names = []              # VER: define_fixed_array
    names.insert(0, "Bob")  # VER: define_fixed_array
    names.insert(1, "Foo")  # VER: define_fixed_array
    names.insert(2, "Rah")  # VER: define_fixed_array
    for name in names:      # VER: define_fixed_array
        print(name)         # VER: define_fixed_array
    print("array size is %s" % len(names))  # VER: define_fixed_array


def define_2d_arrays():
    grid = {}  # Not really a 2D array (it's a dictioary)   # VER: define_2d_arrays
    for x in range(10):  # Fill the grid with 0's           # VER: define_2d_arrays
        for y in range(10):                                 # VER: define_2d_arrays
            grid[(x, y)] = 0                                # VER: define_2d_arrays
    grid[(5, 5)] = 1                                        # VER: define_2d_arrays


def linked_list():
    list = []               # VER: linked_list
    list.append("Bill")     # VER: linked_list
    list.append("Ben")      # VER: linked_list
    list.append("Bob")      # VER: linked_list
    list.remove("Ben")      # VER: linked_list
    list.pop()              # VER: linked_list
    list.insert(0, "Kim")   # VER: linked_list
    for name in list:       # VER: linked_list
        print(name)         # VER: linked_list
    print("list size is %s" % len(list))    # VER: linked_list


def define_map():
    dict = {}                                           # VER: define_map
    dict["Joe"] = 77                                    # VER: define_map
    dict["Jane"] = 51                                   # VER: define_map
    for key in dict.keys():                             # VER: define_map
        print("Key: %s Value: %s" % (key, dict[key]))   # VER: define_map
    #todo add contains


def error_handling():
    try:                                # VER: error_handling
        #thing that may error           # VER: error_handling
        pass
    except:                             # VER: error_handling
        #what to do if things go wrong  # VER: error_handling
        pass


def split_strings():
    csv_line_test = "Jane,09/09/1989,Female,Blue"   # VER: split_strings
    line_split = csv_line_test.split(",")           # VER: split_strings
    print(line_split[1])


def random_number():
    import random                       # VER: random_number
    new_num = random.randint(0, 100)    # VER: random_number
    new_fraction = random.random()      # VER: random_number


def switch():
    #todo
    pass


def _class():
    class Star:     # VER: class
        x = 0       # VER: class
        y = 0       # VER: class
        speed = 0   # VER: class
    #...            # VER: class
    s = Star()      # VER: class
    s.x = 100       # VER: class
    print(s.x)


def read_csv_into_array_of_classs():
    from datetime import date                       # VER: read_csv
                                                    # VER: read_csv
    class Student:                                  # VER: read_csv
        forename = ""                               # VER: read_csv
        surname  = ""                               # VER: read_csv
        dob      = date.today()                     # VER: read_csv
                                                    # VER: read_csv
    students = []                                   # VER: read_csv
    filename = "test.csv"                           # VER: read_csv
                                                    # VER: read_csv
    with open(filename, 'r') as file:               # VER: read_csv
        for line in file:                           # VER: read_csv
            line_split = line.split(",")            # VER: read_csv
            new_student = Student()                 # VER: read_csv
            new_student.forname = line_split[0]     # VER: read_csv
            new_student.surname = line_split[1]     # VER: read_csv
            new_student.date    = line_split[2] #better way needed  # VER: read_csv
            students.append(new_student)            # VER: read_csv
    print("Loaded %s students" % len(students))     # VER: read_csv


def sleep():
    from time import sleep  # VER: sleep
    sleep(1)                # VER: sleep


#-------------------------------------------------------------------------------

if __name__ == "__main__":
    # Aquire functions to run from file
    functions = []
    with open('_function_order.txt', 'r') as file:
        for function_name in file:
            functions.append(function_name.strip())

    def title(title):
        print('-{0}-'.format(title))

    # Run all functions in order
    for function_name in functions:
        title(function_name)
        if function_name not in locals():
            print('UNIMPLEMENTED')
            continue
        locals()[function_name]()

    # Print output of written files
    #for filename in ('out.txt',):
    #    title(filename)
    #    with open(filename, 'r') as f:
    #        print(f.read())
