#The function determines the first element of an array that is not consecutive.
#one of the best tasks

def first_non_consecutive(arr): #the function name is firs_non_consecutive and it has 1 parameter - arr
   i = 0 # created iteration variable that equals to 0
   while i < len(arr) - 1:  #while loop in arr 
      if arr[i+1] - arr[i] != 1: #Check if the difference between the element at index i+1 and the element at index i is not equal to 1
         return arr[i+1] #if the statement in the 7th line is True, return the value of element at index [i+1] in the arr
      i += 1      #The iteration variable will be encreased with 1      
      
print(first_non_consecutive([1,2,3,4,8])) #calling the function and passing 1 argument 



