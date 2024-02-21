# This function returns a number (final grade). There are four types of final grades:

# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases


def final_grade(exam, projects):#the function name is 'final_grade' and it has 2 parameters - exam, projects
    if exam > 90  or  projects > 10 : #check if the exam result is grater than 90 or if the number of project is grater than 10
        return 100 #if the statement in 10th line is true , return 100
    elif exam > 75  and projects >= 5 : #check if the exam result is grater than 75 and if the number of projects are grater than or equal to 5
        return 90 # if the statement in 12th line is true , return 90
    elif exam > 50  and projects >= 2: #if the the exam result is grater than 50 and if the number of projects are grater than or equals to 2 
        return 75# if the statement in 14th line is true , return 75
    return 0 #if the statements above are false, return 0 