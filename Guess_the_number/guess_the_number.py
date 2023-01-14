logo = '''
   ____                         _   _                                    _               
  / ___|_   _  ___  ___ ___    | |_| |__   ___     _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __|   | __| '_ \ / _ \   | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \   | |_| | | |  __/   | | | | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/    \__|_| |_|\___|   |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                         
'''
print(logo)
import random
attempts_easy = 10
attempts_hard = 5
def check(guess , answer , turns ):
    if(guess == answer):
        print(f"You win!! The answer is {answer}")
    elif guess>answer :
        print("Too High , try a lower number")
        return turns-1
    elif guess < answer :
        print("Too Low , try a higher number")
        return turns-1
def difficulty():
    choice = input("Choose difficulty 'easy' or 'hard'")
    if choice == "easy":
        return attempts_easy
    if choice == "hard" :
        return attempts_hard
def game() :
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randrange(1, 100)
    print(f"answer is {answer}")
    turns = difficulty()
    guess = 0
    while guess!=answer:
        print(f"You get {turns} turns to guess")
        guess = int(input("Make a guess : "))
        turns=check(guess, answer, turns)
        if turns==0 :
            print("You loose because you are out of attempts")
            return
        elif guess!= answer :
            print("Guess Again!")

game()
