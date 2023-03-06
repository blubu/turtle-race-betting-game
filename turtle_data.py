from turtle import Turtle

# turtle data
turtles = []
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# creating turtles
for turtle_color in colors:
    tut = Turtle(shape="turtle")
    tut.color(turtle_color)
    tut.penup()
    turtles.append(tut)


# draw tracks
def tracks():
    tracker = Turtle()
    tracker.hideturtle()
    tracker.speed("fast")
    tracker.penup()
    y = 210
    for _ in range(8):
        tracker.goto(-500, y)
        tracker.pendown()
        tracker.goto(500, y)
        tracker.penup()
        y -= 60
