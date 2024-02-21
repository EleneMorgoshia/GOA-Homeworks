#group4
#working on codewars
#task1:
#this function determines the first letter of the name and surname. 
def abbrev_name(name):#the funcion name is abbrev_name and it has 1 parameter - name
    my_list = name.split() #created a new variable called - my_list which equals to a splited string  
    list_name = my_list[0] #created a variable called - list_name which equals to an element at index 0 in my_list
    list_surname = my_list[1] #created a variable called - list_surname which equals to an element at index 1 in my_list
    return (list_name[0] + "." + list_surname[0]).upper() # this function returns an uppered string of the sum of an element at index 0 in list_name and 
                                                          #an element at index 0 in list_surname. 

print(abbrev_name("elene Morgoshia")) #calling the function and passing 1 argument

