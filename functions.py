# reset data
def starting_point(func_turtle):
    y = -180
    for turtle in func_turtle:
        turtle.speed("normal")
        turtle.goto(-480, y)
        y += 60
        turtle.speed("fast")


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

