import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()
root.config(width=300, height=200)
# Crear caja de texto.
mi_Frame = Frame() #Creación del Frame
mi_Frame.pack() #Empaquetamiento del Frame
mi_Frame.config(bg="lightblue")  
mi_Frame.config(width=200,height=130) 
entry = ttk.Entry(mi_Frame)
# Posicionarla en la ventana.
entry.place(x=50, y=50)
root.mainloop()

tk.messagebox.showinfo(title="", message="")