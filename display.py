import os
import sys

stands = [
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
    print(stand, end='\r')
    print()
    
def print_word(word: str, used_letters: list[str]):
    print_word = ' '.join((c if c in used_letters or c == ' ' else '_') for c in word)
    print(print_word)

def update_display(word, used_letters, count_wrong):
    clear_scr()
    print_stand(count_wrong)
    print_word(word, used_letters)
    

if __name__ == "__main__":
    update_display('hello world', {'l', 'o', 'z'}, 1)
    