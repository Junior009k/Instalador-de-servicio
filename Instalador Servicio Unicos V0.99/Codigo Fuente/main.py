from tkinter import *
from Code import *
from Validador import *
from script import *
from iis import *
from udl import *
from db import *
from NCache import *
from NME import *
from portService import *
from configuracionCitas import *
import os
import sys
from funcionesAuxiliares import *
from tkinter import messagebox as MessageBox,font
import tkinter.filedialog
import logging
import datetime
import tkinter as tk

def showConfiguration(event=None):show_Configuration(frame,frame2,frame3,frame4,frame5,frameMenuPrincipal,frameConfiguracionColoresPrincipales)
#Esta funcion se encarga de cargar directamente desde la base de datos los colores de los 5 frame
def loadColor(color):
  frame.config(bg= color[0])
  frame3.config(bg= color[2])
  frame4.config(bg= color[3])
  frame5.config(bg= color[4])
  Titulo.config(bg= color[0])
  Titulo2.config(bg= color[1])
  Titulo3.config(bg= color[2])
  Titulo4.config(bg= color[3])
  Titulo5.config(bg= color[4])
  frame2.config(bg= color[1])
  label1.config(bg= color[0])
  label2.config(bg= color[1])
  label3.config(bg= color[2])
  label4.config(bg= color[3])
  label5.config(bg= color[4])
  labelPort.config(bg= color[3])
  labeldb.config(bg= color[2])
  labelsrv.config(bg= color[2])
  R1.config(bg= color[0])
  R2.config(bg= color[0])
  labelsvr.config(bg= color[4])
  labelCitas.config(bg= color[4])
  labelEflow.config(bg= color[4])
  labelMSMQ.config(bg= color[4])
#Se encarga de validar si un directorio existe o no existe. 
def validateDirectory(path,name):

    # Verifica si la carpeta existe
    if os.path.exists(f"{path}/{name}") and os.path.isdir(f"{path}/{name}"):
        print(f' {datetime.datetime.now() }: La carpeta {path}/{name} existe')
        return False
        logging.info(f' {datetime.datetime.now() }: La carpeta {name}  existe')
    else:
        MessageBox.showerror("Error",f"La carpeta {path}/{name} no existe")
        print(f' {datetime.datetime.now() }: La carpeta {path}/{name} no existe')
        return True
        logging.error(f' {datetime.datetime.now() }: La carpeta {name} no existe')
#Se encarga de validar la entrada del textPort, donde el limite es tres caracter
def validate_entry(text):
    # Validar la entrada del usuario
    if len(text) <= 3:
        return True
    else:
        return False
#Este es un egg easter
def on_key_pressed(event=None):
  k.config(text=str(ko(event,int(k.cget("text")))))
  if(int(k.cget("text"))==9):
    
    tk.messagebox.showinfo(title="codigo konami", message="FELICIDADES CRACK!!!!!,\nTE GANASTE EL ACCESO AL PUNTERO CHEAT ")
    loadColor(["#D4AF37","#D4AF37","#D4AF37","#D4AF37","#D4AF37"])
    menu.config(cursor="pirate")
#esta funcion Se utiliza para establecer el inicio del servicio instalado
def sel():
   if(var.get()==1):
    logging.info(f' {datetime.datetime.now() }: Se establecio el inicio Manual')
    return "demand"    
   if(var.get()==2):
     logging.info(f' {datetime.datetime.now() }: Se establecio el inicio Automatico')
     return "Auto"
   else: return 0
#esta funcion se encarga de abrir el directorio y validar que el archivo seleccionado sea el servicio
def Examine(p):
  logging.info(f' {datetime.datetime.now() }: Se esta examinando el archivo')
  Path = tkinter.filedialog.askopenfilename()
  if(p==1 and validateService(Path.lower(),"sidesys.services.applicationservice.exe","middleware","bin")):label1.config(text=Path) 
#esta funcion se encarga de Seleccionar el directorio donde se creara la aplicacion
def ExamineDirectory(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la creacion de la aplicacion')
  Path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
  Path = Path.replace("/", r"\ ".strip())
  Path=Path.rstrip()
  label.config(text=Path) 
  print(Path)
  return Path
#esta funcion se encarga de ejecutar el script
def executeScript():
  logging.info(f' {datetime.datetime.now() }: Se esta ejecutando la instalacion del servicio')
  if(label1.cget("text")!="" and Textbox.get()!=""): 
    if(installService(Textbox.get(),label1.cget("text"),sel(),logging)):tk.messagebox.showinfo(title="Felicidades", message="El servicio se instalo correctamente")
    else: MessageBox.showerror("Error","El servicio no se ha instalado, valide que se este ejecutando como administrador")
  #mensajes ante posible errores
  if(label1.cget("text")==""): MessageBox.showerror("Error","Debe de haber seleccionado El servicio a instalar")
  if(Textbox.get()==""): MessageBox.showerror("Error","Debe de ingresar un nombre para su servicio a crear")
  if(sel()==0):MessageBox.showerror("Error","Debe seleccionar si el servicio iniciara en automatico o manual")

#esta funcion se encarga de crear los site en el iis
def createSite(loggin):
  logging.info(f' {datetime.datetime.now() }: Se comienza a crear la aplicacion')
  bandera=True
  print(TextboxNameSite.get())
  print(TextboxPortHttp.get())
  print(label6.cget("text"))
  if( TextboxNameSite.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear el site sin especificar nombre del site')
    MessageBox.showerror("Error","Para crear la aplicacion debe de insertar un nombre")
    bandera=False
  if( TextboxPortHttp.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear el site sin especificar nombre del puerto del site')
    MessageBox.showerror("Error","Para crear la aplicacion debe de insertar un nombre")
    bandera=False
  if( label6.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar la ruta')
    MessageBox.showerror("Error","Para crear la aplicacion debe de tener una ruta")
    bandera=False
  print(bandera)
  if(bandera):
    if(createSiteIIS(TextboxNameSite.get(),label6.cget("text"),loggin,TextboxPortHttp.get())):tk.messagebox.showinfo(title="Felicidades", message="La aplicacion se creo correctamente")


#esta funcion se encarga de crear la aplicacion en el iis
def createAplication(loggin):
  logging.info(f' {datetime.datetime.now() }: Se comienza a crear la aplicacion')
  bandera=True
  print(TextboxNameApplication.get())
  if( TextboxNameApplication.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar nombre')
    MessageBox.showerror("Error","Para crear la aplicacion debe de insertar un nombre")
    bandera=False
  if( label2.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar la ruta')
    MessageBox.showerror("Error","Para crear la aplicacion debe de tener una ruta")
    bandera=False
  if(bandera):
    if(createAplicationIIS(TextboxNameApplication.get(),label2.cget("text"),loggin)):tk.messagebox.showinfo(title="Felicidades", message="La aplicacion se creo correctamente")
#esta funcion se encarga de configurar las citas
def modifyAppointment(loggin):
  print("Estoy modificando las Citas")
  print (label5.cget("text"))
  print(Textboxsvr.get())
  print(TextboxCitas.get())
  print(TextboxEflow.get())
  print(TextboxMSMQ.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  Citas')
  bandera=True
  if( Textboxsvr.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar cita sin especificar el nombre del servidor')
    MessageBox.showerror("Error","No se puede modificar  cita sin especificar el nombre del servidor")
    bandera=False
  if( TextboxCitas.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar cita sin especificar el nombre del sitio de citas')
    MessageBox.showerror("Error","No se puede modificar  cita sin especificar el nombre del sitio de citas")
    bandera=False
  if( TextboxEflow.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar cita sin especificar el nombre del sitio de e-Flow')
    MessageBox.showerror("Error","No se puede modificar  cita sin especificar el nombre del sitio de e-Flow")
    bandera=False
  if( TextboxMSMQ.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar cita sin especificar el nombre de la cola de mensajeria')
    MessageBox.showerror("Error","No se puede modificar  cita sin especificar el nombre de la cola de mensajeria")
    bandera=False
  if( label5.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  Citas sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar  Citas debe de tener una ruta")
    bandera=False
  if( validateDirectory(label5.cget("text"),"Middleware")  or validateDirectory(label5.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  Citas,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  Citas,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de los puertos')
    print("Paso todas las pruebas, comenzando proceso de modificacion de los puertos")
    #changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    configurarCitas(label5.cget("text"),Textboxsvr.get(),TextboxCitas.get(),TextboxEflow.get(),TextboxMSMQ.get(),loggin,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de cita termino el proceso de configuracion de los archivos")
#esta funcion se encarga de configurar NCache
def modifyNCache(loggin):
  print("Estoy modificando las NCache")
  print (label7.cget("text"))
  print(TextboxsvrC.get())
  print(TextboxCache.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NCache')
  bandera=True
  if( TextboxsvrC.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar NCache sin especificar el nombre del servidor')
    MessageBox.showerror("Error","No se puede modificar  NCache sin especificar el nombre del servidor")
    bandera=False
  if( TextboxCache.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar NCache sin especificar el nombre del cache')
    MessageBox.showerror("Error","No se puede modificar  NCache sin especificar el nombre del cache")
    bandera=False
  if( label7.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar   sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar  NCache debe de tener una ruta")
    bandera=False
  if( validateDirectory(label7.cget("text"),"Middleware")  or validateDirectory(label7.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  NCache,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  NCache,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de los NCache')
    print("Paso todas las pruebas, comenzando proceso de modificacion de los NCache")
    #changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    configurarNCache( label7.cget("text"),TextboxsvrC.get(), TextboxCache.get(), loggin, datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de NCache termino el proceso de configuracion de los archivos")
#esta funcion se encarga de configurar NME
def modifyNME(loggin):
  print("Estoy modificando NME")
  print (label8.cget("text"))
  print(TextboxeFlowNME.get())
  print(TextboxeAPI.get())
  print(TextboxsvrNME.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NME')
  bandera=True
  if( TextboxsvrNME.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Nuevo Modulo de Emision sin especificar el nombre del servidor')
    MessageBox.showerror("Error","No se puede modificar  Nuevo Modulo de el Emision sin especificar el nombre del servidor")
    bandera=False
  if( TextboxeFlowNME.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Nuevo Modulo de Emision sin especificar el nombre de la aplicacion de e-Flow')
    MessageBox.showerror("Error","No se puede modificar  el Nuevo Modulo de Emision sin especificar el nombre de la aplicacion de e-Flow")
    bandera=False
  if( TextboxeAPI.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Nuevo Modulo de Emision sin especificar el nombre del Emission Api')
    MessageBox.showerror("Error","No se puede modificar  Nuevo Modulo de Emision sin especificar el nombre del Emission Api")
    bandera=False
  if( label8.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Nuevo Modulo de Emision sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar  Nuevo Modulo de Emision debe de tener una ruta")
    bandera=False
  if( validateDirectory(label8.cget("text"),"Middleware")  or validateDirectory(label8.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Nuevo Modulo de Emision,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  el Nuevo Modulo de Emision,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Nuevo Modulo de Emision')
    print("Paso todas las pruebas, comenzando proceso de modificacion de los Nuevo Modulo de Emision")
    #changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    #configurarNCache( label7.cget("text"),TextboxsvrC.get(), TextboxCache.get(), loggin, datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de NCache termino el proceso de configuracion de los archivos")
    configurarNME(label8.cget("text"),TextboxsvrNME.get(),TextboxeFlowNME.get(),TextboxeAPI.get(),loggin,datetime)
#esta funcion se encarga de modificar los puertos
def modifyPort(loggin):
  print("Estoy modificando los Puertos")
  print (label4.cget("text"))
  print(TextboxPort.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  los puertos')
  bandera=True
  if( TextboxPort.get()=="" or TextboxPort.get().isdigit()==False):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  los puertos sin especificar el numero del puerto')
    MessageBox.showerror("Error","No se puede modificar  los puertos sin especificar el el numero del puerto")
    bandera=False
  if( label4.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  los puertos sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar  los puertos debe de tener una ruta")
    bandera=False
  if( validatePort(TextboxPort.get())):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  los puertos, recuerda que debe tener 3 numeros')
    MessageBox.showerror("Error","Para modificar  los puertos recuerda que debe tener 3 numeros")
    bandera=False
  if( validateDirectory(label4.cget("text"),"Middleware")  or validateDirectory(label4.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  los puertos,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  los puertos,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de los puertos')
    print("Paso todas las pruebas, comenzando proceso de modificacion de los puertos")
    changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="Los Puertos se modificaron correctamente")
def modifyUDL(loggin):
  print("Estoy modificando la udl")
  print (label3.cget("text"))
  print(Textboxdb.get())
  print(Textboxsrv.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar los UDLS')
  bandera=True
  if( Textboxdb.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar los UDLS sin especificar el nombre de la base de datos')
    MessageBox.showerror("Error","No se puede modificar los UDLS sin especificar el nombre de la base de datos")
    bandera=False
  if( Textboxsrv.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar los UDLS sin especificar el nombre del servidor de la base de datos')
    MessageBox.showerror("Error","No se puede modificar los UDLS sin especificar el nombre de la base de datos")
    bandera=False
  if( label3.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar los UDLS sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar los UDLS debe de tener una ruta")
    bandera=False
  if(bandera):
    if(manageUDL(Textboxsrv.get(),Textboxdb.get(),label3.cget("text"),loggin)):tk.messagebox.showinfo(title="Felicidades", message="Los udls se modificaron correctamente")
def new_Archive(event=None):
    print("¡Has presionado para crear un nuevo archivo!")
def saveDataConfiguration(loggin):
  loggin.info(f' {datetime.datetime.now() }: guardando los datos de configuracion')
  print(variableColor1.get())
  print(variableColor2.get())
  print(variableColor3.get())
  setConfiguration([fixWord(variableColor1.get()),1],[fixWord(variableColor2.get()),2],[fixWord(variableColor3.get()),3], [fixWord(variableColor4.get()),4],[fixWord(variableColor5.get()),5],loggin,datetime.datetime.now())
  loadColor([getColor(1,"codigo"),getColor(2,"codigo"),getColor(3,"codigo"),getColor(4,"codigo"),getColor(5,"codigo")])
  tk.messagebox.showinfo(title="Los cambios se guardaron satisfactoriamente", message="Los cambios se guardaron satisfactoriamente \nPara ver los cambios, dar click en volver")
  #os.execl(sys.executable, sys.executable, * sys.argv) 

#BODY 

#Declaracion del Loggin
logging.basicConfig(filename=f'Logs\event {datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')

#Cargando los colores
colorframe1=getColor(1,"codigo")
colorframe2=getColor(2,"codigo")
colorframe3=getColor(3,"codigo")
colorframe4=getColor(4,"codigo")
colorframe5=getColor(5,"codigo")
colorframeC="#555"
colorMenuPrincipal="#555"

#Declaracion de la instancia de la aplicacion a utilizar
menu = tk.Tk()
Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
menu.title("Instalador de servicios Unicos V0.99")
menu.geometry('500x350')
menu.config(relief="sunken") 
menu.config(bg="blue")          # color de fondo, background
menu.config(bd=25)  

# Crear el primer menú.
barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=False)
menu_opciones = tk.Menu(barra_menus, tearoff=False)

# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Configuracion")
menu.config(menu=barra_menus)

#Opcion nuevo de la barra de menu archivo
menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command=new_Archive 
)

#Opcion configurar de la barra de menu configuracion
menu_opciones.add_command(
    label="Configurar",
    accelerator="Ctrl+c",
    command=lambda:show_Configuration(frame,frame2,frame3,frame4,frame5,frameMenuPrincipal,frameConfiguracionColoresPrincipales)
)
#Establece las variables a configurar
variableColor1 = StringVar(menu)
variableColor1.set(getColor(1,"c.descripcion")) # default value
variableColor2 = StringVar(menu)
variableColor2.set(getColor(2,"c.descripcion")) # default value
variableColor3 = StringVar(menu)
variableColor3.set(getColor(3,"c.descripcion")) # default value
variableColor4 = StringVar(menu)
variableColor4.set(getColor(4,"c.descripcion")) # default value
variableColor5 = StringVar(menu)
variableColor5.set(getColor(5,"c.descripcion")) # default value
menu_archivo

#------Creacion de los componentes para el Frame 1: MENU PRINCIPAL --------------------------------------------------------------------------------------------------
frameMenuPrincipal = Frame(menu)
frameMenuPrincipal.config(bg=colorMenuPrincipal)  
frameMenuPrincipal.config(width=425,height=350) 
frameMenuPrincipal.pack()
eflowimg= PhotoImage(file="img\eflow2.png")
client= PhotoImage(file="img\client.png")
citas= PhotoImage(file="img\citas.png")
encuesta= PhotoImage(file="img\Encuesta.png")
report= PhotoImage(file="img\\report.png")
automatizacion= PhotoImage(file="img\\automatizacion.png")
imagen= PhotoImage(file="img\sidesys.gif")
confImg = PhotoImage(file='img\conf.png')

k=tk.Label(frameMenuPrincipal,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuPrincipal,text="Menu Principal",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuPrincipal,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)
if(readValueSystem("<Vlvwhpd h-Iorz>\w<Vlvwhpd h-Iorz>")=="a"):buttonEflow = tk.Button(frameMenuPrincipal,width=100,height=41, image = eflowimg,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuEflow)).place(x=45,y=100)
if(readValueSystem("<Folhqw>\w<Folhqw>")=="a"):buttonClient = tk.Button(frameMenuPrincipal,width=100,height=41, image = client,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuClient)).place(x=157,y=100)
if(readValueSystem("<Vlvwhpd flwdv>\w<Vlvwhpd flwdv>")=="a"):buttonCitas = tk.Button(frameMenuPrincipal,width=100,height=41, image = citas,text="Citas", command=lambda: show_frame(frameMenuPrincipal,frameMenuCitas)).place(x=270,y=100)
if(readValueSystem("<Vlvwhpd h-Hqfxhvwd>\w<Vlvwhpd Hqfxhvwd>")=="a"):buttonEncuesta = tk.Button(frameMenuPrincipal,width=100,height=41, image = encuesta,text="Encuesta", command=lambda: show_frame(frameMenuPrincipal,frameMenuEncuesta)).place(x=45,y=175)
if(readValueSystem("<Uhsruwhv>\w<Uhsruwh>")=="a"):buttonReport = tk.Button(frameMenuPrincipal,width=100,height=41, image = report,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuReport)).place(x=157,y=175)
if(readValueSystem("<Dxwrpdwlcdgru>\w<Dxwrpdwlcdgru>")=="a"):buttonAutomatizacion = tk.Button(frameMenuPrincipal,width=100,height=41, image = automatizacion,text="Automatizacion", command=lambda: show_frame(frameMenuPrincipal,frameMenuAuto)).place(x=270,y=175)
if(readValueSystem("<PrghIuhh>\w<PrghIuhh>")=="a"):buttonModoLibre = tk.Button(frameMenuPrincipal,width=46,height=3,text="Modo Libre", command=lambda: show_frame(frameMenuPrincipal,frameMenuML)).place(x=45,y=235)
# Widgets para el frame1-----------------------

#------Creacion de los componentes para el frameMenuEflow: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuEflow = Frame(menu)
frameMenuEflow.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuEflow,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuEflow,text="Menu e-Flow",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuEflow,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)

buttonEflowService = tk.Button(frameMenuEflow,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuEflow,frame)).place(x=45,y=100)
buttonEflowIIS = tk.Button(frameMenuEflow,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(frameMenuEflow,frame2)).place(x=230,y=100)
buttonEflowUDL = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuEflow,frame3)).place(x=230,y=130)
buttonEflowSites = tk.Button(frameMenuEflow,width=20,height=1, text="Creador de sites", command=lambda: show_frame(frameMenuEflow,frame6)).place(x=45,y=130)
buttonEflowPort = tk.Button(frameMenuEflow,width=20,height=1, text="Modificador de puertos", command=lambda: show_frame(frameMenuEflow,frame4)).place(x=45,y=160)
buttonEflowPort = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador NCache", command=lambda: show_frame(frameMenuEflow,frame7)).place(x=230,y=160)
buttonEflowPort = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador NME", command=lambda: show_frame(frameMenuEflow,frame8)).place(x=45,y=190)
buttonEflowBack = tk.Button(frameMenuEflow,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuEflow,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuEflow: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuClient: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuClient = Frame(menu)
frameMenuClient.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuClient,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuClient,text="Menu Client",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuClient,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)

buttonClientService = tk.Button(frameMenuClient,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuClient,frame)).place(x=45,y=100)
buttonClientBack = tk.Button(frameMenuClient,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuClient,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los frameMenuClient para el frameMenuCitas: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuCitas: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuCitas = Frame(menu)
frameMenuCitas.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuCitas,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuCitas,text="Menu Citas",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuCitas,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)

buttonCitasService = tk.Button(frameMenuCitas,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuCitas,frame)).place(x=45,y=100)
buttonCitasIIS = tk.Button(frameMenuCitas,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(frameMenuCitas,frame2)).place(x=230,y=100)
buttonCitasUDL = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuCitas,frame3)).place(x=45,y=130)
buttonCitasPort = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de Citas", command=lambda: show_frame(frameMenuCitas,frame5)).place(x=230,y=130)
buttonCitasBack = tk.Button(frameMenuCitas,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuCitas,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuCitas: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------


#------Creacion de los componentes para el frameMenuEncuesta: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuEncuesta = Frame(menu)
frameMenuEncuesta.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuEncuesta,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuEncuesta,text="Menu Encuestas",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuEncuesta,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)

buttonEncuestaService = tk.Button(frameMenuEncuesta,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuEncuesta,frame)).place(x=45,y=100)
buttonEncuestaIIS = tk.Button(frameMenuEncuesta,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(frameMenuEncuesta,frame2)).place(x=230,y=100)
buttonEncuestaUDL = tk.Button(frameMenuEncuesta,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuEncuesta,frame3)).place(x=45,y=130)
buttonEncuestaBack = tk.Button(frameMenuEncuesta,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuEncuesta,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuEncuesta: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuReport: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuReport = Frame(menu)
frameMenuReport.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuReport,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuReport,text="Reportes",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuReport,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)

buttonReporService = tk.Button(frameMenuReport,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuReport,frame)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuReport,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuReport,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuReport: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuAuto = Frame(menu)
frameMenuAuto.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuAuto,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuAuto,text="Automatizacion del proceso",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuAuto,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)

buttonReporService = tk.Button(frameMenuAuto,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuAuto,frame)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuAuto,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuAuto,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuML = Frame(menu)
frameMenuML.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuML,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuML,text="Modo Libre",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuML,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)

buttonReporService = tk.Button(frameMenuML,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuML,frame)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuML,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuML,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------




#------Creacion de los componentes para el Frame 1: Frame de servicio------------------------------------------------------------------------------------
frame = Frame(menu)
frame.config(bg=colorframe1)  
frame.config(width=425,height=350)
imagen= PhotoImage(file="img\sidesys.gif")
confImg = PhotoImage(file='img\conf.png')

k=tk.Label(frame,text="0")
#Declaracion de la variable seleccion
var = IntVar()
#Declaracion de los radiunRadiobutton
R1 = Radiobutton(frame,text="Manual", variable=var, value=1, command=sel,bg=colorframe1)
R2 = Radiobutton(frame, text="Automatico", variable=var, value=2,command=sel,bg=colorframe1)
R1.place(x=0,y=40)
R2.place(x=0,y=60)
#Declaracion de los label
Titulo = tk.Label(frame,text="Instalador de servicios Unicos",font=Helvfont,pady=12,bg=colorframe1)
Titulo.place(x=75,y=0)
label1 = tk.Label(frame,text="",bg=colorframe1) #se agregan las etiquetas al frame
label1.place(x=40,y=125)
#Declaracion de los label
Textbox = tk.Entry(frame,width=60)
Textbox.insert(1,"e-Flow MiddleWare Service")
Textbox.place(x=40,y=100)
#Declaracion y agregacion de los botones al frame
boton1 = tk.Button(frame,text="Buscar", command=lambda:Examine(1)).place(x=40,y=150)
boton4 = tk.Button(frame,text="Ejecutar", command=lambda:executeScript()).place(x=90,y=150)
# Widgets para el frame1
button2 = tk.Button(frame,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame,frameMenuEflow)).place(x=2.5,y=270)
button5 = tk.Button(frame,width=16,height=1, text="Back to Citas", command=lambda: show_frame(frame,frameMenuCitas)).place(x=130,y=270)
button7 = tk.Button(frame,width=16,height=1, text="Back to Encuesta", command=lambda: show_frame(frame,frameMenuEncuesta)).place(x=275,y=270)
button8 = tk.Button(frame,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame 1: Frame de servicio------------------------------------------------------------------------------------

#------Creacion de los componentes para el Frame2----------------------------------------------------------
#Declaracion de los label al frame2
frame2 = Frame(menu) 
frame2.config(bg=colorframe2)  
frame2.config(width=425,height=350) 
Titulo2 = tk.Label(frame2,text="Creador de aplicaciones en IIS",font=Helvfont,pady=24,bg=colorframe2)
Titulo2.place(x=40,y=0)
label2 = tk.Label(frame2,text="",bg=colorframe2)
#Declaracion de los label al frame2
TextboxNameApplication = tk.Entry(frame2,width=60)
TextboxNameApplication.insert(1,"")
#Declaracion y agregacion de los botones al frame2
boton1 = tk.Button(frame2,text="Buscar", command=lambda:ExamineDirectory(label2)).place(x=40,y=150)
TextboxNameApplication.place(x=40,y=100)
label2.place(x=40,y=125) #se agregan las etiquetas al frame2
boton4 = tk.Button(frame2,text="Crear Aplicacion", command=lambda:createAplication(logging)).place(x=90,y=150)
# Widgets para el frame2
button2 = tk.Button(frame2,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame2,frameMenuEflow)).place(x=2.5,y=270)
button5 = tk.Button(frame2,width=16,height=1, text="Back to Citas", command=lambda: show_frame(frame2,frameMenuCitas)).place(x=130,y=270)
button7 = tk.Button(frame2,width=16,height=1, text="Back to Encuesta", command=lambda: show_frame(frame2,frameMenuEncuesta)).place(x=275,y=270)
button8 = tk.Button(frame2,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame2,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame2, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame2----------------------------------------------------------

#------Creacion de los componentes para el Frame3----------------------------------------------------------
#Declaracion de los label al frame3
frame3 = Frame(menu) 
frame3.config(bg=colorframe3)  
frame3.config(width=425,height=350) 
Titulo3 = tk.Label(frame3,text="Configurador de udls",font=Helvfont,pady=24,bg=colorframe3)
Titulo3.place(x=40,y=0)
label3 = tk.Label(frame3,text="",bg=colorframe3)
#Declaracion de los label al frame3
#Declaracion y agregacion de los botones al frame3
boton1 = tk.Button(frame3,text="Buscar", command=lambda:ExamineDirectory(label3)).place(x=40,y=150)
labeldb = tk.Label(frame3,text="Introduzca el nombre del servidor ",bg=colorframe3)
Textboxdb = tk.Entry(frame3)
labelsrv = tk.Label(frame3,text="Introduzca el nombre de la base de datos",bg=colorframe3)
Textboxsrv = tk.Entry(frame3)
Textboxdb.place(x=40,y=240)
Textboxsrv.place(x=40,y=200)
labeldb.place(x=40,y=180)
labelsrv.place(x=40,y=220)
label3.place(x=40,y=125) #se agregan las etiquetas al frame3
boton4 = tk.Button(frame3,text="Modificar UDLS", command=lambda:modifyUDL(logging)).place(x=90,y=150)
# Widgets para el frame2
button2 = tk.Button(frame3,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame3,frameMenuEflow)).place(x=275,y=240)
button5 = tk.Button(frame3,width=16,height=1, text="Back to Citas", command=lambda: show_frame(frame3,frameMenuCitas)).place(x=275,y=270)
button7 = tk.Button(frame3,width=16,height=1, text="Back to Encuesta", command=lambda: show_frame(frame3,frameMenuEncuesta)).place(x=130,y=270)
button8 = tk.Button(frame3,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame3,frameMenuPrincipal)).place(x=2.5,y=270)
button6 = tk.Button(frame3, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)

#------Fin de la Creacion de los componentes para el Frame3----------------------------------------------------------

#------Creacion de los componentes para el Frame4----------------------------------------------------------
#Declaracion de los label al frame4
frame4 = Frame(menu) 
frame4.config(bg=colorframe4)  
frame4.config(width=425,height=350) 
Titulo4 = tk.Label(frame4,text="Modificador de puertos",font=Helvfont,pady=24,bg=colorframe4)
Titulo4.place(x=40,y=0)
label4 = tk.Label(frame4,text="",bg=colorframe4)
#Declaracion de los label al frame3
labelPort = tk.Label(frame4,text="Puerto:",bg=colorframe4)
labelPort.place(x=40,y=180)
TextboxPort = tk.Entry(frame4,width=5,validate="key", validatecommand=(frame4.register(validate_entry), '%P'))
TextboxPort.place(x=85,y=180)
#Declaracion y agregacion de los botones al frame4
boton1 = tk.Button(frame4,text="Buscar", command=lambda:ExamineDirectory(label4)).place(x=40,y=150)
label4.place(x=40,y=125) #se agregan las etiquetas al frame4
# Widgets para el frame2
boton4 = tk.Button(frame4,text="Modificar Puertos", command=lambda:modifyPort(logging)).place(x=90,y=150)
# Widgets para el frame2
button2 = tk.Button(frame4,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame4,frameMenuEflow)).place(x=275,y=240)
button8 = tk.Button(frame4,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame4,frameMenuPrincipal)).place(x=275,y=270)
button6 = tk.Button(frame4, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame4----------------------------------------------------------

#------Creacion de los componentes para el Frame5----------------------------------------------------------
#Declaracion de los label al frame5
frame5 = Frame(menu) 
frame5.config(bg=colorframe5)  
frame5.config(width=425,height=350) 
Titulo5 = tk.Label(frame5,text="Configurador de citas",font=Helvfont,pady=24,bg=colorframe5)
Titulo5.place(x=40,y=0)
label5 = tk.Label(frame5,text="",bg=colorframe5)
#Declaracion de los label al frame3
labelsvr = tk.Label(frame5,text="Introduzca el nombre del servidor ",bg=colorframe5)
Textboxsvr = tk.Entry(frame5)
labelCitas = tk.Label(frame5,text="Introduzca el nombre de sitio de citas",bg=colorframe5)
TextboxCitas = tk.Entry(frame5)
labelEflow = tk.Label(frame5,text="Introduzca el nombre de sitio de e-Flow",bg=colorframe5)
TextboxEflow = tk.Entry(frame5)
labelMSMQ = tk.Label(frame5,text="Introduzca el nombre de la cola de mensajeria",bg=colorframe5)
TextboxMSMQ = tk.Entry(frame5)
Textboxsvr.place(x=40,y=80)
TextboxCitas.place(x=40,y=120)
TextboxEflow.place(x=40,y=160)
TextboxMSMQ.place(x=40,y=200)
labelsvr.place(x=40,y=60)
labelCitas.place(x=40,y=100)
labelEflow.place(x=40,y=140)
labelMSMQ .place(x=40,y=180)
#Declaracion y agregacion de los botones al frame4
boton1 = tk.Button(frame5,text="Buscar", command=lambda:ExamineDirectory(label5)).place(x=40,y=240)
label5.place(x=40,y=220) #se agregan las etiquetas al frame4
# Widgets para el frame2
boton4 = tk.Button(frame5,text="configurar citas", command=lambda:modifyAppointment(logging)).place(x=90,y=240)
# Widgets para el frame2
button5 = tk.Button(frame5,width=16,height=1, text="Back to Citas", command=lambda: show_frame(frame5,frameMenuCitas)).place(x=275,y=240)
button8 = tk.Button(frame5,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame5,frameMenuPrincipal)).place(x=275,y=270)
button6 = tk.Button(frame5, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame5----------------------------------------------------------

#------Creacion de los componentes para el Frame6: FRAME DE CREACION DE SITE----------------------------------------------------------
#Declaracion de los label al frame6
frame6 = Frame(menu) 
frame6.config(bg=colorframe5)  
frame6.config(width=425,height=350) 
Titulo6 = tk.Label(frame6,text="Creador de Sites en IIS",font=Helvfont,pady=24,bg=colorframe5)
Titulo6.place(x=40,y=0)
label6 = tk.Label(frame6,text="",bg=colorframe5)
#Declaracion de los label al frame2
TextboxNameSite = tk.Entry(frame6,width=60)
TextboxNameSite.insert(1,"")
labelPortHttp  = tk.Label(frame6,text="Introduzca el puerto del site",bg=colorframe5)
TextboxPortHttp = tk.Entry(frame6,width=5)
TextboxPortHttp.insert(1,"")
labelPortHttp.place(x=40,y=180)
TextboxPortHttp.place(x=40,y=200)
#Declaracion y agregacion de los botones al frame2
boton1 = tk.Button(frame6,text="Buscar", command=lambda:ExamineDirectory(label6)).place(x=40,y=135)
TextboxNameSite.place(x=40,y=100)
label6.place(x=40,y=116) #se agregan las etiquetas al frame2
boton4 = tk.Button(frame6,text="Crear Site", command=lambda:createSite(logging)).place(x=40,y=250)
# Widgets para el frame2
button2 = tk.Button(frame6,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame6,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame6,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame6,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame6, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame6----------------------------------------------------------

#------Creacion de los componentes para el Frame7: FRAME DE Configurador de NCache----------------------------------------------------------
#Declaracion de los label al frame7
frame7 = Frame(menu) 
frame7.config(bg=colorframe5)  
frame7.config(width=425,height=350) 
Titulo7 = tk.Label(frame7,text="Configurador de NCache",font=Helvfont,pady=24,bg=colorframe5)
Titulo7.place(x=40,y=0)
label7 = tk.Label(frame7,text="",bg=colorframe5)
#Declaracion de los label al frame7
labelsvr = tk.Label(frame7,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrC = tk.Entry(frame7)
labelCache = tk.Label(frame7,text="Introduzca el nombre del Cache",bg=colorframe5)
TextboxCache = tk.Entry(frame7)
TextboxsvrC.place(x=40,y=200)
TextboxCache.place(x=40,y=240)
labelsvr.place(x=40,y=180)
labelCache.place(x=40,y=220)
#Declaracion y agregacion de los botones al frame2
boton1 = tk.Button(frame7,text="Buscar", command=lambda:ExamineDirectory(label7)).place(x=40,y=135)
label7.place(x=40,y=116) #se agregan las etiquetas al frame2
boton4 = tk.Button(frame7,text="Modificar NCache", command=lambda:modifyNCache(logging)).place(x=40,y=270)
# Widgets para el frame2
button2 = tk.Button(frame7,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame7,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame7,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame7,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame7, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame6----------------------------------------------------------

#------Creacion de los componentes para el Frame8: FRAME DE Configurador NME----------------------------------------------------------
#Declaracion de los label al frame8
frame8 = Frame(menu) 
frame8.config(bg=colorframe5)  
frame8.config(width=425,height=350) 
Titulo8 = tk.Label(frame8,text="Configurador de NME",font=Helvfont,pady=24,bg=colorframe5)
Titulo8.place(x=40,y=0)
label8 = tk.Label(frame8,text="",bg=colorframe5)
labelsvr = tk.Label(frame8,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrNME = tk.Entry(frame8)
labeleFlowNME = tk.Label(frame8,text="Introduzca el nombre de la aplicacion de e-Flow",bg=colorframe5)
TextboxeFlowNME = tk.Entry(frame8)
labelAPI = tk.Label(frame8,text="Introduzca el nombre de la API",bg=colorframe5)
TextboxeAPI = tk.Entry(frame8)
TextboxsvrNME.place(x=40,y=160)
TextboxeFlowNME.place(x=40,y=200)
TextboxeAPI.place(x=40,y=240)
labelsvr.place(x=40,y=140)
labeleFlowNME.place(x=40,y=180)
labelAPI.place(x=40,y=220)
#Declaracion y agregacion de los botones al frame8
boton1 = tk.Button(frame8,text="Buscar", command=lambda:ExamineDirectory(label8)).place(x=40,y=115)
label8.place(x=40,y=96) #se agregan las etiquetas al frame8
boton4 = tk.Button(frame8,text="Modificar NME", command=lambda:modifyNME(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame8,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame8,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame8,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame8,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame8, text="",image=confImg ,command=lambda: show_frame(frame,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame8----------------------------------------------------------



#------Creacion de los componentes para el Frame Configuracion----------------------------------------------------------
#Declaracion de los label al Frame Configuracion
frameConfiguracionColoresPrincipales = Frame(menu) 
frameConfiguracionColoresPrincipales.config(bg=colorframeC)  
frameConfiguracionColoresPrincipales.config(width=425,height=350) 
TituloC = tk.Label(frameConfiguracionColoresPrincipales,text="Configuracion de los colores principales",font=Helvfont,pady=24,bg=colorframeC)
TituloC.place(x=50,y=0)
#Declaracion y agregacion de los botones al Frame Configuracion
button5 = tk.Button(frameConfiguracionColoresPrincipales, text="Volver", command=lambda: show_frame(frameConfiguracionColoresPrincipales,frameMenuPrincipal)).place(x=350,y=270)
OPTIONS = getColors() #etc

labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="Instalador Servicio",bg=colorframeC)
labelColor1.place(x=120,y=70)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="Creador de aplicaciones",bg=colorframeC)
labelColor1.place(x=120,y=110)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="modificador de udl",bg=colorframeC)
labelColor1.place(x=120,y=150)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="modificador de puertos",bg=colorframeC)
labelColor1.place(x=120,y=190)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="configurador de citas",bg=colorframeC)
labelColor1.place(x=120,y=230)

comboBoxColo1 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor1, *OPTIONS)
comboBoxColo1.place(x=270,y=65,width=100)
comboBoxColo2 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor2, *OPTIONS)
comboBoxColo2.place(x=270,y=105,width=100)
comboBoxColo3 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor3, *OPTIONS)
comboBoxColo3.place(x=270,y=145,width=100)
comboBoxColo4 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor4, *OPTIONS)
comboBoxColo4.place(x=270,y=185,width=100)
comboBoxColo5 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor5, *OPTIONS)
comboBoxColo5.place(x=270,y=225,width=100)
buttonC1 = Button(frameConfiguracionColoresPrincipales,bg="#000",fg="#FFF",width=15,height=1,text="Colores principales").place(x=0,y=100)
buttonC2 = Button(frameConfiguracionColoresPrincipales,width=15,height=1,text="Colores Secundarios", command=lambda:show_frame(frameConfiguracionColoresPrincipales,frameConfiguracionColoresSecundarios)).place(x=0,y=150)
buttonC = Button(frameConfiguracionColoresPrincipales, text="Guardar", command=lambda:saveDataConfiguration(logging)).place(x=300,y=270)
#------Fin de la frameConfiguracionColoresPrincipales de los componentes para el Frame Configuracion----------------------------------------------------------

#------Creacion de los componentes para el Frame Configuracion----------------------------------------------------------
#Declaracion de los label al Frame Configuracion
frameConfiguracionColoresSecundarios =Frame(menu) 
frameConfiguracionColoresSecundarios.config(bg=colorframeC)  
frameConfiguracionColoresSecundarios.config(width=425,height=350) 
TituloC = tk.Label(frameConfiguracionColoresSecundarios,text="Configuracion de los colores secundario",font=Helvfont,pady=24,bg=colorframeC)
TituloC.place(x=50,y=0)
#Declaracion y agregacion de los botones al Frame Configuracion
button5 = tk.Button(frameConfiguracionColoresSecundarios, text="Volver", command=lambda: show_frame(frameConfiguracionColoresSecundarios,frameMenuPrincipal)).place(x=350,y=270)
OPTIONS = getColors() #etc



buttonC1 = Button(frameConfiguracionColoresSecundarios,width=15,height=1,text="Colores principales", command=lambda:show_frame(frameConfiguracionColoresSecundarios,frameConfiguracionColoresPrincipales)).place(x=0,y=100)
buttonC2 = Button(frameConfiguracionColoresSecundarios,bg="#000",fg="#FFF",width=15,height=1,text="Colores Secundarios").place(x=0,y=150)
buttonC = Button(frameConfiguracionColoresSecundarios, text="Guardar", command=lambda:saveDataConfiguration(logging)).place(x=300,y=270)
#------Fin de la Creacion de los componentes para el Frame Configuracion----------------------------------------------------------


imagenSidesys=tk.Label(frame,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame2,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame3,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame4,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame5,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frameMenuPrincipal,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
menu.bind('<Key>', on_key_pressed)
menu.bind_all("<Control-n>", new_Archive)
menu.bind_all("<Control-c>", showConfiguration )
menu.mainloop()
logging.info(f' {datetime.datetime.now() }: Fin de la ejecucion de la Aplicacion')

# Import-Module WebAdministration
# New-Item 'IIS:\Sites\Default Web Site\DemoApp' -physicalPath c:\test -type Application