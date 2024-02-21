#the function determines the  position of a particular element in an array
def find_needle(haystack): #the function name is find_needle and it has 1 parameter
    my_arr = haystack.index("needle")  #created a variable called - my_arr which equals to the index of the element "needle" in the array
    return "found the needle at position " + str(my_arr) #this function returns the position of the element "needle" in the haystack(array)

print(find_needle([1000,"elene",1000,"kkkk","needle"])) #calling the function and passing 1 argument(list)
