import tkinter as tk
from tkinter import ttk

class LoginPage(tk.Frame):
    def __init__(self, parent, go_to_welcome):
        tk.Frame.__init__(self, parent)
        self.go_back = go_to_welcome
        # Add username and password fields, labels, and buttons
        tk.Label(self, text="Username:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", command=self.login).pack()
        tk.Button(self, text="Go Back", command=self.clear_and_go_back).pack()

    def login(self):
        # Placeholder for login logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Attempt to login with:", username, password)

    def clear_and_go_back(self):
        self.pack_forget()
        self.go_back()