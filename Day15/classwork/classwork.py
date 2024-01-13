#group102:lesson12
#ლისთის ელემენტების და მისი ინდექსების ბეჭდვა
arr=["nika","luka","giorgi","iva","farna"]
# for i in range(len(arr)):
#     print(i,arr[i])
 
# #ფუნქცია enemurate,რომელსაც 2 არგუმენტი სჭირდება.
# #i-საიტერაციო ცვლადი item-ის ლისთი სადაც ვნომრავთ ელემენტებს
for i, item in enumerate(arr):
    print(i,item)
#--------------------------------
#working on homeworks
#Given a random non-negative number, you have to return 
#the digits of this number within an array in reverse order.
#35231 => [1,3,2,5,3]
#0 => [0]
def digitize(n):
    arr=[]
    for i in str(n): #გავსტრინგეთ
        arr.append(int(i)) #მერე გავაინტეჯერეთ
    arr.reverse()
    return arr
#---------------------------------
#working on codewars:
#task1:
#Given an array of integers, return a new array with each value doubled.
#For example:
#[1, 2, 3] --> [2, 4, 6]
def maps(a):
    new_arr=[]
    for i in range(len(a)):
        new_arr.append(a[i]*2)
    return new_arr

arr=[1,2,3]
print(maps(arr))
#----------------------------
#task2:
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# # patrick feeney => P.F
def abbrev_name(name): # Sam Harris => S.H
    new_str = ""
    for i in range(len(name)):
        if i == 0:
            new_str += name[i]
            new_str += "."
        elif name[i] == " ":
            name[i+1]
            new_str += name[i+1]
    return new_str.upper()
print(abbrev_name("sam Harris"))
#YEEEEEEEEES
#another way:
def abbrev_name(name): 
    name_arr = name.split() #
    print(name_arr[0][0]) #სიის მენულე ელემენის მენულე ელემენტი
    return name_arr[0][0].capitalize() + "." + name_arr[1][0].capitalize()
#სიის მენულე ელემენტის, მენულე სიმბოლო გავადიდოთ დავუმატოთ "." დავუმატოთ სიის ინდექსად 1 ელემენტის მენული სიმბოლო და გავვადიდოთ

print(abbrev_name("Sam Harris"))

#-------------------------
#split function-ამ ფუნქციის გამოყენებით გავწყვიტავთ სფეისებს და სიაში ჩაიყრება თითო სიტყვა ელემენტებად
my_str = "I love coding"
print(my_str.split())
#--------------------------
#task3:
# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
#['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]), 'found the needle at position 3')
def find_needle(haystack):
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            return "found the needle at position {}".format(i)
   
my_arr=['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print(find_needle(my_arr))
#--------------------------------------------
#თუ n არის კენტი, დაიპრინტოს weird
#თუ  n არის ლუწი და არის 2სა და 5ს შორის დაიპრინოტს not weird
#თუ n  არის ლუწი და არის 6სა და 20ს შორის დაიპრინოს wierd
#თუ n არის ლუწი და არის 20ზე მეტი, დაიპრინტოს not weird

#როცა ბევრი პირობაა დაიწყეთ ყველაზე დომინანტით
def check_num(n):
    if n % 2 == 0 and n > 20:
        print("not weird")
    elif n % 2 == 0 and (n <= 20 and  n >= 6):
        print("wierd")
    elif n % 2 == 0 and (n >= 2 and n <= 5):
        print("not weird")
    elif n % 2 == 1:
        print("weird")

check_num(15)
check_num(18)
check_num(20)
#----------------------------
#homework:+3 tasks in codewars