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
