#This function removes all the exclamation marks from a given string

def remove_exclamation_marks(s): #The function name is "remove_exclamation_marks" and it has 1 parameter - s
    new_str = '' #Created a variable called - 'new_str'
    for i in range(len(s)): # For loop in the given string
        if s[i] == "!": # Check if the element at index i (iteration variable) equals to   an exclamation mark
            new_str = s.replace("!",'') #If the statement in the 6th line is true, the  'new_str' will  remove all the exclamation marks in the given string using a replace method .
            return new_str #if the statement in 7th line is True,the function returns 'new_str'
    return s #if the statement in 7th line is Flase,the function  returns 's'

print(remove_exclamation_marks("Hi Hello")) #Calling the function and passing 1 argument

#OR

def remove_exclamation_marks(s):
    new_str =''
    return  new_str.replace("!",'')