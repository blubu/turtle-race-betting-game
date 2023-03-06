from turtle import Screen
from random import randint
from turtle_data import turtles, colors
import functions

# screen setup
screen = Screen()
screen.setup(width=200, height=600)

# user data
users = {}


# check how many users left
def check():
    global users
    for user_left in users:
        if users[user_left]["user_money"] == 0:
            print(f"\n{user_left} has insufficient funds and is removed !!\n")
            users[user_left]["user_in_game"] = False


def play_game():
    # loop variable
    continue_game = True

    # setting players
    for i in range(2):
        users[f"User {i + 1}"] = {
            "user_money": 10,
            "user_bet": 0,
            "user_color": "",
            "user_in_game": True
        }

    # game loop
    while continue_game:
        # turtles to starting point
        functions.starting_point(turtles)

        print(f"\nUsers left {users}\n")
        race_finished = False
        total_bet = 0
        sum_bets = 0

        # entering user bets
        for user in users:
            if users[user]["user_in_game"]:
                users[user]["user_color"] = (screen.textinput(title=f"{user}",
                                                              prompt="Which turtle are you betting on ?").lower())
                while users[user]["user_color"] not in colors:
                    users[user]["user_color"] = (screen.textinput(title=f"{user}",
                                                                  prompt="Enter valid color :").lower())

                users[user]["user_bet"] = int(screen.textinput(title=f"{user}",
                                                               prompt=f"You have ${users[user]['user_money']}."
                                                                      f"\nPlace your bet :"))
                while users[user]["user_bet"] <= 0 or users[user]["user_bet"] > users[user]["user_money"]:
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
            print(f"{user} final money is ${users[user]['user_money']}\n")

        # checking for funds
        check()
        if functions.check_winners(users):
            continue_game = False
            return users


# main loop
game_running = True
while game_running:
    final_list = play_game()
    print("Game exited !")
    print(final_list)

    # replay game
    if functions.check_winners(users):
        last_winner = functions.get_winner(users)
        if last_winner != 0:
            if screen.textinput(title="Winner !",
                                prompt=f"{last_winner} won the game."
                                       f"\nDo you want to play again? (y/n)") != 'y':
                game_running = False
        else:
            if screen.textinput(title="Losers !!",
                                prompt=f"No winner."
                                       f"\nDo you want to play again? (y/n)") != 'y':
                game_running = False

# exit
screen.exitonclick()
