#the function takes an array and remove every second element from the array.

#ჩადური გზა
def remove_every_other(my_list):  #the function name is 'remove_every_other' and it has 1 parameter - my_list
    new_list = [] #created a new variable called - new_list which is empty
    for i in range(len(my_list)): #for loop in my_list
        if i % 2 != 1: #check if the division of  i (iteration variable) and 2 is not equals to 1
            new_list.append(my_list[i]) #if the statement in the 7th line is true, element at index i will be added in the new_list
    return new_list #the function returns the value of the new_list
           

print(remove_every_other([1,2,3,4,5,6])) #calling the function and passing 1 argument

