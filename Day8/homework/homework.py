#group4:homework
#1)შექმენით სია და ამ სიაში ჩაწერეთ სხვადახვა რიცხვები და
#გამოიტანეთ ამ სიაში ყველა რიცხვების ჯამი.აქვე
#ამ სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალკე ცლკე 
#ლუწია თუ კენტი

numbers_arr=[10,20,30,40,80,90,11,19,33,99]
sum=0
i=0
while i<len(numbers_arr):
    sum+=numbers_arr[i]
    if numbers_arr[i]%2==0:
        print("number {} is even ".format(numbers_arr[i]))
    elif numbers_arr[i]%2==1:
        print("number {} is odd".format(numbers_arr[i]))
    i+=1
print("sum of the numbers is: {}".format(sum))
#----------------------------------
#2)შექმენიტ სია.ამ სიაში ჩაწერეთ სხვადასხვა ციფრები(1,2,3, ასე არა, ასე:45,33,87,55)
#და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი
#ასევე ამ სიიდან უნა დაპრინტოთ ყველ რიცხვი ცალ-ცალკე და მიუწეროთ ლუწია თუ  კენტი

numbers_list=[]
numbers_list.append(22)
numbers_list.append(99)
numbers_list.append(20)
numbers_list.append(11)
numbers_list.append(10)
print(numbers_list)
sum=0
i=0
while i<len(numbers_list):
    sum+=numbers_list[i]
    if numbers_list[i]%2==0:
       print("the number {} is even".format(numbers_list[i]))
    elif numbers_list[i]%2==1:
        print("the number {} is odd".format(numbers_list[i]))
    i+=1
print("sum of the list numbers is: {}".format(sum))
# #----------------------------------
# #3)ბილეთი ღირს 25 ლარი,მაგრამ ბავშვებისტ ვის უფასოა
# #გვყავს 13 ადამიანი,აქედან 10 დიდი და 3 ბავშვი
# #გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ

viewers_list=[]
price=0
for i in range(10):
    age=int(input("Enter your age: "))
    if age>18:
     print("you have to pay 25 lari:)")
     price+=25
     viewers_list.append(age)
    else :
        print("we can't give you tickets.Pls move in children's tickets bar")
        changed_age=int(input("Enter your age pls: "))
        price+=25
        viewers_list.append(age)
    
  
print(viewers_list)

for j in range(3):
    ages=int(input("Enter your age: "))
    if ages<18:
     print("tickets are free for you")
     viewers_list.append(ages)
    if ages>18:
        print("You are not a child.You have to pay for your ticket")
        changed_ages=int(input("Enter you age pls: "))
        print("tickets are free for you")
        viewers_list.append(ages)
        
print(viewers_list)
print(price)

# #or
my_list=[10,11,12,18,19,20,40,48,49,46,47,45,47]
whole_price=0
i=0
while i<len(my_list):
    if my_list[i]>18:
        whole_price+=25
    i+=1

print(whole_price)
#------------------------  
#4)მომხმარებელს შემოატანინე სახელი, და
#დაპრინტეთ ეს სახელი იმდენჯერ,რამდენი ასოც არის ამ სახელში

user_name=input("Enter your name: ")
for i in range(len(user_name)):
    print(user_name)
#-----------------------------
#5)GOAში ყოველ შემოყვანილ ადამიანზე გეძლევა 100ლ
#მომხმარებელს შემოატანინეთ თუ რამდენი ადამიანი შმეოიყვანა
#ხოლო თითო შემოყვანილ ადამიანზე  დაერიცხოს 100ლ
#1)რამდენი დაერიცხა თუ შემოიყვან 10 ბავშვს,15 ბავშვს
#2)რამდენი დაგერიცხ თუ შმეოიუვან 100 ბავშვს გამოლებული 37 დამატებული13 გაყოფილი 10
#და გამრავლებული 264ზე

counter=int(input("How many people have you invited to join in GOA?"))
user_bank_account=0
for i in range(counter):
    user_bank_account+=100
print("Congratulation, you will be give {} lari:".format(user_bank_account))

# #1)თუ 10-ს შემოიყვანს- 1000ლ
#2)თუ 15-ს შემოიყვანს -1500ლ
#3)100 ბავშვს გამოლებული 37 დამატებული13 გაყოფილი 10
#და გამრავლებული 264ზე.
print(100*(100-37+13)/10*264) 


#---------------------------
#6)დაპრინტეთ "hello world",ოღონდ ასე არა:print("hello world")
string1="hello"
string2="world"
print(string1+" "+string2)
print("{}  {}".format(string1,string2))
# #--------------------------------
#group102:ისწავლეთ ყველაფერი კარგად და წინა გაკვეთილის ამოცანები ფუნქციებით გააკეთეთ

#homework:1)scores=[20,43,56,73,10,6,87,45,97] სორტის გამოყენების გარეშე დააბრუნეთ ყველაზე დიდი რიცხვი.
#2)students=["nika","ana","mamuka","iva","farna"] შეატრიალეთ უკუღმა sort  და reverse მეთოდის გარეშე.


#ამოცანა ნ1:
def max_score(my_arr):
    print("The highset score in the list is:{}".format(max(my_arr)))

scores=[20,43,56,73,10,6,87,45,97]
max_score(scores)


#ამოცანა ნ2:
def fun_name(my_arr,new_arr):
    i=len(my_arr)
    while i>0:
        new_arr.append(students[i-1])
        i-=1
    print(new_arr)
students=["nika","ana","mamuka","iva","farna"]
new_list_of_students=[]
print(fun_name(students,new_list_of_students))
