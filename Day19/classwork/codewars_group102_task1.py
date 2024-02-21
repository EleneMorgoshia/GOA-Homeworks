#This funcion  takes the collection of championship and returns the number of points of our team.
#if our team wins, a total score will be encreased with 3
#if we our team lose, we will not have any additional scores
#if the match ends  in a draw , the total score will be encreased with 1 


def points(games):# The function name is 'points' and it has 1 parameter- games (collection of points)
    final_scores = 0  #created variable called - final_scores that equals to 0
    for game_scores in games: #for loop in the  array
        print(game_scores[0]) # print our team's scores
        print(game_scores[-1]) #print an opponent team's scores
        if int(game_scores[0]) > int(game_scores[-1]): # check if  our team's score  is grater than the opponent  team's score
            final_scores += 3 #if the statement in the 13th line is True, final score will be encreased with 3
        elif int(game_scores[0]) < int(game_scores[-1]): #check if  our team's score  is lower than the  opponent team's score 
            final_scores += 0 #if the statement in the 15th line is True, final_scores will be enacreased with 0 
        elif int(game_scores[0]) == int(game_scores[-1]): #check if  our team's score  equals to the opponent team's score
            final_scores += 1 #if the statement in 17th line is True , final_scores will be encreased with 1 
    return final_scores #the function returns the 'final_scores '

            
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'])) #calling the function and passing 1 arguments
#----------------------
string2 = ["2:1","3:1"] 
for element in string2:
    print(element[0]) #ეს დაპრინტავს ლისთის პირველი ელემენტის პირველ ელემენტს
    print(element[-1]) #ეს დაპრინტავს ლისთის პირველი ელემენტის ბოლო ელემენტს