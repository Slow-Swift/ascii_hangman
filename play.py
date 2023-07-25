from display import update_display
from display import stands
from random import choice


WORDS = [
    "word",
    "chatgpt",
    "finain",
    "jacob",
    "ask",
    "bed",
    "chair",
    "friend",
    "lipoprotein",
    "computer",
    "intelligence",
    "investigation",
    "isle",
    "cat",
    "wire",
    "electricty",
    "unsubstatiate",
    "song",
    "poem",
    "eye",
    "sky",
    "tea",
    "snake",
    "hope",
    "meaning",
    "change",
    "transformation",
    "illustration",
    "future",
    "monster",
    "self",
    "code",
    "gene",
    "algorithm",
    "structure",
    "movement",
    "water",
    "shape",
    "python",
    "c",
    "language",
    "mind",
]


def generate_word():
    return choice(WORDS)

def main():
    used_letters = {}
    mistakes = 0
    word = generate_word()
    while True:
        update_display(word, used_letters, mistakes)
        guess = input()[0]
        if guess not in word:
            update_display(word, used_letters, mistakes, message=f"{guess} is not in the word!")
            mistakes += 1
        if mistakes == len(stands):
            show_lose_screen(word)
        if solved(word, used_letters):
            show_win_screen(word)
