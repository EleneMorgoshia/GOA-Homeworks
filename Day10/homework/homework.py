#group4:homework
# 1)შექმენით 10 მათემატიკური შეკითხვა მომხარებლისთვის
#ყოველი პასუხის შემთხვევაში ეწერებოდეს სწორია თუ არა. 
#თუ ტესტის დასრულებისს შემდეგ 10 ივე შეკითხვა ჭეშმარიტი იქნება,დაუპრინტეთ:"შენ აშკარად გოაში სწავლობდი ძმაო"
#თუ 1 მაინც იქნება არასწორი დაუპრინოტს:"კიდევ სცადეთ, ან შემოდით GOAში,გოაელს არ ეკადრება"

task1=int(input("answer the question:(100+200)*3="))
if task1==100:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task2=int(input("answer the qusetion: 80%2= "))
if task2==40:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task3=int(input("answer the qusetion: 40*4= "))
if task3==10:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task4=int(input("answer the qusetion: 80*2= "))
if task4==40:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task5=int(input("answer the qusetion: 100+600 = "))
if task5==700:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task6=int(input("answer the qusetion: 80*2*2= "))
if task6==20:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task7=int(input("answer the qusetion: random.randint(1,100)/10= "))
if task7==9:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task8=int(input("answer the qusetion: 20/4= "))
if task8==5:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task9=int(input("answer the qusetion: 4*4= "))
if task9==1:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

task10=int(input("answer the qusetion: 20*2= "))
if task10==10:
    print("your answer is correct")
else:
    print("your answer is incorect.Try again")

if task1==100 and task2==40 and task3==10 and task4==40 and task5==700 and task6==20 and task7==9 and task8==5 and task9==1 and task10==10:
    print("შენ აშკარად გოაში სწავლობდი ძმაო")
else:
    print("კიდევ სცადეთ, ან შემოდით GOAში,გოაელს არ ეკადრება")


#შეკითხვა- ამ ამოცანის სხვანაირი ამოხსნა მინდა. ეს ცუდია.(სულ ქვემოთ)
#-----------------------------------------------------------------

#2)დაწერეთ პროგრამა,რომელიც რენდომად გამოიძახებს ჯგუფის რომელიმე წევრს
#თუ მან შეკითხვაზე პასუხი სწორად გასცა მოემატოს 10  ქულა, ამოვარდეს სიიდან
#თუ არადა დააკლდეს 5 ქულა
#იყოს5 სტდენტი და ქულების სია 

#მინიშნება:  answer=input("did the student answer corectlt: ")
         #       if answer=="yes":
#                       moematos 5 qula
#                if answer=="no":
#                    moakldes 5 qula
import random
students=["nino","anastasia","pavle","rati","giorgi"]
scores=[100,200,300,400,500]
for i in range(len(students)):
    for j in range(len(scores)):
       x=random.choice(students)
       print(x)
       answer=input("Did student answer correctly?")
       if answer=="Yes":
        print("your answer is correcct. Member {} will be given 10 points. Your total score is: {} ".format(x,scores[j]+10))
        students.remove(x)
       elif answer=="No":
        print("Your answer is incorrect. Member {} losted 5 points. Your total score is: {} ".format(x,scores[j]-5))

#რენდომად ამორჩეულ სტუდენტს თავისი ქულა როგორ უნდა მოემატოს ან მოაკლდეს??
#------------------------------------------------------         
#3)შექმენით random password generator პროგრამა ,რომელშიც
#დაგენერირდება პაროლი,8 სიმბოლოინი,სადაც  2 ცალი სიმბოლოები იქნება !#*%(^)
# 2 სიმბოლო იქნება აბგდევზეთიკლმნეოოპჟრ(ასოები),4 სიმბოლო იქნება ციფრები
#ჯამში უნდა გამოვუდეს მაგ:!n8391k"

password=input("Enter your password: ")
for i in range (len(password)):
  if len(password)<8:
   print("Password must conatin 8 character")
  elif password[i]!="!" or password[i]!="#" or password[i]!="*" or password[i]!="%" or password[i]!="(" or password[i]!="^" or password[i]!=")":
    print("Password must contain  2 symbols from :!#*%(^)  ")

#მთლიანად როგორ უნდა აღიქვას.ანუ მთლიან სემოტანილ აროლში რომელიმე 2 მაინც თუ არის !#*%(^)  სიმბოლო..... (day10 ფოლდერში ნახე)
#-------------------------------------------
#4)turtle-თი რენდომ რიცხვებით დახაზეთ შედევრო
# forward(random.randint(100))
    
from turtle import*

import random
speed(3)
width(5)
color("black")
begin_fill()
forward(random.randint(1,100))
left(random.randint(1,100))
forward(random.randint(1,100))
left(random.randint(1,100))
forward(random.randint(1,100))
left(random.randint(1,100))
forward(random.randint(1,100))
end_fill()

penup()
goto(150,150)
pendown()
right(random.randint(1,100))
color("red")
begin_fill()
forward(random.randint(1,100))
left(random.randint(1,100))
forward(random.randint(1,100))
end_fill()

penup()
goto(60,0)
pendown()
left(random.randint(1,100))
color("blue")
begin_fill()
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
end_fill()

penup()
goto(20,120)
pendown()
left(random.randint(1,100))
begin_fill()
color("brown")
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
end_fill()

penup()
goto(20,105)
pendown()
right(random.randint(1,100)) 
color("black")
forward(random.randint(1,100))

penup()
goto(35,90)
pendown()
left(random.randint(1,100))
color("black")
forward(random.randint(1,100))


penup()
goto(110,120)
pendown()
right(random.randint(1,100))
begin_fill()
color("brown")
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
right(random.randint(1,100))
forward(random.randint(1,100))
end_fill()

penup()
goto(110,105)
pendown()
right(random.randint(1,100))
color("black")
forward(random.randint(1,100))

penup()
goto(125,90)
pendown()
left(random.randint(1,1000))
color("black")
forward(random.randint(1,1000))

exitonclick()
#----------------------
#group 102
#1)Codewars- reversed string,sum of positives,convert boolean values to string 'yes' or 'no'

#QUESTION
#1)მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თანხმოვნები
sentence=input("Enter your sentence: ")
consonants_counter=0
for char in sentence:
    if char not in "aeiouAEIOU" and char!=" ":
        consonants_counter+=1
print("In this sentence consonants amount is: {}".format(consonants_counter))
#question1:აქ სფეისებსაც ითვლის და როგორ უდა გავაკეთოთ ისე,რომ სფეისები არ ჩათვალოს?   
#------------------------
#ეს არის სულ პირველი ამოცანის უფრო კარგი ამოხნსა(არ გაგვივლია ეს ოღონდ)
def check_answer(question, correct_answer):
    answer = int(input(question))
    if answer == correct_answer:
        print("Your answer is correct.")
    else:
        print("Your answer is incorrect. Try again.")

questions = [
    ("Answer the question: (100+200)*3 = ", 900),
    ("Answer the question: 80%2 = ", 0),
    ("Answer the question: 40*4 = ", 160),
    ("Answer the question: 80*2 = ", 160),
    ("Answer the question: 100+600 = ", 700),
    ("Answer the question: 80*2*2 = ", 320),
    ("Answer the question: random.randint(1,100)/10 = ", 10),
    ("Answer the question: 20/4 = ", 5),
    ("Answer the question: 4*4 = ", 16),
    ("Answer the question: 20*2 = ", 40)
]

correct_answers = 0

for question, correct_answer in questions:
    check_answer(question, correct_answer)
    if answer == correct_answer:
        correct_answers += 1

if correct_answers == len(questions):
    print("შენ აშკარად გოაში სწავლობდი ძმაო")
else:
    print("კიდევ სცადეთ, ან შემოდით GOAში,გოაელს არ ეკადრება")