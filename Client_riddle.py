import socket
import tkinter as tk
import subprocess


def client_game_riddle():

    def receive_riddle(sock):
        riddle = sock.recv(1024).decode()
        riddle_label.config(text=riddle)

    def send_answer():
        answer = answer_entry.get()
        answer_entry.delete(0, tk.END)  # Clear the entry field
        client_socket.send(answer.encode())
        feedback = client_socket.recv(1024).decode()
        feedback_label.config(text=feedback)

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Riddle Game")

    root.geometry("300x300")
    root.configure(bg="lightblue")

    # # Create GUI elements
    riddle_label = tk.Label(
        root, text="Riddle will appear here", wraplength=300, font=("Arial", 15))
    riddle_label.pack()

    answer_entry = tk.Entry(root)
    answer_entry.pack(padx=10, pady=10)

    submit_button = tk.Button(
        root, text="Submit Answer", command=send_answer, bg="blue", font=("Arial", 15), height=2, width=10)
    submit_button.pack(padx=10, pady=10)

    feedback_label = tk.Label(
        root, text="", fg="red", width=10, height=3, font=("Arial", 10), bg="lightgreen")
    feedback_label.pack(padx=2, pady=2)

    # # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 32007))

    # Receive and display the first riddle
    receive_riddle(client_socket)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    client_game_riddle()
