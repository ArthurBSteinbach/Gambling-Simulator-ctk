import customtkinter as ctk
from tkinter import font
import random

# Função para obter todas as fontes instaladas
def obter_fontes():
    return list(font.families())

# Função para atualizar a label com uma fonte aleatória
def atualizar_label():
    fontes = obter_fontes()
    fonte_aleatoria = random.choice(fontes)  # Escolhe uma fonte aleatória
    label_fontes.configure(text=fonte_aleatoria, font=(fonte_aleatoria, 16))  # Atualiza a label com a fonte escolhida

# configureuração da janela principal
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

janela = ctk.CTk()
janela.title("Fontes Instaladas")
janela.geometry("400x200")

# Label para exibir a fonte
label_fontes = ctk.CTkLabel(janela, text="", text_color="white", justify="center")
label_fontes.pack(pady=20)

# Botão para atualizar a fonte
botao_atualizar = ctk.CTkButton(janela, text="Mostrar Fonte Aleatória", command=atualizar_label)
botao_atualizar.pack(pady=10)

# Iniciar a aplicação
janela.mainloop()