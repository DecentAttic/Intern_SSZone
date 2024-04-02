# Task 2 description(Hangman Game)

# Hangman is a classic word guessing game. Here players guess letters to reveal a hidden word. The game randomly selects a word from 
# a predefined list, displaying blank spaces for each letter. Players guess letters one at a time. Correct guesses reveal the letter's 
# position; incorrect guesses result in penalties. The game continues until the word is guessed correctly or the player runs out of 
# attempts.


import random

def choose_word(): #This function consist of choosing an random word from a list of words
    words = ["apple", "banana", "orange", "grape", "strawberry", "pineapple","watermelon"]
    random_word=random.choice(words)
    return random_word

def display_word(word, guessed_letters):    #To display the word(fills with the letter when guessed)
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman(): #main function of this game 
    word = choose_word()
    guessed_letters = []
    attempts = 6 #Here the the players can get 6 attempts for gussing the word corect if there exist any mistake the attempt value decrements
    
    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")   #To display the length of the string
    print("Hint: Its a fruit")
    
    while True:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess!")
            attempts -= 1
            if attempts == 0:
                print("\nSorry, you're out of attempts. The word was:", word)
                break
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break

hangman()
