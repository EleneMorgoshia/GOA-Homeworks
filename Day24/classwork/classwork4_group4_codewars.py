#this function returns the sum of the numbers that occur only once in the array


def repeats(arr): #the function name is 'repeats' and it has 1 parameter
    sum = 0 #created a variable called -sum that equals to 0
    for i in arr: #for loop in arr
        if arr.count(i) == 1: #check if the counted element at index i (iteration variable) equals to 1 
            sum += i #if the statement in the 7th line is true, sum will be encreased with i (iteration variable)
    return sum #the function returns the value of sum 


            
