# A function  accepts three parameters:
# 'cap' is the amount of people the bus can hold excluding the driver.
# 'on' is the number of people on the bus excluding the driver.
# 'wait' is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait): #A function name is 'enough' and it has 3 parameters - cap , on, wait
    if (cap - on) >= wait: #check if the difference between a 'cap' and an 'on' is grater than or equals to 'wait'
        return 0 #if the statement in the 8th line is true, return 0
    return abs(wait - (cap - on)) # if the statement in the 8th line is false, return the difference between wait and (cap - on)


print(enough(100, 60, 50)) #calling the function and passing 3 arguments
    