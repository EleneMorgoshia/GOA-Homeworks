#task3
#Write a function that takes an array of numbers and 
#returns the sum of the numbers.
# The numbers can be negative or non-integer. 
#If the array does not contain any numbers then you
# should return 0.
#[1.1, 2.2, 3.3]
def sum_array(a):
    if len(a) == 0: #if the array doesnot contain any numbers (empty list)
        return 0
    sum_of_the_numbers = 0
    for i in range(len(a)):
        sum_of_the_numbers += a[i]
    return sum_of_the_numbers

print(sum_array([]))

#or, better way
def sum_array(a):
    if len(a)==0:
        return 0
    return sum(a)

print(sum_array([]))