#this function determines the collor of the traffic light and returns the following collor of the given one   
def update_light(current): #The function name is 'update_light' and it has 1 argument
    if current == 'green': #Check if the 'current' equals to 'green'
        return 'yellow' # if the statement in 3rd line is True, the function returns 'yellow'
    elif current == 'yellow': #Check if the 'current' equals to 'yellow'
        return 'red' #if the statement in 5th line is true, the function returns 'red'
    elif current == 'red': #check if the 'current' equals to 'red'
        return 'green' #the function returns 'green' 
    
#The best version
def update_light(current): #the function name is 'update_light' and it has 1 parameter - current
    new_arr = ['green','yellow','red'] #created a variable called - 'new_arr' that equals to the list of traffic light collors
    print(new_arr.index(current) - 1 ) # 0 -1 = -1  
    print(new_arr[new_arr.index(current)]) # green
    return new_arr[new_arr.index(current)-1] #the function returns the element at index  'new_arr.index(current)-1' from the  list called - 'new_arr'
    

print(update_light('green')) #calling the function and passing 1 argument 