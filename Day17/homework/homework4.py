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