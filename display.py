import os
from string import ascii_lowercase


STANDS = [
    r'''
    --------
    |   |
    |   
    |   
    |   
    ----------
    ''',
    
    r'''
    --------
    |   |
    |   O
    |   
    |   
    ----------
    ''',
    
    r'''
    --------
    |   |
    |   O
    |   |
    |   
    ----------
    ''',
    
    r'''
    --------
    |   |
    |   O
    |  /|
    |   
    ----------
    ''',
    
    r'''
    --------
    |   |
    |   O
    |  /|\
    |   
    ----------
    ''',
    
    r'''
    ---------
    |   |
    |   O
    |  /|\
    |  / 
    ----------
    ''',
    
    r'''
    --------
    |   |
    |   O
    |  /|\
    |  / \
    ----------
    '''
]


def clear_scr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_stand(index: int):
    stand = stands[index]
    print(stand)
    print()


def print_word(word: str, used_letters: list[str]):
    print_word = ' '.join((c if c in used_letters or c == ' ' else '_') for c in word)
    print(print_word)


def print_alphabet(used_letters):
    print()
    print(' '.join(c for c in ascii_lowercase if c not in used_letters))


def show_win_screen(word):
    clear_scr()
    print("You Win!")
    print(f"The word was {word}")


def show_lose_screen(word):
    clear_scr()
    print("You Lose!")
    print(f"The word was {word}")


def update_display(word, used_letters, count_wrong, message=''):
    clear_scr()
    print(message)
    print()
    print_stand(count_wrong)
    print_word(word, used_letters)
    print_alphabet(used_letters)
