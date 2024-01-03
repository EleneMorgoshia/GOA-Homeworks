#group4
#working on homeworks
#1)მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თანხმოვნები
sentence=input("Enter your sentence: ")
consonants_counter=0
for char in sentence:
    if char not in "aeiouAEIOU":
        consonants_counter+=1
print("In this sentence consonants amount is: {}".format(consonants_counter))
#question1:აქ სფეისებსაც ითვლის და როგორ უდა გავაკეთოთ ისე,რომ სფეისები არ ჩათვალოს?

#2)შექმენით გოგონებისა და ბიჭების ლისთი და მომხმარებელს შემოატანინეთ მათი სახელები
# შემოტანილი სახელები ჩაყარეთ შესაბამის ლისთში
girl_list=[]
boy_list=[]

for i in range(4):
    girl_name=input("enter girls name:")
    boy_name=input("enter boys name: ")
    girl_list.append(girl_name)
    boy_list.append(boy_name)

#3)მოცცემული გვაქვს ლისთი, მეხუთე ინდექსად ჩაამატეთ რიცხვი 13 და შეკრიბეთ დადებითი რიცხვები
    
list=[21,3,11,31,7,34,-5]
list.insert(5,13)
sum_numbers=0

for i in list:
    if i>=0:
        sum_numbers+=1
print(list)
print(sum_numbers)
#----------------------------
#random

import random
#example1:
print(random.randint(1,100)) #რენდომად დაპრინტავს 1 დან 100 მდე რაიმე რიცხვს

#examle2:
my_students=["nika","gabrieli","dato","luka","sandro"]
print(my_students[random.randint(0,4)]) #აქ 0-იდან 4 ის ჩათვლით იგულისხმება
[random.randint[1,5]]#-ერთიდან ხუთამდე აირჩევს რენდომად რამე რიცხვი

#example3:
my_students=["nika","gabrieli","dato","luka","sandro"]
arr_of_cars=["BMW","MERCEDES","prius","subaru","porshe","bugati"]

for i in range(len(my_students)):
    winer=random.choice(my_students)
    lucky_car=random.choice(arr_of_cars)
    print(winer,"won the car:",lucky_car)
    my_students.remove(winer)
    arr_of_cars.remove(lucky_car)
# #----------------------------------
# სიიდან რენდომ არჩევნის დაპრინტვის გაიდლაინი
my_students=["nika","gabrieli","dato","luka","sandro"]
print(random.choice(my_students))
#-------------------------------
#group102:
# functions

def reverse_arr(any_arr):
    
    new_arr=[]
    i=len(any_arr)
    while i>0:
        new_arr.append(any_arr[i-1])
        i-=1
    print(new_arr)
#-----------------------------------------
#work1:
#შექმენით ფუნქცია,რომელსაც გადაეცემა 2 მოთამაშის ქულა
#დაპრინტეთ წინადადება "ამ მოთამაშეს უფრო მეტი ქულა აქვს ამდენით"

def compete(score1,score2): 
    if score2>score1:
        print("second player has {} more points ".format(score2-score1))
    elif score1==score2:
     print("Both players have same points and it is:{}".format(score1))
    else:
        print("first player has {} more points".format(score1-score2))

#or
def compare_scores(p1_player,p2_player):
    if p1_player>p2_player:
        print(" player who has {} points  has {} more points than the player who has {} points ".format(p1_player,p1_player-p2_player,p2_player))
    elif p2_player>p1_player:
        print(" player who has {}  points has {} more points  than the player who has {} points".format(p2_player,p2_player-p1_player,p1_player))
    else:
        print("Both players have same points")

#-----------------------------------------
#return
def multiply(a,b):
    return a*b
#-------------------------------------------------------------------------
#REVIEW
#1)Random- print(random.randint(1,100))
#sytnax- import random
#        random.randint(1,100) - ერთიდან 100 ის ჩათვლით ირჩევს რენდომ რიცხვს

#2)Return- ეკრანზე არ გამოაქვს,არამედ მეხსიერებაში ინახავს მნიშვნელობას
#example:
# def multiply(a,b):
#     return a*b
# print(multiply(10,20))


