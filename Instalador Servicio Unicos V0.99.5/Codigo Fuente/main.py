from tkinter import *
from Code import *
from Validador import *
from script import *
from iis import *
from udl import *
from db import *
from NCache import *
from NME import *
from Nodo import *
from portService import *
from configuracionCitas import *
from RHI import *
from mail import *
from Reporte import *
from Encuesta import *
from Consola import *
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
  frame6.config(bg= color[4])
  frame7.config(bg= color[4])
  frame8.config(bg= color[4])
  frame9.config(bg= color[4])
  frame10.config(bg= color[4])
  frame11.config(bg= color[4])
  frame12.config(bg= color[4])
  frame13.config(bg= color[4])
  Titulo.config(bg= color[0])
  Titulo2.config(bg= color[1])
  Titulo3.config(bg= color[2])
  Titulo4.config(bg= color[3])
  Titulo5.config(bg= color[4])
  Titulo6.config(bg= color[4])
  Titulo7.config(bg= color[4])
  Titulo8.config(bg= color[4])
  Titulo9.config(bg= color[4])
  Titulo10.config(bg= color[4])
  Titulo11.config(bg= color[4])
  Titulo12.config(bg= color[4])
  Titulo13.config(bg= color[4])
  frame2.config(bg= color[1])
  label1.config(bg= color[0])
  label2.config(bg= color[1])
  label3.config(bg= color[2])
  label4.config(bg= color[3])
  label5.config(bg= color[4])
  label6.config(bg= color[4])
  label7.config(bg= color[4])
  label8.config(bg= color[4])
  label9.config(bg= color[4])
  label10.config(bg= color[4])
  label11.config(bg= color[4])
  label12.config(bg= color[4])
  label13.config(bg= color[4])
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
    if os.path.exists(f"{path}\{name}") and os.path.isdir(f"{path}\{name}"):
        print(f' {datetime.datetime.now() }: La carpeta {path}\{name} existe')
        logging.info(f' {datetime.datetime.now() }: La carpeta {name}  existe')
        return False
        
    else:
        print(f' {datetime.datetime.now() }: La carpeta {path}\{name} no existe')
        logging.error(f' {datetime.datetime.now() }: La carpeta {name} no existe')
        return True
        
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
def setStart():
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
  path = tkinter.filedialog.askopenfilename()
  if(p==1 and validateService(path.lower(),"sidesys.services.applicationservice.exe","middleware","bin")):label1.config(text=path) 
  if(p==2 and validateService(path.lower(),".xml","FrontEnd","view_configuration")):
    label16.config(text=path) 
    TextboxNodeFont.delete(0, tk.END)
    TextboxNodeVoice.delete(0, tk.END)
    TextboxNodeHeaderColor.delete(0, tk.END)
    TextboxNodeFooterColor.delete(0, tk.END)
    TextboxNodeNumberSize.delete(0, tk.END)
    
    TextboxNodeFont.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','fontFamily":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeVoice.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','voice":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeHeaderColor.insert(0, IdentifyJSON(path,'"header":{[\S|\s]+"logo"','backgroundColor":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeFooterColor.insert(0, IdentifyJSON(path,'"footer":{[\S|\s]+"alignContent"','backgroundColor":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberSize.insert(0, IdentifyJSON(path,'"numbersTableBody":{[\S|\s]+"columnTask"','fontSize":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
      
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
#esta funcion se encarga de Seleccionar el directorio y carga las horas
def ExamineDirectoryRHI(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de hora y minutos del proceso historico')
  Path = tkinter.filedialog.askdirectory()
  Path =Path
  #if(validateService(Path.lower(),"Scheduling.config","middleware","ConfigFiles")):  
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
    Path = Path.replace("/", r"\ ".strip())
    Path=Path.rstrip()
    label.config(text=Path) 
    hour.set(identifyHour(Path,logging, datetime))
    minute.set(identifyMinute(Path,logging, datetime))
    print(Path)
    return Path
#esta funcion se encarga de examinar el directorio.
def ExamineDirectoryReporteria(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de reportes')
  path = tkinter.filedialog.askdirectory()
  path =path
  #if(validateService(Path.lower(),"Scheduling.config","middleware","ConfigFiles")):  
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {path}')
    path = path.replace("/", r"\ ".strip())
    path=path.rstrip()
    if(validateDirectory(f'{path}\\FrontEnd',"STE")==False):
      version=identifyVersion(f"{path}\\FrontEnd\STE\\bin\eflow.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      labelReporteriaEflow.config(fg= "green", text=f"e-Flow    {version}")     
      print("Existe e-Flow")
    else:
      labelReporteriaEflow.config(fg= "red", text=f"e-Flow")  
    if(validateDirectory(f'{path}\\FrontEnd',"Appointment")==False):
      version=identifyVersion(f"{path}\\\FrontEnd\Appointment\\bin\Application.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      labelReporteriaCitas.config(fg= "green", text=f"Citas        {version}")      
      print("Existe Citas")
    else:
      labelReporteriaCitas.config(fg= "red", text=f"Citas")  
    if(validateDirectory(f'{path}\\FrontEnd',"OpinionPoll")==False):      
      version=identifyVersion(f"{path}\\FrontEnd\OpinionPoll\\bin\OpinionPoll.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      labelReporteriaEncuesta.config(fg= "green", text=f"Encuesta v{version}")
      print("Existe encuesta")
    else:
      labelReporteriaEncuesta.config(fg= "red", text=f"Encuesta")
    label.config(text=path) 
    print(path)
    return path
#esta funcion se encarga de examinar los minutos de la sesion del usuario
def ExamineDirectoryConsoleSesion(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de la sesion en consola')
  Path = tkinter.filedialog.askdirectory()
  Path =Path
  #if(validateService(Path.lower(),"Scheduling.config","middleware","ConfigFiles")):  
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
    Path = Path.replace("/", r"\ ".strip())
    Path=Path.rstrip()
    label.config(text=Path) 
    minuteSesion.set(identifyMinuteSesion(Path,logging, datetime))
    print(Path)
    return Path
#esta funcion se encarga de Seleccionar el directorio y carga las horas
def ExamineDirectoryNME(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de datos de NME')
  Path = tkinter.filedialog.askdirectory()
  Path =Path
  #if(validateService(Path.lower(),"Scheduling.config","middleware","ConfigFiles")):  
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
    Path = Path.replace("/", r"\ ".strip())
    Path=Path.rstrip()
    label.config(text=Path) 
    if(identifyNME(Path)):preferencialVar.set(1)
    else:preferencialVar.set(0)
    print(Path)
    return Path
#esta funcion se encarga de ejecutar el script
def executeScript():
  logging.info(f' {datetime.datetime.now() }: Se esta ejecutando la instalacion del servicio')
  if(label1.cget("text")!="" and Textbox.get()!=""): 
    if(installService(Textbox.get(),label1.cget("text"),setStart(),logging)):tk.messagebox.showinfo(title="Felicidades", message="El servicio se instalo correctamente")
    else: MessageBox.showerror("Error","El servicio no se ha instalado, valide que se este ejecutando como administrador")
  #mensajes ante posible errores
  if(label1.cget("text")==""): MessageBox.showerror("Error","Debe de haber seleccionado El servicio a instalar")
  if(Textbox.get()==""): MessageBox.showerror("Error","Debe de ingresar un nombre para su servicio a crear")
  if(setStart()==0):MessageBox.showerror("Error","Debe seleccionar si el servicio iniciara en automatico o manual")
#Este metodo se encarga de automatizar el proceso
def automateProcess(loggin):
  print("Estoy automatizando el proceso")
  print (label17.cget("text"))
  print(TextboxAutomatizadorSRVBD.get())
  print(TextboxAutomatizadorSRVAPP.get())
  print(TextboxAutomatizadorName.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a automatizar el aplicativo')
  bandera=True
  if( TextboxAutomatizadorSRVBD.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede automatizar el aplicativo sin especificar el nombre del servidor de base de datos')
    MessageBox.showerror("Error","No se puede automatizar el aplicativon sin especificar el nombre del servidor de base de datos")
    bandera=False
  if( TextboxAutomatizadorSRVAPP.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede automatizar el aplicativo sin especificar el nombre del servidor de la aplicaciones')
    MessageBox.showerror("Error","No se puede automatizar el aplicativon sin especificar el nombre del servidor de la aplicaciones")
    bandera=False
  if( TextboxAutomatizadorName.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede automatizar el aplicativo sin especificar el nombre del aplicativo')
    MessageBox.showerror("Error","No se puede automatizar el aplicativo sin especificar el nombre del aplicativo")
    bandera=False
  if( label17.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede automatizar el aplicativon sin especificar la ruta')
    MessageBox.showerror("Error","Para automatizar el aplicativo debe de tener una ruta")
    bandera=False
  if( validateDirectory(label17.cget("text"),"Middleware")  or validateDirectory(label17.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede automatizar el aplicativo ,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para automatizar el aplicativo, tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso automatizacion ')
    print("Paso todas las pruebas, comenzando proceso de automatizacion")
    #Instala el servicio de e-Flow
    installService(f'e-Flow {TextboxAutomatizadorName.get()} Middleware Service',f'{label17.cget("text")}\MiddleWare\STE\\bin\Sidesys.Services.ApplicationService.exe','demand',loggin)
    #Instala el servicio de e-Flow Nodo
    installService(f'e-Flow {TextboxAutomatizadorName.get()} MiddlewareNode Service',f'{label17.cget("text")}\MiddleWareNode\STE\\bin\Sidesys.Services.ApplicationService.exe','demand',loggin)
    #Instala el servicio de Citas
    installService(f'e-Flow Citas {TextboxAutomatizadorName.get()} Middleware Service',f'{label17.cget("text")}\MiddleWare\Appointment\\bin\Sidesys.Services.ApplicationService.exe','demand',loggin)
    #Instala el servicio de Encuesta
    installService(f'e-Flow Encuesta {TextboxAutomatizadorName.get()} Middleware Service',f'{label17.cget("text")}\MiddleWare\OpinionPoll\\bin\Sidesys.Services.ApplicationService.exe','demand',loggin)
  if(TextboxAutomatizadorName.get()=="STE"):
    createAplicationIIS("STE",f'{label17.cget("text")}\FrontEnd\STE',loggin)
    createAplicationIIS("Appointment",f'{label17.cget("text")}\FrontEnd\Appointment',loggin)
    createAplicationIIS("AppointmentWeb",f'{label17.cget("text")}\FrontEnd\AppointmentWeb',loggin)
    createAplicationIIS("AppointmentWebService",f'{label17.cget("text")}\FrontEnd\AppointmentWebService',loggin)
    createAplicationIIS("OpinionPoll",f'{label17.cget("text")}\FrontEnd\OpinionPoll',loggin)
  else:
    createAplicationIIS(f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\FrontEnd\STE',loggin)
    createAplicationIIS(f"{TextboxAutomatizadorName.get()}-Appointment",f'{label17.cget("text")}\FrontEnd\Appointment',loggin)
    createAplicationIIS(f"{TextboxAutomatizadorName.get()}-AppointmentWeb",f'{label17.cget("text")}\FrontEnd\AppointmentWeb',loggin)
    createAplicationIIS(f"{TextboxAutomatizadorName.get()}-AppointmentWebService",f'{label17.cget("text")}\FrontEnd\AppointmentWebService',loggin)
    createAplicationIIS(f"{TextboxAutomatizadorName.get()}-OpinionPoll",f'{label17.cget("text")}\FrontEnd\OpinionPoll',loggin)

  if(TextboxAutomatizadorName.get()=="STE"):
    manageUDL(TextboxAutomatizadorSRVBD.get(),"STE",f'{label17.cget("text")}\MiddleWare\STE\\ConfigFiles',loggin)
    manageUDL(TextboxAutomatizadorSRVBD.get(),"STE",f'{label17.cget("text")}\MiddleWareNode\STE\\ConfigFiles',loggin)
    manageUDL(TextboxAutomatizadorSRVAPP.get(),"Appointment",f'{label17.cget("text")}\MiddleWare\Appointment\\ConfigFiles',loggin)
    manageUDL(TextboxAutomatizadorSRVBD.get(),"STE",f'{label17.cget("text")}\MiddleWare\OpinionPoll\\ConfigFiles',loggin)  
  else:
    manageUDL(TextboxAutomatizadorSRVBD.get(),f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\MiddleWare\STE\\ConfigFiles',loggin)
    manageUDL(TextboxAutomatizadorSRVBD.get(),f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\MiddleWareNode\STE\\ConfigFiles',loggin)
    manageUDL(TextboxAutomatizadorSRVAPP.get(),f"{TextboxAutomatizadorName.get()}-Appointment",f'{label17.cget("text")}\MiddleWare\Appointment\\ConfigFiles',loggin)
    manageUDL(TextboxAutomatizadorSRVBD.get(),f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\MiddleWare\OpinionPoll\\ConfigFiles',loggin)
#esta funcion se encarga de crear los site en el iis
def createSite(loggin):
  logging.info(f' {datetime.datetime.now() }: Se comienza a crear el site')
  bandera=True
  print(TextboxNameSite.get())
  print(TextboxPortHttp.get())
  print(label6.cget("text"))
  if( TextboxNameSite.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear el site sin especificar nombre del site')
    MessageBox.showerror("Error","Para crear el site debe de insertar un nombre")
    bandera=False
  if( TextboxPortHttp.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear el site sin especificar nombre del puerto del site')
    MessageBox.showerror("Error","Para crear el site debe de insertar un nombre")
    bandera=False
  if( label6.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede crear una aplicacion sin especificar la ruta')
    MessageBox.showerror("Error","Para crear el site debe de tener una ruta")
    bandera=False
  print(bandera)
  if(bandera):
    if(createSiteIIS(TextboxNameSite.get(),label6.cget("text"),loggin,TextboxPortHttp.get())):tk.messagebox.showinfo(title="Felicidades", message="El site se creo correctamente")
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
#esta funcion se encarga de modificar la ejecucion del reporte historico integrado
def modifyRHI(loggin):
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion del historico integrado')
  bandera=True
  print(spinHour.get())
  print(spinMinute.get())
  print(label10.cget("text"))
  if( spinHour.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el horario de ejecucion del historico si la hora es nula o igual a 0')
    MessageBox.showerror("Error","No se puede modificar el horario de ejecucion del historico si la hora es nula o igual a 0")
    bandera=False
  if( spinMinute.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el horario de ejecucion del historico si la minutos es nula o igual a 0')
    MessageBox.showerror("Error","No se puede modificar el horario de ejecucion del historico si la minutos es nula o igual a 0")
    bandera=False
  if( label10.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el horario de ejecucion del historico sin especificar la ruta')
    MessageBox.showerror("Error","No se puede modificar el horario de ejecucion del historico sin especificar la ruta")
    bandera=False
  print(bandera)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion del historico integrado paso correctamente')
    configurarHorario(label10.cget("text"),spinHour.get(),spinMinute.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="La hora de ejecucion del historico integrado se modifico correctamente")
  #esta funcion se encarga de modificar la ejecucion del reporte historico integrado
#esta funcion se encarga de modificar el tiempo de sesion de la consola
def modifyConsoleSesion(loggin):
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion de la consola de sesion')
  bandera=True
  print(spinMinuteConsole.get())
  print(label13.cget("text"))
  if( spinMinute.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el horario de el tiempo de ejecucion de tiempo de consola si la minutos es nula o igual a 0')
    MessageBox.showerror("Error","No se puede modificar el horario de el tiempo de ejecucion de tiempo de consola si la minutos es nula o igual a 0")
    bandera=False
  if( label13.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el tiempo de ejecucion de tiempo de consola del historico sin especificar la ruta')
    MessageBox.showerror("Error","No se puede modificar el horario de el tiempo de ejecucion de tiempo de consola sin especificar la ruta")
    bandera=False
  print(bandera)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion del historico integrado paso correctamente')
    configurarMinuteConsole(label13.cget("text"),spinMinuteConsole.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="Se modifico correctamente el tiempo de sesion.")
#esta funcion se encarga de modificar el correo
def modifyMail(loggin):
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar el MailServer')
  bandera=True
  print(TextboxMailsrv.get())
  print(TextboxMailPort.get())
  print(varMail.get())
  print(TextboxMailSenderAccount.get())
  print(TextboxMailPassword.get())
  print(label11.cget("text"))
  if( label11.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el el MailServer sin especificar la ruta')
    MessageBox.showerror("Error","No se puede modificar el el MailServer sin especificar la ruta")
    bandera=False
  print(bandera)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion del historico integrado paso correctamente')
    #configurarHorario(label10.cget("text"),spinHour.get(),spinMinute.get(),logging,datetime)
    configurarMail(label11.cget("text"),varMail.get(),TextboxMailsrv.get(),TextboxMailPort.get(),TextboxMailSenderAccount.get(),TextboxMailPassword.get(),logging, datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El correo se configuro  correctamente")   
#esta funcion se encarga de modificar los parametros de encuestas
def modifyPoll(loggin):
  print("Estoy modificando Encuesta")
  print (label12.cget("text"))
  print(TextboxsvrEncuesta.get())
  print(TextboxEncuesta.get())
  print(TextboxEflowEncuesta.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  Encuesta')
  bandera=True
  if( TextboxsvrEncuesta.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar Encuesta sin especificar el nombre del servidor')
    MessageBox.showerror("Error","No se puede modificar  Encuesta sin especificar el nombre del servidor")
    bandera=False
  if( TextboxEncuesta.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar Encuesta sin especificar el nombre del sitio de Encuesta')
    MessageBox.showerror("Error","No se puede modificar  cita sin especificar el nombre del sitio de Encuesta")
    bandera=False
  if( TextboxEflowEncuesta.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar Encuesta sin especificar el nombre del sitio de e-Flow')
    MessageBox.showerror("Error","No se puede modificar  Encuesta sin especificar el nombre del sitio de e-Flow")
    bandera=False
  if( label12.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  Encuesta sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar  Encuesta debe de tener una ruta")
    bandera=False
  if( validateDirectory(label12.cget("text"),"Middleware")  or validateDirectory(label12.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  Encuesta,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  Encuesta,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de encuesta')
    print("Paso todas las pruebas, comenzando proceso de modificacion de Encuesta")
    #changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    configurarEncuesta(label12.cget("text"),TextboxsvrEncuesta.get(),TextboxEncuesta.get(),TextboxEflowEncuesta.get(),loggin,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de Encuesta termino el proceso de configuracion de los archivos")
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
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de citas')
    print("Paso todas las pruebas, comenzando proceso de modificacion de citas")
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
#esta funcion se encarga de configurar NME en e-Flow
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
    tk.messagebox.showinfo(title="Felicidades", message="NME termino el proceso de configuracion de los archivos")
    configurarNME(label8.cget("text"),TextboxsvrNME.get(),TextboxeFlowNME.get(),TextboxeAPI.get(),loggin,datetime)
#esta funcion se encarga de configurar NME en e-Flow
def modifyNMEEmissionConfig(loggin):
  print("Estoy modificando el emission.config")
  print (label15.cget("text"))
  print(preferencialVar.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  emission.config')
  bandera=True
  if( label15.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el emission.config sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar  emission.config debe de tener una ruta")
    bandera=False
  if( validateDirectory(label15.cget("text"),"Middleware")  or validateDirectory(label15.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el emission.config,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  el emission.config,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Nuevo Modulo de Emision')
    print("Paso todas las pruebas, comenzando proceso de modificacion de los emission.config")
    #changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    #configurarNCache( label7.cget("text"),TextboxsvrC.get(), TextboxCache.get(), loggin, datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El Emission.config termino el proceso de configuracion de los archivos")
    #configurarNME(label8.cget("text"),TextboxsvrNME.get(),TextboxeFlowNME.get(),TextboxeAPI.get(),loggin,datetime)
    configurarEmissionConfig(label15.cget("text"), preferencialVar.get(), loggin,datetime)
#esta funcion se encarga de configurar NME en e-Flow con site
def modifyNMESite(loggin):
  print("Estoy modificando NME con Site")
  print (label14.cget("text"))
  print(TextboxeFlowNMESite.get())
  print(TextboxeAPISite.get())
  print(TextboxsvrNMESite.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NME')
  bandera=True
  if( TextboxsvrNMESite.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Nuevo Modulo de Emision sin especificar el nombre del servidor')
    MessageBox.showerror("Error","No se puede modificar  Nuevo Modulo de el Emision sin especificar el nombre del servidor")
    bandera=False
  if( TextboxeFlowNMESite.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Nuevo Modulo de Emision sin especificar el nombre de la aplicacion de e-Flow')
    MessageBox.showerror("Error","No se puede modificar  el Nuevo Modulo de Emision sin especificar el nombre de la aplicacion de e-Flow")
    bandera=False
  if( TextboxeAPISite.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Nuevo Modulo de Emision sin especificar el nombre del Emission Api')
    MessageBox.showerror("Error","No se puede modificar  Nuevo Modulo de Emision sin especificar el nombre del Emission Api")
    bandera=False
  if( label14.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Nuevo Modulo de Emision sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar  Nuevo Modulo de Emision debe de tener una ruta")
    bandera=False
  if( validateDirectory(label14.cget("text"),"Middleware")  or validateDirectory(label14.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Nuevo Modulo de Emision,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  el Nuevo Modulo de Emision,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Nuevo Modulo de Emision')
    print("Paso todas las pruebas, comenzando proceso de modificacion de los Nuevo Modulo de Emision")
    #changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    #configurarNCache( label7.cget("text"),TextboxsvrC.get(), TextboxCache.get(), loggin, datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El NME con site termino el proceso de configuracion de los archivos")
    configurarNMESite(label14.cget("text"),TextboxsvrNMESite.get(),TextboxeFlowNMESite.get(),TextboxeAPISite.get(),loggin,datetime)
#esta funcion se encarga de configurar NME en citas
def modifyNMECitas(loggin):
  print("Estoy modificando NME citas web service")
  print (label9.cget("text"))
  print(TextboxsvrNMECitas.get())
  print(TextboxCitasNME.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NME')
  bandera=True
  if(TextboxsvrNMECitas.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Web sevice de citas sin especificar el nombre del servidor')
    MessageBox.showerror("Error","No se puede modificar el Web sevice de citas sin especificar el nombre del servidor")
    bandera=False
  if(TextboxCitasNME.get()==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar el Web sevice de citas sin especificar el nombre de la aplicacion de e-Flow')
    MessageBox.showerror("Error","No se puede modificar  el Web sevice de citas sin especificar el nombre de la aplicacion de e-Flow")
    bandera=False
  if( label9.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Web sevice de citas sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar el Web sevice de citas debe de tener una ruta")
    bandera=False
  if( validateDirectory(label9.cget("text"),"Middleware")  or validateDirectory(label9.cget("text"),"FrontEnd")):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Web sevice de citas,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para modificar  el Web sevice de citas,tiene que estar en la carpeta del aplicativo")
    bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Web sevice de citas')
    print("Paso todas las pruebas, comenzando proceso de modificacion del Web sevice de citas")
    #changePort(label4.cget("text"),TextboxPort.get(),loggin,datetime)
    #configurarNCache( label7.cget("text"),TextboxsvrC.get(), TextboxCache.get(), loggin, datetime)
    #tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de NCache termino el proceso de configuracion de los archivos")
    #configurarNME(label8.cget("text"),TextboxsvrNME.get(),TextboxeFlowNME.get(),TextboxeAPI.get(),loggin,datetime)
    configurarNMECitas(label9.cget("text"),TextboxsvrNMECitas.get(),TextboxCitasNME.get(),logging,datetime)
#esta funcion se encarga de modificar el nodo xml
def modifyNode(loggin):
  print("Estoy modificando nod")
  print (label16.cget("text"))
  print(TextboxNodeFont.get())
  print(TextboxNodeVoice.get())
  print(TextboxNodeHeaderColor.get())
  print(TextboxNodeFooterColor.get())
  print(TextboxNodeNumberSize.get())
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar el nodo')
  bandera=True
  #if(TextboxNodeFont.get()==""):
  #  logging.error(f' {datetime.datetime.now() }: No se puede modificar el nodo.xml sin especificar el nombre de la fuente')
  #  MessageBox.showerror("Error","No se puede modificar el nodo.xmls sin especificar el nombre de la fuente")
  #  bandera=False
  #if(TextboxNodeVoice.get()==""):
  #  logging.error(f' {datetime.datetime.now() }: No se puede modificar el nodo.xml sin especificar el nombre de la voz')
  #  MessageBox.showerror("Error","No se puede modificar  el nodo.xml sin especificar el nombre de la voz")
  #  bandera=False
  #if(TextboxNodeHeaderColor.get()==""):
  #  logging.error(f' {datetime.datetime.now() }: No se puede modificar el nodo.xml sin especificar el nombre del color del header')
  #  MessageBox.showerror("Error","No se puede modificar  el nodo.xml sin especificar el nombre del color del header")
  #  bandera=False
  #if(TextboxNodeFooterColor.get()==""):
  #  logging.error(f' {datetime.datetime.now() }: No se puede modificar el nodo.xml sin especificar el nombre de la aplicacion de e-Flow')
  #  MessageBox.showerror("Error","No se puede modificar  el nodo.xml sin especificar el nombre de la aplicacion de e-Flow")
  #  bandera=False
  #if(TextboxNodeNumberSize.get()==""):
  #  logging.error(f' {datetime.datetime.now() }: No se puede modificar el nodo.xml sin especificar el nombre de la aplicacion de e-Flow')
  #  MessageBox.showerror("Error","No se puede modificar  el # sin especificar el nombre de la aplicacion de e-Flow")
  #  bandera=False
  if( label16.cget("text")==""):
    logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Web nodo.xml sin especificar la ruta')
    MessageBox.showerror("Error","Para modificar el nodo.xml debe de tener una ruta")
    bandera=False
  #if( validateDirectory(label16.cget("text"),"FrontEnd")):
  #  logging.error(f' {datetime.datetime.now() }: No se puede modificar  el Web sevice de citas,tiene que estar en la carpeta del aplicativo')
  #  MessageBox.showerror("Error","Para modificar  el Web sevice de citas,tiene que estar en la carpeta del aplicativo")
  #  bandera=False
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Web sevice de citas')
    print("Paso todas las pruebas, comenzando proceso de modificacion del Web sevice de citas")
   #configurarNMECitas(label9.cget("text"),TextboxsvrNMECitas.get(),TextboxCitasNME.get(),logging,datetime)
    configurarNodo(label16.cget("text"),TextboxNodeFont.get(),TextboxNodeVoice.get(),TextboxNodeHeaderColor.get(),TextboxNodeFooterColor.get(), TextboxNodeNumberSize.get(),logging,datetime)    

#esta funcion se encarga de modificar los puertos de e-Flow 
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
#esta funcion se encarga de modificar los UDLS
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
menu.title("Instalador de servicios Unicos V0.99.5")
menu.geometry('500x350')
menu.config(relief="sunken") 
menu.config(bg="blue")          # color de fondo, background
menu.config(bd=25)  
menu.resizable(False, False)
icono = tk.PhotoImage(file="img\icon-16.png")
menu.iconphoto(True, icono)
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
try:
  eflowimg= PhotoImage(file="img\eflow2.png")
  client= PhotoImage(file="img\client.png")
  citas= PhotoImage(file="img\citas.png")
  encuesta= PhotoImage(file="img\Encuesta.png")
  report= PhotoImage(file="img\\report.png")
  automatizacion= PhotoImage(file="img\\automatizacion.png")
  imagen= PhotoImage(file="img\sidesys.gif")
  confImg = PhotoImage(file='img\conf.png')
  correo = PhotoImage(file='img\correo.png')
except:
        print("No se han podido cargar las imagenes")
        logging.info(f' {datetime.datetime.now() }: La imagenes no fueron cargadas correctamente, valide que la carpeta img se encuentre en el aplicativo')
tk.Label(frameMenuPrincipal,text="0")

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
if(readValueSystem("<PrghIuhh>\w<PrghIuhh>")=="a"):buttonCorreo = tk.Button(frameMenuPrincipal,width=100,height=41,image = correo,text="Modo Libre", command=lambda: show_frame(frameMenuPrincipal,frameMenuML)).place(x=45,y=250)
# Widgets para el frame1-----------------------

#------Creacion de los componentes para el frameMenuEflow: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuEflow = Frame(menu)
frameMenuEflow.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuEflow,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuEflow,text="Menu e-Flow",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=160,y=30)

buttonEflowService = tk.Button(frameMenuEflow,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuEflow,frame)).place(x=45,y=100)
buttonEflowIIS = tk.Button(frameMenuEflow,width=20,height=1, text="IIS", command=lambda: show_frame(frameMenuEflow,framesubMenuIIS)).place(x=230,y=100)
buttonEflowUDL = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuEflow,frame3)).place(x=230,y=130)
buttonEflowSites = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador del nodo", command=lambda: show_frame(frameMenuEflow,frame16)).place(x=45,y=130)
buttonEflowPort = tk.Button(frameMenuEflow,width=20,height=1, text="Modificador de puertos", command=lambda: show_frame(frameMenuEflow,frame4)).place(x=45,y=160)
buttonEflowNCache = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador NCache", command=lambda: show_frame(frameMenuEflow,frame7)).place(x=230,y=160)
buttonEflowNME = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador NME", command=lambda: show_frame(frameMenuEflow,framesubMenuNME)).place(x=45,y=190)
buttonEflowProcesoHistorico = tk.Button(frameMenuEflow,width=20,height=1, text="Procesamiento del RHI", command=lambda: show_frame(frameMenuEflow,frame10)).place(x=230,y=190)
buttonEflowMail = tk.Button(frameMenuEflow,width=20,height=1, text="Configuracion de correo", command=lambda: show_frame(frameMenuEflow,frame11)).place(x=45,y=220)
buttonEflowConsole = tk.Button(frameMenuEflow,width=20,height=1, text="tiempo de sesion consola", command=lambda: show_frame(frameMenuEflow,frame13)).place(x=230,y=220)
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
Titulo.place(x=162,y=30)

buttonCitasService = tk.Button(frameMenuCitas,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuCitas,frame)).place(x=45,y=100)
buttonCitasIIS = tk.Button(frameMenuCitas,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(frameMenuCitas,frame2)).place(x=230,y=100)
buttonCitasUDL = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuCitas,frame3)).place(x=45,y=130)
buttonCitasPort = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de Citas", command=lambda: show_frame(frameMenuCitas,frame5)).place(x=230,y=130)
buttonCitasNME = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de NME", command=lambda: show_frame(frameMenuCitas,frame9)).place(x=45,y=160)
buttonCitasMail = tk.Button(frameMenuCitas,width=20,height=1, text="Configuracion de correo", command=lambda: show_frame(frameMenuCitas,frame11)).place(x=230,y=160)
buttonCitasBack = tk.Button(frameMenuCitas,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuCitas,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuCitas: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------


#------Creacion de los componentes para el frameMenuEncuesta: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuEncuesta = Frame(menu)
frameMenuEncuesta.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuEncuesta,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuEncuesta,text="Menu Encuestas",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)

buttonEncuestaService = tk.Button(frameMenuEncuesta,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuEncuesta,frame)).place(x=45,y=100)
buttonEncuestaIIS = tk.Button(frameMenuEncuesta,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(frameMenuEncuesta,frame2)).place(x=230,y=100)
buttonEncuestaUDL = tk.Button(frameMenuEncuesta,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuEncuesta,frame3)).place(x=45,y=130)
buttonEncuestaMail = tk.Button(frameMenuEncuesta,width=20,height=1, text="Configuracion de correo", command=lambda: show_frame(frameMenuEncuesta,frame11)).place(x=230,y=130)
buttonEncuestaConfig = tk.Button(frameMenuEncuesta,width=20,height=1, text="Configuracion de encuesta", command=lambda: show_frame(frameMenuEncuesta,frame12)).place(x=45,y=160)
buttonEncuestaBack = tk.Button(frameMenuEncuesta,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuEncuesta,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuEncuesta: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuReport: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuReport = Frame(menu)
frameMenuReport.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuReport,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuReport,text="Reportes",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)

buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte General", command=lambda: show_frame(frameMenuReport,frame18)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuReport,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuReport,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuReport: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuAuto = Frame(menu)
frameMenuAuto.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuAuto,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuAuto,text="Automatizacion del proceso",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)

buttonReporService = tk.Button(frameMenuAuto,width=20,height=1, text="Automatizador Basico", command=lambda: show_frame(frameMenuAuto,frame17)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuAuto,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuAuto,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuML = Frame(menu)
frameMenuML.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(frameMenuML,text="0")
#Declaracion de los label
Titulo = tk.Label(frameMenuML,text="Correo",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
buttonReporService = tk.Button(frameMenuML,width=20,height=1, text="Ver mis correo", command=lambda: show_frame(frameMenuML,frame)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuML,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuML,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#--------------------------Sub-Sub-menu IIS: MENU SECUNDARIO e-Flow ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
framesubMenuIIS = Frame(menu)
framesubMenuIIS.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(framesubMenuIIS,text="0")
#Declaracion de los label
Titulo = tk.Label(framesubMenuIIS,text="Sub menu IIS",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
buttonAplicationIIS = tk.Button(framesubMenuIIS,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(framesubMenuIIS,frame2)).place(x=45,y=100)
buttonSiteIIS = tk.Button(framesubMenuIIS,width=20,height=1, text="Creador de site", command=lambda: show_frame(framesubMenuIIS,frame6)).place(x=230,y=100)
buttonEflowBack = tk.Button(framesubMenuIIS,width=20,height=1, text="Back e-Flow", command=lambda: show_frame(framesubMenuIIS,frameMenuEflow)).place(x=45,y=270)
buttonEflowBack = tk.Button(framesubMenuIIS,width=20,height=1, text="Back to Menu Principal", command=lambda: show_frame(framesubMenuIIS,frameMenuPrincipal)).place(x=230,y=270)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------Sub-Sub-menu NME: MENU SECUNDARIO e-Flow ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
framesubMenuNME = Frame(menu)
framesubMenuNME.config(bg=colorMenuPrincipal,width=425,height=350) 

k=tk.Label(framesubMenuNME,text="0")
#Declaracion de los label
Titulo = tk.Label(framesubMenuNME,text="Sub menu NME",font=Helvfont,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
buttonAplication = tk.Button(framesubMenuNME,width=20,height=1, text="NME Aplication", command=lambda: show_frame(framesubMenuNME,frame8)).place(x=45,y=100)
buttonSite = tk.Button(framesubMenuNME,width=20,height=1, text="NME Site", command=lambda: show_frame(framesubMenuNME,frame14)).place(x=230,y=100)
buttonSetting = tk.Button(framesubMenuNME,width=20,height=1, text="Emission.config", command=lambda: show_frame(framesubMenuNME,frame15)).place(x=45,y=130)
buttonEflowBack = tk.Button(framesubMenuNME,width=20,height=1, text="Back e-Flow", command=lambda: show_frame(framesubMenuNME,frameMenuEflow)).place(x=45,y=270)
buttonEflowBack = tk.Button(framesubMenuNME,width=20,height=1, text="Back to Menu Principal", command=lambda: show_frame(framesubMenuNME,frameMenuPrincipal)).place(x=230,y=270)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
R1 = Radiobutton(frame,text="Manual", variable=var, value=1, command=setStart,bg=colorframe1)
R2 = Radiobutton(frame, text="Automatico", variable=var, value=2,command=setStart,bg=colorframe1)
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
button6 = tk.Button(frame2, text="",image=confImg ,command=lambda: show_frame(frame2,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
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
button6 = tk.Button(frame3, text="",image=confImg ,command=lambda: show_frame(frame3,frameConfiguracionColoresPrincipales)).place(x=375,y=40)

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
button6 = tk.Button(frame4, text="",image=confImg ,command=lambda: show_frame(frame4,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
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
button6 = tk.Button(frame5, text="",image=confImg ,command=lambda: show_frame(frame5,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
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
button6 = tk.Button(frame6, text="",image=confImg ,command=lambda: show_frame(frame6,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
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
button6 = tk.Button(frame7, text="",image=confImg ,command=lambda: show_frame(frame7,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
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
button6 = tk.Button(frame8, text="",image=confImg ,command=lambda: show_frame(frame8,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame8----------------------------------------------------------

#------Creacion de los componentes para el Frame9: FRAME DE Configurador NME----------------------------------------------------------
#Declaracion de los label al frame8
frame9 = Frame(menu) 
frame9.config(bg=colorframe5)  
frame9.config(width=425,height=350) 
Titulo9 = tk.Label(frame9,text="Configurador de Citas NME ",font=Helvfont,pady=24,bg=colorframe5)
Titulo9.place(x=40,y=0)
label9 = tk.Label(frame9,text="",bg=colorframe5)
labelsvrNMECitas = tk.Label(frame9,text="Introduzca el nombre del servidor del web service de citas ",bg=colorframe5)
TextboxsvrNMECitas = tk.Entry(frame9)
labelCitasNME = tk.Label(frame9,text="Introduzca el nombre de la aplicacion del web service de citas",bg=colorframe5)
TextboxCitasNME = tk.Entry(frame9)
TextboxsvrNMECitas.place(x=40,y=160)
TextboxCitasNME.place(x=40,y=200)
labelsvrNMECitas.place(x=40,y=140)
labelCitasNME.place(x=40,y=180)
#Declaracion y agregacion de los botones al frame8
boton1 = tk.Button(frame9,text="Buscar", command=lambda:ExamineDirectory(label9)).place(x=40,y=115)
label9.place(x=40,y=96) #se agregan las etiquetas al frame8
boton4 = tk.Button(frame9,text="Modificar NME", command=lambda:modifyNMECitas(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame9,width=16,height=1, text="Back to Citas", command=lambda: show_frame(frame9,frameMenuCitas)).place(x=275,y=270)
button8 = tk.Button(frame9,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame9,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame9, text="",image=confImg ,command=lambda: show_frame(frame9,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame9----------------------------------------------------------


#------Creacion de los componentes para el Frame10: FRAME DE Configurador RHI----------------------------------------------------------
#Declaracion de los label al frame10
hour=IntVar()
minute=IntVar()
frame10 = Frame(menu) 
frame10.config(bg=colorframe5)  
frame10.config(width=425,height=350) 
Titulo10 = tk.Label(frame10,text="Configurador de horario procesamiento historico ",font=Helvfont,pady=24,bg=colorframe5)
Titulo10.place(x=0,y=0)
label10 = tk.Label(frame10,text="",bg=colorframe5)
labelHour = tk.Label(frame10,text="Introduzca la hora",bg=colorframe5)
spinHour = tk.Spinbox(frame10,from_=0, to=23, increment=1,width=2, textvariable=hour)
labelMinute = tk.Label(frame10,text="Introduzca el minuto",bg=colorframe5)
spinMinute = tk.Spinbox(frame10,from_=0, to=59, increment=1,width=2, textvariable=minute)
spinHour.place(x=40,y=160)
spinMinute.place(x=40,y=200)
labelHour.place(x=40,y=140)
labelMinute.place(x=40,y=180)

#Declaracion y agregacion de los botones al frame8
boton1 = tk.Button(frame10,text="Buscar", command=lambda:ExamineDirectoryRHI(label10)).place(x=40,y=115)
label10.place(x=40,y=96) #se agregan las etiquetas al frame8
boton4 = tk.Button(frame10,text="Modificar Horario", command=lambda:modifyRHI(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame10,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame10,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame10,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame10,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame10, text="",image=confImg ,command=lambda: show_frame(frame10,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame10----------------------------------------------------------

#------Creacion de los componentes para el Frame11 ---> Mail ----------------------------------------------------------
#Declaracion de los label al frame11
frame11 = Frame(menu) 
frame11.config(bg=colorframe3)  
frame11.config(width=425,height=350) 
Titulo11 = tk.Label(frame11,text="Configuracion de un correo",font=Helvfont,pady=24,bg=colorframe3)
Titulo11.place(x=40,y=0)
label11 = tk.Label(frame11,text="",bg=colorframe3)
varMail=IntVar()
#Declaracion de los label al frame3
#Declaracion y agregacion de los botones al frame3
boton1 = tk.Button(frame11,text="Buscar", command=lambda:ExamineDirectory(label11)).place(x=40,y=80)
#Declaracion de los radiunRadiobutton
R1Mail = Radiobutton(frame11,text="Sin SSL", variable=varMail,width=5 ,value=0, command=setStart,bg=colorframe1)
R2Mail = Radiobutton(frame11, text="Con SSL", variable=varMail,width=5, value=1,command=setStart,bg=colorframe1)
R1Mail.place(x=342,y=80)
R2Mail.place(x=342,y=100)
labelMailsrv = tk.Label(frame11,text="Servidor",bg=colorframe3)
TextboxMailsrv = tk.Entry(frame11)
labelMailPort = tk.Label(frame11,text="Puerto",bg=colorframe3)
TextboxMailPort = tk.Entry(frame11)
labelMailSenderAccount = tk.Label(frame11,text="Correo",bg=colorframe3)
TextboxMailSenderAccount = tk.Entry(frame11)
labelMailPassword= tk.Label(frame11,text="Password",bg=colorframe3)
TextboxMailPassword = tk.Entry(frame11)
TextboxMailsrv.place(x=110,y=120)
TextboxMailPort.place(x=110,y=150)
TextboxMailSenderAccount.place(x=110,y=180)
TextboxMailPassword.place(x=110,y=210)
labelMailsrv.place(x=40,y=120)
labelMailPort.place(x=40,y=150)
labelMailSenderAccount.place(x=40,y=180)
labelMailPassword.place(x=40,y=210)
label11.place(x=40,y=60) #se agregan las etiquetas al frame11
boton4 = tk.Button(frame11,text="Modificar Correo", command=lambda:modifyMail(logging)).place(x=40,y=235)
# Widgets para el frame2
button2 = tk.Button(frame11,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame11,frameMenuEflow)).place(x=275,y=240)
button5 = tk.Button(frame11,width=16,height=1, text="Back to Citas", command=lambda: show_frame(frame11,frameMenuCitas)).place(x=275,y=270)
button7 = tk.Button(frame11,width=16,height=1, text="Back to Encuesta", command=lambda: show_frame(frame11,frameMenuEncuesta)).place(x=130,y=270)
button8 = tk.Button(frame11,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame11,frameMenuPrincipal)).place(x=2.5,y=270)
button6 = tk.Button(frame11, text="",image=confImg ,command=lambda: show_frame(frame11,frameConfiguracionColoresPrincipales)).place(x=375,y=40)

#------Fin de la Creacion de los componentes para el Frame11----------------------------------------------------------

#------Creacion de los componentes para el Frame12----------------------------------------------------------
#Declaracion de los label al frame12
frame12 = Frame(menu) 
frame12.config(bg=colorframe5)  
frame12.config(width=425,height=350) 
Titulo12 = tk.Label(frame12,text="Configurador de Encuesta",font=Helvfont,pady=24,bg=colorframe5)
Titulo12.place(x=40,y=0)
label12 = tk.Label(frame12,text="",bg=colorframe5)
#Declaracion de los label al frame3
labelsvrEncuesta = tk.Label(frame12,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrEncuesta = tk.Entry(frame12)
labelEncuesta = tk.Label(frame12,text="Introduzca el nombre de sitio de Encuesta",bg=colorframe5)
TextboxEncuesta = tk.Entry(frame12)
labelEflowEncuesta = tk.Label(frame12,text="Introduzca el nombre de sitio de e-Flow",bg=colorframe5)
TextboxEflowEncuesta = tk.Entry(frame12)
TextboxsvrEncuesta.place(x=40,y=80)
TextboxEncuesta.place(x=40,y=120)
TextboxEflowEncuesta.place(x=40,y=160)
labelsvrEncuesta.place(x=40,y=60)
labelEncuesta.place(x=40,y=100)
labelEflowEncuesta.place(x=40,y=140)
#Declaracion y agregacion de los botones al frame4
boton1 = tk.Button(frame12,text="Buscar", command=lambda:ExamineDirectory(label12)).place(x=40,y=240)
label12.place(x=40,y=220) #se agregan las etiquetas al frame4
# Widgets para el frame2
boton4 = tk.Button(frame12,text="configurar Encuesta", command=lambda:modifyPoll(logging)).place(x=90,y=240)
# Widgets para el frame2
button5 = tk.Button(frame12,width=16,height=1, text="Back to Encuesta", command=lambda: show_frame(frame12,frameMenuEncuesta)).place(x=275,y=240)
button8 = tk.Button(frame12,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame12,frameMenuPrincipal)).place(x=275,y=270)
button6 = tk.Button(frame12, text="",image=confImg ,command=lambda: show_frame(frame12,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el Frame12----------------------------------------------------------

#------Creacion de los componentes para el frame13: FRAME DE Tiempo de seccion en consola----------------------------------------------------------
#Declaracion de los label al frame13
minuteSesion=IntVar()
frame13 = Frame(menu) 
frame13.config(bg=colorframe5)  
frame13.config(width=425,height=350) 
Titulo13 = tk.Label(frame13,text="Configurador de tiempo de sesion",font=Helvfont,pady=24,bg=colorframe5)
Titulo13.place(x=40,y=0)
label13 = tk.Label(frame13,text="",bg=colorframe5)
labelMinuteConsole = tk.Label(frame13,text="Introduzca los minuto",bg=colorframe5)
spinMinuteConsole = tk.Spinbox(frame13,from_=0, to=1000, increment=1,width=5, textvariable=minuteSesion)
spinMinuteConsole.place(x=40,y=200)
labelMinuteConsole.place(x=40,y=180)

#Declaracion y agregacion de los botones al frame13
boton1 = tk.Button(frame13,text="Buscar", command=lambda:ExamineDirectoryConsoleSesion(label13)).place(x=40,y=115)
label13.place(x=40,y=96) #se agregan las etiquetas al frame13
boton4 = tk.Button(frame13,text="Modificar tiempo", command=lambda:modifyConsoleSesion(logging)).place(x=40,y=265)
# Widgets para el frame13
button2 = tk.Button(frame13,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame13,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame13,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame13,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame13, text="",image=confImg ,command=lambda: show_frame(frame13,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el frame13----------------------------------------------------------

#------Creacion de los componentes para el Frame14: FRAME DE Configurador NME con site----------------------------------------------------------
#Declaracion de los label al frame14
frame14 = Frame(menu) 
frame14.config(bg=colorframe5)  
frame14.config(width=425,height=350) 
Titulo14 = tk.Label(frame14,text="Configurador de NME por Site",font=Helvfont,pady=24,bg=colorframe5)
Titulo14.place(x=40,y=0)
label14 = tk.Label(frame14,text="",bg=colorframe5)
labelsvrSite = tk.Label(frame14,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrNMESite = tk.Entry(frame14)
labeleFlowNMESite = tk.Label(frame14,text="Introduzca el puerto del site de e-Flow",bg=colorframe5)
TextboxeFlowNMESite = tk.Entry(frame14)
labelAPISite = tk.Label(frame14,text="Introduzca el puerto del site de API",bg=colorframe5)
TextboxeAPISite = tk.Entry(frame14)
TextboxsvrNMESite.place(x=40,y=160)
TextboxeFlowNMESite.place(x=40,y=200)
TextboxeAPISite.place(x=40,y=240)
labelsvrSite.place(x=40,y=140)
labeleFlowNMESite.place(x=40,y=180)
labelAPISite.place(x=40,y=220)
#Declaracion y agregacion de los botones al frame8
boton1 = tk.Button(frame14,text="Buscar", command=lambda:ExamineDirectory(label14)).place(x=40,y=115)
label14.place(x=40,y=96) #se agregan las etiquetas al frame8
boton4 = tk.Button(frame14,text="Modificar NME", command=lambda:modifyNMESite(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame14,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame14,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame14,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame14,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame14, text="",image=confImg ,command=lambda: show_frame(frame14,frameConfiguracionColoresPrincipales)).place(x=375,y=40)
#------Fin de la Creacion de los componentes para el frame14----------------------------------------------------------

#------Creacion de los componentes para el frame15: FRAME DE Configurador emission.config----------------------------------------------------------
#Declaracion de los label al frame15
frame15 = Frame(menu) 
frame15.config(bg=colorframe5)  
frame15.config(width=425,height=350) 
Titulo15 = tk.Label(frame15,text="emission.config",font=Helvfont,pady=24,bg=colorframe5)
label15 = tk.Label(frame15,text="",bg=colorframe5)
preferencialVar=IntVar()
preferencialVar.set(0)
#Declaracion y agregacion de los botones al frame15
boton1 = tk.Button(frame15,text="Buscar", command=lambda:ExamineDirectoryNME(label15)).place(x=40,y=55)
label15.place(x=40,y=36) #se agregan las etiquetas al frame15
Titulo15.place(x=160,y=-10) #se agregan las etiquetas al frame15
boton4 = tk.Button(frame15,text="Modificar Emission.config", command=lambda:modifyNMEEmissionConfig(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame15,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame15,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame15,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame15,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame15, text="",image=confImg ,command=lambda: show_frame(frame15,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
preferencialTrue = Radiobutton(frame15,text="Mostrar boton preferencial", variable=preferencialVar, value=1, command=setStart,bg=colorframe1,width=24)
preferencialFalse = Radiobutton(frame15, text="No mostrar boton preferencial", variable=preferencialVar, value=0,command=setStart,bg=colorframe1,width=24)
preferencialTrue.place(x=2,y=90)
preferencialFalse.place(x=2,y=110)
#------Fin de la Creacion de los componentes para el frame15----------------------------------------------------------

#------Creacion de los componentes para el frame15: FRAME DE Configurador emission.config----------------------------------------------------------
#Declaracion de los label al frame15
frame16 = Frame(menu) 
frame16.config(bg=colorframe5)  
frame16.config(width=425,height=350) 
Titulo16 = tk.Label(frame16,text="Nodo.xml",font=Helvfont,pady=24,bg=colorframe5)
label16 = tk.Label(frame16,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame15
boton1 = tk.Button(frame16,text="Buscar", command=lambda:Examine(2)).place(x=40,y=55)
label16.place(x=40,y=36) #se agregan las etiquetas al frame15

Titulo16.place(x=160,y=-10) #se agregan las etiquetas al frame15
labelNodeFont= tk.Label(frame16,text="GENERAL: Font-Family",bg=colorframe5)
TextboxNodeFont = tk.Entry(frame16)
labelNodeVoice= tk.Label(frame16,text="GENERAL: Voz",bg=colorframe5)
TextboxNodeVoice = tk.Entry(frame16)
labelNodeHeaderColor= tk.Label(frame16,text="HEADER: Color",bg=colorframe5)
TextboxNodeHeaderColor = tk.Entry(frame16)
labelNodeFooterColor= tk.Label(frame16,text="FOOTER: Color",bg=colorframe5)
TextboxNodeFooterColor = tk.Entry(frame16)
labelNodeNumberSize= tk.Label(frame16,text="NumberTableBodyandNewNumber: Size",bg=colorframe5)
TextboxNodeNumberSize = tk.Entry(frame16)
labelNodeFont.place(x=40,y=80)
TextboxNodeFont.place(x=40,y=100)
labelNodeVoice.place(x=40,y=120)
TextboxNodeVoice.place(x=40,y=140)
labelNodeHeaderColor.place(x=40,y=160)
TextboxNodeHeaderColor.place(x=40,y=180)
labelNodeFooterColor.place(x=40,y=200)
TextboxNodeFooterColor.place(x=40,y=220)
labelNodeNumberSize.place(x=200,y=80)
TextboxNodeNumberSize.place(x=200,y=100)
boton4 = tk.Button(frame16,text="Modificar nodo XML", command=lambda:modifyNode(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame16,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame16,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame16,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame16,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame16, text="",image=confImg ,command=lambda: show_frame(frame16,frameConfiguracionColoresPrincipales)).place(x=375,y=55)

#------Fin de la Creacion de los componentes para el frame15----------------------------------------------------------

#------Creacion de los componentes para el frame17: Automatizador----------------------------------------------------------
#Declaracion de los label al frame17
frame17 = Frame(menu) 
frame17.config(bg=colorframe5)  
frame17.config(width=425,height=350) 
Titulo17 = tk.Label(frame17,text="Automatizador",font=Helvfont,pady=24,bg=colorframe5)
label17 = tk.Label(frame17,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame17
boton1 = tk.Button(frame17,text="Buscar", command=lambda:ExamineDirectory(label17)).place(x=40,y=55)
label17.place(x=40,y=36) #se agregan las etiquetas al frame17
Titulo17.place(x=160,y=-10) #se agregan las etiquetas al frame17
labelAutomatizadorSRVBD= tk.Label(frame17,text="Servidor de base de datos e-Flow",bg=colorframe5)
TextboxAutomatizadorSRVBD = tk.Entry(frame17)
labelAutomatizadorSRVAPP= tk.Label(frame17,text="Servidor de base de datos Appoinmet",bg=colorframe5)
TextboxAutomatizadorSRVAPP = tk.Entry(frame17)
labelAutomatizadorName= tk.Label(frame17,text="Nombre del aplicativo",bg=colorframe5)
TextboxAutomatizadorName = tk.Entry(frame17)
labelAutomatizadorSRVBD.place(x=40,y=80)
TextboxAutomatizadorSRVBD.place(x=40,y=100)
labelAutomatizadorSRVAPP.place(x=40,y=120)
TextboxAutomatizadorSRVAPP.place(x=40,y=140)
labelAutomatizadorName.place(x=40,y=160)
TextboxAutomatizadorName.place(x=40,y=180)
boton4 = tk.Button(frame17,text="Automatizar", command=lambda:automateProcess(logging)).place(x=40,y=265)
# Widgets para el frame17
button2 = tk.Button(frame17,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame17,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame17,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame17,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame17, text="",image=confImg ,command=lambda: show_frame(frame17,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
#------Fin de la Creacion de los componentes para el frame17----------------------------------------------------------

#------Creacion de los componentes para el frame18: Reporteria----------------------------------------------------------
#Declaracion de los label al frame18
frame18 = Frame(menu) 
frame18.config(bg=colorframe5)  
frame18.config(width=425,height=350) 
Titulo18 = tk.Label(frame18,text="Reporteria",font=Helvfont,pady=24,bg=colorframe5)
label18 = tk.Label(frame18,text="",bg=colorframe5)
labelReporteriaEflow= tk.Label(frame18,text="e-Flow",bg=colorframe5)
labelReporteriaCitas= tk.Label(frame18,text="Citas",bg=colorframe5)
labelReporteriaEncuesta= tk.Label(frame18,text="Encuestas",bg=colorframe5)

label18 = tk.Label(frame18,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame18
boton1 = tk.Button(frame18,text="Buscar", command=lambda:ExamineDirectoryReporteria(label18)).place(x=40,y=55)
label18.place(x=40,y=36) #se agregan las etiquetas al frame18
labelReporteriaEflow.place(x=40,y=106) #se agregan las etiquetas al frame18
labelReporteriaCitas.place(x=40,y=126) #se agregan las etiquetas al frame18
labelReporteriaEncuesta.place(x=40,y=146) #se agregan las etiquetas al frame18
Titulo18.place(x=160,y=-10) #se agregan las etiquetas al frame18
# Widgets para el frame18
button2 = tk.Button(frame18,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame18,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame18,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame18,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame18, text="",image=confImg ,command=lambda: show_frame(frame18,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
#------Fin de la Creacion de los componentes para el frame17----------------------------------------------------------



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