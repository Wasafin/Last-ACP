import tkinter as tk
import random

# Main window setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Variables
user_choice = tk.StringVar()
computer_choice = tk.StringVar()
result = tk.StringVar()

# Function to play the game
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer = random.choice(options)
    computer_choice.set(f"Computer: {computer}")
    user_choice.set(f"You: {choice}")
    
    # Determine the winner
    if choice == computer:
        result.set("It's a Tie!")
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissors" and computer == "Paper"):
        result.set("You Win!")
    else:
        result.set("Computer Wins!")

# UI Components
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

# Buttons for Rock, Paper, and Scissors
rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Labels to display user choice, computer choice, and result
user_label = tk.Label(root, textvariable=user_choice, font=("Arial", 12))
user_label.pack()

computer_label = tk.Label(root, textvariable=computer_choice, font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, textvariable=result, font=("Arial", 16), fg="blue")
result_label.pack(pady=10)

# Start the application
root.mainloop()
