from turtle import Turtle, Screen
from random import randint

# screen setup
screen = Screen()
screen.setup(width=200, height=600)

# turtle data
turtles = []
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y = -180
race_finished = False

# user data
user_money = [10, 10, 10]
user_color = []
user_bet = []

# creating turtles
for turtle_color in colors:
    tut = Turtle(shape="turtle")
    tut.speed("fastest")
    tut.color(turtle_color)
    tut.penup()
    tut.goto(-80, y)
    turtles.append(tut)
    y += 60

# entering user bets
for i in range(1):
    user_color.append(screen.textinput(title=f"User {i+1}", prompt="Which turtle are you betting on ?").lower())
    # user_bet.append(int(screen.textinput(title=f"User {i+1}", prompt=f"You have ${user_money[i]}.\nPlace your bet :")))
    # user_money[i] -= user_bet[i]

# total bet placed
# total_bet = sum(user_bet)
# sum_bets = 0

# race loop
while not race_finished:
    for tut in turtles:
        if tut.xcor() > 80:
            winner = tut.pencolor()
            race_finished = True
            break
        tut.forward(randint(1, 10))

print(winner)
print(user_color[0])
# # winnings
# for i in range(2):
#     if user_color[i] == winner:
#         sum_bets += user_bet[i]
#     else:
#         lost_money = user_bet[i]
#         user_bet[i] = 0
#     winnings = (user_bet/sum_bets)*total_bet
#     if winnings:
#         print(f"User {i+1} won ${winnings}")
#     else:
#         print(f"User {i+1} lost ${lost_money}")

screen.exitonclick()