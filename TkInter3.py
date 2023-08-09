from tkinter import *
import tkinter as tk 
from tkinter import ttk 

class Application:
    def __init__(self, master=None):

        self.quartoContainer = Label(bg="#274360")
        self.quartoContainer["padx"] = 348
        self.quartoContainer["pady"] = 20
        self.quartoContainer.grid()

        self.quintoContainer = self.ComboBox()

    def ComboBox(self):

        # labelTop = tk.Label(root, text = "Tipo de Automação")
        # labelTop.grid(column= 0, row=0, padx=50, pady=10)

        comboExample = ttk.Combobox(root, values= [
                                            "",
                                            "Auditoria Geap", 
                                            "Soma Consenso"],
                                            width=50,)
        
        print(dict(comboExample))
        comboExample.grid(column= 0, row=5 )
        comboExample.current(0)

        print(comboExample.current(), comboExample.get())

root = tk.Tk()
Application(root)
root.title('Automação')
root.geometry("700x500")
root.resizable(width=0, height=0)
root.configure(bg='white')

root.mainloop()