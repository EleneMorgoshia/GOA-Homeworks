#group4:
#working on homework
total=0
total_nums=0

for i in  range(5):
    num=int(input("Enter your grade: "))
    total +=num
    total_nums+=1
print(total//total_nums)
avg_grade=total//total_nums

if avg_grade>9:
    print("გილოცავ შენ მოიგე ტოსტერი")
elif avg_grade<5:
    print("gilocav shen gaeqeci matricas")
elif avg_grade>5 and avg_grade<10:
    print("yu are mid")
elif avg_grade>10 or avg_grade<0:
    print("something wrong with you")
#-----------------------------
#lists
# example1:
my_list=["xinkali","mwvadi","vashli",7,5]
print(my_list) 

# example2:
compositions=[
"symphony no. 5",
"symphony no.3 ",
"symphony no.7"
] #you can place list items on seperate lines 
print(compositions)
#--------------------
# \n==making space
print("hello \n world") # resrut will be:hello   
# world
#-----------------------
#LIST
last_calls=["mum","dave","lara"]
print(last_calls[0])
print(last_calls[1])
print(last_calls[2])
print(last_calls[0],last_calls[1],last_calls[2]) # every value will be printed together

#example2
animals=["dog","cat","bird"]
my_pet=animals[1]
print(my_pet)

#example3: lists are mutable
nums=[8,9,10]
nums[0]=11 #first element will be changed with 11
print(nums)

#example4:
words=["rise","sun","glasses"]
print(words[1]+words[2]) #it will be printed as str prints

#example5:slicing
nums=[8,6,19,7,15]
print(nums[1:4])# in [] : creates ranges. from 1 to 3

nums[1]=1
print(nums)
#----------------------------
#group 102:
#working on homeworks:
my_list=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]
prices=[2,20,15,10,15,2]
print(len(my_list))
print(len(prices))
i=0
while i<len(my_list):
    print(my_list[i]+ " girs "+ str(prices[i])+ " lari ")
    i+=1
#---------------------------
#LIST
my_arr=["banana",11,True,10.5,[1,2,3],5,10]
print(my_arr[-1])
print(my_arr[3])
print(my_arr[1:3]) # from 1 to 3)
print(my_arr[0:6:2])
print(my_arr[:4])
#----------------------
#how to find out if our list contains specific elements or not?
manu=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]
if "lobiani" in manu:
    print("we have  a lobiani")

# changing elements
manu[1]="BBQ"
print(manu)

manu[2:4]=["aa","bb","cc"]
print(manu)
#--------------------
#changing elements in string
my_name="Elensio"

new_name=" "

for i in range(len(my_name)):
    if i ==2 or i==3:
        new_name+="x"
    else:
        new_name+=my_name[i]

print(new_name)

# or use replace function
print(my_name.replace("el","kk"))

#-----------------------------
#insert function in list:
manu=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]
manu.insert(3,"nayini")
print(manu)
#-------------------------
#append- addin element in the and of the list
manu=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]
manu.append("cecxli")
manu.append("navti")
print(manu)
#---------------------------
#empty list
manu=[]
manu.append("pizza")
print(manu)
#---------------------------
#work1
#მომხმარებელს შემოატანინეთ 5 საჭმელი, 
# სიაში შეიტანეთ ისინი,რომელიც შეიცავენ მინიმუმ 2 "ა"-ს

"marwyvi","atami","mawoni","ananasi","kitri"

food_list=[]
for i in range(5):
    food=input("Enter food pls: ")
    if food.count("a")>=2: # if elements in food includes a tweice
     print(food)
     food_list.append(food)

print(food_list)

#or
food_list=[]
for i in range(5):
    food=input("Enter food pls: ")
    count_of_a=0 #create counter for counting "a"s
    for char in food:
        if char=="a":
         count_of_a+=1
    if count_of_a>=2:
       food_list.append(food)
       count_of_a=0
print(food_list)



my_name="elene morgoshia"
if my_name.count("e")>=2:
    print("YES")
#---------------------------
#remove method
manu=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]
manu.remove("wyali")
print(manu)
manu.remove("mwvadi")
print(manu)
del manu[2] #delating third value
print(manu)
#-------------------------
#work2: წაშალეთ სიიდან ის ელემენტები,რომლბშიც მეორე ასო არის "ა"
manu=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]

for i in range(len(manu)):
  new_variable=manu[i] #ახალი ცვლადი იმისთვის ,რომ ინდექსებზე წვდომა მქონდეს!
if new_variable[1]=="a":
     manu.remove(i)
print(manu) 
# #არ მუშაობს:(

#easiest way.! remove and append method do not use with List. make another list 
new_manu=[]
for food in manu:
    if food[1]!="a":
        new_manu.append(food)
print(new_manu)

#--------------------------
#sorting-ზრდის მიხედვით დალაგება
scores=[20,43,56,73,10,6,87,45,97]
scores.sort()
print(scores)

#sorting in string - ანბანის მიხედვით ალაგებს ზრდადობით
students=["nika","ana","mamuka","iva","farna"]
students.sort()
print(students)
students.sort(reverse=True)# შეტრიალება ზემოდან ქვემოთ
print(students)
#---------------------
#REVIEW
#1)List- you can place list items on seperate lines. 
#example:# compositions=[
# "symphony no. 5",
# "symphony no.3 ",
# "symphony no.7"
# ]

#2)#\n- making space 
#example:print("hello \n world") # resrut will be:hello
#                                       world

#3)lists are mutable- this means you can change their values even after they've been crated
#example: 
#nums=[8,9,10]
#nums[0]=11 #first element will be changed with 11
#print(nums)

#4)summing of list values-
#example
#words=["rise","sun","glasses"]
#print(words[1]+words[2]) #it will be printed as str prints (sunglasses)

#5)slicing
# nums=[8,6,19,7,15]
# print(nums[1:4])# in [] : creates ranges. from 1 to 3

#6)insert function- when you want to add something in your list
#example:#insert function in list:  listname.insert(where you want to add,what do you want to add)
# manu=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]
# manu.insert(3,"nayini")
# print(manu)

#7)#append- adding element in the and of the list: 
#example + syntax: syntax- listname.appedn(additional element)
# manu=["xinkali","mwvadi","lobiani","kababi","khatchapuri","wyali"]
# manu.append("cecxli")

#8)function count-Determines the frequency of a specified element within a given sequence
#examle 1+ syntax: syntax- variable name.count(the value you would like to enter)
# food=input("Enter food pls: ")
#     if food.count("a")>=2: # if elements in food includes "a" tweice, print food
#      print(food)
#example2:
# my_name="elene morgoshia"
# if my_name.count("e")>=2:
#     print("YES") 

#9)interesting case of count function:
#მომხმარებელს შემოატანინეთ 5 საჭმელი, 
# სიაში შეიტანეთ ისინი,რომელიც შეიცავენ მინიმუმ 2 "ა"-ს
# food_list=[]
# for i in range(5):
#     food=input("Enter food pls: ")
#     if food.count("a")>=2: # if elements in food includes a tweice
#      print(food)
#      food_list.append(food)

# print(food_list)

#10) remove method-delating elements from the list
#syntax- listname.remove("which element you want")
#example:manu.remove("mwvadi")

#11) del method- delating spacific element by it's index in the list
#syntax- del listname[index]
##example-del manu[2]- element that is on the second index will be delated

#12) remove and append method do not use with  first List. make another list in that kind of  cases

#13)sorting-ზრდის მიხედვით დალაგება
#exaple:
# scores=[20,43,56,73,10,6,87,45,97]
# scores.sort()
# print(scores)

#14)reserve method-კლებადობით დალაგება( ზემოდან ქვემოთ)
#syntax-listname.sort(reserve=True)
#example:
# students=["nika","ana","mamuka","iva","farna"]
# students.sort()
# print(students)
# students.sort(reverse=True)