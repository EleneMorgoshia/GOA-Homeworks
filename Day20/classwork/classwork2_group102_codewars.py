
#this function takes month as a parameter and returns quarter of the month 
def quarter_of(month): #the function name is 'quarter_of ' and it has 1 parameter - month 
    if month >= 1 and month <= 3: #check if the month is grater than or equals to 1 and if the  month is less than or equals to 3
        return 1 # if the statement in 11th line is correct the function returns 1
    elif month >= 4 and month <= 6: #check if the month is grater than or equals to 4 and if month is less than or equals to 6
        return 2 #if the statement in 13th line is correct, the funtion returns 2
    elif month >= 7 and month <= 9: #check if the month is grater or equals to 7 and if the month is less than or equals to 9
        return 3 #if the statement in 15th line is correct, the function returns 3
    elif month >= 10 and month <=12: #check if the month is grater than or equals to 10 and if the month is less than ot equals to 12
        return 4 # if the statement in 17th line is correct , the function returns 4

print(quarter_of(11)) #calling the function and passing 1 argument

#another way 

def quarter_of(month):
    months = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    if month in months[0]:
        return 1
    elif month in months[1]:
        return 2
    elif month in months[2]:
        return 3
    else:
        return 4 

print(quarter_of(12))