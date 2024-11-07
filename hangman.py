import random
import string
import unicodedata
from words_en import words_list_en
from words_pt import words_list_pt
from messages import MESSAGES

def get_valid_word():
    lang = input('Choose an idiom (PT or EN): ').upper()
    
    if lang == 'PT':
        word = random.choice(words_list_pt).upper()
        
        while '-' in word or ' ' in word:
            word = random.choice(words_list_pt).upper()
        
        word = ''.join(ch for ch in unicodedata.normalize('NFKD', word) if not unicodedata.combining(ch))
        
    else:
        word = random.choice(words_list_en).upper()
        
        while '-' in word or ' ' in word:
            word = random.choice(words_list_en).upper()
            
    return word, lang

def hangman():
    word, lang = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10
    
    while len(word_letters) > 0 and lives > 0:
        print(MESSAGES[f"{lang}_ALREADY_USED_LETTERS"], ' '.join(used_letters))
        
        show_word = [letter if letter in used_letters else '_' for letter in word]
        print(MESSAGES[f"{lang}_CURRENT_WORD"], ' '.join(show_word))
        
        user_letter = input(MESSAGES[f"{lang}_GUESS_A_LETTER"]).upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"{MESSAGES[f"{lang}_THE_LETTER"]} '{user_letter}' {MESSAGES[f"{lang}_IS_NOT_IN_THE_WORD"]}")
                
        elif user_letter in used_letters:
            print(MESSAGES[f"{lang}_YOU_HAVE_ALREADY_USED_THE_LETTER"])
            
        else:
            print(MESSAGES[f"{lang}_INVALID_CHARACTER"])
    
    if lives == 0:
        print(MESSAGES[f"{lang}_SORRY_YOU_DEAD"], word)
    else:
        print(f"{MESSAGES[f"{lang}_YOU_GUESSED_THE_WORD"]}, {word}!!!")

hangman()