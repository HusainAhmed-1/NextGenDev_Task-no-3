import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x400")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        self.user_choice = tk.StringVar()
        self.result_text = tk.StringVar()
        self.score_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Rock Paper Scissors", font=('arial', 20, 'bold'))
        title.pack(pady=10)

        # Buttons for user choices
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: self.play("Rock"))
        rock_button.grid(row=0, column=0, padx=5)

        paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: self.play("Paper"))
        paper_button.grid(row=0, column=1, padx=5)

        scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: self.play("Scissors"))
        scissors_button.grid(row=0, column=2, padx=5)

        # Result display
        result_label = tk.Label(self.root, textvariable=self.result_text, font=('arial', 16))
        result_label.pack(pady=20)

        # Score display
        score_label = tk.Label(self.root, textvariable=self.score_text, font=('arial', 16))
        score_label.pack(pady=10)
        self.update_score()

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.result_text.set(f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}")
        self.update_score()

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def update_score(self):
        self.score_text.set(f"Score:\nYou: {self.user_score} - Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    RockPaperScissors(root)
    root.mainloop()
