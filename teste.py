import pandas as pd
import pyautogui
import time
from abc import ABC
from tkinter import filedialog
from selenium import webdriver
from openpyxl import Workbook, load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from tkinter import filedialog
import tkinter.messagebox


tkinter.messagebox.showinfo( 'Automação GEAP Financeiro' , 'Busca de Faturas na GEAP Concluído com sucesso 😎✌' )
tkinter.messagebox.showerror( 'Erro Automação' , 'Ocorreu um enquanto o Robô trabalhava, provavelmente o portal da GEAP caiu 😢' )
# tkinter.messagebox.showerror( 'title' , 'ERRO' )


