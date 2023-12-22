import tkinter as tk
from tkinter import ttk, PhotoImage, COMMAND
from .login_and_register_page import LoginAndRegisterPage
from .register_page import RegisterPage
from .common_functions import *


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("800x800")
        self.root['bg'] = 'black'

        self.current_page = ''
        self.configure_styles()
        self.welcome_label = self.create_welcome_label()

        # Add logo here
        self.logo_image = PhotoImage(file=LOGO_PATH)
        self.logo = self.create_logo()

        self.login_button = self.create_button(text="Login", style="BW.TButton", command=self.login)
        self.register_button = self.create_button(text="Register", style="BW.TButton", command=self.register)
        self.about_button = self.create_button(text="About", style="BW.TButton", command=self.about)

        self.login_page = LoginAndRegisterPage(self.root, self.show_welcome_page, page_type='Login')
        self.register_page = LoginAndRegisterPage(self.root, self.show_welcome_page, page_type='Register')

        self.show_welcome_page()

    def show_welcome_page(self):
        self.welcome_label.pack()
        self.logo.pack()
        self.login_button.pack()
        self.register_button.pack()
        self.about_button.pack()

    def create_welcome_label(self):
        welcome_label = ttk.Label(self.root, text="Welcome to Login System", style="BW.TLabel", font=('Arial Bold', 40))
        return welcome_label

    def create_logo(self):
        logo = ttk.Label(self.root, image=self.logo_image, background='black')
        return logo

    @staticmethod
    def configure_styles():
        style = ttk.Style()
        style.configure("BW.TButton", foreground=MAIN_BUTTON_COLOR, background=MAIN_BG_COLOR, font=('Arial', 12))
        style.configure("BW.TLabel", foreground=LOGO_COLOR, background=MAIN_BG_COLOR)
        style.configure("BW.TEntry", foreground=LOGO_COLOR, background=MAIN_BG_COLOR)
        style.configure("BW.TRadiobutton", foreground=LOGO_COLOR, background=MAIN_BG_COLOR)
        style.configure("BW.TRegister", foreground=LOGO_COLOR, background=MAIN_BG_COLOR)
        style.configure("BW.TBack", foreground=LOGO_COLOR, background=MAIN_BG_COLOR)

    def create_button(self, text: str, style: str, command: COMMAND):
        button = ttk.Button(self.root, text=text, style=style, command=command)
        return button

    def hide_all_frames(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def login(self):
        self.hide_all_frames()
        self.current_page = "login"
        self.login_page.pack(fill='both', expand=True)

    def register(self):
        self.hide_all_frames()
        self.current_page = "register"
        self.register_page.pack(fill='both', expand=True)

    def about(self):
        print("about")
