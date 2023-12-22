import tkinter as tk
from .login_page import LoginPage
from .register_page import RegisterPage


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("400x300")

        # self.login_page = LoginPage(self.root)
        # self.login_page.pack(fill='both', expand=True)
        #
        # self.register_page = RegisterPage(self.root)
        # self.register_page.pack(fill='both', expand=True)