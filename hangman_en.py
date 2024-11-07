import random
import string
from words_en import words_list_en as words_list

def get_valid_word():
    word = random.choice(words_list).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words_list).upper()

def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10
    
    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        
        show_word = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(show_word))
        
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"Letter '{user_letter}' is not in the word. Please, try again.")
                
        elif user_letter in used_letters:
            print('You have already used that character. Please, try again.')
            
        else:
            print('You type an invalid character. Please, try again.')
    
    if lives == 0:
        print('Sorry, you died D: \n The word was ', word)
    else:
        print(f"You guessed the word, {word}!!!")

hangman()