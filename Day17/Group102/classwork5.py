#task6:
#This function returns an array of integers from n to 1 where n>0.
def reverse_seq(n): #The function name is reverse_seq and it has one parameter(n)
    integers_array = [] # created empty list named- integers_array
    i= n #iteration variabel equals to n
    while i > 0: #while loop 
        integers_array.append(i) #iteration variable will be added in integers_array.
        i-=1 #interation variable decrease with 1
    return integers_array#function returns integers_array

print(reverse_seq(10)) #calling function and passing 10 as an argument