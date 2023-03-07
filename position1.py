
from turtle import Turtle

# constants
WIDTH = -500

# data
circle = Turtle(shape="circle")
circle.hideturtle()
circle.color("white")
circle.penup()
circle.shapesize(0.8)


# moving circles to starting point
def start():
    circle.goto(11, 270)
    circle.showturtle()
    circle.color("white")


# update leaderboard
def update_position(p1):
    circle.color(p1)


# return position
def position(turtles):
    pos1 = WIDTH
    for c_turtle in turtles:
        if c_turtle.xcor() > pos1:
            pos1 = c_turtle.xcor()
            col1 = c_turtle.pencolor()

    update_position(col1)


# clearing screens
def clear_screen():
    circle.color("white")
