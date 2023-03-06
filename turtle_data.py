from turtle import Turtle

# colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# turtle data
turtles = []
colors = ["red", "blue"]

# creating turtles
for turtle_color in colors:
    tut = Turtle(shape="turtle")
    tut.speed("fastest")
    tut.color(turtle_color)
    tut.penup()
    turtles.append(tut)
