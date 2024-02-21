#this function takes a string as a parameter and returns the  reversed string

def reverse_words(s): #the function name is reverse_words and it has 1 parameter - s
    arr_of_words = s.split() #created the variable called - arr_of_words that equals to the splited string.
    print(arr_of_words) #the print function for the variable called -arr_of_words
    arr_of_words.reverse() # reverse method on the arr_of_words
    print(arr_of_words) #the print function for arr_of_words
    result_str = " ".join(arr_of_words) #created new variable called - result_str that equals to the joined string
    return result_str #this function returns the result_str's value


print(reverse_words('hello world')) #calling the function and passing 1 arguments


    
    