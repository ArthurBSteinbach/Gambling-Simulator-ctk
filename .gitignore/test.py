import customtkinter as ctk
from tkinter import font

index = 0

def atualizar_label(operator):
    global index
    fontes = list(font.families())
    
    if operator == 1:  
        index += 1
    else:  
        index -= 1

    if index >= len(fontes):  
        index = 0
    elif index < 0:  
        index = len(fontes) - 1
    
    fonte_aleatoria = fontes[index]  
    label_fontes.configure(text=fonte_aleatoria, font=(fonte_aleatoria, 16))  
    index_label.configure(text=index)

    if len(fontes) > 19:
        fonte_19 = fontes[19]
        label_fonte_19.configure(text="LOREM IPSUM BOLDER\nabcdefghijklmnopqrstuvwxyz", font=(fonte_aleatoria, 16)) 
    else:
        label_fonte_19.configure(text="Fonte 19 não disponível", font=("Arial", 16))

    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;':\",.<>?/"
    label_caracteres_especiais.configure(text=caracteres_especiais, font=(fonte_aleatoria, 16))  

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Fontes Instaladas")
root.geometry("500x300")  # Aumentei a altura para acomodar as novas labels

label_fontes = ctk.CTkLabel(root, text="", text_color="white", justify="center")
label_fontes.pack(pady=20)

# Nova label para a fonte na posição 19
label_fonte_19 = ctk.CTkLabel(root, text="", text_color="white", justify="center")
label_fonte_19.pack(pady=10)

# Nova label para caracteres especiais
label_caracteres_especiais = ctk.CTkLabel(root, text="", text_color="white", justify="center")
label_caracteres_especiais.pack(pady=10)

root_botões = ctk.CTkFrame(root)
root_botões.pack(pady=10)

botao_menos = ctk.CTkButton(root_botões, text="-", command=lambda: atualizar_label(0), width=40, font=("Arial", 16, "bold"))
botao_menos.grid(row=0, column=1, padx=5)

botao_mais = ctk.CTkButton(root_botões, text="+", command=lambda: atualizar_label(1), width=40, font=("Arial", 16, "bold"))
botao_mais.grid(row=0, column=2, padx=5)

index_label = ctk.CTkLabel(root, text=index, font=("Arial", 16, "bold"))
index_label.pack()

root.mainloop()