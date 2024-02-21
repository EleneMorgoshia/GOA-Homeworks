#This function takes the numbers of  monkeys as a parameter
#and fills an array with all numbers up to and including that number, but excluding zero.
def monkey_count(n): #the function name is 'monkey_count' and it has 1 parameter-n
    new_arr = [] #created a variable called - 'new_arr' that is empty
    i=1 # iteration variable which equals to 1
    while i <= n: #while loop 
        new_arr.append(i) #element at index i (iteration variable) will be added in the 'new_arr'
        i+=1 #i will be encreased with 1
    return new_arr #this function returns the value of 'new_arr'

print(monkey_count(5)) #calling the function and passing 1 argument



