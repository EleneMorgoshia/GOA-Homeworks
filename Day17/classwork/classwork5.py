#new codewars' tasks
#task1:
#divisible-გაყოფადი
#Create a function that checks if a number n is divisible 
#by two numbers x AND y. 
#All inputs are positive, non-zero numbers.
#n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
    
print(is_divisible(8,3,4))

# #or
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    return False 