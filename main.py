
from turtle import Screen
from random import randint
from turtle_data import turtles, colors, tracks
import positions
import functions

# constants
WIDTH = 1000
MAX_PLAYERS = 10
MOVE_DISTANCE = 20

# screen setup
screen = Screen()
screen.setup(width=WIDTH, height=600)
screen.title("! TURTLE RACER !")

# user data
users = {}
tracks()


# check how many users left
def check():
    global users
    for user_left in users:
        if users[user_left]["user_in_game"] and users[user_left]["user_money"] == 0:
            screen.textinput(title="Message", prompt=f"\n{users[user_left]['user_name']} "
                                                     f"has insufficient funds and is removed !!\n")
            users[user_left]["user_in_game"] = False


def play_game():
    # loop variable
    continue_game = True
    positions.start()

    # setting players
    for i in range(no_of_players):
        name = screen.textinput(title=f"User {i+1}", prompt=f"Enter user {i+1} name :")
        users[f"User {i + 1}"] = {
            "user_name": name,
            "user_money": 10,
            "user_bet": 0,
            "user_color": "",
            "user_in_game": True
        }

    # game loop
    while continue_game:
        # turtles to starting point
        functions.starting_point(turtles)

        print(f"\nUsers left : ")
        print(functions.users_left_in_game(users))
        race_finished = False
        total_bet = 0
        sum_bets = 0

        # entering user bets
        for user in users:
            if users[user]["user_in_game"]:
                users[user]["user_color"] = (screen.textinput(title=f"{user}",
                                                              prompt=f"Which turtle are you betting on "
                                                                     f"{users[user]['user_name']}?").lower())
                while users[user]["user_color"] not in colors:
                    users[user]["user_color"] = (screen.textinput(title=f"{user}",
                                                                  prompt="Enter valid color :").lower())

                users[user]["user_bet"] = float(screen.textinput(title=f"{user}",
                                                                 prompt=f"You have ${users[user]['user_money']}."
                                                                        f"\nPlace your bet :"))
                while users[user]["user_bet"] <= 0 or users[user]["user_bet"] > users[user]["user_money"]:
                    users[user]["user_bet"] = float(screen.textinput(title=f"{user}",
                                                                     prompt=f"You have ${users[user]['user_money']}."
                                                                            f"\nPlace your bet :"))

                users[user]["user_money"] -= users[user]["user_bet"]
                total_bet += users[user]["user_bet"]

        # race loop
        while not race_finished:
            for tut in turtles:
                if tut.xcor() > functions.X:
                    winner = tut.pencolor()
                    screen.textinput(title="", prompt=f"The winner of this round is {winner}.")
                    race_finished = True
                    break
                tut.forward(randint(1, MOVE_DISTANCE))
                positions.position(turtles)

        # total bets on winner
        for user in users:
            if users[user]["user_color"] == winner:
                sum_bets += users[user]["user_bet"]

        # winnings
        for user in users:
            if users[user]["user_color"] == winner:
                winnings = (users[user]["user_bet"]/sum_bets)*total_bet
                users[user]["user_money"] += winnings
                print(f"{users[user]['user_name']} won ${winnings}")
            else:
                print(f"{users[user]['user_name']} lost ${users[user]['user_bet']}")
            print(f"{users[user]['user_name']} final money is ${users[user]['user_money']}\n")

        # checking for funds
        check()
        if functions.check_winners(users):
            continue_game = False
            return users


# main loop
game_running = True

while game_running:
    # total players
    no_of_players = 0
    while no_of_players < 2 or no_of_players > MAX_PLAYERS:
        no_of_players = int(screen.textinput(title="Players", prompt=f"Enter number of players (2-{MAX_PLAYERS})"))

    final_list = play_game()
    print("Game exited !")
    print(final_list)

    # replay game
    if functions.check_winners(users):
        last_winner = functions.get_winner(users)
        if last_winner != 0:
            if screen.textinput(title="Winner !",
                                prompt=f"{users[last_winner]['user_name']} won the game."
                                       f"\nDo you want to play again? (y/n)") != 'y':
                game_running = False
        else:
            if screen.textinput(title="Losers !!",
                                prompt=f"No winner."
                                       f"\nDo you want to play again? (y/n)") != 'y':
                game_running = False

# exit
screen.exitonclick()
