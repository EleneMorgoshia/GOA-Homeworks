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
