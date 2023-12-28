#group4:working on homeworks

#ბილეთი ღირს 25 ლარი,მაგრამ ბავშვებისტ ვის უფასოა
# #გვყავს 13 ადამიანი,აქედან 10 დიდი და 3 ბავშვი
# #გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ

amount_of_kids=0
amount_of_adults=0
total_cost=0
for i in range(3):
    age=int(input("Enter your age: "))
    if age>18:
        print("25 lari")
        amount_of_adults+=1
        total_cost+=25
        print("jamshi gadasaxdeli iqneba am etapze 10"+str(total_cost))
    elif age<=18 and age>0:
        print("it is free for you")
        amount_of_kids+=1
    else:
        print("are you a human?")
print("The total price will be "+str(amount_of_adults*25))
print("Amount of adults: {} , Amount of kids: {}".format(amount_of_adults,amount_of_kids))
print("sul iqneba:"+str(amount_of_kids+amount_of_adults))
#------------------------------------
#interesting case
foods=["kinkhali","mwvadi","xachapuri","xizilala"]
x_counter=0

for food in foods:
    for char in food:
     if char=="x": #თითოეული ასო,თითუეულ სიტყვაში, შეედარება x-ს.
        x_counter+=1
print(x_counter)
#მარტო პირველ ინდექსზე მდგომს რომ არ შეადაროს, ანუ მთლიან სიტყვაში თუ რის"x"
#მაშინ რომ მოემატოს сounter-ს ერთი
my_list=["nika","gabrieli","rati"]
for element in my_list:
    print(element)
   #როგორ მივწვდეთ თითოეულ ელემენტში,თითოეულ სიმბოლოს
    for char in element:
        print(char)
#--------------------------------------
