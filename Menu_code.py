import tkinter as tk
import socket
import threading
from Server_riddle import server_game_riddle
from Client_riddle import client_game_riddle
from Script_riddle_client import Run_Script
from Script_riddle_server import Run_Script_server
import os

# Main menu window


def main_menu():
    root = tk.Tk()
    root.title("Riddle Option Select")

    heading = tk.Label(root, text="Welcome to Riddles ✅",
                       font=("Arial", 20, "bold"))
    heading.pack(pady=20)

    root.geometry("500x500")
    root.configure(bg="lightblue")

    # Create buttons to start different games
    riddle_game_button_client = tk.Button(
        root, text="Start Riddle for player 1", command=Run_Script, font=("Ariral", 16), width=20, height=5)
    riddle_game_button_client.pack(padx=30, pady=30)

    riddle_game_button_client = tk.Button(
        root, text="Start Riddle for player 2", command=Run_Script, font=("Ariral", 16), width=20, height=5)
    riddle_game_button_client.pack(padx=30, pady=30)

    riddle_game_button_server = tk.Button(
        root, text="Start Riddle Server", command=Run_Script_server, font=("Ariral", 16), width=20, height=5)
    riddle_game_button_server.pack(padx=30, pady=30)

    root.mainloop()


if __name__ == "__main__":
    main_menu()
