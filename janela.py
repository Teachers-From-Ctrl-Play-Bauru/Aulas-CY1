import tkinter as tk # importando modulo tkinter com o apelido de "tk" 

root = tk.Tk() # criando um >>objeto<< da classe TK()
root.geometry("300x600")

# criando um objeto da classe Label()
message = tk.Label(root, text = "hello, world!") 
message.pack()

root.mainloop() #mostrando a janela em looping