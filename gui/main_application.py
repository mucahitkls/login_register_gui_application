import tkinter as tk
from tkinter import ttk, PhotoImage
from .login_page import LoginPage
from .register_page import RegisterPage


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
        self.logo_image = PhotoImage(file='custom/images/login_system_logo.png')
        self.logo = self.create_logo()

        self.login_button = self.create_login_button()
        self.register_button = self.create_register_button()
        self.about_button = self.create_about_button()

        self.login_page = LoginPage(self.root, self.show_welcome_page)
        self.register_page = RegisterPage(self.root, self.show_welcome_page)

        self.show_welcome_page()

    def show_welcome_page(self):
        self.welcome_label.pack()
        self.logo.pack()
        self.login_button.pack()
        self.register_button.pack()
        self.about_button.pack()

    def create_welcome_label(self):
        style1 = ttk.Style()
        style1.configure("BW.TLabel", foreground="#b07a4b", background="black")
        welcome_label = ttk.Label(self.root, text="Welcome to Login System", style="BW.TLabel",
                                  font=('Arial Bold', 40))
        return welcome_label

    def create_logo(self):
        logo = ttk.Label(self.root, image=self.logo_image, background='black', )
        return logo

    @staticmethod
    def configure_styles():
        style = ttk.Style()
        style.configure("BW.TButton", foreground="green", background="black")
        style.configure("BW.TLabel", foreground="#b07a4b", background="black")

    def create_login_button(self):
        # style2 = ttk.Style()
        # style2.configure("BW.TButton", foreground="green", background="black")
        login_button = ttk.Button(self.root, text="Login", style="BW.TButton", command=self.login)
        return login_button

    def create_register_button(self):
        # style2 = ttk.Style()
        # style2.configure("BW.TButton", foreground="green", background="black")
        register_button = ttk.Button(self.root, text="Register", style="BW.TButton", command=self.register)
        return register_button

    def create_about_button(self):
        # style2 = ttk.Style()
        # style2.configure("BW.TButton", foreground="green", background="black")
        about_button = ttk.Button(self.root, text="About", command=self.about)
        return about_button

    def hide_all_frames(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def go_back_to_welcome(self):
        if self.current_page == "login":
            self.login_page.clear_and_go_back()
        elif self.current_page == "register":
            self.register_page.clear_and_go_back()
        self.show_welcome_page()

    def login(self):
        self.hide_all_frames()
        self.current_page = "login"
        self.login_page.pack(fill='both', expand=True)

    def register(self):
        self.hide_all_frames()
        self.current_page = "register"
        self.register_page.pack(fill='both', expand=True)

    def about(self):
        ...
