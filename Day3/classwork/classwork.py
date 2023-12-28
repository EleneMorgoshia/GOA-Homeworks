#Group 4

name="Tom"
salary=1000
print(name)
#print word "name"
print("name")
name="name"
print(name)
#----------------------
#here we learned about debugging
message="Debbuging"
print(message)
#-------------------------
#Group 102

format
my_name="Elene"
my_surname="Morgoshia"
my_age=19
my_pet_name="miki"
my_sentence="My name is {0}, My username is {1}, My petname is {2}, My age is {3}.".format(my_name, my_surname , my_pet_name,my_age)
print(my_sentence)
#----------------------------
#if else
my_name="Elene"
if "e"in my_name:
    print("letter e is in my_name")
else:
    print("letter e is not in my_name")
#----------------------------------
#input and output 
   # input-Data given to a program.(mouse)
   # output- Result produced by the program. (monitor)
my_name=input("enter your name: ") #your name value  will be saved in my_name variable
print("My name is"+ " " + my_name)
#--------------------------------------
#guideline of incresing values
my_age=19
#after 3 year
my_age+=3
print(my_age)
#------------------------------------------
#work1: ask user to enter his/her name,surname,age
#            print this variables as a beauiful sentence ( use format method)
#             print what will heppen after 3 years

your_name=input("Enter your name pls: ") #input function always has string type value as a parameter !
your_surname=(input("Enter your surname pls: "))
your_age=int(input("Enter your age pls: ")) # add int in order to have integer type for age 
print(your_age)
beautiful_sentence="My name is {0}, My surname is {1}, I am {2} years old ".format(your_name,your_surname,your_age)
print(beautiful_sentence)
increase_age=("What will happen after 3 years?")
print(increase_age) #what is happening-explanation in line 62
print(type(your_age))
your_age=int(your_age)+3 # rewrite  variable. changeing  types.  
another_beautiful_sentence="After 3 years,my age will be: {}".format(your_age)
print(another_beautiful_sentence)
#-----------------------------------------------
#how to make values as a same types
print(2+2)
print("2"+2)#error.different type
print("2"+"2"+"2")#222
print(int("2")+2)
#---------------------------------------------
#work N2: aks user to enter 2 number.
# if multiplication of these numbers is grater thant 100, print multiplication,
# or print :" you lose the game "

first_number=int(input("enter the number pls: "))
second_number=int(input("enter another number pls "))
if first_number*second_number>100:
       print(first_number*second_number)
else :
       print("you lose:(")

# another way:
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
product=num1*num2
if product>100:
   print(product)
else :
      print("you lose")
#--------------------------------
#% operator
print(20%6) # 6*3=18, 20-18=2 , so,result will be 2
#-------------------------------------------
#REVIEW
#1)format- my_sentence="My name is {0},my surname is {1}, i am {2} years old".format("elene","morgoshia",19)

#2)if else - if 10>5:
#                print("Yes")
#             else:
#               print("No")

#3)input and output-   Input-Data given to a program.(mouse)  #input function always has string type value as a parameter !
#  Output- Result produced by the program. (monitor)
# input example: first_name=input("enter your name ") - when user enters his/her name, this will be the value of the variable called first_name

#4)#guideline of incresing values- my_age+=3- it means: my_age=my_age+3

#5)#how to change values type.(e.g how to change string value with int value)- 
#     your_age=(input("Enter your age pls: ")) # add int in order to have integer type for age 

#6)% operator -# print(20%6) # 6*3=18, 20-18=2 , so,result will be 2
