#group102:
#task1:
#Clock shows h hours, m minutes and s seconds after midnight.
#Your task is to write a function which returns the time 
#since midnight in milliseconds.
#Milliseconds=Hours×(60×60×1000)
#Milliseconds=Minutes×(60×1000)
#Milliseconds=Seconds×1000

# test.assert_equals(past(0,1,1),61000)
# test.assert_equals(past(1,1,1),3661000)
#test.assert_equals(past(0,0,0),0)
def past(h, m, s):
    variable_for_hours = h * (60*60*1000)
    print("hours:",variable_for_hours)
    variable_for_minutes = m * (60*1000)
    print("minutes:",variable_for_minutes)
    variable_for_second = s * 1000
    print("second:",variable_for_second)
    return variable_for_hours + variable_for_minutes + variable_for_second

print(past(0,0,0))
#--------------------------------
#task2:
#Given an array of integers.
#Return an array, where the first element is the count of positives numbers and 
#the second element is sum of negative numbers. 
#0 is neither positive nor negative.
#If the input is an empty array or is null, return an empty array.
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    new_arr=[]
    count_of_positives_number = 0
    sum_of_negative_numbers = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count_of_positives_number += 1
        elif arr[i] <  0:
            sum_of_negative_numbers += arr[i]

    new_arr.append(count_of_positives_number)
    new_arr.append(sum_of_negative_numbers)
    return new_arr

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
#ცარიელი ლისთისთვის არ გამოდის 
#-----------------------------------
#task3
#Your classmates asked you to copy some paperwork for them.
#You know that there are 'n' classmates and the paperwork has 'm' pages.
#Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
def paperwork(n, m): #n-classmates m-pages
    if n <= 0 or m <= 0:
        return 0
    elif n>0 and m>0:
        return n*m


    
