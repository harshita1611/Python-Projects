import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False


from hangman_art import logo
print(logo)


print(f"the solution is {chosen_word}")



display =[]
for _ in chosen_word :
    display.append("_")



while not end_of_game :
    guess = input (" Guess letter :").lower()
    
    #same letter
    if guess in display :
        print(f"You have already guessed {guess}")

    #check guessed letter
    for position in range (word_length) :
        letter = chosen_word[position]

        #current position , letter
        if letter == guess :
            display[position] = letter 


    #wrong guess
    if guess not in chosen_word :
        print(f"you guessed {guess}, that's not in the word , you lose a life")

        lives-=1
        if lives == 0 :
            end_of_game = True
            print("you lose")

    #join all elemnts and make a string    
    print(f"{''.join(display)}")
    if "_" not in display :
        end_of_game=True 
        print("you win")


    from hangman_art import stages
    print(stages[lives])
