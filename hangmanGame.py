# Hangman Game with predefined words
import random

# List of 5 predefined words
word_list = ['python', 'hangman', 'developer', 'computer', 'programming']

# Function to display the current state of the word (with underscores for unguessed letters)


def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the game


def play_hangman():
    # Choose a random word from the list
    word = random.choice(word_list)
    guessed_letters = set()  # Set of guessed letters
    incorrect_guesses = 0  # Number of incorrect guesses
    max_incorrect_guesses = 6  # Max allowed incorrect guesses

    print("Welcome to Hangman!")
    print("Guess the word. You have 6 incorrect guesses.")

    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        print("Word: " + display_word(word, guessed_letters))
        print(
            f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        # Get the player's guess
        guess = input("Enter a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # If the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the guessed letter to the set
        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! The letter {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! The letter {guess} is not in the word.")

        # Check if the word has been completely guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(
            f"Game over! You've used all your incorrect guesses. The word was: {word}")


# Start the game
if __name__ == "__main__":
    play_hangman()

# With GUI + predefined words
'''
import tkinter as tk
from tkinter import messagebox
import random

# List of predefined words
word_list = ['python', 'hangman', 'developer', 'computer', 'programming']


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = random.choice(word_list)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6

        self.create_widgets()

    def create_widgets(self):
        # Display word (with underscores for unguessed letters)
        self.word_label = tk.Label(
            self.root, text=self.get_display_word(), font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        # Label for incorrect guesses
        self.incorrect_label = tk.Label(
            self.root, text=f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}", font=("Helvetica", 14))
        self.incorrect_label.pack()

        # Buttons for each letter of the alphabet
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.letter_buttons = {}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            button = tk.Button(self.buttons_frame, text=letter, width=4, height=2,
                               command=lambda letter=letter: self.guess_letter(letter))
            button.grid(row=(ord(letter) - ord('a')) // 9,
                        column=(ord(letter) - ord('a')) % 9)
            self.letter_buttons[letter] = button

        # Reset button to restart the game
        self.reset_button = tk.Button(
            self.root, text="Restart Game", command=self.reset_game)
        self.reset_button.pack(pady=20)

    def guess_letter(self, letter):
        """Handles the logic when the user guesses a letter."""
        if letter in self.guessed_letters:
            return  # Do nothing if the letter was already guessed

        self.guessed_letters.add(letter)
        # Disable the button after the letter is guessed
        self.letter_buttons[letter].config(state=tk.DISABLED)

        if letter in self.word:
            self.update_word_label()
            if '_' not in self.get_display_word():
                self.end_game(won=True)
        else:
            self.incorrect_guesses += 1
            self.incorrect_label.config(
                text=f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")
            if self.incorrect_guesses == self.max_incorrect_guesses:
                self.end_game(won=False)

    def get_display_word(self):
        """Returns the word with guessed letters and underscores for unguessed ones."""
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def update_word_label(self):
        """Updates the word label with the current guessed word."""
        self.word_label.config(text=self.get_display_word())

    def end_game(self, won):
        """Ends the game and displays a message box."""
        if won:
            messagebox.showinfo("Congratulations!",
                                f"You've guessed the word: {self.word}")
        else:
            messagebox.showinfo(
                "Game Over", f"You've used all your guesses! The word was: {self.word}")
        self.reset_game()

    def reset_game(self):
        """Resets the game to a new word and clears guesses."""
        self.word = random.choice(word_list)
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.update_word_label()
        self.incorrect_label.config(
            text=f"Incorrect guesses left: {self.max_incorrect_guesses}")

        # Enable all buttons again
        for button in self.letter_buttons.values():
            button.config(state=tk.NORMAL)


# Create the main window
root = tk.Tk()

# Start the game
game = HangmanGame(root)

# Run the Tkinter event loop
root.mainloop()
'''

# GUI + Random words from API

'''
 import tkinter as tk
from tkinter import messagebox
import random
import requests

# Function to fetch a random word from the Datamuse API


def get_random_word():
    """Fetch a random word from the Datamuse API that starts with a random letter."""
    try:
        starting_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        response = requests.get(
            f"https://api.datamuse.com/words?sp={starting_letter}*&max=1000")

        if response.status_code != 200:
            return "python"  # fallback if API fails

        words = [word["word"] for word in response.json() if len(
            word["word"]) > 3 and word["word"].isalpha()]

        if not words:
            return "python"  # fallback if list is empty

        return random.choice(words)

    except Exception as e:
        print(f"API error: {e}")
        return "python"  # fallback if request fails

# Hangman game class


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = get_random_word().lower()
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6

        self.create_widgets()

    def create_widgets(self):
        # Display the word with underscores for unguessed letters
        self.word_label = tk.Label(
            self.root, text=self.get_display_word(), font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        # Display number of incorrect guesses left
        self.incorrect_label = tk.Label(
            self.root, text=f"Incorrect guesses left: {self.max_incorrect_guesses}", font=("Helvetica", 14))
        self.incorrect_label.pack()

        # Create buttons for letters A-Z
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=20)

        self.letter_buttons = {}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            btn = tk.Button(self.buttons_frame, text=letter, width=4, height=2,
                            command=lambda l=letter: self.guess_letter(l))
            btn.grid(row=(ord(letter) - ord('a')) // 9,
                     column=(ord(letter) - ord('a')) % 9)
            self.letter_buttons[letter] = btn

        # Reset/Restart button
        self.reset_button = tk.Button(
            self.root, text="Restart Game", command=self.reset_game)
        self.reset_button.pack(pady=20)

    def get_display_word(self):
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def update_word_label(self):
        self.word_label.config(text=self.get_display_word())

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return  # Already guessed

        self.guessed_letters.add(letter)
        self.letter_buttons[letter].config(state=tk.DISABLED)

        if letter in self.word:
            self.update_word_label()
            if '_' not in self.get_display_word():
                self.end_game(True)
        else:
            self.incorrect_guesses += 1
            self.incorrect_label.config(
                text=f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")
            if self.incorrect_guesses >= self.max_incorrect_guesses:
                self.end_game(False)

    def end_game(self, won):
        if won:
            messagebox.showinfo(
                "You Win!", f"Congratulations! You guessed the word: {self.word}")
        else:
            messagebox.showinfo(
                "Game Over", f"You lost! The word was: {self.word}")
        self.reset_game()

    def reset_game(self):
        self.word = get_random_word().lower()
        self.guessed_letters.clear()
        self.incorrect_guesses = 0
        self.update_word_label()
        self.incorrect_label.config(
            text=f"Incorrect guesses left: {self.max_incorrect_guesses}")
        for button in self.letter_buttons.values():
            button.config(state=tk.NORMAL)


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

'''
