from random import choice


WORDS = {
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
}


def generate_word():
    return choice(WORDS)


def guess(char, word):
    # add letters if correct
    if char in word:
        add_letter_to_word(char)
    # update hangman and record incorrect letter
    else:
        hangman_state += 1
        hangman(hangman_state)
        record_incorrect_letter(char)
