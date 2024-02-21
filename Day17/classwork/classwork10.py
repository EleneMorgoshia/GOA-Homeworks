#task 6:
#Write a function which calculates the average of the numbers
# in a given list.
#Note: Empty arrays should return 0.
#(find_average([1, 2, 3],2)
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    sum = 0
    average_of_the_numbers = 0
    for i in range(len(numbers)):
        sum += numbers[i]
        average_of_the_numbers = sum/(len(numbers))
    return average_of_the_numbers


print(find_average([1,2]))