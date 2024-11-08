import random
import string
import unicodedata
from words_en import words_list_en
from words_pt import words_list_pt
from messages import MESSAGES

word = '' 
lang = 'EN'
word_letters = set(word)
alphabet = set(string.ascii_uppercase)
used_letters = set()
lives = 10

def hangman():    
    global lang, word, word_letters
    lang, word = get_valid_word()
    word_letters = set(word)
    user_letter = ''
    
    while len(word_letters) > 0 and lives > 0:
        if user_letter != '':
            print('\n', MESSAGES[f"{lang}_ALREADY_USED_LETTERS"], ' '.join(used_letters))
        
        show_word = [letter if letter in used_letters else '_' for letter in word]
        print(MESSAGES[f"{lang}_CURRENT_WORD"], ' '.join(show_word))
        
        user_letter = input(MESSAGES[f"{lang}_GUESS_A_LETTER"]).upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            verifyGuessedLetterInWord(user_letter)   
                
        elif user_letter in used_letters:
            print(MESSAGES[f"{lang}_YOU_HAVE_ALREADY_USED_THE_LETTER"], MESSAGES[f"{lang}_TRY_AGAIN"])
            
        else:
            print(MESSAGES[f"{lang}_INVALID_CHARACTER"], MESSAGES[f"{lang}_TRY_AGAIN"])
    
    gameOverMessage()
    
    
def verifyGuessedLetterInWord(user_letter):    
    global lives
    
    if user_letter in word_letters:
        word_letters.remove(user_letter)
                
    else:
        lives = lives - 1
        returnMessage(user_letter)
        

def returnMessage(user_letter):
    if lives > 0:
        print(f"{MESSAGES[f"{lang}_THE_LETTER"]} '{user_letter}' {MESSAGES[f"{lang}_IS_NOT_IN_THE_WORD"]} {MESSAGES[f"{lang}_TRY_AGAIN"]}")
    else:
        print(f"{MESSAGES[f"{lang}_THE_LETTER"]} '{user_letter}' {MESSAGES[f"{lang}_IS_NOT_IN_THE_WORD"]}")


def gameOverMessage():
    print('\n',MESSAGES[f"{lang}_GAME_OVER"])
    
    if lives == 0:
        print(MESSAGES[f"{lang}_SORRY_YOU_DEAD"], word)
    else:
        print(f"{MESSAGES[f"{lang}_YOU_GUESSED_THE_WORD"]}, {word}!!!")


def get_valid_word():    
    global lang, word
    lang = input('Choose an idiom (PT or EN): ').upper()
    
    if lang == 'PT':
        word = returnWord(words_list_pt)        
        word = ''.join(ch for ch in unicodedata.normalize('NFKD', word) if not unicodedata.combining(ch))
        
    else:
        word = returnWord(words_list_en)
        
    return lang, word.upper()


def returnWord(words_list):
    global word
    word = getRandomWord(words_list)

    while '-' in word or ' ' in word:
        word = getRandomWord(words_list)

    return word


def getRandomWord(words_list):
    return random.choice(words_list)


hangman()