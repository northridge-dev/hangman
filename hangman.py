#!/usr/bin/env python

import os
from ascii_art import BANNER, HANGMAN_PICS

"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - If you try to write all the code in `play_hangman`, 
    it's going to be a mess. Instead, break your logic
    into smaller functions that you can call from 
    `play_hangman`.

Run your code from the terminal:
  - make sure you're in the right directory (`projects/hangman`)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: python hangman.py

Tests? No tests for this project. 
"""


def clear_screen():
    os.system("clear")


def start_game():
    print(BANNER)
    input("Press enter to start the game")
    clear_screen()


def render_board(guessed_word, incorrect_guesses):
    clear_screen()
    print("\n" * 3)
    print(HANGMAN_PICS[len(incorrect_guesses)], end="\n\n")
    print(" ".join(guessed_word), end="\n\n")
    print("Incorrect guesses:", " ".join(sorted(incorrect_guesses)), end="\n\n")
    print("\n" * 3)


def check_guess(current_guess, secret_word, guessed_word, incorrect_guesses):
    incorrect = True

    for i, letter in enumerate(secret_word):
        if letter == current_guess:
            incorrect = False
            guessed_word[i] = current_guess

    if incorrect:
        incorrect_guesses.append(current_guess)


def play_hangman():
    start_game()

    # Outer loop, to play multiple games
    while True:
        secret_word = input("Enter the secret word: ").lower()
        guessed_word = ["_"] * len(secret_word)
        incorrect_guesses = []
        max_incorrect_guesses = len(HANGMAN_PICS) - 1

        while len(incorrect_guesses) < max_incorrect_guesses:
            render_board(guessed_word, incorrect_guesses)
            current_guess = input("Enter a letter: ").lower()
            check_guess(current_guess, secret_word, guessed_word, incorrect_guesses)

            if len(incorrect_guesses) == max_incorrect_guesses:
                render_board(guessed_word, incorrect_guesses)
                print("You lost! The word was", secret_word)
                break
            if "_" not in guessed_word:
                render_board(guessed_word, incorrect_guesses)
                print("You won!")
                break

        play_again = input("Do you want to play again? (y/n): ").lower()
        clear_screen()
        if play_again != "y":
            break


if __name__ == "__main__":
    play_hangman()
