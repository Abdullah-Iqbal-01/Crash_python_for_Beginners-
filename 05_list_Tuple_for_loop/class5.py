# -*- coding: utf-8 -*-
"""class5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IE1NrEhwgQBSI1GOsOlWnx6pIR1nrTgL

# List
  

*   iteration operation with loop
*    apply any operation on element
"""

names :list[str] = ["Abdullah" , "Qadir", "Mustafa", "Hamzah"]
print(names)

for name in names:
  print(name)

for name in names[0:3]: # 3 + -1 =  2 => [0 , 1 ,2]
  print(name)

"""# this Iteration in JavaScript Method

    names = names = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

*    for(i=0; i<names.length; i++){
  *  names[i]
*         }
"""

names = ['Abdullah', "Qadir", "Mustafa"]

i:int = 0 # counter = 0

while i<len(names): # names length =3
    print(names[i])
    i += 1

names = ["Sir Qasim" ,'Abdullah', "Qadir"]

for name in names:
    print(f"Welcome Dear Teacher {name}")
    print("At our Today's Session\n")

print("Thanks to ALL For joining us")

names = ["Sir Qasim" ,'Abdullah', "Qadir", ]

for name in names[0:2]: # it's Called Slicing
    print(f"Welcome Dear Teacher {name}")
    print("At our Today's Session\n")

print("Thanks to joining us")

names = ["Sir Qasim" ,'Abdullah', "Qadir", ]

for name in names: # it's Called Slicing
    print(f"Welcome Dear Teacher {name.upper()}")
    print("At our Today's Session\n")

print("Thanks to joining us")

"""# Tuples
## What is a Tuple?
A tuple is an immutable collection of ordered elements. Tuples are like lists, but their values cannot be changed after assignment. Tuples are defined using parentheses ().
"""

Data_base : tuple[str , str]  = [("Abdullah" , "123"),
                                 ("Qadir" , '234'),
                                  ("Ali" , '444')]


for data in Data_base:
    print(data)

# this is your practice
# Please think and resolve this Error

Data_base : tuple[str , str]  = [("Abdullah" , "123"),
                                 ("Qadir" , '234'),
                                  ("Ali" , '444')]

for data in Data_base:
  user , password = data
   print(user , password)

Data_base : tuple[str , str]  = [("Abdullah" , "123"),
                                 ("Qadir" , '234'),
                                  ("Ali" , '444')]

for data in Data_base:
  user , password = data
  print(user , password)

input_user :str = input("Enter you name\t")
print(input_user)

Data_base : tuple[str , str]  = [("Abdullah" , "123"),
                                 ("Qadir" , '234'),
                                  ("Ali" , '444')]
input_user : str = input("Enter Your User Name\n")
input_password : str = input("Enter Your Password\n")

for data in Data_base:
  user , password = data
  if user.lower() == input_user.lower() and password == input_password:
    print(f"{user} Login Successfully")
    break
else:
    print("Login Failed")

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names:
print(name)

names = ["Sir Qasim" ,'Abdullah', "Qadir", ]

for name in names:
 print(name)

names:list[str] = ['Sir Zia', "Muhammad Qasim", "DR Noman"]

for name in names
    print(name)

names : list[str] = ["Sir Qasim" ,'Abdullah', "Qadir", ]

for name in names:
    print(name)

greetings = "Hello Python How Are you!"
 print(greetings)

greetings = "Hello Python How Are you!"
print(greetings)

Students : list[str] = ["Ali", "Bala" , "Lagbataq" , "Chacho" , "NanKachori"]

for student in Students:
    print(f"Hello That's a great news {student}!!")
    print(f"We are going to School Picnic on sunday {student}!!\n")

print("Every Student Be Raady on Time") # last message for everyone

# enumerate showing all index numbers
#              0        1         2
magicians = ['alice', 'david', 'carolina']

list(enumerate(magicians))

magicians = ['alice', 'david', 'carolina']

for index , value in enumerate(magicians):
    print(index , value)

"""#  Numbers with loop
* range(start,end,step)
"""

range(10)

list(range(10)) # Bhaia Samjho esko Yaha Pr 0 se HoRaha He start and Last Number me se n-1 means Ak number (-).

list(range(2,21,2))

for num in range(1,11):
    print(num)

for num in range(1, 11):
    print(f"2 x {num} = {num * 2}")

for num in range(1, 11):
    print(f"3 x {num} = {num * 3}")

squares :list[num] = []

for Value in range(1, 11):
  square = Value ** 2
  squares.append(square)

print(squares)

"""# list comprehensive
## Normal Loop

* for item in item_list:
*     * Loop_body

# Comprehensive Style
*   [loop_bodu for item in items_list]
"""

'line1'
'line2'
'line3' # always return last line

[staff for staff in Staff]

Staff :list[str] = ["Abdullah", "Qadir", "Ali" , "Mustafa"]

for staff in Staff:
  print(staff)

Staff :list[str] = ["Abdullah", "Qadir", "Ali" , "Mustafa"]

[staff for staff in Staff]

numbers :list[int] = [1,2,3,4,5,6,7,8,9,0]

print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

menu_item :list[str] = ["Chicken", "Beef pulao" , "Tikka" , "Biryani" , "Karahi"]
change_menu = menu_item[:]

print(menu_item)
print(change_menu)

change_menu [0] = "Fish"

print(menu_item)
print(change_menu)

menu_item :list[str] = ["Chicken", "Beef pulao" , "Tikka" , "Biryani" , "Karahi"]
change_menu = menu_item[:] # deep Copy

print(menu_item)
print(change_menu)

change_menu.append("Fish")

print(menu_item)
print(change_menu)

"""# tuple

"""

names : tuple[str] = ("A" , "B" , "C")

print(names[0])
print(names[1])
print(names[2])

names : tuple[str] = ("A" , "B" , "C")

names[0] = "Ali"

a  = input("abc") # return string type
print(type(a))
print(a)

b = input("Laqbataq") # return string also

print(type(b))
print(b)

a = "Type"

print(type(a))

a = 123

print(type(a))

sorted([1, 5, 3 ,2 ,4])

Digits = 1 , 5 , 4, 3, 2 , 6, 8, 7 , 9,

print(Digits)

print(sorted(Digits))

"""#  **Thanks** to Read this **note book**




"""

