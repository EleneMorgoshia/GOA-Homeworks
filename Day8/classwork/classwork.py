#group 4:
word="run"
word[0]="f"
print(word)# string-unmutable!!!

brands = ["Honda", "Toyota", "BMW", "Mercedes"]
print(brands[-2:-4])
#------------------------
#working on homework:
my_arr=["molodini","djanezaahvili","tkeshelashvili","philishvili"]
for element in my_arr:#checking evrey element in the list
    if element=="tkeshelashvili":
        print(element)
#---------------------------
for i in range(40,60,5): #from 40 to 60
    print(i)# i =iteration
#--------------------------
#work1:
my_str="nika 11 keshelava"
print(int(my_str[5])+int(my_str[6]+"4"))
print(my_str[5]+my_str[6]+"4") # გადააკეთეთ ეს კოდი ისე,რომ მიიღოთ 15
print(int(my_str[5])+int(my_str[6]+"4"))
#or
print(int(my_str[5]+my_str[6])+4)
#--------------------------
i=0
while i<5:
    print("python is cool")
    i+=1
    print("javascript is also cool")
#meore print-ic while-s ekutvnis.amitom 10jer gamoitans ekranze winadadebebs
#---------------------------
foods=["khinkali",",wvadi","xachapuri","xizilala"]

foods.append("pizza") #boloshi elementi chavamatet
print(foods[4]) #daiprinteba pizza (list-shi atvla iwyeba 0-idan!)

foods.insert(2,"lobiani")# elementis chamateba 2indeqsze.libians vamatbet meore indeqszee
print(foods)
print(len(foods)) # am dros atvla iwyeba 1-dan
print(len(foods[0])) #pirveli elementis asoebis raodenoba
#--------------------
#group 102
#working on homeworks:

#find out the max value in the list. do no use sorting method
my_arr=[20,43,56,73,10,6,87,45,97] 
# using max-first way
print(max(my_arr)) #function that will find out which one is the max value

#second way:
my_arr.sort() #sorting(from lowes to highest)
print(my_arr)
print(my_arr[len(my_arr)-1])
#or
print(my_arr[-1])

#third way: using for
max_num=my_arr[0]
for score in my_arr: #for each score in my_arr
   if score>max_num:
      max_num=score
print(max_num)

#using while
max_num=my_arr[0]
i=0
while i<len(my_arr):
   if my_arr[i]>max_num:
      max_num=my_arr[i]
print(max)

#------------------------
#work1
name="nikax"
my_arr=[20,43,5,97,73]

i=0
while i<len(name):
     print(name[i]+"-"+ str(my_arr[i]))
     i+=1
#------------------------------------------
#working on homeworks ****
students=["nika","ana","mamuka","iva","farna"] 
# # შეატრიალეთ უკუღმა sort  და reverse მეთოდის გარეშე.

new_arr=[]
i=len(students)
while i>0:
     new_arr.append(students[i-1])
     i-=1
print(new_arr) 
#-----------------------------
#FUNCTIONAL ROGRAMMING
print("nika")
print(max([10,23,6]))

def wish_a_good_day(name,day):
    print(name+"karg dges gisurveb  "+ str(day) +"  octobers")
wish_a_good_day("kako",5)
wish_a_good_day("tamuna",17)
wish_a_good_day("maro",19)

names=["nika","ana","mamuka","iva","farna"]

for name in names:
    wish_a_good_day(name,17)
#--------------
#work1:შექმენით ფუნქცია,დაარქვით შეკრება,არგუმენტად 
#გადაეცემოდეს ორი რიცვი და პრინტავდეს მათ ჯამს
def sum(num1,num2):
    print(num1+num2)
number1=int(input("Enter number1: "))
number2=int(input("enter number2: "))
sum_of_the_two_numebers_is=sum(number1,number2)
sum(100,900)
#-----------------------
scores=[20,43,5,97,73,10,6,87,45,53,6]
def calculate_max(scores):
    max_num=scores[0]
max_num=scores[0]
for score in scores:
    if score>max_num:
        max_num=score

calculate_max([20,43,5,97,73,10,6,87,45,53,6])
calculate_max([20,43,5,97,73,10,6,87])
calculate_max([20,43,5,97,73])
#-------------------------
#work1:შექმენით ფუნქცია,დაარქვით შეკრება,არგუმენტად 
#გადაეცემოდეს ორი რიცვი და პრინტავდეს მათ ჯამს- მეორე გზა ამოხსნის

def pair_sum(arr1,arr2):
    for i in range(len(arr1)):
        print(arr1[i]+arr2[i])

pair_sum([20,43,5],
         [2,4,51])


def pair_sum(arr1,arr2):
    for i in range(min([len(arr1),len(arr2)])):
        print(arr1[i]+arr2[i])

pair_sum([20,43,5,10],
         [2,4,51])
#----------------------------------------
#REVIEW
#1)# string-unmutable!!!LIST-MUTABLE

#2)function max- function what will find out which element is the max value.
#syntax: max(name of the variable or list you would like)
#example:(max(my_arr))-function that will find out which element is the max value in the list my_arr


#3)FUNCTIONAL ROGRAMMING-
#syntx- def name of the function(variable as a parameter):
#             operations
#exmaple: 
#def wish_a_good_day(name,day):
#     print(name+"karg dges gisurveb  "+ str(day) +"  octobers")
# wish_a_good_day("kako",5)