import customtkinter as ctk

# Configuração inicial da janela
root = ctk.CTk()
root.geometry("400x300")
root.title("Frame com Fundo Transparente")
root.configure(fg_color="red")
# Criando um frame com fundo transparente
frame = ctk.CTkFrame(root, fg_color="black")
frame.pack(pady=20, padx=20, expand=True)

# Adicionando widgets ao frame
label = ctk.CTkLabel(frame, text="Este é um frame com fundo transparente", text_color="black")
label.pack(pady=10)

button = ctk.CTkButton(frame, text="Clique aqui")
button.pack(pady=10)

# Iniciando o loop principal da interface
root.mainloop()