#This function determines whether a person is employed or on vacation

def set_alarm(employed, vacation):#The function name is 'set_alarm' and it has 2 parameters- employed , vacation
    #Check if the employeed is True and the vacation is True or check if the employeed is false and the vacation is true 
    #or check if the employeed is false and the vacation is false
    if employed == True and vacation == True or  employed == False and vacation == True or employed == False and vacation == False :
        return False#if the statement in the 6th line is True, retrun False
    elif employed == True and vacation == False: #Check if the employeed is true and the vacation is false
        return True #if the statement in the 8th line is True, return True
  
#or
def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    return False