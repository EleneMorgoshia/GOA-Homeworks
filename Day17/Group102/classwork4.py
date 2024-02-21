#task5
#This function calculates body mass index (bmi = weight / height^2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"
#(bmi(50, 1.80), "Underweight")

def bmi(weight, height): #The function name is 'bmi' and it has 2 parameters(weight,height)
    bmi = weight / height ** 2 # created variable named-' bmi' which is equal to weight/height^2
    if bmi <= 18.5: #check if bmi is less than or eqauls to 18.5
        return "Underweight" #if statement below is true, return 'Underweight'
    elif bmi <= 25.0: #check if bmi is less than or equals to 25.5
        return "Normal"  #if statement in 65th line is true, return 'Normal'
    elif bmi <= 30.0: #check if bmi  is less than ot equals to 30.0
        return "Overweight"#if statement in 67th line is true, return 'Overweight'
    elif bmi > 30:#check if bmi is grater than 30
        return "Obese" #if statement in 69th line is true, return 'Obese'

print(bmi(50,1.80)) #calling function and passing two arguments