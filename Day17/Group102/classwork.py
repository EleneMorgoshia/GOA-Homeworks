#group102 lesson14
#codewars
#-------------------------
#task1:
#This function determines if an array contains a specific element or not.
def check(seq, elem):# The function name is 'check' and it has two parameters(seq-araay, elem-element)
    for i in range(len(seq)): #for loop in the array
        if seq[i] == elem: #Check if the  element at index i (iteration variable) in the array  is equal to the elem(specific element)
            return True #if the statement above is true, return True
    return False#if the statemen in 8th line is not true, return False

print(check(["come", "on", 110, "2500", 10, '!', 7, 15], "Come")) #calling the function and passing 2 arguments

#or
def check(seq, elem): #The function  name is 'check' and it has 2 parameters(seq-array, elem-element)
    if elem in seq:#Check if the specific element(elem) is in array(seq) 
        return True #if statement below is true, return True
    else:
        return False #if the statement in 17th line is false, return False
#--------------------------------------
#taks2:
#This function determanies if a specific number is even or odd.
# Afer that the number will be multiplied by eigth if it is an even and by nine otherwise.

def simple_multiplication(number) :# the function name is 'simple_multiplication' and it has 1 parameter(number)
    if number % 2 == 0:  #Check if the number is even
        return number * 8    #if statement below is true, return number*8
    elif number % 2 == 1:    #check if the number is odd
        return number * 9   #if the statement below is true, return number*9
    
print(simple_multiplication(2)) #calling function and passing  2 as an argument 
#---------------------------
#task3:
#This function identifies how many bullets are needed for a specific amount of dragons.
#each dragon takes 2 bullets to be defeated.
def hero(bullets, dragons): # the function name is 'hero' and it has 2 parameters(bullets and dragons)
    if bullets >= dragons * 2 : #Check if the amount of bullets is grater than or equals to dragons * 2 
        return True # if the statement below is True, return True
    return False #if the statement in 37th line is False,return False. 
# # #------------------------------------
# #taks4:
#This function determines if a character in string is 'T' or not. if it's 'T', it will be replaced with  'U'.
def dna_to_rna(dna): #the function name is 'dna_to_rna' and it has 1 parameter(dna)
    rna = "" # created a new empty string named- rna
    for char in dna: #for loop in dna
        if char == 'T': #check if the char(character) in 'dna'(string) equals to 'T'
            rna += 'U' #if statement below is true, rna will be encreased with character 'U'
        else:
            rna += char# if statement in 48th line is false, rna will be encreased with char
    return rna #function returns rna varibale 

print(dna_to_rna("TTTT"))# calling function and passing 'TTTT'  as a parameter
# # #----------------------------------
#task5
# #This function calculates body mass index (bmi = weight / height^2).
# # if bmi <= 18.5 return "Underweight"
# # if bmi <= 25.0 return "Normal"
# # if bmi <= 30.0 return "Overweight"
# # if bmi > 30 return "Obese"
# #(bmi(50, 1.80), "Underweight")

def bmi(weight, height): #The function name is 'bmi' and it has 2 parameters(weight,height)
    bmi = weight / height ** 2 # created variable named-' bmi' which is equal to weight/height^2
    if bmi <= 18.5: #check if bmi is less than or eqauls to 18.5
        return "Underweight" #if statement below is true, return 'Underweight'
    elif bmi <= 25.0: #check if bmi is less than or equals to 25.5
        return "Normal"  #if statement in 65th line is true, return 'Normal'
    elif bmi <= 30.0: #check if bmi  is less than ot equals to 30.0
        return "Overweight"#if statement in 67th line is true, return 'Overweight'
    elif bmi > 30:#check if bmi is grater than 30
        return "Obese" #if statement in 69th line is true, return 'Obese'

print(bmi(50,1.80)) #calling function and passing two arguments
# #---------------------------------------
#task6:
#This function returns an array of integers from n to 1 where n>0.
def reverse_seq(n): #The function name is reverse_seq and it has one parameter(n)
    integers_array = [] # created empty list named- integers_array
    i= n #iteration variabel equals to n
    while i > 0: #while loop 
        integers_array.append(i) #iteration variable will be added in integers_array.
        i-=1 #interation variable decrease with 1
    return integers_array#function returns integers_array

print(reverse_seq(10)) #calling function and passing 10 as an argument
# #------------------------------------------
# #kahoot
# #1)ფოლდერი- green - (ყველაფერს) git add . 
# #2)folder- green - (metadata)
# #3)ფაილის და ფოლდერის-red+
# #4)*********
# #5)what??  არაფერი - (none)
# #6)6111-green+
# #7)ერთნაირებია red+
# #8)green- (error)
# #9)green+
# #10)4-blue +
# #11)82121-blue+
# #12)green+
# #13)error-green+
# #14)true-blue+
# #-----------------------------------------
# lesson15
# working on ccodewars
#task1:
#Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
#This function defines the multiplication of the integers from a list. 
def grow(arr):# The function name is grow and has 1 parameter-'arr'
    result = 1 #created variable named- 'result'. it is equal to 1
    for i in range(len(arr)): #for loop in the list of integers
        result *=  arr[i] #result will be multiplied  by the number at index i(iteration variable) in the list
    return result #The function will return the value of the 'result'

print(grow([1,2,3,4]))#calling the function and passing 1 argument
    
# #---------------------------------
#task2:
#This function  takes an array of words and smashes them together into a sentence and returns the sentence.
#['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
#'hello world ' should equal 'hello world'
def smash(words):
    string_for_the_sentence = ''
    for i in range(len(words)):
        string_for_the_sentence += words[i]
        string_for_the_sentence += ' '
    return string_for_the_sentence
       
    
print(smash(['hello', 'world', 'this', 'is', 'great']))
#როგორ კეთდება join-ის გარეშე?ეს არასწორია. 
#better version
def smash(words): #The function name is-smash and it has 1 parameter- words
    result = " ".join(words) #The variable result equals to the value of the  joined words with space from the list
    return result #this function return the value of the result
       
print(smash(['hello', 'world', 'this', 'is', 'great'])) #calling the fanction and passing 1 argument
# #------------------------------------
#task3:
#This function splits a string and convert it into an array of words
def string_to_array(s): #The function name is -'string-to_array' and it has 1 parameter - 's'
    if len(s) == 0: #Check if the length of the array equals to 0
        return ['']# if the statement below is true, return an empty list
    return  s.split() #The function returns the list of the splited words from the string

print(string_to_array("hello world")) #Calling the function and passing 1 argument
# #----------------------------------
#task4:
#This function takes two arguments that will return an array of the first n multiples of x.
def count_by(x, n): #the function name is 'count-by' and it has 2 parameters- x,n
    result_arr = [] #created the empty list named- result_arr
    i=1 #iteration variable equals to 1
    while i <= n: #while loop in n
        result_arr.append(x*i)  #The list named-'result_arr' will be added by elements at index (x*i). 
        i+=1 #iteration varible encreases by 1
    return result_arr #the function return the 'result_arr'

print(count_by(100,5)) #Calling the function and passing 2 arguments
#-------------------------------
#group 102
#lesson 16 
#create the funtion that returns the  joined elements from a list 
#Do not use function join
def my_join(arr): #The function name is my_join and it has 1 parameter- arr
    new_str = '' #created empty string named-'new_str'
    for i in range(len(arr)):#for loop in the arr
        new_str += str(arr[i]) #'new_str' will be encreased by the string form of the element at index i(iteration variable) in the 'arr'
    return new_str #The function return the 'new_str'

print(my_join([5,6,4,3]))#calling the function and passing 1 argument

#or
def my_join(any_arr):
    final_str = ''
    for element in any_arr:
        final_str += str(element)
    return final_str

print(my_join([5,6,4,3]))
#---------------------------------
#working on homowork
#task1: reversed words
def reverse_words(s): #the function name is 'reverse_words' and it has 1 parameter -'s'
    x = s.split() #created variable that equals to splited string
    x.reverse() # used function reverse for revsing the list
    final_str = "" #created the empty list
    for element in x: #for loop in the reversed array
        final_str += element + " " # final-str will be encreased by the element in the array + space
    
    return final_str[:-1] #the function returns the value of the  'final_str' without the last character

print(reverse_words("hello world!"))  #calling the function and passing 1 arguments
#------------------------------------
#kahoot
#1)error -yellow -(არცერთი პასუხი არ არის სწორი)
#2)14 "14"- red - (14 14)
#3) error- green +
#4)551-red -(არცერთი პასხი არ არის სწორი)
#5)blue +
#6)არცერთი +
#7)red - (yellow)
#8)error- green+
#9)error- yellow - (none)
