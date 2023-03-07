
# constants
""" X = (WIDTH/2)-20 """
X = 480
NORMAL_SPEED = "normal"
RACE_SPEED = "fast"


# reset data
def starting_point(func_turtle):
    y = -180
    for turtle in func_turtle:
        turtle.speed(NORMAL_SPEED)
        turtle.goto(-X, y)
        y += 60
        turtle.speed(RACE_SPEED)


# check for winner
def check_winners(users_left):
    num_left = 0
    for user_left in users_left:
        if users_left[user_left]["user_in_game"]:
            num_left += 1
    if num_left == 1 or num_left == 0:
        return True
    else:
        return False


# get winner
def get_winner(users_left):
    for user_left in users_left:
        if users_left[user_left]["user_in_game"]:
            return user_left
    return 0


# get users left
def users_left_in_game(users):
    players = []
    for user in users:
        if users[user]["user_in_game"]:
            players.append(users[user]["user_name"])
    return players

