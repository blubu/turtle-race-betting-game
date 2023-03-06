from turtle import Turtle, Screen
from random import randint

# screen setup
screen = Screen()
screen.setup(width=200, height=600)

# turtle data
turtles = []
# colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
colors = ["red", "blue"]

# user data
users = {}

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

# setting players
for i in range(2):
    users[f"User {i+1}"] = {
            "user_money": 10,
            "user_bet": 0,
            "user_color": ""
        }

print(users)
print(users["User 1"])

# game loop
while play_again == 'y':
    # turtles to starting point
    starting_point(turtles)
    race_finished = False
    total_bet = 0
    sum_bets = 0

    # entering user bets
    for user in users:
        users[user]["user_color"] = (screen.textinput(title=f"{user}", prompt="Which turtle are you betting on ?").lower())
        users[user]["user_bet"] = int(screen.textinput(title=f"{user}",
                                                       prompt=f"You have ${users[user]['user_money']}."
                                                              f"\nPlace your bet :"))
        users[user]["user_money"] -= users[user]["user_bet"]
        total_bet += users[user]["user_bet"]

    # race loop
    while not race_finished:
        for tut in turtles:
            if tut.xcor() > 80:
                winner = tut.pencolor()
                race_finished = True
                break
            tut.forward(randint(1, 10))

    # total bets on winner
    for user in users:
        if users[user]["user_color"] == winner:
            sum_bets += users[user]["user_bet"]

    # winnings
    for user in users:
        if users[user]["user_color"] == winner:
            winnings = (users[user]["user_bet"]/sum_bets)*total_bet
            users[user]["user_money"] += winnings
            print(f"{user} won ${winnings}")
        else:
            print(f"{user} lost ${users[user]['user_bet']}")
        print(f"{user} final money is ${users[user]['user_money']}")

    # play again
    play_again = screen.textinput(title="Exit Game", prompt="Do you want to play again? (y/n)").lower()

# game end
for tut in turtles:
    tut.hideturtle()


screen.exitonclick()
