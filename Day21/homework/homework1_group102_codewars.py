#the function determines  whether the string is ALL CAPS.


def is_uppercase(inp): #the function name is 'is_uppercase' and it has 1 parameter - inp
    for i in range(len(inp)): #for loop in the 'inp'
        if inp[i]  in  'abcdefjhijqlmnopqrstuvwxyz': #check if the element at index i (iteration variable) is in the 'abcdefjhijqlmnopqrstuvwxyz'
            return False #if the statement in the 6th line is true, return false
    return True #if the statement in the 6th line is false, return true
    
print(is_uppercase('$%^')) #calling the function and passing 1 argument

#or
def is_uppercase(inp):
    return inp == inp.upper()

print(is_uppercase('$%^'))
