#task1:
#This funcion counts how many times a character appears in the string
def str_count(str,char): #we defined a function named-str_count
                        #and we created two parameters
    list=[] #we created an empty list
    list.append(char)#we appended the value of variable 'char' in our list
    for i in str:# we did for loop in our string
        if char == i: #we check if our variable 'char' equals to iteration variable i 
            list.append(i) #if the statement above is true, we append our iteration variable in the list
    return len(list)-1 #this funcion returns integer(calculates length of the list and subtracts one )

print(str_count("hello","l")) # we call the function and pass two arguments

#better code
def str_count_chad(str,my_char): #we defined function called- str_count_chad. and we created two parameters
    counter = 0 #we created variable which equals to 0 
    for char in str: #we did  a for loop for our string
        if char == my_char: #we check if 'my_char' equals to iteration variable 'char'
            counter += 1    # if the statemet above is true, counter encreases with 1 
    return counter #this function returns integer ( counter)

print(str_count_chad("hello",'l')) # we call this function and pass two arguments



