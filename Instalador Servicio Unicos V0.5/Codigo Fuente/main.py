import tkinter as tk
import tkinter.filedialog
from Validador import validarServicioEflow
from tkinter import messagebox as MessageBox
from script import instalarServicio

def Examinar(p):
  Path = tkinter.filedialog.askopenfilename()
  if(p==1 and validarServicioEflow(Path,"Sidesys.Services.ApplicationService.exe","Middleware","bin")):label1.config(text=Path) 
def Ejecutar():
  if(label1.cget("text")!=""): 
    instalarServicio(Textbox.get(),label1.cget("text"))
    MessageBox.showinfo("Info","El  servicio de cita se ha instalado")
  else: MessageBox.showerror("Error","Debe de haber seleccionado todos los servicios a instalar")

#Declaracion del frame a utilizar
menu = tk.Tk()

#Declaracion de los label
label1 = tk.Label(text="")

#Declaracion de los label
Textbox = tk.Entry()

#Declaracion y agregacion de los botones al frame
boton1 = tk.Button(text="Buscar", command=lambda:Examinar(1)).pack()
Textbox.pack()
boton4 = tk.Button(text="Ejecutar", command=lambda:Ejecutar()).pack()

#se agregan las etiquetas al frame
label1.pack()

menu.mainloop()