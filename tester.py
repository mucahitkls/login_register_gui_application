import tkinter as tk
from tkinter import ttk, PhotoImage
from gui.common_functions import *

class LoginAndRegisterPage(tk.Frame):
    def __init__(self, parent, go_to_welcome, page_type):
        super().__init__(parent, bg=MAIN_BG_COLOR)

        self.go_back = go_to_welcome
        self.page_type = page_type
        self.function = self.login if page_type == 'Login' else self.register_db

        self.logo_image = PhotoImage(file=LOGO_PATH)
        self.logo = ttk.Label(self, image=self.logo_image, background='black')
        self.logo.pack()

        ttk.Label(self, text=f"{page_type} to your account", style="BW.TLabel", font=("Arial", 12)).pack()

        # Add username and password fields, labels, and buttons
        self.user_label, self.username_entry = self.create_label_and_entry('Username')
        self.password_label, self.password_entry = self.create_label_and_entry('Password')
        self.approval_label, self.approval_entry = self.create_label_and_entry('Manager Approval Code')

        self.login_or_register_button = ttk.Button(self, text=page_type, style="BW.TButton", command=self.function)
        self.back_button = ttk.Button(self, text='Back', style="BW.TButton", command=self.clear_and_go_back)

        self.initiate_widgets()

    def create_label_and_entry(self, text: str):
        label = ttk.Label(self, text=text, style="BW.TLabel")
        entry = ttk.Entry(self, style="BW.TEntry")
        return label, entry

    def initiate_widgets(self):
        widgets = [self.user_label, self.username_entry, self.password_label, self.password_entry]
        if self.page_type == 'Register':
            widgets += [self.approval_label, self.approval_entry]
        widgets += [self.login_or_register_button, self.back_button]

        for widget in widgets:
            widget.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Attempt to login with:", username, password)
        # Implement your login logic here

    def register_db(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        approval = self.approval_entry.get() if self.page_type == 'Register' else None
        print("Attempt to register with:", username, password, "Approval:", approval)
        # Implement your registration logic here

    def clear_and_go_back(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.go_back()
