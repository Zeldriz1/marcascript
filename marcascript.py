import pyautogui as pyau
from time import sleep
import keyboard

def mudaJanela():
    pyau.hotkey('alt','tab')

def copiar():
    pyau.hotkey('ctrl', 'c')
    
def colar():
    pyau.hotkey('ctrl', 'v')

def selecionar():
    keyboard.press('shift')
    sleep(1)
def selecionar2():
    keyboard.press('ctrl')
    sleep(1)

def selecionar3():
    keyboard.press('right') 
    keyboard.release('right')
    sleep(1)
    keyboard.release('shift')
    sleep(1)
    keyboard.release('ctrl')
    sleep(1)
    

mudaJanela()
selecionar()
selecionar2()
selecionar3()
copiar()