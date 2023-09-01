from tkinter import *
from Validador import *
from script import *
from iis import *
from udl import *
from funcionesAuxiliares import *
from tkinter import messagebox as MessageBox,font
import tkinter.filedialog
import logging
import datetime
import tkinter as tk


def on_key_pressed(event=None):
  k.config(text=str(ko(event,int(k.cget("text")))))
  if(int(k.cget("text"))==9):
    menu.config(cursor="pirate")
    frame.config(bg= "#D4AF37")
    frame3.config(bg= "#D4AF37")
    Titulo.config(bg= "#D4AF37")
    Titulo2.config(bg= "#D4AF37")
    Titulo3.config(bg= "#D4AF37")
    frame2.config(bg= "#D4AF37")
    label1.config(bg= "#D4AF37")
    label2.config(bg= "#D4AF37")
    label3.config(bg= "#D4AF37")
    R1.config(bg= "#D4AF37")
    R2.config(bg= "#D4AF37")
    tk.messagebox.showinfo(title="codigo konami", message="FELICIDADES CRACK!!!!!,\nTE GANASTE EL ACCESO A UN NUEVO PUNTERO")
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
#esta funcion se encarga de Seleccionar el directorio donde se creara la aplicacion
def ExaminarDirectorio(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la creacion de la aplicacion')
  Path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
  Path = Path.replace("/", r"\ ".strip())
  Path=Path.rstrip()
  label.config(text=Path) 
  print(Path)
  return Path
#esta funcion se encarga de ejecutar el script
def Ejecutar():
  logging.info(f' {datetime.datetime.now() }: Se esta ejecutando la instalacion del servicio')
  if(label1.cget("text")!="" and Textbox.get()!=""): 
    if(instalarServicio(Textbox.get(),label1.cget("text"),sel(),logging)):tk.messagebox.showinfo(title="Felicidades", message="El servicio se instalo correctamente")
    else: MessageBox.showerror("Error","El servicio no se ha instalado, valide que se este ejecutando como administrador")
  #mensajes ante posible errores
  if(label1.cget("text")==""): MessageBox.showerror("Error","Debe de haber seleccionado El servicio a instalar")
  if(Textbox.get()==""): MessageBox.showerror("Error","Debe de ingresar un nombre para su servicio a crear")
  if(sel()==0):MessageBox.showerror("Error","Debe seleccionar si el servicio iniciara en automatico o manual")
#esta funcion se encarga de crear la aplicacion en el iis
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
    if(creacionAplicacion(Textboxb.get(),label2.cget("text"),loggin)):tk.messagebox.showinfo(title="Felicidades", message="La aplicacion se instalo correctamente")
 
def modificarUDL(loggin):
  print("Estoy modificando la udl")
  print (label3.cget("text"))
  print(Textboxdb.get())
  print(Textboxsrv.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  la aplicacion')
  bandera=True
  if( Textboxdb.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar el nombre de la base de datos')
    MessageBox.showerror("Error","No se puede crear una aplicacion sin especificar el nombre de la base de datos")
    bandera=False
  if( Textboxsrv.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar el nombre de la base de datos')
    MessageBox.showerror("Error","No se puede crear una aplicacion sin especificar el nombre de la base de datos")
    bandera=False
  if( label3.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar la ruta')
    MessageBox.showerror("Error","Para crear la aplicacion debe de tener una ruta")
    bandera=False
  if(bandera):
    if(gestionaUDL(Textboxsrv.get(),Textboxdb.get(),label3.cget("text"),loggin)):tk.messagebox.showinfo(title="Felicidades", message="Los udls se modificaron correctamente")

#Declaracion del Loggin
logging.basicConfig(filename=f'Logs\event{datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')

colorframe1="#f00"
colorframe2="#0f0"
colorframe3="#00f"
#Declaracion de la instancia de la aplicacion a utilizar
menu = tk.Tk()
menu.title("Instalador de servicios Unicos V0.98")
menu.geometry('500x350')
Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
menu.config(relief="sunken") 
menu.config(bg="blue")          # color de fondo, background
menu.config(bd=25)  

#------Creacion de los componentes para el Frame------------------------------------------------------------------------------------
frame = Frame(menu)
frame.config(bg="#F00")  
frame.config(width=425,height=350) 
frame.pack()
imagen= PhotoImage(file="sidesys.gif")

k=tk.Label(frame,text="0")
#Declaracion de la variable seleccion
var = IntVar()
#Declaracion de los radiunRadiobutton
R1 = Radiobutton(frame,text="Manual", variable=var, value=1, command=sel,bg=colorframe1)
R2 = Radiobutton(frame, text="Automatico", variable=var, value=2,command=sel,bg=colorframe1)
R1.place(x=0,y=40)
R2.place(x=0,y=60)
#Declaracion de los label
Titulo = tk.Label(frame,text="Instalador de servicios Unicos V0.98",font=Helvfont,pady=12,bg=colorframe1)
Titulo.place(x=75,y=0)
label1 = tk.Label(frame,text="",bg=colorframe1) #se agregan las etiquetas al frame
label1.place(x=40,y=125)
#Declaracion de los label
Textbox = tk.Entry(frame,width=60)
Textbox.insert(1,"e-Flow MiddleWare Service")
Textbox.place(x=40,y=100)
#Declaracion y agregacion de los botones al frame
boton1 = tk.Button(frame,text="Buscar", command=lambda:Examinar(1)).place(x=40,y=150)
boton4 = tk.Button(frame,text="Ejecutar", command=lambda:Ejecutar()).place(x=90,y=150)
# Widgets para el frame1
button2 = tk.Button(frame, text="Creador de aplicaciones", command=lambda: show_frame(frame,frame2)).place(x=275,y=240)
button5 = tk.Button(frame, text="Configurador de UDLS", command=lambda: show_frame(frame,frame3)).place(x=275,y=270)
#------Fin de la Creacion de los componentes para el Frame------------------------------------------------------------------------------------

#------Creacion de los componentes para el Frame2----------------------------------------------------------
#Declaracion de los label al frame2
frame2 = Frame(menu) 
frame2.config(bg=colorframe2)  
frame2.config(width=425,height=350) 
Titulo2 = tk.Label(frame2,text="Creador de aplicaciones en IIS",font=Helvfont,pady=24,bg=colorframe2)
Titulo2.place(x=40,y=0)
label2 = tk.Label(frame2,text="",bg=colorframe2)
#Declaracion de los label al frame2
Textboxb = tk.Entry(frame2,width=60)
Textboxb.insert(1,"")
#Declaracion y agregacion de los botones al frame2
boton1 = tk.Button(frame2,text="Buscar", command=lambda:ExaminarDirectorio(label2)).place(x=40,y=150)
Textboxb.place(x=40,y=100)
label2.place(x=40,y=125) #se agregan las etiquetas al frame2
boton4 = tk.Button(frame2,text="Crear Aplicacion", command=lambda:crearAplicacion(logging)).place(x=90,y=150)
# Widgets para el frame2
button2 = tk.Button(frame2, text="Instalador de servicio", command=lambda: show_frame(frame2,frame)).place(x=275,y=240)
button5 = tk.Button(frame2, text="Configurador de UDLS", command=lambda: show_frame(frame2,frame3)).place(x=275,y=270)
#------Fin de la Creacion de los componentes para el Frame2----------------------------------------------------------

#------Creacion de los componentes para el Frame3----------------------------------------------------------
#Declaracion de los label al frame2
frame3 = Frame(menu) 
frame3.config(bg=colorframe3)  
frame3.config(width=425,height=350) 
Titulo3 = tk.Label(frame3,text="Configurador de udls",font=Helvfont,pady=24,bg=colorframe3)
Titulo3.place(x=40,y=0)
label3 = tk.Label(frame3,text="",bg=colorframe3)
#Declaracion de los label al frame2
Textboxb = tk.Entry(frame3,width=60)
Textboxb.insert(1,"")
#Declaracion y agregacion de los botones al frame2
boton1 = tk.Button(frame3,text="Buscar", command=lambda:ExaminarDirectorio(label3)).place(x=40,y=150)
labeldb = tk.Label(frame3,text="Introduzca el nombre del servidor ",bg=colorframe3)
Textboxdb = tk.Entry(frame3)
labelsrv = tk.Label(frame3,text="Introduzca el nombre de la base de datos",bg=colorframe3)
Textboxsrv = tk.Entry(frame3)
Textboxb.place(x=40,y=100)
Textboxdb.place(x=40,y=240)
Textboxsrv.place(x=40,y=200)
labeldb.place(x=40,y=180)
labelsrv.place(x=40,y=220)
label3.place(x=40,y=125) #se agregan las etiquetas al frame2
boton4 = tk.Button(frame3,text="Modificar UDLS", command=lambda:modificarUDL(logging)).place(x=90,y=150)
# Widgets para el frame2
button2 = tk.Button(frame3, text="Instalador de servicio", command=lambda: show_frame(frame3,frame)).place(x=275,y=240)
button5 = tk.Button(frame3, text="Creador de aplicaciones", command=lambda: show_frame(frame3,frame2)).place(x=275,y=270)
#------Fin de la Creacion de los componentes para el Frame2----------------------------------------------------------
imagenSidesys=tk.Label(frame,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame2,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame3,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
menu.bind('<Key>', on_key_pressed)
menu.mainloop()
logging.info(f' {datetime.datetime.now() }: Fin de la ejecucion de la Aplicacion')

# Import-Module WebAdministration
# New-Item 'IIS:\Sites\Default Web Site\DemoApp' -physicalPath c:\test -type Application