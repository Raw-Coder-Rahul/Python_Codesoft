import random
import tkinter as tk
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Your Score: 0 | Computer Score: 0")
    messagebox.showinfo("Game Reset", "Scores have been reset!")

def main():
    global result_label, score_label

    window = tk.Tk()
    window.title("Rock-Paper-Scissors Game")
    window.geometry("400x300")
    window.configure(bg="#F0F0F0")

    title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#F0F0F0")
    title_label.pack(pady=10)

    instruction_label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 12), bg="#F0F0F0")
    instruction_label.pack(pady=5)

    button_frame = tk.Frame(window, bg="#F0F0F0")
    button_frame.pack(pady=10)

    rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 12), bg="#FF5733", fg="white", command=lambda: play_game("Rock"))
    rock_button.grid(row=0, column=0, padx=5)

    paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 12), bg="#33CFFF", fg="white", command=lambda: play_game("Paper"))
    paper_button.grid(row=0, column=1, padx=5)

    scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 12), bg="#75FF33", fg="white", command=lambda: play_game("Scissors"))
    scissors_button.grid(row=0, column=2, padx=5)

    result_label = tk.Label(window, text="", font=("Helvetica", 12), bg="#F0F0F0")
    result_label.pack(pady=5)

    score_label = tk.Label(window, text="Your Score: 0 | Computer Score: 0", font=("Helvetica", 12), bg="#F0F0F0")
    score_label.pack(pady=5)

    reset_button = tk.Button(window, text="Reset Game", font=("Helvetica", 12, "bold"), bg="#f44336", fg="white", command=reset_game)
    reset_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
