from turtle import Turtle, Screen
from random import randint

# screen setup
screen = Screen()
screen.setup(width=200, height=600)

# turtle data
turtles = []
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# user data
user_money = [10, 10, 10]

# race data
play_again = 'y'


# reset data
def starting_point(func_turtle):
    y = -180
    for turtle in func_turtle:
        turtle.goto(-80, y)
        y += 60


# creating turtles
for turtle_color in colors:
    tut = Turtle(shape="turtle")
    tut.speed("fastest")
    tut.color(turtle_color)
    tut.penup()
    turtles.append(tut)

# game loop
while play_again == 'y':
    # turtles to starting point
    starting_point(turtles)
    user_color = []
    user_bet = []
    race_finished = False

    # entering user bets
    for i in range(1):
        user_color.append(screen.textinput(title=f"User {i+1}", prompt="Which turtle are you betting on ?").lower())
        user_bet.append(int(screen.textinput(title=f"User {i+1}", prompt=f"You have ${user_money[i]}.\nPlace your bet :")))
        user_money[i] -= user_bet[i]

    # total bet placed
    total_bet = sum(user_bet)
    sum_bets = 0

    # race loop
    while not race_finished:
        for tut in turtles:
            if tut.xcor() > 80:
                winner = tut.pencolor()
                race_finished = True
                break
            tut.forward(randint(1, 10))

    print(user_bet[0])
    print(user_money[0])

    # total bets on winner
    for i in range(1):
        if user_color[i] == winner:
            sum_bets += user_bet[i]

    # winnings
    for i in range(1):
        if user_color[i] == winner:
            winnings = (user_bet[i]/sum_bets)*total_bet
            user_money[i] += winnings
            print(f"User {i+1} won ${winnings}")
        else:
            print(f"User {i+1} lost ${user_bet[i]}")

    # play again
    play_again = screen.textinput(title="Exit Game", prompt="Do you want to play again? (y/n)").lower()


screen.exitonclick()
