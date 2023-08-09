from tkinter import *
import tkinter as tk 
from tkinter import ttk 

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer.pack()

   

        self.rodape = Label(self.primeiroContainer, bg="#274360")
        self.rodape["padx"] = 348
        self.rodape["pady"] = 18
        self.rodape.pack()

        foto = tk.PhotoImage(file="amhplogo.png")
        self.img = tk.Label(self.segundoContainer,image=foto)
        self.img.foto = foto
        self.img.pack()

        self.nomeLabel = Label(self.quartoContainer, text="Selecione a automação",font=self.fontePadrao)
        self.nomeLabel["background"] = 'white'
        self.nomeLabel.pack(side=LEFT)


        self.comboBox = ttk.Combobox(self.quintoContainer, 
                                     values= ["Auditoria Geap","Anexar Honorario Geap","Teste"],
                                     width=50)
        self.comboBox["background"] = 'white'
        self.comboBox.pack(side=LEFT)




root = tk.Tk()
Application(root)
root.title('Automação')
root.geometry("700x500")
root.resizable(width=0, height=0)
root.configure(bg='white')

root.mainloop()