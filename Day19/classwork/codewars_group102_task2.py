#This function gets the students grades and returns the letter value associated with that grade:

# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
#100, 85, 96), "A"

def get_grade(s1, s2, s3): #The function name is 'get_grade' and it has 3 parameters
    average = (s1 + s2 + s3) // 3 #created a variable called - average  that equals to the division of sumed scores with 3 
    if average >= 90 and average <= 100: #check if the 'average' is grater than or equals to 90 and if the average is lower than or equals to 100 
        return 'A' #If the statement in 13th line is True, retun 'A'
    elif average >= 80 and average < 90 :#check if the 'average' is grater than or equals to 80 and if the average is lower than  90 
        return 'B' #If the statement in 15th line is True, return 'B'
    elif average >= 70 and average < 80: #check if the 'average' is grater than or equals to 70 and if the average is lower than  80
        return 'C'#If the statement in 17th line is True, return 'C'
    elif average >= 60 and average < 70:#check if the 'average' is grater than or equals to 60 and if the average is lower than  70
        return 'D'#If the statement in 19th line is True, return 'D'
    elif average >= 0 and average < 60: #Check if the average is grater than or equals to 0 and if the average is lower than 60 
        return 'F' #if the statement in 21th line is True, return 'F'
    

print(get_grade(99, 95, 91)) #calling the function and passing 3 arguments
