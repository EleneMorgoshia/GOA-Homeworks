#მოიფიქრეთ ამოცანა და ჩააგდეთ ჩათში 
#1)იპოვეთ ყველაზე პატარარიცხვი minფუქციის გამოყენები გარეშე-[7,5,2,20,652,6,3,62,9]
#2)ჩემი მოფიქრებული:შექმენით 
#მომხმარებელს მოსთხოვეთ საიტზე შემოსასვლელად შემოივანოს მისი იუზერი და პაროლი. თუ მისი პაროლი 8 სიმბოლოზე ნაკლებია,გამოუტანოს 
#"არასწორი პროლი" და "თუ დარეგისტრირებული არ ხართ,გთხოვთ დარეგისტრირდეთ "
#(რეგისტრაციის ფუქნციის დაწერასაც შეეცადე :))
#საიტზე შემოსვლისას მას დახვდება სია სხვადასხვ ინსტრუმენტების. მას
#საშუალება აქვს აირჩიოს სასურველი ინსტრუმენტების(როიალი,პიანინო,საქსაფონი,ფლეიტა,საყვირი,ქსილოფონი) სიიდან.
#ასევე შექმენით მეორე სია ,სადაც იქნება ფასები მოცემული ინსტრუმენტების და დაბეჭდეთ : როიალი ღირს- 1000ლ, პიანინო ღირს- 1200ლ ..ა.შ
# რადგან ახალი წელი მოდის, თითოეულ ინსტრუმენტზე არის 30 პროცენტიანი ფასდაკლება. ეს გამოიტანეთ ეკრანზე და დაბეჭდეთ ინსტრუმენტების ახალი ფასები
#დაწერეთ ზემოთ მოცემული კოდი)

#1)
my_arr=[7,5,2,20,652,6,3,62,9]
min=my_arr[0]
for i in range(len(my_arr)):
    if my_arr[i]<min:
        min=my_arr[i]
print(min)

#2)
#საიტზე შესვლის ფუნქცია
def long_in(user_name,password):
    if len(password)<8:
        print("Wrong password!if you don't have an  account,please create it ")
    else:
        print("You made it ")
   
def registration(name,last_name,birth_date):
     print("Your name is: {}".format(name))
     print("your lastname is: {}".format(last_name))
     print("Your birth date is: {}".format(birth_date))
     password=input("Enter a password. Password must contain more than 8 characters:")
     if len(password)<8:
       print("Password must contain more than 8 characters:")
     else:
         print("Your password is: {}".format(password))


user_name=input("Enter your name: ")
password=input("Enter you password: ")
print(long_in(user_name,password))

name="elene"
last_name="morgoshia"
birth_date=20
print(registration(name,last_name,birth_date))

instruments_arr=["როიალი","საქსაფონი","პიანინო","ფლეიტა","საყვირი","ქსილოფონი"]
price_arr=[10000,9990,1200,1500,900,1580]
for i in range(len(instruments_arr)):
    print("{}'s price is  {} lari ".format(instruments_arr[i],price_arr[i]))

discount_prices=[]
minus_thirty_percent=0
print("Discounted prices are:")
for j in range(len(price_arr)):
    minus_thirty_percent=price_arr[j]-((price_arr[j]*30)/100)
    discount_prices.append(minus_thirty_percent)
    print("{}'s price is {} lari".format(instruments_arr[j],discount_prices[j]))
print(discount_prices)