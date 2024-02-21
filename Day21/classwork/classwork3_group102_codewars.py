#This function tests if the factor is a factor of base.
# it returns true if it is a factor or false if it is not.

def check_for_factor(base, factor):#The function name is 'check_for_factor' and it has 2 parameters - base, factor
    if  base % factor == 0: #check if the base is divisable by factor
        return True #if the statement in the 5th line is true, return true
    return False  #if the statement in the 5th line in false, return false

print(check_for_factor(63,7)) #calling the function and passing 2 arguments 

#or
def check_for_factor(base, factor):
   return base % factor == 0
 
