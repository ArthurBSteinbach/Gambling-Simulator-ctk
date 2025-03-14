import customtkinter as ctk
import os
import json
import sys
import pywinstyles
from PIL import Image, ImageTk

import customtkinter as ctk

class Menu:
    def __init__(self, app_instance):
        self.app = app_instance
        self.create_widgets()

    def create_widgets(self):
        label = ctk.CTkLabel(self.app, text="Texto do Menu", font=("Arial", 16))
        label.pack(pady=20)

        button = ctk.CTkButton(self.app, text="Clique aqui", command=self.on_button_click)
        button.pack(pady=10)

    def on_button_click(self):
        print("Botão clicado!")