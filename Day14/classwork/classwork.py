#group102:lesson11

my_str="nika 11 keshelava"
print(my_str.index("k")) #გამოიტანს იმ ინდექსის ნომერს,რომელზედაც არის პირველი k
print(my_str.count("k")) #გამოიტანს 2-ს , იმიტომ რომ ორი ცალი kარის სტრინგში

#უმაგრესი ამოცანა
#შექმენით ფუნქცია,რომელსაც გადავცემთ სიმბოლოს(ასოს)
#და დააბრუნებს იმ ინდექს,რომელ ინდექსზეც არის ის. 

def find_index_of_chars(any_str, any_char): #რამე სტრინგი, რამე სიმბოლო
    arr_of_indexes=[]
    i=0
    while i<len(any_str): #nika keshelava python
        if any_str[i]== any_char:
            arr_of_indexes.append(i)
        i += 1
    print(any_char, "gvxvdeva" ,arr_of_indexes,"adgilebze")

print(find_index_of_chars("nika keshelava python","n"))    
print(find_index_of_chars("nika keshelava beta version nice","n"))
#--------------------------------------------------------
#working on codewars
#task1:We need a function that can transform a string into a number. What ways of achieving this do you know?
def string_to_number(s):
    print(int(s))
#------------------------------------------------------
#task2:
# Make a function that will return a greeting statement that uses an input; 
# your program should return, "Hello, <name> how are you doing today?".
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

print(greet("Ryan"))
#--------------------------------------------------------
#task3:
#Your task is to create a function that does four basic mathematical operations.
#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1/value2
    
#მეორე გზა. eval  არ გვისწავლია ჯერ ოღონდ
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

print(basic_op("+",1,1))

#---------------------------------------
#task4
#The first century spans from the year 1 up to and including the year 100,
# the second century - from the year 101 up to and including the year 200, etc.
def century(year):
    if year % 100 == 0: 
        return year/100 #მაგ:1800-ის ქეისი, 1800/100=18
    else:
        return year//100 + 1 #მაგ: 1708-ის ქეისი, 1708//100+1=18

print(century(1800))
print(century(1708))
#----------------------------------------------------
#task5:
#Convert number to reversed array of digits
#Given a random non-negative number, you have to return 
#the digits of this number within an array in reverse order.
#35231 => [1,3,2,5,3]
#0 => [0]
def digitize(n):
    str_number=str(n) #"195"
    my_arr=[]
    for number in str_number:
        int_number=int(number)
        my_arr.append(int_number)
    my_arr.sort() #ზრდის მიხედვით დალაგება
    my_arr.reverse() #უკუღმა დალაგება
    return my_arr

print(digitize(195))