#task5:
#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
#The function takes a name as its only argument, and returns one of the following strings:
#(are_you_playing_banjo("martin"), "martin does not play banjo");
#(are_you_playing_banjo("Rikke"), "Rikke plays banjo");
def are_you_playing_banjo(name):
        if name[0] == "R" or name[0] == "r":
            return "{} plays banjo".format(name)
        return "{} does not play banjo".format(name)

print(are_you_playing_banjo("rolf"))