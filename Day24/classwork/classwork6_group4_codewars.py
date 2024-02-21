#A function determines which player moves to the next round 

def whose_move(last_player, win): #the function name is 'whose_move' and it has 2 parameters - last_player , win
    if last_player == 'black' and win == False and last_player == 'white' and win == True: #check if the last_player equals to 'black'
        #and  the win equals to False and check if the last_player equals to 'white' and win equals to True
        return 'white' #if the statement in the 4th line is True, return 'White'
    elif last_player == 'black' and win == True and last_player == 'white' and win == False:#check if the last_player equals to 'black'
        #and  the win equals to True and check if the last_player equals to 'white' and win equals to false
        return 'black' #if the statement in the 7th line is True, return 'black'