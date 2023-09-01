import tkinter as tk
from tkinter import font
from tkinter import *
import tkinter.filedialog
from Validador import validarServicioEflow
from tkinter import messagebox as MessageBox
from script import instalarServicio

def Examinar(p):
  Path = tkinter.filedialog.askopenfilename()
  if(p==1 and validarServicioEflow(Path,"Sidesys.Services.ApplicationService.exe","Middleware","bin")):label1.config(text=Path) 
def Ejecutar():
  if(label1.cget("text")!="" and Textbox.get()!=""): 
    instalarServicio(Textbox.get(),label1.cget("text"))
    MessageBox.showinfo("Info","El  servicio de cita se ha instalado")
  if(label1.cget("text")==""): MessageBox.showerror("Error","Debe de haber seleccionado todos los servicios a instalar")
  if(Textbox.get()==""): MessageBox.showerror("Error","Debe de ingresar un nombre para su servicio a crear")

#Declaracion del frame a utilizar
menu = tk.Tk()
menu.title("Instalador de servicios Unicos V0.8")
menu.config(relief="sunken") 
menu.geometry('600x230')
Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
frame = Frame(menu)  
#frame.pack()   
#frame.config(bg="lightblue")  
frame.config(width=700,height=200) 
#menu.config(bg="blue")          # color de fondo, background
menu.config(cursor="pirate")    # tipo de cursor (arrow defecto)
menu.config(relief="sunken")    # relieve del root 
menu.config(bd=25)  

#Declaracion de los label
Titulo = tk.Label(text="Instalador de servicios Unicos V0.8",font=Helvfont,pady=24).pack()
label1 = tk.Label(text="")

#Declaracion de los label
Textbox = tk.Entry(width=60)
Textbox.insert(1,"")
#Declaracion y agregacion de los botones al frame
boton1 = tk.Button(text="Buscar", command=lambda:Examinar(1)).pack()
Textbox.pack(padx=0,pady=5)
label1.pack() #se agregan las etiquetas al frame
informacion= tk.Label(text="e-Flow MiddleWare Service").place(x=390,y=50)
boton4 = tk.Button(text="Ejecutar", command=lambda:Ejecutar()).pack()




menu.mainloop()