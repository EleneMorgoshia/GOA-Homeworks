#the function takes an array and remove every second element from the array.

def remove_every_other(my_list): # A  function name is 'remove_every_other' and it has 1 parameter - my_list
    return my_list[0:len(my_list):2] #the function returns the list with  removed second elements 

print(remove_every_other(['Hello', 'Goodbye', 'Hello Again'])) # Calling the function and passing 1 argument

#or 
def remove_every_other(my_list):
    return my_list[::2]

#or
def remove_every_other(my_list):
    arr1 = []
    i = 0
    while i < len(my_list):
        arr1.append(my_list[i])
        i += 2
    return arr1