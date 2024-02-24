#!/usr/bin/env python

import os
from ascii_art import BANNER, HANGMAN_PICS


def clear_screen():
    """Clear the terminal screen"""
    os.system("clear")


def start_game():
    """Display the game banner and wait for the user to start the game"""
    print(BANNER)
    input("Press enter to start the game")
    clear_screen()


def render_board(guessed_word, incorrect_guesses):
    """Render the game board"""
    clear_screen()
    print("\n" * 3)
    print(HANGMAN_PICS[len(incorrect_guesses)], end="\n\n")
    print(" ".join(guessed_word), end="\n\n")
    print("Incorrect guesses:", " ".join(sorted(incorrect_guesses)), end="\n\n")
    print("\n" * 3)


def check_guess(current_guess, secret_word, guessed_word, incorrect_guesses):
    """Check the current guess and update the game state"""
    incorrect = True  # Flag toggled to false if the guess is correct

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

        # Main game loop, continues until the game is won or lost
        while True:
            render_board(guessed_word, incorrect_guesses)

            current_guess = input("Enter a letter: ").lower()

            # Updates `guessed_word` and `incorrect_guesses`
            check_guess(current_guess, secret_word, guessed_word, incorrect_guesses)

            # Test if lost
            if len(incorrect_guesses) == max_incorrect_guesses:
                render_board(guessed_word, incorrect_guesses)
                print("You lost! The word was", secret_word)
                break

            # Test if won
            if "_" not in guessed_word:
                render_board(guessed_word, incorrect_guesses)
                print("You won!")
                break

        # Offer to play again. If user declines, break outer loop and exit program
        play_again = input("Do you want to play again? (y/n): ").lower()
        clear_screen()
        if play_again != "y":
            print("Buh-bye!")
            break


if __name__ == "__main__":
    play_hangman()
