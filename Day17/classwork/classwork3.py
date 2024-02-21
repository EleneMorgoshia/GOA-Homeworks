#task2:
#Given an array of integers.
#Return an array, where the first element is the count of positives numbers and 
#the second element is sum of negative numbers. 
#0 is neither positive nor negative.
#If the input is an empty array or is null, return an empty array.
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    if len(arr) == 0: #თუ სიის სიგრძე უდრის ნულს,ანუ ცარიელია და არ გვაქვს ცარიელი ელემენტები
        return arr
    amount_of_positives = 0
    sum_of_negatives = 0
    for element in arr:
        if element > 0:
            amount_of_positives += 1
        elif element < 0:
            sum_of_negatives += element
    return [amount_of_positives,sum_of_negatives]
    

my_arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(my_arr))