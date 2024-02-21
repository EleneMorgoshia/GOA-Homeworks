#task3:
#This function identifies how many bullets are needed for a specific amount of dragons.
#each dragon takes 2 bullets to be defeated.
def hero(bullets, dragons): # the function name is 'hero' and it has 2 parameters(bullets and dragons)
    if bullets >= dragons * 2 : #Check if the amount of bullets is grater than or equals to dragons * 2 
        return True # if the statement below is True, return True
    return False #if the statement in 37th line is False,return False. 