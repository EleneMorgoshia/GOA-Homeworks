#This function returns the average of the given array
#rounded down to its neares integer.
def get_average(marks): #the function name is get_average and it has 1 parameter - marks
    sum = 0 #created variable named - sum that equals to 0
    for i in range(len(marks)): #for loop in the array
        sum += marks[i] #vairable 'sum' will be encreased with the element at index i (iteration variable) in the array 
    average = sum // (len(marks)) #created variable named- average that equals to the division of varable' sum' by the length of the array
    return average #the function returs the value of the average variable

print(get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7])) #calling the function and passing 1 argument

#or
def get_average(marks): 
    ave = sum(marks) // len(marks)
    return ave

print(get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]))