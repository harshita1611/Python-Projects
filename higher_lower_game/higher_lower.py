import random
#displaying logo
from higher_lower_art import logo
print(logo)


#asking users choice
game_continue = True
points = 0
while game_continue :
    # random choice 1
    from higher_lower_data import data

    choice1 = random.choice(data)
    print(f"Compare A  : {choice1['name']} , {choice1['description']}  , from  {choice1['country']}")

    # display vs
    from higher_lower_art import vs

    print(vs)

    # random choice 2
    from higher_lower_data import data

    choice2 = random.choice(data)
    print(f"Against B   : {choice2['name']} , {choice2['description']}  , from  {choice2['country']}")

    # comparing both followers
    followers_A = choice1['follower_count']
    followers_B = choice2['follower_count']

    user_choice = input("Who has more followers A or B :")
    if (followers_A > followers_B and user_choice == "A") or (followers_B > followers_A and user_choice == "B"):
        points += 1
        game_continue=True
        print("You are Right!!")
    else:
        points += 0
        game_continue=False
        print("Oops!! you are wrong")

    print(f"Your score is {points}")