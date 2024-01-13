#group4:
#1)write a function that accepts  an integer n and a string s
#as parameters and returns a string of s repeted exactly n times
#2)it's preatty straightforward.your goal is to create a function that
# removes the first and last characters of a string.you're giveen one parameter,
#the original string.you don't have to worry wit hstring with less than two characters
#3)find the smallest integer in the array
#--------------------------------------
#1)task1:
def repeat_str(repeat,string):
    return repeat*string

print(repeat_str(5,"elene"))

#2)task2: არ არის სწორი

def remove_char(s): 
    for i in range(len(s)):
        new_str = " "
        if i != 0 and i != (len(s)-1) :
            new_str += s[i]
    return new_str


print(remove_char("ioane"))

#3)task3:
def find_smallest_int(arr):
    min_value=arr[0]
    for i in range(len(arr)):
        if arr[i]<min_value:
            min_value=arr[i]
    return min_value

my_arr=[1,2,100,900,-10]
print(find_smallest_int(my_arr))

                       