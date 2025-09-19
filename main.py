from tkinter import *
import ttkbootstrap as ttk
from scanner.gui import ApplicationGUI

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    ApplicationGUI(root)
    root.mainloop()