#the function returns the corrected string

# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1

def correct(s): #the function name is 'cerrect' and it has 1 parameters - s 
    new_str = "" #created an empty variable called - new_str
    for char in s: #for loop in s
        if char == '1': #check if a character equals to '1'
            new_str += 'I' #if the statement in the 10th line is true, the 'new_str' will be encreased with 'I'
        elif char == '5': #check if the character equlas to '5'
            new_str += 'S'#if the statement in the 12th line is true, the 'new_str' will be encreased with 'S'
        elif char == '0':#check if the character equals to '0'
            new_str += 'O'#if the statement in the 14th line is true, the 'new_str' will be encreased with 'O'
        else:
            new_str += char #if the statement in the 10th line is false, the 'new_str' will be encreased with the char
    return new_str #the function returns the value of 'new_str'

print(correct('015kl'))  #calling the function and passing  1 argument


#or the simplest way:
def correct(s):
   return  s.replace('1','I').replace('0','O').replace('5','S')

print(correct('EL05'))