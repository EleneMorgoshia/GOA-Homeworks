#taks2:
#This function determanies if a specific number is even or odd.
# Afer that the number will be multiplied by eigth if it is an even and by nine otherwise.

def simple_multiplication(number) :# the function name is 'simple_multiplication' and it has 1 parameter(number)
    if number % 2 == 0:  #Check if the number is even
        return number * 8    #if statement below is true, return number*8
    elif number % 2 == 1:    #check if the number is odd
        return number * 9   #if the statement below is true, return number*9
    
print(simple_multiplication(2)) #calling function and passing  2 as an argument