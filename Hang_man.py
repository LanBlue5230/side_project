
import random
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


import hangman_art
print(hangman_art.logo)

#print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"
guessed = []

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print(f"You already guessed {guess},try again!")
      
    guessed.append(guess)
    
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            guessed.append(guess)
    
    if guess not in chosen_word:
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        print(f"This word {guess} is not in the word!Try again!")

    
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    import hangman_art
    print(hangman_art.stages[lives])
