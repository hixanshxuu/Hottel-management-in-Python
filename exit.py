
import tkinter as tk
from tkinter import messagebox


class exit_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

def exit_application():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Create the main window
root = tk.Tk()

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.pack()

# Start the GUI event loop
root.mainloop()



if __name__ == '__main__':
    root=Tk()
    obj=exit_window(root)
    root.mainloop()