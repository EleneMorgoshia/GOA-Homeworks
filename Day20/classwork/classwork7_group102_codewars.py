#the function returns a sum of elments from array , except the highest and the lowest element(by value,not by index!)

#https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

def sum_array(arr):#the function name is 'sum_array' and it has 1 parameter - arr
    if not arr: #check if the given argument is an array or not 
        return 0 #if the statement in the 5th line is True, return 0
    elif len(arr) < 2: #check if the length of the array is less than 2 
        return 0 #if the statement in the 7th line is True, return 0
    sum = 0 #created a variable called - 'sum' that equals to 0
    arr.sort() # sorting elements in the given array
    print(arr) #print the 'arr'
    arr.pop(0) #poping an element at index 0 in the 'arr'
    arr.pop(len(arr)-1) #poping an element at index (len(arr)-1) in the 'arr'
    print(arr) #print the 'arr'
    for i in range(len(arr)): #for loop in the 'arr'
        sum += arr[i] #the variable sum will be encreased with the element at index i (iteration variable) in the 'arr'
    return sum #this function returns the sum value 


print(sum_array([10,10,2,5,6,1,1])) #callign the function and passing 1 argument