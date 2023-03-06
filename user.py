import turtle

user = {
    "user_name": {
        "user_money": 10,
        "user_bet": 0,
        "user_color": ""
    }
}

user += {f"User {i+1}": {"user_money": 10,
                   "user_bet": 0,
                   "user_color": ""}
         }