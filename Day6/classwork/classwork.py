#group 102
#working on homework
# ask user to enter his/her name and print which index is the vowel.
full_name=input("Enter you name: ")
i=0
while i<len(full_name):
    if full_name[i] in "aeiou":
        print(str(i)+full_name[i])
    i+=1
#--------------------
#loop in loop means squaring the range number. in this example elene will be printed 10*10=100
for i in range(10):
    for j in range(10):
        print("elene") # elene will br printed 10*10=100 times
# the result will be 100 (10*10)

x=0 # incremenation variable
for i in range(5):
    for j in range(4 ):
     print(str(x)+"elene")
    x+=1


x=0  
for i in range(5):
    for j in range(4 ):
      for k in range(3):
       print(str(x)+"elene")
       x+=1 # x should be under print in here
    # the result will be 60 . (5*4*3)
    

#-------------------------
#sololearn works:
#work1:
total_price=0
for i in range(5):
    age_of_user=int(input("Enter your age :"))
    if age_of_user>=3:
        total_price+=100
print(total_price)
# use while in this task
total_price=0
i=0
while i<5:
    age_of_user=int(input("Enter your age :"))
    if age_of_user>=3:
        total_price+=100
    i+=1
    
print(total_price)

#work2:
n=int(input("enter n :"))
#x is index=0,1,2,3,4...........
for x in range(1,n):
    if x%3==0 and x&5==0:
        print("sololearn")
    elif x%3==0:
        print("solo")
    elif x%5==0:
        print("Learn")
    else:
        print(x)

#work3
user_weight=int(input("Enter your weight:"))
user_height=int(input("Enter you heigh: "))

bmi=user_weight/(user_height**2)

if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<30:
    print("normal")
elif bmi>=25 and bmi<30:
    print("oerweight")
elif bmi>30:
    print("obesity")
#----------------------
#List
my_list=["xinkali","mwvadi","lobiani","qababi","khachapuri","wyali"]
prices=[2, 20, 15, 10 , 15, 2 ]

weird_list=["elene","elene2","elene3",[1,2,3],"Elene",[4,5,6]] #-list in list
print(my_list)
print(my_list[1]) #mwvadi

print(weird_list[3])

print(weird_list[3][1]) # 2

for food in my_list:
    print(food) #food- xinkali,mwvadi,lobiani,qababi,khatcagpuri,wyali
#-------------------------
if 0>0:#it will not work
  print("yes") 
#-------------------
#an infinite loop
counter=0
while counter<4:
    print(counter)
# -----------------
#while loop
for i in range(3):
    print(i<1) #it will have boolean result
#----------------------
print(5==5)# it will have boolean result
#-----------------------------
pas="secret"
gues="123"
print(gues!=pas) #true
#----------------------------
#group 4 :
#working on homeworks N2:
odd=1
even=2
 
while even<-30:
    print(str(odd)+'odd')
    print(str(even)+"even")
    even+=2
    odd+=2
# or

i=0
while i<30:
    print(i,"odd")
    print(i+1,"even")
    i+=2
#--------------------
# work1:3-ის ჯერადი რიცხვები 1იდან 30ის ჩთ

for i in range(31):
    if i%3==0:
        print("რიცხვი"+ str(i)+ ' '+ " არის 3 -ის ჯერადი")

# or,more simple way
i=3
while i<30:
    
    print(i,"3-is jeradia")
    i+=3
#--------------------------

age=7
is_student=False

if age<18:
 #execue if age is less han 18
 if is_student:
    #execue if under 18 an also a student
    print("20% discount")
 else:
      #execute if under 18 and not a student
      print("10% discount")
else:
   #execute this coe costomer 19 or over
   print("regular price")
#----------------------------------
age=19
if age<18:
   if is_student:
      print("dicount 20 %")
else:
   print("regular price")
print("proceed to payment")
#-------------------------
count=1
while count<10:
   print(count)
#infinite looop
#-------------------------
#REVIEW
#1)Loop in loop- loop in loop means squaring the range number. in this example elene will be printed 10*10=100
# for i in range(10):
#     for j in range(10):
#         print("elene") # elene will be printed 10*10=100 times

# REMEMBER-if we have 3 loop .(loop in loop in loop) result will be: first range() * second range* third range() 
#example: # x=0  
# for i in range(5):
#     for j in range(4 ):
#       for k in range(3):
#        print(str(x)+"elene")
#        x+=1 # x should be under print in here
    # the result will be 60 . (5*4*3)

#2)LIST- syntax list_name=["first value","second value","thord value"]
#example:
# my_list=["xinkali","mwvadi","lobiani","qababi","khachapuri","wyali"]
# prices=[2, 20, 15, 10 , 15, 2 ]
# food_list[0]-xinkali  price_list[0]-2 
 
#interesting cases 
 
#3)boolean types
# for i in range(3):
#     print(i<1)  #it will have boolean result!
## print(5==5)# it will also have boolean result

#4)3-ის ჯერადი რიცხვები 1-იდან 30-ის ჩთ
# i=3
# while i<30:
    
#     print(i,"3-is jeradia")
#     i+=3

#5)# age=7
# is_student=False

# if age<18:
#  #execue if age is less han 18
#  if is_student:
#     #execue if under 18 an also a student
#     print("20% discount")
#  else:
#       #execute if under 18 and not a student
#       print("10% discount")
# else:
#    #execute this coe costomer 19 or over
#    print("regular price")
