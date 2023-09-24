"""
python3  # VER: title
www.python.org  # VER: download
Python 3 or higher  # VER: download
http://docs.python.org/3/  # VER: help

python my_file.py  # VER: run
"""


def hello_world():
  print("Hello World")  # VER: hello_world


def read_line_from_console():
  input = lambda: 'bob'
  username = input()  # VER: read_line_from_console
  print(username)


def comment():
  ##This is a comment  # VER: comment
  pass


def define_variables():
  count = 0            # VER: define_variables
  username = "Betty"   # VER: define_variables
  distance = 3.14      # VER: define_variables
  email_errors = True  # VER: define_variables
  multiline = """a b"""    # VER: define_variables


def define_constants():
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

  print(xpos)
  print(distance)
  print(total_cost)
  print(remainder)
  print(count)


def if_statement():
  username = 'bob'
  count = 3

  if count >= 5 and username == "Jim":  # VER: if_statement
    print("Yes")                      # VER: if_statement
  elif username == "admin" or username == "Bob":  # VER: if_statement
    print("Admin")                    # VER: if_statement
  else:                                 # VER: if_statement
    print("No")                       # VER: if_statement


def if_statement_more():
  # Not or # VER: more_if INCOMPLETE
  pass


def for_loop():
  data = [5,6,7]                                                                # VER: for_loop
  for i in range(len(data)):                                                    # VER: for_loop
    print(data[i])                                                              # VER: for_loop

def while_loop():
  count = 0                         # VER: while_loop
  while count < 10:                 # VER: while_loop
    print(f"Count is {count}")  # VER: while_loop
    count = count + 2             # VER: while_loop

# TODO: break and return in loop

def until_loop():
  """
  Not implemented in python
  """
  pass


def for_each_loop():
  ff = ["a", "b", "c"]  # VER: for_each_loop
  for f in ff:              # VER: for_each_loop
    print(f)               # VER: for_each_loop


def file_write():
  line_to_write = "Append to end of file"     # VER: file_write
  with open("out.txt", 'a') as file:          # VER: file_write
    file.write(line_to_write + "\n")        # VER: file_write
                        # VER: file_write
  ## Alternate way of writing file             # VER: file_write
  file = open("out.txt", 'a')                 # VER: file_write
  file.write(line_to_write + "\n")            # VER: file_write
  file.close()                                # VER: file_write


def file_read():
  line_count = 0                                          # VER: file_read
  with open("in.txt", 'r') as file:                       # VER: file_read
    for line in file:                                   # VER: file_read
      print(f"Line {line_count} : {line}")             # VER: file_read
      line_count += 1                                 # VER: file_read
                              # VER: file_read
  ## Alternate way of reading file                         # VER: file_read
  #file = open("in.txt", 'r')                              # VER: file_read
  #for line in file:                                       # VER: file_read
  #    print(f"Line {line_count}: {line}")                 # VER: file_read
  #    line_count += 1                                     # VER: file_read
  #file.close()                                            # VER: file_read


def string_concatenation():
  forename = 'bob'
  surname = 'jones'
  fullname2 = f'{forename} {surname}'                      # VER: string_concatenation
  fullname = forename + " " + surname                     # VER: string_concatenation
  fullname3 = "%s %s" % (forename, surname)                 # VER: string_concatenation
  fullname4 = "{} {}".format(forename, surname)                 # VER: string_concatenation
  print(fullname)

def split_strings():
  pass ## TODO # VER: split_strings

def convert_string_to_integer_and_back():
  sum = 5 + int('5')                      # VER: convert_string_to_integer_and_back
  print(str(sum))                         # VER: convert_string_to_integer_and_back


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
  aa = [None,] * 3              # VER: define_fixed_array
  aa[1] = "test"   # VER: define_fixed_array
  print(aa)  # VER: define_fixed_array
  print(aa[1])   # VER: define_fixed_array
      # VER: define_fixed_array
  bb = ["a", "b", "c"]   # VER: define_fixed_array
  print(f"bb size is {len(bb)}")  # VER: define_fixed_array
  for i in bb:      # VER: define_fixed_array
    print(i)         # VER: define_fixed_array
  if "a" in bb:    # VER: define_fixed_array
    print("a exists in array")   # VER: define_fixed_array

def define_list():
  cc = ["a", "b", "c"]        # VER: define_list
  print(cc[0])                # VER: define_list
  last = cc.pop()             # VER: define_list
  cc.append("d")              # VER: define_list
  first = cc.pop(0)           # VER: define_list
  cc.insert(0, "z")           # VER: define_list
  cc.remove("b")              # VER: define_list
  for i in cc:                # VER: define_list
    print(i)  # z d           # VER: define_list
  if "z" in cc:               # VER: define_list
    print("z exists in list") # VER: define_list
  # TODO: concat list


def define_2d_arrays():
  width = 3
  height = 3
  value = 1
           
  grid1 = [[value,] * width for y in range(height)]   # VER: define_2d_arrays_with_nested_arrays
  grid1[2][1] = 5   # VER: define_2d_arrays_with_nested_arrays
  print(grid1[0][0])   # VER: define_2d_arrays_with_nested_arrays

  from typing import NamedTuple
  class Dimension(NamedTuple):
    width: int
    height: int
    @property
    def size(self):
      return self.width * self.height
    def coord_to_index(self, x, y):
      return (y * self.width) + (x % self.width)
    def index_to_cord(self, i):
      return (i % self.width, i//self.width)

  grid2 = [value,] * (width * height)   # VER: define_2d_arrays_with_1d_array_with_lookup_function
  def coord_to_index(x, y):   # VER: define_2d_arrays_with_1d_array_with_lookup_function
    return (y * width) + (x % width)   # VER: define_2d_arrays_with_1d_array_with_lookup_function
  grid2[coord_to_index(2, 1)] = 5   # VER: define_2d_arrays_with_1d_array_with_lookup_function
  print(grid2[coord_to_index(0, 0)])   # VER: define_2d_arrays_with_1d_array_with_lookup_function
  def index_to_cord(i):   # VER: define_2d_arrays_with_1d_array_with_lookup_function
    return (i % width, i//width)   # VER: define_2d_arrays_with_1d_array_with_lookup_function

  grid3 = {       # VER: define_2d_arrays_with_dictionary
    (x, y): value           # VER: define_2d_arrays_with_dictionary
    for x in range(width)  # VER: define_2d_arrays_with_dictionary
    for y in range(height)  # VER: define_2d_arrays_with_dictionary
  }   # VER: define_2d_arrays_with_dictionary
  grid3[(2, 1)] = 5   # VER: define_2d_arrays_with_dictionary
  print(grid3[(0, 0)])   # VER: define_2d_arrays_with_dictionary



def define_map():
  data = { # VER: define_map
    "a": 1,                                                            # VER: define_map
    "b": 2,                                                            # VER: define_map
  }  # VER: define_map
  print(data["b"])  # prints 2   # VER: define_map
  data["c"] = 3  # VER: define_map
  del data["a"]  # VER: define_map
  for k, v in  data.items():  # VER: define_map
    print(f"Key: {k}, Value: {v}")  #  VER: define_map
  if "d" in data:  # VER: define_map
    pass  # VER: define_map


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
  csv_line_test2 = " : ".join(line_split)         # VER: split_strings
  print(csv_line_test2)

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
      new_student.date    = line_split[2] #better?  # VER: read_csv
      students.append(new_student)            # VER: read_csv
  print(f"Loaded {len(students)} students")     # VER: read_csv


def sleep():
  from time import sleep  # VER: sleep
  sleep(1)                # VER: sleep
  print("slept for a second")

#-------------------------------------------------------------------------------

# Unsorted

def list_comprehension():
  data1 = [1,2,3,4,5,6]   # VER: list_comprehension
  data2 = [               # VER: list_comprehension
    i * 2               # VER: list_comprehension
    for i in data1      # VER: list_comprehension
    if i >= 3           # VER: list_comprehension
  ]                       # VER: list_comprehension

def dict_comprehension():
  data3 = {              # VER: dict_comprehension
    'a': 1,            # VER: dict_comprehension
    'b': 2,            # VER: dict_comprehension
    'c': 3,            # VER: dict_comprehension
  }                      # VER: dict_comprehension
  data4 = {              # VER: dict_comprehension
    v + 10: k         # VER: dict_comprehension
    for k, v in data3.items()  # VER: dict_comprehension
    if v >= 2             # VER: dict_comprehension
  }                     # VER: dict_comprehension

def function_with_param_function():
  def my_func_1(a, b):  # VER: function_with_param_function
    return a + b  # VER: function_with_param_function
  my_func_2 = lambda a, b: a * b # VER: function_with_param_function
  def print_my_func(ff):  # VER: function_with_param_function
    print(ff(2,3))  # VER: function_with_param_function
  print_my_func(my_func_1) # VER: function_with_param_function
  print_my_func(my_func_2) # VER: function_with_param_function


def define_set():
  aa = {1,2,3}    # VER: define_set
  bb = {2,3,4}    # VER: define_set
  cc = {1,2}      # VER: define_set
  print(aa | bb)  # VER: define_set
  print(aa & bb)  # VER: define_set
  print(aa - cc)  # VER: define_set
  print(cc in aa) # VER: define_set
  aa.add(5)       # VER: define_set
  

def json_data():
  data = [                                     # VER: json_data
    {'a': 1, 'b': 2},                          # VER: json_data
    {'c': 3, 'd': 4},                          # VER: json_data
    {'e': [5,6,7], 'f': {'g': 10, 'h': "something"}}   # VER: json_data
  ]         # VER: json_data
  import json    # VER: json_data
  string_data = json.dumps(data)          # VER: json_data
  print(string_data)              # VER: json_data
  # '[{"a": 1, "b": 2}, {"c": 3, "d": 4}, {"e": [5, 6, 7], "f": {"g": 10, "h": "something"}}]'
  data2 = json.loads(string_data)         # VER: json_data


def nested_data():
  ## TODO: nested datastructures - towards json?  # VER: nested_data
  pass    

def commandline_args():
  pass  # TODO     # VER: commandline_args


def network_tcp_send():
  pass  # TODO    # ver: network_tcp_send
def network_tcp_recv():
  pass  # TODO    # ver: network_tcp_recv
def network_udp_send():
  pass  # TODO    # ver: network_upd_send
def network_udp_recv():
  pass  # TODO    # ver: network_udp_recv

import urllib.request                                 # ver: http_request
def urllib_request(*args, **kwargs):                  # ver: http_request
    request = urllib.request.Request(*args, **kwargs) # ver: http_request
    with urllib.request.urlopen(request) as response: # ver: http_request
        return response.read()                        # ver: http_request
      
def http_request():
  pass

def http_request_json():
  import json                                           # ver: http_request_json
  def fetch_json(url, data={}, method='GET'):           # ver: http_request_json
      return json.loads(urllib_request(                 # ver: http_request_json
        url,                                            # ver: http_request_json
        json.dumps(data).encode('utf8'),                # ver: http_request_json
        method=method,                                  # ver: http_request_json
        headers={"Content-type": "application/json"}    # ver: http_request_json
      ))                                                # ver: http_request_json
                                                        # ver: http_request_json
  from pprint import pprint                             # ver: http_request_json
  pprint(fetch_json('https://jsonplaceholder.typicode.com/posts/1', method="GET"))  # ver: http_request_json
  #pprint(fetch_json('http://localhost:8000/item', {"user_id": "user1234", "keywords": ["hammer", "nails", "tools"], "description": "A hammer and nails set. In canterbury", "lat": 51.2798438, "lon": 1.0830275}, method='POST'))

def file_binary():
  pass   # TODO    # ver: file_binary
  # TODO: seek?

def assertion():
  name = "bob"
  count = 3
  assert name == "bob", f"I am expecting {name} to be 'bob'"  # ver: assertion
  assert count >= 3  # ver: assertion

def sort():
  # TODO: sort with comparator # ver: sort
  # reverse=True - key function
  data = ["b", "d", "c", "a"]    # ver: sort


def regex():
  # TODO: regex
  import re   # ver: regex



def function_named_defaults():
  """
  
  """
  # TODO
  pass


# cool bits
# a,b = b, a   # swap 
# ll = list(map(int, input().split()))
# ll = [line.strip() for line in open('FILE.TXT', 'r')]
# 

#-------------------------------------------------------------------------------

if __name__ == "__main__":

  def title(title):
    print('-{0}-'.format(title))

  hello_world()
  #read_line_from_console()
  define_variables()
  define_constants()
  arithmetic()
  if_statement()
  for_loop()
  while_loop()
  for_each_loop()
  file_write()
  #file_read()
  #function()
  function_with_return_value()
  function_with_param_function()
  list_comprehension()
  dict_comprehension()
  define_fixed_array()
  define_list()
  define_map()
  define_set()
  define_2d_arrays()
  function_with_param_function()
  json_data()
  nested_data()

  commandline_args()
  network_tcp_send()
  network_tcp_recv()
  network_udp_send()
  network_udp_recv()
  http_request()
  http_request_json()
  file_binary()
  assertion()
  sort()
  regex()

  # Run all functions in order
  #for function_name in functions:
  #    title(function_name)
  #    if function_name not in locals():
  #        print('UNIMPLEMENTED')
  #        continue
  #    locals()[function_name]()
