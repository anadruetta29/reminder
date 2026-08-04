import time
import tkinter as tk
from tkinter import messagebox
import threading


def show_alert():
    root = tk.Tk()
    root.withdraw()

    answer = messagebox.showwarning(
        "¡Bianca recordá guardar tus cambios!"
    )
    root.destroy()


def reminders():
    while True:
        time.sleep(600)
        show_alert()


if __name__ == "__main__":
    thread = threading.Thread(target=reminders(), daemon=True)
    thread.start()

    print("Corriendo en segundo plano...")
    while True:
        time.sleep(1)