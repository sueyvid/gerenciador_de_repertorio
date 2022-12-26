import tkinter as tk

tela = tk.Tk("Gerenciador de Repertórios")
area_de_trabalho = tk.Frame(tela)
tTitulo = tk.Label(area_de_trabalho, text="Titulo 1", font=('', 32))
area_de_trabalho.pack()
tTitulo.pack()
tela.mainloop()