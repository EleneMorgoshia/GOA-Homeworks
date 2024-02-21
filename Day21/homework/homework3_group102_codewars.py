#A function returns the largest number obtained after inserting the following operators and brackets: +, *, () 
    
def expression_matter(a, b, c): #the function name is 'expression_matter' and it has 3 parameters - a,b ,c
    return max(a*b*c,(a+b)*c,(a+b+c),a*(b+c)) #the function finds a maximum value from the given mathematical operations