import tkinter as tk
from tkinter import *
import tkinter.filedialog
from Validador import validarServicioEflow
from tkinter import messagebox as MessageBox,font
from script import instalarServicio
import logging
import datetime

def on_key_pressed(event=None):
  if(event.keycode==220 ):menu.config(cursor="pirate")    # tipo de cursor (arrow defecto)
#esta funcion es para desarrollo 
def sel():
   if(var.get()==1):
    logging.info(f' {datetime.datetime.now() }: Se establecio el inicio Manual')
    return "demand"    
   if(var.get()==2):
     logging.info(f' {datetime.datetime.now() }: Se establecio el inicio Automatico')
     return "Auto"
   else: return 0
#esta funcion se encarga de abrir el directorio y validar que el archivo seleccionado sea el servicio
def Examinar(p):
  logging.info(f' {datetime.datetime.now() }: Se esta examinando el archivo')
  Path = tkinter.filedialog.askopenfilename()
  if(p==1 and validarServicioEflow(Path.lower(),"sidesys.services.applicationservice.exe","middleware","bin")):label1.config(text=Path) 
#esta funcion se encarga de ejecutar el script
def Ejecutar():
  logging.info(f' {datetime.datetime.now() }: Se esta ejecutando la instalacion del servicio')
  if(label1.cget("text")!="" and Textbox.get()!=""): 
    if(instalarServicio(Textbox.get(),label1.cget("text"),sel(),logging)):MessageBox.INFO("Error","El servicio se instalo correctamente")
    else: MessageBox.showerror("Error","El servicio no se ha instalado, valide que se este ejecutando como administrador")
  #mensajes ante posible errores
  if(label1.cget("text")==""): MessageBox.showerror("Error","Debe de haber seleccionado El servicio a instalar")
  if(Textbox.get()==""): MessageBox.showerror("Error","Debe de ingresar un nombre para su servicio a crear")
  if(sel()==0):MessageBox.showerror("Error","Debe seleccionar si el servicio iniciara en automatico o manual")

#Declaracion del Loggin
logging.basicConfig(filename=f'event{datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')
#Declaracion del frame a utilizar
menu = tk.Tk()
menu.title("Instalador de servicios Unicos V0.9")
menu.config(relief="sunken") 
menu.geometry('600x330')
Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
frame = Frame(menu)  
#frame.pack()   
#frame.config(bg="lightblue")  
frame.config(width=700,height=200) 
#menu.config(bg="blue")          # color de fondo, background
menu.config(relief="sunken")    # relieve del menuroot 
menu.config(bd=25)  
#Declaracion de la variable seleccion
var = IntVar()

#Declaracion de los radiunRadiobutton
R1 = Radiobutton(text="Manual", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(menu, text="Automatico", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )
#Declaracion de los label
Titulo = tk.Label(text="Instalador de servicios Unicos V0.9",font=Helvfont,pady=24).pack()
label1 = tk.Label(text="")

#Declaracion de los label
Textbox = tk.Entry(width=60)
Textbox.insert(1,"e-Flow MiddleWare Service")
#Declaracion y agregacion de los botones al frame
boton1 = tk.Button(text="Buscar", command=lambda:Examinar(1)).pack()
Textbox.pack(padx=0,pady=5)
label1.pack() #se agregan las etiquetas al frame
informacion= tk.Label(text="e-Flow MiddleWare Service").place(x=390,y=50)
boton4 = tk.Button(text="Ejecutar", command=lambda:Ejecutar()).pack()


menu.bind('<Key>', on_key_pressed)
menu.mainloop()
logging.info(f' {datetime.datetime.now() }: Fin de la ejecucion de la Aplicacion')