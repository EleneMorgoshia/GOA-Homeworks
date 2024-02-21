#task2 -group102

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