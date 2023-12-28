#group 4:sololearn-conditional statment)+
#2)ask user to enter his/her age and his/her father's age
#print each year how how much greater will the father be compared to the son?
#3)print every odds and evens from 0 to 30. and write wich one is odd and which one is even.

son_age=int(input("Enter your age: "))
father_age=int(input("Enter your father's age: "))
year_variable=int(input("Enter year"))
#son_age=10 , father_age=20
for i in range(5): 
    print("son's age:{}, father's age:{} ".format(son_age,father_age))
    print(" father is  "+ str((father_age+i)/(son_age+i)) + " "+ " -times grater than his son" + " "+ "in" + " " +  str(year_variable)+" year")
    year_variable+=1
    father_age+=1  
    son_age+=1


# homework3:
for i in range(0,30):
    if i%2==1:
        print("Number {} is odd ".format(i))
    elif i%2==0:
        print("Number {} is even".format(i))



# #group102:ask user to enter his/her name and print the letters indexes that are  vowel.
user_name=input("Enter your name: ")
# print(len(user_name))

for j in  range(len(user_name)):
        #user_name[j]-letter print(j)- index
         if user_name[j] in "aeiou":
                print("the leter"+ " "+ str(user_name[j])+" "+" is on" +" "+ str(j)+ " "+"index and it is vowel!")
