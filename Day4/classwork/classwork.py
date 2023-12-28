#lesson4: group 102

#exponentiation operator 
print(5**3) # 5*5*5 
print(5**4) #5*5*5*5
print(3**4)#3*3*3*3
#----------------------------------
#working on homework!
num1=int(input("enter num1: "))
num2=int(input("enter num1: "))
num3=int(input("enter num1: "))

#create incrementation variable
my_sum=0 # variable for summing odd numbers

#now,we have to realise if a number is odd or even
#our random numbers: 13,20,7
if num1%2==1:
   my_sum+=num1 #our variable will be increase with num1 (which is an odd)
if num2%2==1:
   my_sum+=num2
if num3%2==1:
   my_sum+=num3

print("the sum of odd numbers is :{}".format(my_sum))
#--------------------------------------
# For loop
my_name="elene"
 
for char in my_name: #char-iterative variable in here
    print(char)
#----------------------------
#how to find if the specific char is in other chars or not
print("e"in "elene")
#--------------------------
#workN1: ask user to enter 2 names and  print the name that will have more vowel.use format method for beautiful sentence

first_name=input("enter name pls: ")
second_name=input("enter name pls: ")

#find out if name has vowel or not 
char_counter1=0
char_counter2=0

if "a" in first_name:
        char_counter1+=1
if "e"in first_name:
    char_counter1+=1
if "i" in first_name:
    char_counter1+=1
if "o" in first_name:
    char_counter1+=1
if "u" in first_name:
    char_counter1+=1

print(char_counter1)
     
if "a" in  second_name:
    char_counter2+=1
if "e"in second_name:
    char_counter2+=1
if "i" in second_name:
    char_counter2+=1
if "o" in second_name:
    char_counter2+=1
if "u" in second_name:
    char_counter2+=1
print(char_counter2)

if char_counter1>char_counter2:
    print("the name {} has more vowel than{} name ".format(first_name,second_name))
if    char_counter2>char_counter1:
     print("the name {} has more vowel than {} name ".format(second_name,first_name))


# #another way:it is the best and more simple version!
name1=input("enter name pls :")
name2=input("enter name pls: ")
#incrementation variable
amount_of_vowels_in_name1=0
amount_of_vowels_in_name2=0

# #nika
for char in name1:
    if  char in "aeiou": #  we would use not in"aeiou", if we had asked about consonant
        amount_of_vowels_in_name1+=1 
# # what is happening here:
# #1) for loop will  check name "nika" forth time
# #2)each letter will be chacked: if letter "n" is in "aeiou", vowels' variable  will be increase with 1
# #3)if letter"i" is in "aeiou", vowels' variable  will be increase with 1
# #4)if letter "k" is in "aeiou", vowels' variable  will be increase with 1
# #4)if letter "a" is in "aeiou", vowels' variable  will be increase with 1
for char in name2:
    if char in "aeiou":
        amount_of_vowels_in_name2+=1

if amount_of_vowels_in_name1>amount_of_vowels_in_name2:
    print("the amount of vowels in name 1 is more and it contains {} vowels".format(amount_of_vowels_in_name1))
elif amount_of_vowels_in_name2>amount_of_vowels_in_name1:

    print("the amount of vowels in name2 is grater and it contains{} vowles".format(amount_of_vowels_in_name2))
else:
    print("they have equal amount of vowels")


#-------------------
# #elif-else if 
age1=10
age2=5

if age1>age2:
    print("1>2")
elif age2>age1: #same as if.when we want to check another statment 
    print("2>1")
else:
    print("age1=age2")
#-----------------------------
#workN2-enter a string and count "a" in there
string=input("enter the sentence pls: ")

#incrementation variable
amount_of_a_in_string=0
#i am elene      # == it meats if left variable is equal to wright variable
for char in string: # in 124 line,write operator ==,not in.
    if char=="a": # in "" - you have to write the char,that you are looking for 
        amount_of_a_in_string+=1

print("there are {} 'a' in your sentence ".format(amount_of_a_in_string))

#--------------------------------------
#print quote:

quote='"stay hungry,stay foolish"by steve jobs'
print(quote)
#or
print('"stay hungry,stay foolish" by steve jobs')
#----------------------------------------
# which one will be printed:

spam=7
if spam>5:
    print("five")
if spam>3:
    print("three")
# both will be printed

spam=7
if spam>5:
    print("five")
elif spam>3:
    print("three")
    
#only first, five, will be prined-because,if is main.if "if" wii work,than  "elif" does not metter at all.

#--------------------------------------------
#multifle "if"-s
#example1
num=12
if num>5:
    print("bigger than 5") 
    if num<=47:
        print("between 5 and 47")
# second if will be checked if first 'if'  works. 
#so,both will be printed

#example2    
#remember: if we have tabs beween "if"s, first "if" will be main
# if there is no space between "if"-s,then every "if" will be main
num=7
if num>3:
    print("3")
    if num<5:
        print("5")
        if num==7:
            print("7")
#first "if" will work because 7>3 and 3 will be printed.
#second 'if" will not work (7<5-false) 
#third "if" will not be even chacked!
#------------------------------------------
#review
#1)#exponentiation operator- print(5**4) the result will be : 5*5*5*5

#2)# For loop- e.g for char in sting1:
#                    if char in "aeiou"
#                       amount_of_vowels_in_name1+=1
#how does it work:using name "nika"
#1) for loop will  check name "nika" forth time
#2)each letter will be chacked: if letter "n" is in "aeiou", vowels' variable  will be increase with 1
#3)if letter"i" is in "aeiou", vowels' variable  will be increase with 1
#4)if letter "k" is in "aeiou", vowels' variable  will be increase with 1
#4)if letter "a" is in "aeiou", vowels' variable  will be increase with 1

#3)elif-else if (same as if.when we want to check another statment.it will wokr if first "if" will not work in specific situation)

#4)== operator- it meats: if left variable is equal to wright variable.
# e.g  for char in string: 
#          if char=="a": # in "" - you have to write the char,that you are looking for 
#         amount_of_a_in_string+=1

#5)#multifle "if"-s - second if will be checked if first 'if'  works.
#remember: if we have tabs beween "if"s, first "if" will be main
# if there is no space between "if"-s,then every "if" will be main