import random
import tkinter as tk
from tkinter import messagebox
import time

class SimonGame:
    def __init__(self, root):
        self.root = root
        self.sequence = []
        self.player_sequence = []
        self.colors = ['red', 'green', 'blue', 'yellow']
        self.score = 0
        self.highest_score = 0
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start", command=self.play)
        self.start_button.pack()

        self.color_buttons = []
        for color in self.colors:
            button = tk.Button(self.root, bg=color, width=10, height=5, command=lambda c=color: self.click_color(c))
            button.pack()
            self.color_buttons.append(button)

        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

    def play(self):
        self.start_button.config(state=tk.DISABLED)
        self.sequence = []
        self.score = 0
        self.game_over = False
        self.status_label.config(text="Watch the sequence...")
        self.root.update()
        time.sleep(1)

        while not self.game_over:
            self.generate_sequence()
            self.display_sequence()
            self.get_player_input()
            self.check_sequence()

        self.start_button.config(state=tk.NORMAL)

    def generate_sequence(self):
        self.sequence.append(random.choice(self.colors))

    def display_sequence(self):
        for color in self.sequence:
            self.flash_color(color)
            time.sleep(0.5)
            self.root.update()
            time.sleep(0.5)

    def flash_color(self, color):
        for button in self.color_buttons:
            if button.cget("bg") == color:
                button.config(bg="white")
                self.root.update()
                time.sleep(0.5)
                button.config(bg=color)
                self.root.update()

    def get_player_input(self):
        self.status_label.config(text="Your turn!")
        self.player_sequence = []

        for button in self.color_buttons:
            button.config(state=tk.NORMAL)

    def click_color(self, color):
        self.player_sequence.append(color)
        if len(self.player_sequence) == len(self.sequence):
            self.check_sequence()

    def check_sequence(self):
        if self.player_sequence == self.sequence:
            self.score += 1
            self.status_label.config(text=f"Correct! Your score is now: {self.score}")
            if self.score > self.highest_score:
                self.highest_score = self.score
                self.status_label.config(text=f"Correct! Your score is now: {self.score}\nCongratulations! You've achieved a new highest score!")
            self.root.update()
            time.sleep(1)
        else:
            messagebox.showinfo("Game Over", f"Incorrect! Game over. Your final score is: {self.score}\nHighest score: {self.highest_score}")
            self.game_over = True

            for button in self.color_buttons:
                button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.title("Simon Game")
    game = SimonGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
