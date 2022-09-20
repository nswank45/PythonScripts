"""A hangman game
"""
import random

import requests
from typing import NamedTuple

Difficulty = NamedTuple("Difficulty", [("max_word_length", int), ("guesses", int)])

web_string = "http://random-word-api.herokuapp.com/word?length={}"


def play_hangman(difficulty):
    """
    Play a game of hangman
    """
    # get a random word from the api
    print("Welcome to Hangman!")
    response = requests.get(web_string.format(random.randint(3, difficulty.max_word_length+1)))
    word = response.text.upper()[2:-2]
    found_letters = {letter: False for letter in word}
    guessed_wrong = set()
    print(f"The word is {len(word)} letters long.")
    print("You have {} guesses.".format(difficulty.guesses))
    print("You can guess letters or the whole word.")
    print("The word is: {}".format("".join(letter if found_letters[letter] else "_" for letter in word)))
    print("Guess the word!")
    print()
    num_of_guesses = 0
    while num_of_guesses < difficulty.guesses:
        guess = None
        while guess is None:
            attempt = input("Guess a letter: ").upper()
            if len(attempt) == 1 and attempt.isalpha():
                if attempt in found_letters and found_letters[attempt] or attempt in guessed_wrong:
                    print("You already guessed that letter")
                else:
                    guess = attempt
            elif len(attempt) == len(word):
                if attempt == word:
                    print("You guessed the word!\n")
                    return
            else:
                print("Invalid input")
        if guess in found_letters:
            found_letters[guess] = True
        else:
            print("Wrong guess")
            guessed_wrong.add(guess)
            num_of_guesses += 1
        if all(found_letters.values()):
            print("You win!\n")
            break
        else:
            print("You have {} guesses left".format(difficulty.guesses - num_of_guesses))
            print("The word is: {}".format("".join(letter if found_letters[letter] else "_" for letter in word)))
    else:
        print("You lose!")
        print("The word was: {}\n".format(word))


if __name__ == "__main__":
    levels = [
        Difficulty(max_word_length=5, guesses=6),
        Difficulty(max_word_length=6, guesses=6),
        Difficulty(max_word_length=7, guesses=5),
        Difficulty(max_word_length=8, guesses=5),
        Difficulty(max_word_length=9, guesses=4),
        Difficulty(max_word_length=10, guesses=4),
        Difficulty(max_word_length=11, guesses=3),
        Difficulty(max_word_length=12, guesses=3)
    ]
    for level in levels:
        play_hangman(level)