from tkinter import *
from Validador import *
from script import *
from iis import *
from udl import *
from db import *
from portService import *
import os
import sys
from funcionesAuxiliares import *
from tkinter import messagebox as MessageBox,font
import tkinter.filedialog
import logging
import datetime
import tkinter as tk

def showConfiguration(event=None):show_Configuration(frame,frame2,frame3,frameC)
def loadColor(color):
  frame.config(bg= color[0])
  frame3.config(bg= color[2])
  frame4.config(bg= color[3])
  Titulo.config(bg= color[0])
  Titulo2.config(bg= color[1])
  Titulo3.config(bg= color[2])
  Titulo4.config(bg= color[3])
  frame2.config(bg= color[1])
  label1.config(bg= color[0])
  label2.config(bg= color[1])
  label3.config(bg= color[2])
  label4.config(bg= color[3])
  labelPort.config(bg= color[3])
  labeldb.config(bg= color[2])
  labelsrv.config(bg= color[2])
  R1.config(bg= color[0])
  R2.config(bg= color[0])
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

def validate_entry(text):
    # Validar la entrada del usuario
    if len(text) <= 3:
        return True
    else:
        return False

def on_key_pressed(event=None):
  k.config(text=str(ko(event,int(k.cget("text")))))
  if(int(k.cget("text"))==9):
    
    tk.messagebox.showinfo(title="codigo konami", message="FELICIDADES CRACK!!!!!,\nTE GANASTE EL ACCESO AL PUNTERO CHEAT ")
    loadColor(["#D4AF37","#D4AF37","#D4AF37","#D4AF37"])
    menu.config(cursor="pirate")
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
#esta funcion se encarga de crear la aplicacion en el iis
def createAplication(loggin):
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
    if(createAplicationIIS(Textboxb.get(),label2.cget("text"),loggin)):tk.messagebox.showinfo(title="Felicidades", message="La aplicacion se instalo correctamente")
#esta funcion se encarga de modificar los udls 
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
  if( validateDirectory(label4.cget("text"),"Middleware") or validateDirectory(label4.cget("text"),"MiddlewareNode") or validateDirectory(label4.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  los puertos,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  los puertos,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de los puertos')
    print("Paso todas las pruebas, comenzando proceso de modificacion de los puertos")
    changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    bandera=False  
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
    logging.error(f' {datetime.datetime.now() }: No se puede modificar los UDLS sin especificar el nombre de la base de datos')
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
  setConfiguration([fixWord(variableColor1.get()),1],[fixWord(variableColor2.get()),2],[fixWord(variableColor3.get()),3], [fixWord(variableColor4.get()),4],loggin,datetime.datetime.now())
  loadColor([getColor(1,"codigo"),getColor(2,"codigo"),getColor(3,"codigo"),getColor(4,"codigo")])
  tk.messagebox.showinfo(title="Los cambios se guardaron satisfactoriamente", message="Los cambios se guardaron satisfactoriamente \nPara ver los cambios, dar click en volver")
  #os.execl(sys.executable, sys.executable, * sys.argv) 
#Declaracion del Loggin
logging.basicConfig(filename=f'Logs\event {datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')


colorframe1=getColor(1,"codigo")
colorframe2=getColor(2,"codigo")
colorframe3=getColor(3,"codigo")
colorframe4=getColor(4,"codigo")
colorframeC="#555"
#Declaracion de la instancia de la aplicacion a utilizar
menu = tk.Tk()
menu.title("Instalador de servicios Unicos V0.98.5")
menu.geometry('500x350')
Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
menu.config(relief="sunken") 
menu.config(bg="blue")          # color de fondo, background
menu.config(bd=25)  
barra_menus = tk.Menu()
# Crear el primer menú.
menu_archivo = tk.Menu(barra_menus, tearoff=False)
menu_opciones = tk.Menu(barra_menus, tearoff=False)
# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Configuracion")
menu.config(menu=barra_menus)
menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command=new_Archive 
)
menu_opciones.add_command(
    label="Configurar",
    accelerator="Ctrl+c",
    command=lambda:show_Configuration(frame,frame2,frame3,frameC)
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
menu_archivo
#------Creacion de los componentes para el Frame------------------------------------------------------------------------------------
frame = Frame(menu)
frame.config(bg=colorframe1)  
frame.config(width=425,height=350) 
frame.pack()
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
button2 = tk.Button(frame, text="Creador de aplicaciones", command=lambda: show_frame(frame,frame2)).place(x=275,y=240)
button5 = tk.Button(frame, text="Configurador de UDLS", command=lambda: show_frame(frame,frame3)).place(x=275,y=270)
button7 = tk.Button(frame, text="Modificador de puertos", command=lambda: show_frame(frame,frame4)).place(x=130,y=270)
button6 = tk.Button(frame, text="",image=confImg ,command=lambda: show_frame(frame,frameC)).place(x=375,y=40)
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
boton1 = tk.Button(frame2,text="Buscar", command=lambda:ExamineDirectory(label2)).place(x=40,y=150)
Textboxb.place(x=40,y=100)
label2.place(x=40,y=125) #se agregan las etiquetas al frame2
boton4 = tk.Button(frame2,text="Crear Aplicacion", command=lambda:createAplication(logging)).place(x=90,y=150)
# Widgets para el frame2
button2 = tk.Button(frame2, text="Instalador de servicio", command=lambda: show_frame(frame2,frame)).place(x=275,y=240)
button5 = tk.Button(frame2, text="Configurador de UDLS", command=lambda: show_frame(frame2,frame3)).place(x=275,y=270)
button7 = tk.Button(frame2, text="Modificador de puertos", command=lambda: show_frame(frame2,frame4)).place(x=130,y=270)
button6 = tk.Button(frame2, text="",image=confImg ,command=lambda: show_frame(frame2,frameC)).place(x=375,y=40)
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
Textboxb = tk.Entry(frame3,width=60)
Textboxb.insert(1,"")
#Declaracion y agregacion de los botones al frame3
boton1 = tk.Button(frame3,text="Buscar", command=lambda:ExamineDirectory(label3)).place(x=40,y=150)
labeldb = tk.Label(frame3,text="Introduzca el nombre del servidor ",bg=colorframe3)
Textboxdb = tk.Entry(frame3)
labelsrv = tk.Label(frame3,text="Introduzca el nombre de la base de datos",bg=colorframe3)
Textboxsrv = tk.Entry(frame3)
Textboxb.place(x=40,y=100)
Textboxdb.place(x=40,y=240)
Textboxsrv.place(x=40,y=200)
labeldb.place(x=40,y=180)
labelsrv.place(x=40,y=220)
label3.place(x=40,y=125) #se agregan las etiquetas al frame3
boton4 = tk.Button(frame3,text="Modificar UDLS", command=lambda:modifyUDL(logging)).place(x=90,y=150)
# Widgets para el frame2
button2 = tk.Button(frame3, text="Instalador de servicio", command=lambda: show_frame(frame3,frame)).place(x=275,y=240)
button5 = tk.Button(frame3, text="Creador de aplicaciones", command=lambda: show_frame(frame3,frame2)).place(x=275,y=270)
button7 = tk.Button(frame3, text="Modificador de puertos", command=lambda: show_frame(frame3,frame4)).place(x=130,y=270)
button6 = tk.Button(frame3, text="",image=confImg ,command=lambda: show_frame(frame3,frameC)).place(x=375,y=40)

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
button2 = tk.Button(frame4, text="Instalador de servicio", command=lambda: show_frame(frame4,frame)).place(x=275,y=240)
button5 = tk.Button(frame4, text="Creador de aplicaciones", command=lambda: show_frame(frame4,frame2)).place(x=275,y=270)
button7 = tk.Button(frame4, text="Configurador UDLS", command=lambda: show_frame(frame4,frame3)).place(x=130,y=270)
button6 = tk.Button(frame4, text="",image=confImg ,command=lambda: show_frame(frame4,frameC)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame4----------------------------------------------------------

#------Creacion de los componentes para el Frame Configuracion----------------------------------------------------------
#Declaracion de los label al Frame Configuracion
frameC = Frame(menu) 
frameC.config(bg=colorframeC)  
frameC.config(width=425,height=350) 
TituloC = tk.Label(frameC,text="Configuracion del aplicativo",font=Helvfont,pady=24,bg=colorframeC)
TituloC.place(x=40,y=0)
#Declaracion y agregacion de los botones al Frame Configuracion
button5 = tk.Button(frameC, text="Volver", command=lambda: show_frame(frameC,frame)).place(x=350,y=270)
OPTIONS = getColors() #etc

labelColor1 = tk.Label(frameC,text="Color frame 1",bg=colorframeC)
labelColor1.place(x=10,y=100)
labelColor1 = tk.Label(frameC,text="Color frame 2",bg=colorframeC)
labelColor1.place(x=10,y=140)
labelColor1 = tk.Label(frameC,text="Color frame 3",bg=colorframeC)
labelColor1.place(x=10,y=180)
labelColor1 = tk.Label(frameC,text="Color frame 4",bg=colorframeC)
labelColor1.place(x=10,y=220)

comboBoxColo1 = OptionMenu(frameC, variableColor1, *OPTIONS)
comboBoxColo1.place(x=270,y=95,width=100)
comboBoxColo2 = OptionMenu(frameC, variableColor2, *OPTIONS)
comboBoxColo2.place(x=270,y=135,width=100)
comboBoxColo3 = OptionMenu(frameC, variableColor3, *OPTIONS)
comboBoxColo3.place(x=270,y=175,width=100)
comboBoxColo4 = OptionMenu(frameC, variableColor4, *OPTIONS)
comboBoxColo4.place(x=270,y=215,width=100)

buttonC = Button(frameC, text="Guardar", command=lambda:saveDataConfiguration(logging)).place(x=300,y=270)
#------Fin de la Creacion de los componentes para el Frame Configuracion----------------------------------------------------------


imagenSidesys=tk.Label(frame,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame2,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame3,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
imagenSidesys=tk.Label(frame4,text="0",image=imagen,width=40,height=40)
imagenSidesys.place(x=0,y=0)
menu.bind('<Key>', on_key_pressed)
menu.bind_all("<Control-n>", new_Archive)
menu.bind_all("<Control-c>", showConfiguration )
menu.mainloop()
logging.info(f' {datetime.datetime.now() }: Fin de la ejecucion de la Aplicacion')

# Import-Module WebAdministration
# New-Item 'IIS:\Sites\Default Web Site\DemoApp' -physicalPath c:\test -type Application