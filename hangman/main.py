import tkinter as tk
from tkinter import messagebox
import random

# Daftar kata untuk permainan
word_list = ['PYTHON', 'JAVA', 'JAVASCRIPT', 'HTML', 'CSS', 'HANGMAN']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        self.word = random.choice(word_list)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0
        
        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, text="", font=('Helvetica', 24))
        self.word_label.pack(pady=20)
        
        self.guess_entry = tk.Entry(self.root, font=('Helvetica', 18))
        self.guess_entry.pack(pady=10)
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, font=('Helvetica', 18))
        self.guess_button.pack(pady=10)
        
        self.status_label = tk.Label(self.root, text="", font=('Helvetica', 18))
        self.status_label.pack(pady=20)
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=('Helvetica', 18))
        self.restart_button.pack(pady=10)
        self.restart_button.config(state=tk.DISABLED)

    def update_display(self):
        displayed_word = " ".join([letter if letter in self.guesses else "_" for letter in self.word])
        self.word_label.config(text=displayed_word)
        
        if "_" not in displayed_word:
            self.status_label.config(text="You Win!")
            self.restart_button.config(state=tk.NORMAL)
            self.guess_button.config(state=tk.DISABLED)
        elif self.attempts >= self.max_attempts:
            self.status_label.config(text="Game Over! The word was " + self.word)
            self.restart_button.config(state=tk.NORMAL)
            self.guess_button.config(state=tk.DISABLED)

    def make_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)
        
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        if guess in self.guesses:
            messagebox.showinfo("Already Guessed", "You've already guessed that letter.")
            return
        
        self.guesses.append(guess)
        
        if guess not in self.word:
            self.attempts += 1
        
        self.update_display()

    def restart_game(self):
        self.word = random.choice(word_list)
        self.guesses = []
        self.attempts = 0
        self.update_display()
        self.restart_button.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
