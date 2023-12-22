import tkinter as tk
from tkinter import ttk, COMMAND, PhotoImage
from .common_functions import *


class LoginAndRegisterPage(tk.Frame):
    def __init__(self, parent, go_to_welcome, type):
        tk.Frame.__init__(self, parent)

        self.go_back = go_to_welcome
        self['bg'] = MAIN_BG_COLOR
        self.page_type = ''
        self.function = None

        if type == 'Login Page':
            self.page_type = 'Login'
            self.function = self.login
        elif type == 'Register Page':
            self.page_type = 'Register'
            self.function = self.register_db

        self.logo_image = PhotoImage(file=LOGO_PATH)
        self.logo = self.create_logo()
        self.logo.pack()
        ttk.Label(self, text="Login to your account", style="BW.TLabel", font=("Arial", 12)).pack()

        # Add username and password fields, labels, and buttons
        self.user_label, self.username_entry = self.create_entry_and_entry(text='Username', label_style="BW.TLabel",
                                                                           entry_style="BW.TEntry")
        self.password_label, self.password_entry = self.create_entry_and_entry('Password', label_style="BW.TLabel",
                                                                               entry_style="BW.TEntry")
        self.approval_label, self.approval_entry = self.create_entry_and_entry('Manager Approval Code', label_style="BW.TLabel",
                                                                               entry_style="BW.TEntry")

        self.login_or_register_button = self.create_button(text=self.page_type, command=self.login)
        self.back_button = self.create_button(text='Back', command=self.clear_and_go_back)

        self.initiate_widgets()

    def create_entry_and_entry(self, text: str, label_style: str, entry_style: str):
        label = ttk.Label(self, text=text, style=label_style)
        entry = ttk.Entry(self, style=entry_style)
        return label, entry

    def create_button(self, text: str, command: COMMAND):
        button = ttk.Button(self, text=text, style="BW.TButton", command=command)
        return button

    def create_logo(self):
        logo = ttk.Label(self, image=self.logo_image, background='black')

        return logo

    def initiate_widgets(self):
        self.user_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        if self.page_type == 'Register':
            self.approval_label.pack()
            self.approval_entry.pack()
        self.login_or_register_button.pack()
        self.back_button.pack()

    def login(self):
        # Placeholder for login logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Attempt to login with:", username, password)

    def register_db(self):
        # Placeholder for login logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Attempt to login with:", username, password)

    def clear_and_go_back(self):
        self.pack_forget()
        self.go_back()
