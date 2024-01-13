#working on codewars's tasks
#task1:even or odd
def even_or_odd(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"

print("your number is :", even_or_odd(100))
#--------------------------------
#task2: transform a number(integeer) into a string
def number_to_string(num):
    return str(num)


print(number_to_string(15)) # არ აბრუნებს "15"-ს და რატომ??
#-------------------------------------------
#task3:vary simple.given an ineger or a floating-point number,find its opposite
def opposite(numebr):
    return  -1*numebr

print("your number's opposite is : ", opposite(-5))
#------------------------------------------
#task4:complete the solution so that it reverses the string passed into it.
def solution(string):#elene
    new_str = " "
    i = len(string) 
    while i>0:
        new_str += string[i-1]
        i-=1
    return new_str

#or

def solution(string):
    new_string = ""
    for i in range(len(string)):
        new_string += string[-i-1]
        i-=1
    return new_string

print(solution('elene'))
#------------------------------------------
#task5:in this ssigment you are given a number and have to make it megative
def make_negative(number):
    if number > 0:
        return -1*number
    return number

print(make_negative(-100))
#--------------------------------------
#task6:complete the method that takes a boolean value and return
# a "Yes" string for true.or "No" for flase.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    return "No"
    
print(bool_to_word(True))
#--------------------------------------
#task7: you get an array of numbers ,return the sum of all of the postivie ones
def positive_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            sum += arr[i]
    return sum

my_arr=[1,2,-3,-4,5,10,-10,-800]
print(positive_sum(my_arr))

#or

def positive_sum(arr):
    sum=0
    for element in arr:
        if element > 0 :
            sum+=element
    return sum

my_arr=[1,2,-3,-4,5,10,-10,-800]
print(positive_sum(my_arr))
