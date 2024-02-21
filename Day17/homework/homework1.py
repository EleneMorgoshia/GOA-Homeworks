#task1: group102

#This function determines the  lowest number in a list
def minimum(arr):#the function name is minimum and  it has 1 parameter-'arr'
    min = arr[0] # created the variable named-'min' which is  equal to the first element in the list 
    for i in range(len(arr)): #for loop in the list
        if arr [i] < min: #check if the number at index i (iteration variable) in the list is lower than min 
            min = arr[i] #if the statement below is true, the min equals to the number at index i(iteration variable)
    return min #function returns the value of min number

print(minimum([-52, 56, 30, 29, -54, 0, -110])) #calling the function and passing the array as an argument

#This function determines the largest number in a list
def maximum(arr): #The function name is maximum and it has 1 parameter- 'arr'
    max = arr[0] #created the  variable named- 'max' which is  equal to the  first element in the list
    for i in range(len(arr)): #for loop in  a list
        if arr[i] > max: #Check if the number at index i(iteration variable) in the list is grater than max
            max = arr[i] #if statement below is true, the max equals to the number at index i (iteration variable)
    return max #function returns the value of the max number

print(maximum([4,6,2,1,9,63,-134,566])) #calling the function and passing the array as an argument