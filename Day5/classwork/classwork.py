#group 102:
# Loops: 1)for loop 2) while loop

#for loop
for i in range(7): # i-iterative variable! range-function that is written for python
    print("nika") # range(7)-variable which's lenght is 7. range(7)=0,1,2,3,4,5,6 same as range(0,7)

for i in range(len("elene")): #range=Sequence(მიმდევრობა) it has always integer as a parameter!, len("elene") the result wil be 5 (amount of letters)
    print("kako")

for x in range(3,6): #range(3,6)=3,4,5  loop will be lasted for three times
   print(str(x)+  " elene ")  


for x in range(5,10,2): #range(5,10,2)=5,7,9 start-finish-step
    print(str(x)+" ELENE ")

#while loop
i=0 #iterative vriable
while i<5:
    print("elene")
    print(i)
    i+=1 #incrementation variable

full_name="Elene Morgoshia" #while counting names,we have to remeber 2 things:1)counting starts with 1 end 2)space is counted as well.
i=0
while i<len(full_name):
     print(full_name[i])
     i+=1
#-----------------------
#work1: a="qwerty" b="asdfgh" you have to print:
# qa
#ws
#ed
#rf
#tg
#yh
a="qwerty"
b="asdfgh"

i=0
while i<len(a):
    print(a[i]+b[i])
    i+=1
# explanation of this process :
#1) i=0 a[i]=a[0]=q, b[i]=b[0]=a
#2) i=1 a[i]=a[1]=w,  b[i]=b[1]=s
#3) i=2 a[i]=a[2]=e,  b[i]=b[2]=d
#4) i=3 a[i]=a[3]=r,  b[i]=b[3]=f
#5) i=4 a[i]=a[4]=t,  b[i]=b[4]=g
#6) i=5 a[i]=a[5]=y,  b[i]=b[5]=h
#---------------------------------------
#and ,  or

if 10>5 and 3>1:
    print("cool")
if 10>5 or 15>5:
    print("good")

#--------------------------
#not
#example1:
print(not 1==1)
False
print(not 1>7)
True
#example2 
if not True: #not True= False
    print("1")
elif not (1+1==3): #not False=True
    print("2")
else:
    print("3")
# the resul will be 2
#-----------------------
#group 4

#for loop
for i in range(3):
    # print("Hello")
    # print("elene")
    print(str(i)+"elene")
#-----------------------------
#work1:ask user to enter his/her age and name.
# print:" in 2024 your age will be .......
#         in 2025 your age will be ........." sentences like that 10 times.

name=input("Enter your name pls: ")
age=int(input("Enter your age pls: "))

# incrementation variable for years:
years_variable=2023
# for loop
for i in range(10):
    if i==0: #  if i==0.(i=0 is syntax eroor) == checks whether the values on the left and right sides are equal.
      print("in {} your age is:{}".format(years_variable,age))
    elif i>0:
      age+=1
      years_variable+=1
    print("{} your age in {} is {}".format(name,years_variable,age))
    i+=1

#also you can write like that- more easier!
name=input("Enter your name: ")
age=int(input("Enter your age: "))
years=int(input("Enter Year: "))
for i in range(10):
    print(name + " you  will  be " + str(age + i) + " " +"year"+" " + "in" + " " +str(years+i))
#-----------------------------------
#While loop
 
seats=100 # amount of seats
while seats>0: 
      print("sell tickets")
      seats=seats-1
#----------------------
#work2:you have to print  hom many seats are left in each iteration

seats=5
while seats>0:
    print(str(seats)+"seats are left")
    seats=seats-1

for i in range(1,5):
    print("elene")
#-----------------------------
#REVIEW
#1)for loop- for i in range(7): - i-iterative variable! range-function that is written for python.
# range()-in () we have to write number that will be the amount of looping 
# range(7)- range(7)=0,1,2,3,4,5,6 same as range(0,7)
#range(5,10,2)=5,7,9 start-finish-

# example: #user_name[j]-letter print(j)- index
#user_name=input("enter your age : ")
#for j in  range(len(user_name)):
  #       if user_name[j] in "aeiou":

#2)while loop- syntax:
# i=0
# while i<len(full_name):
#      print(full_name[i])
#      i+=1