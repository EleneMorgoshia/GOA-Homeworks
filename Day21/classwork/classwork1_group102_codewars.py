#this function determines  the 4- sided polygon. 
#The polygon can either be a rectangle or a square.
#If it is a square, return its area. If it is a rectangle, return its perimeter.

def area_or_perimeter(l , w): # the function name is 'area_of_perimeter ' and it has 2 parameters - l,w
    if l == w : #check if a l equals to w
        return l * l #if the statement in the 6th lin is true, return l*l
    return 2 * (l + w) #if the statement in the 6yh line is false, return 2*(l+w)

print(area_or_perimeter(6,10)) #calling the function and passing 2 arguments