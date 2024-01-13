# #group4:
# #working on Codewars' tasks
# #--------------------------
# #task1:
# #This funcion counts how many times a character appears in the string
def str_count(str,char): #we defined a function named-str_count
                        #and we created two parameters
    list=[] #we created an empty list
    list.append(char)#we appended the value of variable 'char' in our list
    for i in str:# we did for loop in our string
        if char == i: #we check if our variable 'char' equals to iteration variable i 
            list.append(i) #if the statement above is true, we append our iteration variable in the list
    return len(list)-1 #this funcion returns integer(calculates length of the list and subtracts one )

print(str_count("hello","l")) # we call the function and pass two arguments

# #better code
def str_count_chad(str,my_char): #we defined function called- str_count_chad. and we created two parameters
    counter = 0 #we created variable which equals to 0 
    for char in str: #we did  a for loop for our string
        if char == my_char: #we check if 'my_char' equals to iteration variable 'char'
            counter += 1    # if the statemet above is true, counter encreases with 1 
    return counter #this function returns integer ( counter)

print(str_count_chad("hello",'l')) # we call this function and pass two arguments
#-------------------------------------
#task2:
#This function counts sheeps in the list . (True means present)
def count_sheeps(sheep):# we defined function named-count_sheeps.
                       # and crete one parameter 'sheep'(list)
    amount_of_sheeps= 0 #we created variable named- amount_of_sheeps. It equals to 0
    for i in range(len(sheep)): #we did a for loop in list(sheep)
        if sheep[i] == True:#we check if a list element equals to True
            amount_of_sheeps+= 1 #if the statement above is true, amount_of_sheeps will be encreased with 1
    return "There are {} sheeps in total".format(amount_of_sheeps) #function returns integer value(amount_of_sheeps)
    
my_arr=[True,True,False,True] #we created list
print(count_sheeps(my_arr)) # we called this function and pass our list(my_arr) as an argument 
#-----------------------------
#group102
#working on homeworks:
#task1
#Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time 
#since midnight in milliseconds.
# test.assert_equals(past(0,1,1),61000)
# test.assert_equals(past(1,1,1),3661000)
#test.assert_equals(past(0,0,0),0)
def past(h, m, s):
    return (h*3600 + m*60 + s)*1000
#------------------------------
#task2:
#Given an array of integers.
#Return an array, where the first element is the count of positives numbers and 
#the second element is sum of negative numbers. 
#0 is neither positive nor negative.
#If the input is an empty array or is null, return an empty array.
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    if len(arr) == 0: #თუ სიის სიგრძე უდრის ნულს,ანუ ცარიელია და არ გვაქვს ცარიელი ელემენტები
        return arr
    amount_of_positives = 0
    sum_of_negatives = 0
    for element in arr:
        if element > 0:
            amount_of_positives += 1
        elif element < 0:
            sum_of_negatives += element
    return [amount_of_positives,sum_of_negatives]
    

my_arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(my_arr))
#------------------------------------------
#task3
#Your classmates asked you to copy some paperwork for them.
#You know that there are 'n' classmates and the paperwork has 'm' pages.
#Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
def paperwork(n, m): #n-classmates m-pages
    if n <= 0 or m <= 0:
        return 0
    elif n>0 and m>0:
        return n*m
#---------------------------
#new codewars' tasks
#task1:
#divisible-გაყოფადი
#Create a function that checks if a number n is divisible 
#by two numbers x AND y. 
#All inputs are positive, non-zero numbers.
#n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
    
print(is_divisible(8,3,4))

#or
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    return False 
#-------------------------------
#task2
#Timmy & Sarah think they are in love, but around where 
#they live, they will only know once they pick a flower each. 
#If one of the flowers has an even number of petals and 
#the other has an odd number of petals it means they 
#are in love.
#Write a function that will take the number of petals of
# each flower and return true if they are in love and false
# if they aren't.
#example:lovefunc(1,4), True
def lovefunc( flower1, flower2 ): 
    if (flower1 % 2 == 0 and flower2 % 2 == 1) or (flower1 % 2 == 1 and flower2 % 2 == 0):
        return True
    return False

print(lovefunc(0,0))
#------------------------------------
#task3
#Write a function that takes an array of numbers and 
#returns the sum of the numbers.
# The numbers can be negative or non-integer. 
#If the array does not contain any numbers then you
# should return 0.
#[1.1, 2.2, 3.3]
def sum_array(a):
    if len(a) == 0: #if the array doesnot contain any numbers (empty list)
        return 0
    sum_of_the_numbers = 0
    for i in range(len(a)):
        sum_of_the_numbers += a[i]
    return sum_of_the_numbers

print(sum_array([]))

#or, better way
def sum_array(a):
    if len(a)==0:
        return 0
    return sum(a)

print(sum_array([]))
#----------------------------------------------
#task4:

