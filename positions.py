
from turtle import Turtle

# constants
WIDTH = 500

# data
circles = []

# creating turtles
for i in range(2):
    tut = Turtle(shape="circle")
    tut.hideturtle()
    tut.color("white")
    tut.penup()
    tut.shapesize(0.8)
    circles.append(tut)


# moving circles to starting point
def start():
    circles[0].goto(11, 270)
    circles[1].goto(-11, 270)
    circles[0].showturtle()
    circles[1].showturtle()
    circles[0].color("white")
    circles[1].color("white")


# update leaderboard
def update_position(p1, p2):
    circles[0].color(p1)
    circles[1].color(p2)


# return position
def position(turtles):
    pos1 = -WIDTH
    pos2 = -WIDTH
    for c_turtle in turtles:
        if c_turtle.xcor() > pos1:
            pos1 = c_turtle.xcor()
            col1 = c_turtle.pencolor()
        elif c_turtle.xcor() > pos2:
            pos2 = c_turtle.xcor()
            col2 = c_turtle.pencolor()
    update_position(col1, col2)
