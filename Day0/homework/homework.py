#homework N1
from turtle import*

#task1:drawing the square
speed(3)
width(5)
color("black")
begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()


#task2: drawing the roof

penup()
goto(150,150)
pendown()
right(150)
color("red")
begin_fill()
forward(150)
left(120)
forward(150)
end_fill()

#task3:drawing the door
penup()
goto(60,0)
pendown()
left(210)
color("blue")
begin_fill()
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()


#task4:drawing the windows

#the first one
penup()
goto(20,120)
pendown()
left(90)
begin_fill()
color("brown")
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(20,105)
pendown()
right(90) 
color("black")
forward(30)

penup()
goto(35,90)
pendown()
left(90)
color("black")
forward(30)

#the second one

penup()
goto(110,120)
pendown()
right(90)
begin_fill()
color("brown")
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(110,105)
pendown()
right(90)
color("black")
forward(30)

penup()
goto(125,90)
pendown()
left(90)
color("black")
forward(30)

exitonclick()
