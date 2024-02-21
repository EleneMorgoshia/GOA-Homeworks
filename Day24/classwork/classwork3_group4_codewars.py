#this function returns the doubled elements from a given array

def maps(a): #the function name is 'maps' and it has 1 parameter - a
    result_arr = [] #created an empty array called - 'result_arr'
    for i in range(len(a)): #for loop in a
        result_arr.append(2*a[i]) # an element at index i(iteration variable) * 2 will be added in the 'result_arr'
    return result_arr #this function returns the value of 'result_arr'

print(maps([1,2,3])) #calling the function and passing 1 argument 

#or
def maps(a):
    result_list = []
    for element in a:
        result_list.append(element * 2 )
    return result_list