#the function takes two integers a and b as a parameters (where a < b) and returns 
#an array of all integers between the input parameters, including them.

def between(a,b): #the function name is 'between' and it has 2 parameters - a , b
    result_array = [] #created an empty array called - 'result_array' 
    i = a #created an iteration variable that equals to 'a'
    while i <= b: #while loop
        result_array.append(i) #An element at index i(iteration variable) will be added in the 'result_array'
        i += 1 #iteration variable will be encreased with 1 
    return result_array #the function returns the value of 'result_array'

print(between(1,4)) #calling the function and passing 2 arguments 

#or

def between(a,b):
    result_array = []
    for i in range(a, b + 1):
        result_array.append(i)
    return result_array

#or the best way:
def between(a,b):
    return [x for x in range(a,b+1)]

print(between(1,4))