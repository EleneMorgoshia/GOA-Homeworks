#this function takes 2 arrays as an argument and returns the sum of all their elements 

def array_plus_array(arr1,arr2): #The function name is 'array_plus_array' and it has 2 arguments - arr1 ,arr2
    sum = 0 #created the variable called - sum
    for i in range(len(arr1)): #for loop in arr1
        sum += arr1[i] #the variable sum will be encreased with an  element at index i(iteration variable) from  arr1 
    for k in range(len(arr2)): # for loop in arr2 
        sum += arr2[k]  # the variable sum will be encreased with an element at index k(iteration variable) from arr2
    return sum #the function retruns the value of 'sum'

print(array_plus_array([1,2,3],[4,5,6])) #calling the function and passing 2 arguments 

#or
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)

print(array_plus_array([1,2,3],[4,5,6]))