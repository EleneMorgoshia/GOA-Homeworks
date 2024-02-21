#This function returns the sum of the values from  the given array

def sum_mix(arr): #The function name is 'sum_mix' and it has 1 parameter
    final_sum = 0 #created the variable called -'sum' that equals to 0 
    for i in range(len(arr)): # for loop in the array
        final_sum += int(arr[i]) #The variable sum will be encreased with the converting  elemenet at index i(iteration variable) in the array to integer
    return final_sum #The function returns the 'sum' variable's value

print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7])) #calling the function and passing 1 arguments