import random
import string
import unicodedata
from words_pt import words_list_pt as words_list

def get_valid_word():
    word = random.choice(words_list).upper()
    
    while '-' in word or ' ' in word:
        word = random.choice(words_list).upper()
        
    word = ''.join(ch for ch in unicodedata.normalize('NFKD', word) if not unicodedata.combining(ch))
        
    return word

def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10
    user_letter = ''
    
    while len(word_letters) > 0 and lives > 0:
        if user_letter != '':
            print('Você já usou essas letras: ', ' '.join(used_letters))
        
        show_word = [letter if letter in used_letters else '_' for letter in word]
        print('Palavra atual: ', ' '.join(show_word))
        
        user_letter = input('Advinhe uma letra: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"A letra '{user_letter}' não está na palavra. Por favor, tente novamente.")
                
        elif user_letter in used_letters:
            print('Você já usou essa letra. Por favor, tente novamente.')
            
        else:
            print('Você digitou um caracter inválido. Por favor, tente novamente.')
    
    print('---------------- FIM DE JOGO!!! ----------------')
    if lives == 0:
        print('Sinto muito, você morreu D: \nA palavra era ', word)
    else:
        print(f"Você advinhou a palavra: {word}!!!")

hangman()