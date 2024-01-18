#+3 tasks in codewars
#---------------
#task1:

#This function determines the  lowest number in a list
def minimum(arr):#the function name is minimum and  it has 1 parameter-'arr'
    min = arr[0] # created the variable named-'min' which is  equal to the first element in the list 
    for i in range(len(arr)): #for loop in the list
        if arr [i] < min: #check if the number at index i (iteration variable) in the list is lower than min 
            min = arr[i] #if the statement below is true, the min equals to the number at index i(iteration variable)
    return min #function returns the value of min number

print(minimum([-52, 56, 30, 29, -54, 0, -110])) #calling the function and passing the array as an argument

#This function determines the largest number in a list
def maximum(arr): #The function name is maximum and it has 1 parameter- 'arr'
    max = arr[0] #created the  variable named- 'max' which is  equal to the  first element in the list
    for i in range(len(arr)): #for loop in  a list
        if arr[i] > max: #Check if the number at index i(iteration variable) in the list is grater than max
            max = arr[i] #if statement below is true, the max equals to the number at index i (iteration variable)
    return max #function returns the value of the max number

print(maximum([4,6,2,1,9,63,-134,566])) #calling the function and passing the array as an argument

#------------------------------------------------
#task2:

#This functon determines the average number from a list of class scores and compare it to your score. 
def better_than_average(class_points, your_points): #The function name is better_than_average and it has 2 parameters-'class_points',' your_points'
    sum = 0 #created the variable named-'sum' which is  equal to 0 
    average_number = 0 #created variale named-'avetage_number' which is equal to 0
    for i in range(len(class_points)): #for loop in the list of class points
        sum += class_points[i] #the variable 'sum' will be increased with the number at the index of i (iteration variable) in the list
    sum += your_points # sum incerased with the value of 'your points'
    average_number = sum / (len(class_points)+1) #the variable average_number eqauals to the division of 'sum' by the length of the list +1 
    if your_points > average_number:#Check if the variable 'your_points' is grater than the 'average_number'
        return True#if statement below is true, return True
    return False#if the statement in 36th line is false,return False


print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)) #calling the function and passing two arguments
#---------------------------------------------
#task3:
#this function determines if is is possible to get to the pump or not
def zero_fuel(distance_to_pump, mpg, fuel_left): #the function name is zero_fuel and it has 3 parameters
    if mpg * fuel_left >= distance_to_pump: #Check if the multiplication of the 'mpg' to 'fuel_left' is grater than or equals to 'distance_to_pump'
        return True#if statement below is true, return True
    return False #if the statement is 46th line is false,return False

print(zero_fuel(50,25,2)) #calling the function and passing 3 arguments
#--------------------------
#Lesson 15's homework
#task1:
#This function gives out the total amount of money for different days
# the cost of one day is 40$
#if d > 7 you will be given 50$ discount
#if d>3 and d<7 you will be given 20% discount
def rental_car_cost(d): #the function name is rental_car_cost and it has 1 parameter-d
    if d >= 7: #Check if the number of rental days is greater than or equal to 7
        return 40 * d - 50 #if the statement below is true, return 40*d - 50
    elif d > 3 and d < 7: #Check if the number of rental days is greater than 3  or less than  7
        return 40 * d - 20 #if the statemen in 61th line is true, return 40*d-20
    return 40 * d # return the multilication of daily amount by 40$
#--------------------------------------------
