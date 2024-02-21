#lowercase letter becomes uppercase and each uppercase letter becomes lowercase. 

def to_alternating_case(string): #the function name is 'to_alternating_case' and it has 1 parameter- string
    result_str = '' #created an empty variable called - 'result_str' 
    i = 0 #created an iteration variable that equals to 0
    while i < len(string): #while loop in the string
        if string[i].isupper(): # Check if the character at index i in the string is an uppercase letter
            result_str += string[i].lower() # if the statement in the 7th line is true, result_str will be 
            #encreased with the lowered element at index i (iteration variable)
        else:
            result_str += string[i].upper() #if the statement in the 7th line is false, result_str will be
            #encreased with the uppered element at index i (iteration variable) 
        i += 1 #iteration variable will be encreased with 1
    return result_str #the function returns the value of 'result_str'

print(to_alternating_case("HELLO world")) #calling the function and passing 1 argument  

