import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

calificaciones=[None]*5

for i in range(5):
    entrada = simpledialog.askstring("Entrada", f"Captura la calificación:")
    if entrada is not None:
        calificaciones[i] = int(entrada)

    
