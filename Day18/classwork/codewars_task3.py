#this function determines the winner of the game called - Rock Paper Scissors
def rps(p1, p2): #the function name is rps and it has 2 parameters
    if p1 == "scissors" and p2 == "paper" or p1 == "paper" and p2 == "rock" or p1 == "rock" and p2 == "scissors" : #check if the varible p1 equals to 'scissors' and the variable p2 equals to 'paper'  
        # or the variable p1 equals to 'paper' and the variable p2 equals to 'rock' , or the variable p1 equals to 'rock' and the variable pw equals to 'scissors'
        return "Player 1 won!" #if the statement below is true, return 'Player 1 won'
    elif p1 == "scissors" and p2 == "rock" or p1 == "paper" and p2 == "scissors" or p1 == "rock" and p2 == "paper"  :#check if the varible p1 equals to 'scissors' and the variable p2 equals to 'rock'
        #or the variable p1 equals to 'paper' and the variable p2 equals to 'scissors' , or the variable p1 equals to 'rock' and the variable p2 equals to ' paper'
        return "Player 2 won!"#if the statement below is true, return 'Player 2 won'
    else:
        return "Draw!" #if the statement in third line is false and the statement in the 6th line is false, return 'Draw'
    
 
print(rps('rock', 'rock')) #calling the function and passing 2 arguments

#ჩადური გზა: 
def rps(p1, p2):
    winner_combo ={ "rock" : "scissors", #რა რას უგებს
                    "scissors": "paper",
                    "paper": "rock"}
    print(winner_combo[p1])
    print(winner_combo['paper'])
    if winner_combo[p1] == p2: #აქ გამოვიდა scissors =scissors რაც არის True, ამიტომ ქვემოთ return შესრულდება 
        return "Player 1 won!" 
    if winner_combo[p2] == p1: #აქ გამოვიდა paper == rock რაც არის false , ამიტომ ქვემოთ return არ შესრულდება
        return "Player 2 won"
    return "Draw!"
#კოდი რას შვრება გავიგე, მაგრამ ეს ლოგიკა რომ ყველა ქეისზე მუშაობს მაგას საიდან ვხვდებით? (ყველა ვარიანტზე მუშაობს)
#ამ ამოცანის ესეთი ამოხნის გზის მოფიქრება პრაქტიკას მოაქვს თუ რა არი ესსსს??????
print(rps('rock','scissors'))

#https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python