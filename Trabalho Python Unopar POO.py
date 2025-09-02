import tkinter as tk

# Função que será chamada quando uma tecla for pressionada
def tecla_pressionada(evento):
    print(f"Tecla pressionada: {evento.keysym}")  # Mostra no terminal do IDLE

# Criando a janela principal
janela = tk.Tk()
janela.title("Detecção de Teclas - Tkinter")
janela.geometry("400x200")

# Texto de instrução na janela
label = tk.Label(janela, text="Digite algo no teclado.\nAs teclas pressionadas aparecerão no terminal do IDLE.",
                 font=("Arial", 12), wraplength=350, justify="center")
label.pack(expand=True)

# Vincula o evento de tecla pressionada à função
janela.bind("<Key>", tecla_pressionada)

# Mantém a janela aberta
janela.mainloop()
