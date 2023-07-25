from display import show_win_screen, show_lose_screen, update_display, stands
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


def main():
    used_letters = set()
    mistakes = 0
    word = choice(WORDS)
    update_display(word, used_letters, mistakes)
    while True:
        guess = input().lower()[0]
        used_letters.add(guess)
        if guess not in word:
            mistakes += 1
            update_display(word, used_letters, mistakes, message=f"{guess} is not in the word!")
        else:
            update_display(word, used_letters, mistakes, message=f"{guess} is a letter in the word!")
        if mistakes >= len(stands):
            show_lose_screen(word)
            break
        if all(char in used_letters for char in word):
            show_win_screen(word)
            break


if __name__ == "__main__":
    main()
