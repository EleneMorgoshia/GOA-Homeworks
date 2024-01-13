#group 102:
#task5:
#Convert number to reversed array of digits
#Given a random non-negative number, you have to return 
#the digits of this number within an array in reverse order.
#35231 => [1,3,2,5,3]
#0 => [0]
def digitize(n):
    str_number=str(n) #"195"
    my_arr=[]
    for number in str_number:
        int_number=int(number)
        my_arr.append(int_number)
    my_arr.sort() #ზრდის მიხედვით დალაგება
    my_arr.reverse() #უკუღმა დალაგება
    return my_arr

print(digitize(195))
