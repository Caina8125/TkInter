from tkinter import *
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
from Buscar_fatura import *

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
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 100
        self.sextoContainer["pady"] = 28
        self.sextoContainer.pack()

        self.rodape = Label(self.primeiroContainer, bg="#274360")
        self.rodape["padx"] = 340
        self.rodape["pady"] = 12
        self.rodape.pack()

        foto = tk.PhotoImage(file="icone.png")
        self.img = tk.Label(self.segundoContainer,image=foto)
        self.img.foto = foto
        self.img["pady"] = 5
        self.img.pack()

        self.nomeLabel = Label(self.terceiroContainer, text="Selecione a automação",font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.comboBox = ttk.Combobox(self.quartoContainer, 
                                     values= ["Auditoria Geap - (Glosa)",
                                              "Anexar Honorario Geap - (Faturamento)",
                                              "Buscar Faturas - (Financeiro)"],
                                     width=50)
        self.comboBox["background"] = 'white'
        self.comboBox.pack(side=LEFT)

        self.buttonIniciar = Button(self.sextoContainer, bg="#274360",foreground="white",width=10)
        self.buttonIniciar["text"] = "Iniciar"
        self.buttonIniciar["command"] = self.chamarAutomacao
        self.buttonIniciar.pack(side=LEFT)

        self.buttonCancelar = Button(self.sextoContainer, background="red",foreground="white",width=10)
        self.buttonCancelar["text"] = "Parar"
        # self.buttonCancelar["command"] = self.chamarAutomacao
        self.buttonCancelar.pack()



    def chamarAutomacao(self):
        automacao = self.comboBox.get()
        
        if automacao == "Buscar Faturas - (Financeiro)":
            iniciar()
                




root = tk.Tk()
Application(root)
root.title('Automação')
root.geometry("500x300")
root.resizable(width=0, height=0)

root.mainloop()