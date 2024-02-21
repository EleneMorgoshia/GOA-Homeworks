#The function takes father's age and son's age as  parameters and calculates
# many years ago the father was twice as old as his son (or in how many years he will be twice as old). 

def twice_as_old(dad_years_old, son_years_old): #The function name is 'twice_as_old' and it has 2 parameters - dad_years_old , son_years_old
    result_variable = dad_years_old - (son_years_old * 2) #Created a variable called - 'result_variable' that equals to a difference between
    #dad_years_old and (son_years_old multiplied by 2 )
    if result_variable < 0: #Check if the result_variable is grater than 0 
        result_variable *= -1 #if the statement in the 7th line is True, result_variale will be multiplied by -1 
    return result_variable #the function returns the value of 'result_variable'


print(twice_as_old(22,1)) #calling the function and passing 2 arguments 

#or 
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))