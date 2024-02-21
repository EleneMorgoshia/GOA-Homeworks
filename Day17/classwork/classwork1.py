# task2:
# This function counts sheeps in the list . (True means present)
def count_sheeps(sheep):# we defined function named-count_sheeps.
                       # and crete one parameter 'sheep'(list)
    amount_of_sheeps= 0 #we created variable named- amount_of_sheeps. It equals to 0
    for i in range(len(sheep)): #we did a for loop in list(sheep)
        if sheep[i] == True:#we check if a list element equals to True
            amount_of_sheeps+= 1 #if the statement above is true, amount_of_sheeps will be encreased with 1
    return "There are {} sheeps in total".format(amount_of_sheeps) #function returns integer value(amount_of_sheeps)
    
my_arr=[True,True,False,True] #we created list
print(count_sheeps(my_arr)) # we called this function and pass our list(my_arr) as an argument 
