import tkinter as tk
import socket
import threading
from Script_TTT_server import Run_Script_TTT_server
from Script_TTT_client import Run_Script_TTT_client
import os

# Function to start the riddle game


def TTT_server():
    Run_Script_TTT_server()


def TTT_client():
    Run_Script_TTT_client()


# Main menu window
def main_menu():
    root = tk.Tk()
    root.title("Tic-Tac-Toe Option Select")

    heading = tk.Label(root, text="Welcome to Tic-Tac-Toe ❌ 🅾️",
                       font=("Arial", 20, "bold"))
    heading.pack(pady=20)

    root.geometry("500x500")
    root.configure(bg="lightblue")

    # Different Game options

    TTT_game_button_client = tk.Button(
        root, text="Start Tic-Tac-Toe for player 1", command=TTT_client, font=("Ariral", 16), width=20, height=5)
    TTT_game_button_client.pack(padx=30, pady=30)

    TTT_game_button_client = tk.Button(
        root, text="Start Tic-Tac-Toe for player 2", command=TTT_client, font=("Ariral", 16), width=20, height=5)
    TTT_game_button_client.pack(padx=30, pady=30)

    TTT_game_button_server = tk.Button(
        root, text="Start Tic-Tac-Toe Server", command=TTT_server, font=("Ariral", 16), width=20, height=5)
    TTT_game_button_server.pack(padx=30, pady=30)

    root.mainloop()


if __name__ == "__main__":
    main_menu()
