import tkinter as tk

def open_second_window():
    root.withdraw()  # Hide the main window
    second_window.deiconify()  # Show the second window

def back_to_main():
    second_window.withdraw()  # Hide the second window
    root.deiconify()  # Show the main window

# Main window
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

open_button = tk.Button(root, text="Go to Second Window", command=open_second_window)
open_button.pack(expand=True)

# Second window (start hidden)
second_window = tk.Toplevel(root)
second_window.title("Second Window")
second_window.geometry("300x200")
second_window.withdraw()  # Hide it initially

back_button = tk.Button(second_window, text="Back to Main Window", command=back_to_main)
back_button.pack(expand=True)

root.mainloop()
