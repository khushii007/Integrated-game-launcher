import tkinter as tk
from tkinter import *
import socket
import threading
import os

# Function to start the riddle game

command4 = "python /Users/adityakhurana/Developer/CN_Proj_new/Menu_code.py"
command5 = "python /Users/adityakhurana/Developer/CN_Proj_new/Menu_code_TTT.py"


def Play_riddle():
    os.system(
        f"osascript -e 'tell app \"Terminal\" to do script \"{command4}\"'")


def Play_TTT():
    os.system(
        f"osascript -e 'tell app \"Terminal\" to do script \"{command5}\"'")


# Main menu window
def main_menu():
    root = tk.Tk()
    root.title("Choose a game")

    heading = tk.Label(root, text="Welcome to The Game Selector 🕹️",
                       font=("Arial", 20, "bold"))
    heading.pack(pady=20)

    root.geometry("400x350")
    root.configure(bg="lightblue")

    Game_button_riddle = tk.Button(
        root, text="Play Riddles", command=Play_riddle, font=("Ariral", 16), width=15, height=3)
    Game_button_riddle.pack(padx=20, pady=30)

    Game_button_TTT = tk.Button(
        root, text="Play TicTacToe", command=Play_TTT, font=("Ariral", 16), width=15, height=3)
    Game_button_TTT.pack(padx=20, pady=30)

    root.mainloop()


if __name__ == "__main__":
    main_menu()
