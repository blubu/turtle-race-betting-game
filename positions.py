
from turtle import Turtle

# constants
WIDTH = -500

# data
circles = {}
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
coord = [75, 50, 25, 0, -25, -50, -75]

# creating turtles
for i in range(7):
    tut = Turtle(shape="circle")
    tut.hideturtle()
    tut.color("white")
    tut.penup()
    tut.shapesize(0.8)
    circles[colors[i]] = tut


# moving circles to starting point
def start():
    for n in range(7):
        circles[colors[n]].goto(coord[n], 270)
        circles[colors[n]].showturtle()
        circles[colors[n]].color(colors[n])


# update leaderboard
def update_position(cols):
    n = 0
    for col in cols:
        circles[col].goto(coord[n], 270)
        n += 1


# return position
def position(turtles):
    pos = [WIDTH]
    col = []

    for c_turtle in turtles:
        if c_turtle.xcor() > pos[0]:
            pos.insert(0, c_turtle.xcor())
            col.insert(0, c_turtle.pencolor())
        elif c_turtle.xcor() > pos[1]:
            pos.insert(1, c_turtle.xcor())
            col.insert(1, c_turtle.pencolor())
        elif c_turtle.xcor() > pos[2]:
            pos.insert(2, c_turtle.xcor())
            col.insert(2, c_turtle.pencolor())
        elif c_turtle.xcor() > pos[3]:
            pos.insert(3, c_turtle.xcor())
            col.insert(3, c_turtle.pencolor())
        elif c_turtle.xcor() > pos[4]:
            pos.insert(4, c_turtle.xcor())
            col.insert(4, c_turtle.pencolor())
        elif c_turtle.xcor() > pos[5]:
            pos.insert(5, c_turtle.xcor())
            col.insert(5, c_turtle.pencolor())
        else:
            pos.insert(6, c_turtle.xcor())
            col.insert(6, c_turtle.pencolor())

    update_position(col)
