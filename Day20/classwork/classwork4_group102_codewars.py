#This function returns a  third interior angle of a triangle

def other_angle(a, b): #A function name is 'other_angle' and it has 2 parameters - a , b
    return ( 180 - a - b ) #The function returns 180 - a - b

print(other_angle(60,60)) #Calling the function and passing 2 arguments 