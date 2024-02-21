#A function returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

def powers_of_two(n): #the function name is 'powers_of_two' and it has 1 parameter - n
    result_array = [] #created an empty list called - 'result_array'
    i = 0 #created an iteration variable that equals to 0
    while i <= n  : #while loop 
        result_array.append(2 ** i ) # elements at index 2 ** i will be appended in the result_array
        i += 1 #the iteration variable will be encreased with 1 
    return result_array #the function returns the value of 'result_array'

print(powers_of_two(1)) #calling the function and passing 1 argument

