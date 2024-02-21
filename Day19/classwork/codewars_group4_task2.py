#this function determines a century with the given year
def century(year): #the function name is century and it has 1 parameter
    if year % 100 == 0: #check if the year is a  multiple of 100.
        return year // 100 #if the statement in third line is true, return year//100
    return year // 100 + 1 #if the statement in third line is flase, return year // 100 +1

print(century(1701)) #calling the function and passing 1 argument