#A  function  finds the integral of the expression passed.

def integrate(coefficient, exponent): # the function name is 'integrate' and it has 2 parameters - coefficient , exponent
    new_exponent= exponent + 1 #created a variable called- new_exponent that equals to 'exponent' + 1 
    new_coef = coefficient // new_exponent #created a variable called - new_coef which equals to dividing the coefficient by new_exponent 
    result_variable = str(new_coef) + "x^" + str(new_exponent) #created a variable called - 'result_cariable" which equlas to sum of new_coef(stringed) , 'x^' and new_exponent(stringed)
    return result_variable # the function returns the value of 'result_variable'

print(integrate(3,2)) #calling the function and passing 2 arguments 

