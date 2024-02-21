#This function gives a personalized greeting. it takes 2 parameters - name and owner
#if name equals to owner , the function returns "Hello boss" otherwise "hello guest"
# greet('Daniel', 'Daniel'), 'Hello boss'
def greet(name, owner):#the functio name is 'greet' and it has 2 parameters - name , owner
    if name == owner: # Check if the variable name equals to the variable owner
        return "Hello boss" #if the statement below is true, return "Hello boss"
    return "Hello guest" # if the statement in 6th line is false, return "Hello guest"

print(greet('Greg', 'Daniel')) #calling the function and passing  2 arguments

