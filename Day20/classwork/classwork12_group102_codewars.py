#this function return a string in which each character(case-sensitive) is repeated once.

def double_char(s): #the function name is 'double_char' and it has 1 parameter - s 
    char_arr = [] #created an empty array called - char_arr  
    for i in range(len(s)): #for loop in the s 
        char_arr.append(s[i]*2) # doubling each caracter in the string 's' and appending the result in to the 'cahr_arr'
    print(char_arr) #printing the 'char_arr'
    new_str = "".join(char_arr) #created the variable called new_str that equals to the string of joined elements from the list -'char_arr'
    print(new_str) #printing the 'new_str'

print(double_char("String")) #calling the function and passing 1 argument

#or
def double_char(s):
    new_s = ""
    for char in s:
        new_s += char * 2
    return new_s