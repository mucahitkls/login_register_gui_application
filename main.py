import tkinter as tk
from gui.main_application import MainApplication


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()