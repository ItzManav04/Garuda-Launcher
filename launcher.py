import tkinter as tk

root = tk.Tk()
root.title("Garuda Launcher")
root.geometry("500x300")

title = tk.Label(
    root,
    text="GARUDA LAUNCHER",
    font=("Arial", 24, "bold")
)
title.pack(pady=50)

play = tk.Button(
    root,
    text="PLAY MINECRAFT",
    font=("Arial", 14),
    width=20
)
play.pack()

root.mainloop()
