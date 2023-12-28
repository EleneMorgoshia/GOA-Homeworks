#group102
#homwwork:print sentences like that : 
# xinkali's price is 2 lari
#mwvadi's price is 20 lari

food_list=["xinkali","mwvadi","lobiani","qababi","khatchapuri","wyali"]
price_list=[2,20,15,10,15,2]

for i in range(len(food_list)):
    print(str(food_list[i])+"'s price is "+ str((price_list[i]))+" "+ "lari")
#------------------------------------
#group4:#homework3-module 4 quize]+
#homework1:
#მომხმარებელს შეეკითხეთ ხელფასი
#თუუ 10000ზე მეტია,დაუპრინტეთ, გოა-ში სწავლობდი?
#თუ 1000-10000 ის,დაუპრინეთ you mid
#თუ 1000 ზე დაბალია,დაუპრინტეთ,შემოსულიყავი გოაში,მატრიცელო

income=int(input("enter your income: "))

if income>10000:
   print("Did you study in GOA?")
elif income>1000 and income<10000:
   print("you are mid")
else:
   print("you should have joined in GOA")
#--------------------------
#homework2:იმუშავეთ floatებში!
# მომხმარებლის ნიშნებისგან გამოიანგარიშება საშვალო არითმეიკული და
# თუ ცხრაზე მეტი იქნება დაუპრინტეთ გილოცავ მატრიცელო შენ გამოგეცემა
# 300 ლარიანი ბანძი ოსტერი,რასაც შეალიე შენი ცხოვრება
#თუ იქნება 5ზე ნაკლები დაუპრინტეთ,გილოცვ გაექეცი მატრიცას
#თ იქნება 5 იდან 9მდე დაუპრინტე you are mid
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე :there is something wrong with you
grade1=int(input("Enter your grade"))
grade2=int(input("Enter your grade"))
grade3=int(input("Enter your grade"))
grade4=int(input("Enter your grade"))
grade5=int(input("Enter your grade"))

average=(grade1+grade2+grade3+grade4+grade5)/5

if average>9 and average<=10:
    print(average)
    print("გილოცავ მატრიცელო შენ გადმოგეცემა 300 ლარიანი ბანძი ტოსტერი,რასაც შეალიე შენი ცხოვრება")
elif average<5 and average>0:
   print(average)
   print("გილოცავ გაექეცი მატრიცას")
elif average>5 and average<9:
    print(" you are mid")
else:
    print(average)
    print("something wrong with you")

#FINALLYYYYYYY