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


def generate_word():
    return choice(WORDS)


def solved(word, used_letters):
    for c in word:
        if c not in used_letters:
            return False
    return True


def main():
    used_letters = set()
    mistakes = 0
    word = generate_word()
    update_display(word, used_letters, mistakes)
    while True:
        guess = input().lower()[0]
        used_letters.add(guess)
        if guess not in word:
            update_display(word, used_letters, mistakes, message=f"{guess} is not in the word!")
            mistakes += 1
        else:
            update_display(word, used_letters, mistakes, message=f"{guess} is a letter in the word!")
        if mistakes >= len(stands):
            show_lose_screen(word)
            break
        if solved(word, used_letters):
            show_win_screen(word)
            break


if __name__ == "__main__":
    main()
