# # FUNCTIONS
from turtle import*
for i in range(4):
    forward(100)
    left(90)

penup()
goto(0,200)
pendown()
for i in range(4):
    forward(100)
    left(90)

penup()
goto(-200,200)
pendown()
for i in range(4):
    forward(100)
    left(90)

penup()
goto(-200,0)
pendown()
for i in range(4):
    forward(100)
    left(90)

#same task written with function
from turtle import*
def draw_square():
    for i in range(4):
        forward(100)
        left(90)

def kalmis_wageba(x,y):
    penup()
    goto(x,y)
    pendown()

draw_square()
kalmis_wageba(0,200)
draw_square()
kalmis_wageba(-200,200)
draw_square()
kalmis_wageba(-200,0)
draw_square()
#---------------------------
print(range(4)) #(0,4)- 0,1,2,3
#---------------------------
#Sololearn
#example1:
print("happy birthday".capitalize()) 
#--------------------------------
# #find()
print("Bee".find("e"))
#-----------------------------
#len
movie = "Avatar"
print(len(movie)) #ათვლას ვიწყეთ 1-იდან
#---------------------------------
#insert()
items = ["book", "pen", "pencil"]
items.insert(2,"marker")
print(items)
#-----------------------------------
#pop()
items = ["book", "pen", "pencil"]
items.pop(0)
print(items)
#-----------------------------
#REVIEW
#1)capitalize function- convert the first character of a string to uppercase,
#while making the remaining characters lowercase.
#syntax- string.capitalize()
#example:print("happy birthday".capitalize()) 
 
#2)find function-The find() function checks if a character (or a pattern of characters) is present in a string.
# The function returns the index (position) of the given value. 
#If the given value is present multiple times, the function will return the first occurrence (the lowest index).
#syntax- string.find("any letter you want")
#example-print("Bee".find("e"))

#3)#insert() function-The insert() function allows you to add an element to a list, at a specific position
#sytax- listname.insert(where to insert,what to insert )
#example:
# items = ["book", "pen", "pencil"]
# items.insert(2,"marker")
# print(items)

#4)pop()-The pop() function removes an element from a list
#syntax- listname.pop(index of value you want to remove)
#example:
# #items = ["book", "pen", "pencil"]
# items.pop(0)
# print(items)