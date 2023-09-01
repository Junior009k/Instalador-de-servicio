import tkinter as tk
from tkinter import *
import tkinter.filedialog
from Validador import validarServicioEflow
from tkinter import messagebox as MessageBox,font
from script import instalarServicio
from iis import creacionAplicacion
import logging
import datetime

def show_frame(frame1,frame2):
    frame1.pack_forget()
    frame2.pack(fill=tk.BOTH, expand=True)
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
def ExaminarDirectorio():
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la creacion de la aplicacion')
  Path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
  Path = Path.replace("/", r"\ ".strip())
  Path=Path.rstrip()
  label2.config(text=Path) 
  print(Path)
  return Path
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
def crearAplicacion(loggin):
  logging.info(f' {datetime.datetime.now() }: Se comienza a crear la aplicacion')
  bandera=True
  if( Textboxb.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar nombre')
    MessageBox.showerror("Error","Para crear la aplicacion debe de insertar un nombre")
    bandera=False
  if( label2.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar la ruta')
    MessageBox.showerror("Error","Para crear la aplicacion debe de tener una ruta")
    bandera=False
  if(bandera):
    if(creacionAplicacion(Textboxb.get(),label2.cget("text"),loggin)):MessageBox.INFO("Error","La aplicacion se instalo correctamente")
    


#Declaracion del Loggin
logging.basicConfig(filename=f'event{datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')
#Declaracion del frame a utilizar
menu = tk.Tk()
menu.title("Instalador de servicios Unicos V0.91")
#menu.config(relief="sunken") 
menu.geometry('600x350')
Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
frame = Frame(menu)  
frame2 = Frame(menu)  
frame.pack()   
#frame.config(bg="lightblue")  
#frame.config(width=600,height=330) 
#menu.config(bg="blue")          # color de fondo, background
#menu.config(relief="sunken")    # relieve del menuroot 
#menu.config(bd=25)  
#Declaracion de la variable seleccion
var = IntVar()

#------Creacion de los componentes para el Frame------------------------------------------------------------------------------------
#Declaracion de los radiunRadiobutton
R1 = Radiobutton(frame,text="Manual", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(frame, text="Automatico", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )
#Declaracion de los label
Titulo = tk.Label(frame,text="Instalador de servicios Unicos V0.91",font=Helvfont,pady=24).pack()
label1 = tk.Label(frame,text="")
#Declaracion de los label
Textbox = tk.Entry(frame,width=60)
Textbox.insert(1,"e-Flow MiddleWare Service")
#Declaracion y agregacion de los botones al frame
boton1 = tk.Button(frame,text="Buscar", command=lambda:Examinar(1)).pack()
Textbox.pack(padx=0,pady=5)
label1.pack() #se agregan las etiquetas al frame
boton4 = tk.Button(frame,text="Ejecutar", command=lambda:Ejecutar()).pack()
# Widgets para el frame1
button1 = tk.Button(frame, text="Proximo", command=lambda: show_frame(frame,frame2),)
button1.pack(side="right",padx=100)
#------Fin de la Creacion de los componentes para el Frame------------------------------------------------------------------------------------

#------Creacion de los componentes para el Frame2----------------------------------------------------------
#Declaracion de los label al frame2
Titulo = tk.Label(frame2,text="Creador de aplicaciones",font=Helvfont,pady=24).pack()
label2 = tk.Label(frame2,text="")
#Declaracion de los label al frame2
Textboxb = tk.Entry(frame2,width=60)
Textboxb.insert(1,"")
#Declaracion y agregacion de los botones al frame2
boton1 = tk.Button(frame2,text="Buscar", command=lambda:ExaminarDirectorio()).pack()
Textboxb.pack(padx=0,pady=5)
label2.pack() #se agregan las etiquetas al frame2
boton4 = tk.Button(frame2,text="Crear Aplicacion", command=lambda:crearAplicacion(logging)).pack()
# Widgets para el frame2
button2 = tk.Button(frame2, text="Atras", command=lambda: show_frame(frame2,frame))
button2.pack(side="right",padx=100)
#------Fin de la Creacion de los componentes para el Frame2----------------------------------------------------------


menu.bind('<Key>', on_key_pressed)
menu.mainloop()
logging.info(f' {datetime.datetime.now() }: Fin de la ejecucion de la Aplicacion')


# Import-Module WebAdministration
# New-Item 'IIS:\Sites\Default Web Site\DemoApp' -physicalPath c:\test -type Application