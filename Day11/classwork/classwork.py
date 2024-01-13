# #group4:
# #working on homeworks
# #4)turtle-თი რენდომ რიცხვებით დახაზეთ შედევრო
# # forward(random.randint(100))
    
from turtle import*
import random
speed(10000)

colors=["red","green","blue","purple","yellow"]
for i in range(100000):
    width(random.randint(1,10))
    color(random.choice(colors))
    forward(random.randint(0,100))
    left(random.randint(0,100))
exitonclick()
# #-------------------------
# #working on homeworks:
# #შექმენით random password generator პროგრამა ,რომელშიც
# #დაგენერირდება პაროლი,48 სიმბოლოინი,სადაც  6 ცალი სიმბოლოები იქნება !#*%(^)
# #25 სიმბოლო იქნება აბგდევზეთიკლმნეოოპჟრ(ასოები),9 სიმბოლო იქნება ციფრები
# #ჯამში უნდა გამოვუდეს მაგ:!n8391k"
import random
my_arr=[]
chars=list("abcdefghijklmnopqrstuvwrandomstudentyz")
symbols=list("#$%^&*")
numbers=list("0123456789")
for i in range(9):
    random_num=random.choice(numbers)
    my_arr.append(random_num)
    numbers.remove(random_num)

for i in range(25):
    random_char=random.choice(chars)
    my_arr.append(random_char)
    chars.remove(random_char)

for i in range(6):
    random_symbol=random.choice(symbols)
    my_arr.append(random_symbol)
    symbols.remove(random_symbol)

print("the program chose these characters:",  my_arr)
final_password=""
for i in range (len(my_arr)):
    current_char=random.choice(my_arr)
    final_password+=current_char
    my_arr.remove(current_char) #რათა my_arr სიაში არსბეული ყველა სიმბოლო ერთხელ გამოვიყენოთ
print("THE FINAL PASSWORD IS:",  final_password)
# #------------------------------------------
# #working on homeworks
# #დაწერეთ პროგრამა,რომელიც რენდომად გამოიძახებს ჯგუფის რომელიმე წევრს
# #თუ მან შეკითხვაზე პასუხი სწორად გასცა მოემატოს 10  ქულა, ამოვარდეს სიიდან
# #თუ არადა დააკლდეს 5 ქულა
# #იყოს5 სტდენტი და ქულების სია 

# #მინიშნება:  answer=input("did the student answer corectlt: ")
#          #       if answer=="yes":
# #                       moematos 5 qula
# #                if answer=="no":
# #                    moakldes 5 qula

students=["giorgi","rati","salome","anri","demetre","giorgi molodini"]
grades=[10,20,30,40,10,100]
giorgis_index=students.index("giorgi") #ეს დაპრინტავს მერამდენე ინდექსზეა გიორგი,ანუ 0-ს.
giorgis_grades=grades[giorgis_index]
print(giorgis_index)
print(giorgis_grades)
print(giorgis_grades+10)


import random
students=["nino","anastasia","pavle","rati","giorgi"]
scores=[100,200,300,400,500]
for i in range(len(students)):
    for j in range(len(scores)):
       random_student=random.choice(students)
       students_index=students.index(random_student)
       each_students_score=scores[students_index]

       print(random_student)
       answer=input("Did student answer correctly?")
       if answer=="Yes":
        print("your answer is correcct. Member {} will be given 10 points. Your total score is: {} ".format(random_student,each_students_score+10))
        students.remove(random_student)
        scores.remove(each_students_score)
       elif answer=="No":
        print("Your answer is incorrect. Member {} losted 5 points. Your total score is: {} ".format(random_student,each_students_score-5))
#YESSSSSSSSSSSSSSSSS
        
#or you can write like that:
import random
arr_of_students=["nino","anastasia","pavle","rati","giorgi"]
arr_of_grades=[0,0,0,0,0]

for i in range(len(arr_of_students)):
    random_student=random.choice(arr_of_students)
    print(random_student)
    answer=input("did the student answer correctly?: ")
    index_of_random_student=arr_of_students.index(random_student)
    if answer=="Yes":
       random_student_grade=arr_of_grades[index_of_random_student]
       print(random_student,"has plus 10 grade and the next student is: ")
       random_student_grade+=10
       arr_of_students.remove(random_student)
    elif answer=="No":
       random_student_gtade=arr_of_students[index_of_random_student]
       random_student_grade-=5
       print("the student has minus  points and the next student is: ")
    else:
       print("yes or no:")
print("quiz is over and the students have overall grade",arr_of_grades)
#--------------------------------------------------------
#group102
#working on homeworks:
#You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.
  
def positive_sum(arr):
    sum=0
    for i in arr:
        if i>=0:
            sum+=i
        
    return sum

my_arr=[1,-2,3,4,5]
print(len(my_arr))
positive_sum(my_arr)

#ეს რატომ არ მუშაობს სწორად?  #QUESTION
def positive_sum(arr):
    sum=0
    for i in range(len(arr)): 
        if arr[i]>=0:
            sum+=arr[i]
        elif arr[i]<0:
          sum=0
    print("sum=", sum)

my_arr=[1,-2,3,4,5]
positive_sum(my_arr)


arr=[1,-2,3,4,5]
sum=0
for i in range(len(arr)): 
        print(arr[i])
        if arr[i]>0:
            sum+=arr[i]
            print("sum=", sum)
        
print(sum)
#----------------------------------------------------------
#working on codewars
#task1:
#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# def repeat_str(repeat, string):
#     return repeat*(string)
# print(repeat_str(5,"elene"))


my_name="elene"
print(my_name*3)#გამრავლება სტრინგის და ინტის მოსულა
print(my_name+3) #შეკრება სტრინგის და ინიtს არ მოსულა

#-------------------------------------------------
#task2: string's slycing
#It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
#You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

# fixed tests
def remove_char(s): 
    return(s[1:-1])
    # return (s[1:(len(s))-1])#ეს უფრო რთული გზაა



name="fixed tests"
print(remove_char(name))

# working
my_surname="Morgoshia"
print(my_surname[1:5])
print(my_surname[1:(len(my_surname))-1])
print(my_surname[1:-1])
#----------------------------------------------------
#task3:
#Given an array of integers your solution should find the smallest integer.
def find_smallest_int(arr): #arr=[1,2,90,3]
      min=arr[0]
      for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
      return min
        
my_arr=[1,2,3]
print(find_smallest_int(my_arr))
#--------------------------------------------------
#task4
#Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers): #numbers=[1,2,3]
    sum=0
    for i in range(len(numbers)):
        numbers[i]=numbers[i]**2
        sum+=numbers[i]
    return sum
numbers=[1,2]
print("squared sum=", square_sum(numbers))
#--------------------------------------------
#task5
#Write a program that finds the summation of every number from 1 to num. 
#The number will always be a positive integer greater than 0.
#Your function only needs to return the result, 
#what is shown between parentheses in the example below is how you reach that result and 
#it's not part of it, see the sample tests.

#ერთიდან numამდე რიცხვები უნდა შევკრიბოთ
def summation(num):#5 1+2+3+4
    sum=0 
    i=1
    while i<=num: # როცა გიწერია i<num, num-ამდე ატრიალებს და არა num-ის ჩათვლით
        print("i=",i )
        sum+=i
        print(sum)
        i+=1
    return(sum)

print("sum=",summation(8))    
#----------------------------------------------
#task6:
#Consider an array/list of sheep where some sheep may be missing from their place. 
#We need a function that counts the number of sheep present in the array (true means present).
def count_sheeps(sheep): #sheep=["true","true"]
    count_sheeps=0
    for i in range(len(sheep)):
        if sheep[i]==True:
            count_sheeps+=1
    return count_sheeps

array1 = [True,  True,  True,  False, True,  True,  True,  True ,
 True,  False, True,  False,True,  False, False, True ,True,  True,  True,  True,False, False, True,  True ]

print(count_sheeps(array1))

#or
def count_sheeps(sheep):
    my_sum=0
    for element in sheep:
        if element==True:
            my_sum+=1
    return my_sum
#-------------------------------------------------
#REVIEW
#1)index- ლისთის კონკრეტული ელმენტის ინდექსის დასადგენი მეთოდი
#syntax: listname.index(any element you want)
#example:
      # students=["giorgi","rati","salome","anri","demetre"]
# grades=[10,20,30,40,10]
# giorgis_index=students.index("giorgi") #ეს დაპრინტავს მერამდენე ინდექსზეა გიორგი,ანუ 0-ს.
# giorgis_grades=grades[giorgis_index]
# print(giorgis_index)
# print(giorgis_grades)
# print(giorgis_grades+10)  

#2)mathemtacial operations:
# my_name="elene"
# print(my_name*3)#we can multiply string and int
# print(my_name+3) #we can not sum string and int