#task3: group102
#this function determines if is is possible to get to the pump or not
def zero_fuel(distance_to_pump, mpg, fuel_left): #the function name is zero_fuel and it has 3 parameters
    if mpg * fuel_left >= distance_to_pump: #Check if the multiplication of the 'mpg' to 'fuel_left' is grater than or equals to 'distance_to_pump'
        return True#if statement below is true, return True
    return False #if the statement is 46th line is false,return False

print(zero_fuel(50,25,2)) #calling the function and passing 3 arguments