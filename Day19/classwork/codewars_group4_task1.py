def lovefunc(flower1 , flower2): #the function name is 'lovefunc' and it has 2 parameters - flower1 , flower2
    if (flower1 % 2 == 0 and flower2 % 2 == 1) or ( flower2 % 2 == 0 and flower1 % 2 == 1): #check if the number of petals of flower1 is even and number of petals of flower 2 is odd,  
        #or if the number of petals of flower2 is even  and number of petals of flower 1 is odd
        return True  #if the statement in the third line is true, return True
    return False#if the statement in the third line is false, return False

print(lovefunc(0,0)) #calling the function and passing 2 arguments

