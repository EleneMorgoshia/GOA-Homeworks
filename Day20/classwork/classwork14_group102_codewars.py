#this function takes the animal's name and dish as arguments and returns true or false to indicate 
# whether the beast is allowed to bring the dish to the feast.
#There is just one rule: the dish must start and end with the same letters as the animal's name. 


def feast(beast, dish):#the function name is 'feast' and it has 2 parameters - beast , dish
#check if the char at index 0 in the beast(string) equals to the char at index 0 in the dish(string) and
# if the char at index (len(beast)-1)-(the last element)in the beast(string) equals to the char at index (len(dish)-1) in the dish(string) 
    if beast[0] == dish[0] and beast[len(beast)-1] == dish[len(dish)-1]: 
        return True #if the statement in the 9th line is True, return true
    return False #if the statement in the 9th line is false, return false


print(feast("brown bear", "bear claw")) #calling the function and passing 2 arguments