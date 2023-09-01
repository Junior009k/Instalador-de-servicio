
from VariableDeterminadas import *
import os
import sys
from funcionesAuxiliares import *
from tkinter import messagebox as MessageBox,font
import tkinter.filedialog
import logging
import datetime
import tkinter as tk
from tkinter import ttk
#Funcion que permite manejar los servicios cargado en reporte generales
def loadOptionService(p,boton,path,labelReporteriaService,framei):
  logging.info(f' {datetime.datetime.now() }: Se ejecuta la funcion loadOptionService')
  if(p==1):
    manageService(1,labelReporteriaService.cget("text"),path,logging)
    boton.config(text="Detener", command=lambda:loadOptionService(2,boton,label19,labelReporteriaService))
  if(p==2):
    manageService(2,labelReporteriaService.cget("text"),path,logging)
    boton.config(text="Ejecutar", command=lambda:loadOptionService(1,boton,label19,labelReporteriaService))
  if(p==3):
    label1.config(text=path)
    boton.destroy()
    show_frame(framei,frame)
#Funcion que permite exportar los datos a excel
def exportExcel(loggin):
  a=[]
  b=[]
  c=[]
  d=[]
  logging.info(f' {datetime.datetime.now() }: Se estan exportando los siguientes datos a excel')
  for child in tree.get_children():
        a.append(tree.item(child)["values"][0])
        b.append(tree.item(child)["values"][1])
        c.append(tree.item(child)["values"][2])
        d.append(tree.item(child)["values"][3])
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][0]}')
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][1]}')
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][2]}')
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][3]}')           
  nombre=tkinter.filedialog.asksaveasfilename(initialdir="/",title="Guardar como",filetypes=(("Libro de excel","*.xlsx"),("todos los archivos","*.*")))
  if(re.findall(".xlsx",nombre)==[]):nombre=F"{nombre}.xlsx"
  try:
    registrarReporte(nombre,[b[0],b[1],b[2],b[3],b[4]],[c[0],c[1],c[2],c[3],c[4]],[d[0],d[1],d[2],d[3],d[4]], datetime, logging)
  except Exception as e:
    loggin.error(f' {datetime.datetime.now() }: No se pudo exportar el archivo excel')
    loggin.error(f' {datetime.datetime.now() }: {e}')
#Funcion se encarga de mostrar el menu de configuracion
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
  #nodo xml
  if(p==2 and validateService(path.lower(),".xml","FrontEnd","view_configuration")):
    label16.config(text=path) 
    TextboxNodeFont.delete(0, tk.END)
    TextboxNodeVoice.delete(0, tk.END)
    TextboxNodeHeaderColor.delete(0, tk.END)
    TextboxNodeFooterColor.delete(0, tk.END)
    TextboxNodeNumberSize.delete(0, tk.END)
    TextboxNodeLang.delete(0, tk.END)
    TextboxNodeW.delete(0, tk.END)
    TextboxNodeUW.delete(0, tk.END)
    TextboxNodeNumberTableHeaderColor.delete(0, tk.END)
    TextboxNodeNumberTableHeaderSize.delete(0, tk.END)
    TextboxNodeNumberTableHeaderfontColor.delete(0, tk.END)
    TextboxNodeBannerBackgroundColor.delete(0, tk.END)
    TextboxNodeBannerFontColor.delete(0, tk.END)
    
    TextboxNodeFont.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','fontFamily":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeVoice.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','voice":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeHeaderColor.insert(0, IdentifyJSON(path,'"header":{[\S|\s]+"logo"','backgroundColor":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeFooterColor.insert(0, IdentifyJSON(path,'"footer":{[\S|\s]+"alignContent"','backgroundColor":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberSize.insert(0, IdentifyJSON(path,'"numbersTableBody":{[\S|\s]+"columnTask"','fontSize":[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeLang.insert(0, IdentifyJSON(path,'"node":{[\S|\s]+"header"','lang":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeW.insert(0, IdentifyJSON(path,'"header":{[\S|\s]+"text"','width":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeUW.insert(0, IdentifyJSON(path,'"header":{[\S|\s]+"text"','unitWidth":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberTableHeaderColor.insert(0, IdentifyJSON(path,'"numbersTableHeclader":{[\S|\s]+"columnTask"','backgroundColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberTableHeaderSize.insert(0, IdentifyJSON(path,'"numbersTableHeader":{[\S|\s]+"columnTask"','fontSize":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeNumberTableHeaderfontColor.insert(0, IdentifyJSON(path,'"numbersTableHeader":{[\S|\s]+"columnTask"','fontColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeBannerBackgroundColor.insert(0, IdentifyJSON(path,'"banner":{[\S|\s]+"fontColor"','backgroundColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
    TextboxNodeBannerFontColor.insert(0, IdentifyJSON(path,'"banner":{[\S|\s]+}','fontColor":"[\S|\\b|" "]+',logging,datetime).replace('"', r''))
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
def ExamineDirectoryReportesAplicativos(p,label):
  path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {path} donde se identificaran los reportes')
  path = path.replace("/", r"\ ".strip())
  path=path.rstrip()
  label.config(text=path) 
  if(p==1):
    #e-Flow - SERVICE
    #limpia todos los label
    labelReporteriaServiceEflow.config(text="Service",fg="black")
    labelReporteriaServiceEflowDetail.config(text="",fg="black")
    labelReporteriaIISEflow.config(text="IIS")
    labelReporteriaUDLEflow.config(text="UDL")

    #se asigna los servicios devueltos que coinciden con la ruta
    s=identifyService(f"{path}\Middleware\STE\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
    if(s!=None): 
      labelReporteriaServiceEflow.config(text=f"{s[0]}",fg="green")
      labelReporteriaServiceEflowDetail.config(text=f"{s[1]}|{s[2]}",fg="green")
      if(s[1]=="Stopped"):botonReporteriaServiceEflow = tk.Button(frame19,text="Ejecutar", command=lambda:loadOptionService(1,botonReporteriaServiceEflow,f"{label19.cget('text')}\Middleware\STE\\bin\Sidesys.Services.ApplicationService.exe,labelReporteriaServiceEflow",labelReporteriaServiceEflow,frame19))
      if(s[1]=="Running"):botonReporteriaServiceEflow = tk.Button(frame19,text="Detener", command=lambda:loadOptionService(2,botonReporteriaServiceEflow,f"{label19.cget('text')}\Middleware\STE\\bin\Sidesys.Services.ApplicationService.exe,labelReporteriaServiceEflow",labelReporteriaServiceEflow,frame19))
      botonReporteriaServiceEflow.place(x=200,y=125)
    else:
      labelReporteriaServiceEflow.config(text=f"No existe el aplicativo e-Flow",fg="red")
      if(validateDirectory(f"{path}\\FrontEnd","STE")==False): 
        labelReporteriaServiceEflow.config(text=f"No hay servicio instalado",fg="red")
        botonReporteriaServiceEflow = tk.Button(frame19,text="Instalar Servicio", command=lambda:loadOptionService(3,botonReporteriaServiceEflow,f"{label19.cget('text')}\Middleware\STE\\bin\Sidesys.Services.ApplicationService.exe,labelReporteriaServiceEflow",labelReporteriaServiceEflow,frame19))
        botonReporteriaServiceEflow.place(x=200,y=125)
    #e-Flow - IIS
    texto=''
    datosApp=findApp(f"{path}\\FrontEnd\\STE",logging,datetime)
    datosSite=findSite(f"{path}\\FrontEnd\\STE",logging,datetime)
  
    if(datosApp!=False):
      name,site,protocol=datosApp
      i=0
      while(i<len(name)):
        texto=f"{texto}Aplication {name[i]} {site[i]} {protocol[i]}\n"
        i=i+1
    if(datosSite!=False):
      name,site,protocol=datosSite
      i=0
      while(i<len(name)):
        texto=f"{texto}Site {name[i]} {site[i]} {protocol[i]}\n"
        i=i+1
    print(texto.replace("\\n","|"))
    labelReporteriaIISEflow.config(text=f"{texto}",fg="green")
    if(texto==''):
      logging.error(f' {datetime.datetime.now() }: No se encontro aplicacion o site asociado a este paquete')
      labelReporteriaIISEflow.config(text="No se encontro aplicacion o site asociado a este paquete",fg="red")
    #e-Flow - UDL
    textoUDL=''
    datosSOF=findUdls(f"{path}\\Middleware\\STE\\ConfigFiles","SOF",logging,datetime)
    datosusrSTE=findUdls(f"{path}\\Middleware\\STE\\ConfigFiles","STE",logging,datetime)
    if(datosSOF!=False):textoUDL=f"{textoUDL}user:{datosSOF[1]} password:{datosSOF[0]} db:{datosSOF[2]} srv:{datosSOF[3]}\n"
    if(datosusrSTE!=False):textoUDL=f"{textoUDL}user:{datosusrSTE[1]} password:{datosusrSTE[0]} db:{datosusrSTE[2]} srv:{datosusrSTE[3]}\n"
    labelReporteriaUDLEflow.config(text=f"{textoUDL}",fg="green")
    if(textoUDL==''):
      logging.error(f' {datetime.datetime.now() }: Hubo un error al identificar los udls ')
      labelReporteriaUDLEflow.config(text="Revisar UDLS",fg="red")
  if(p==2):
    #Citas - SERVICE
    #limpia todos los label
    labelReporteriaServiceCitas.config(text="Service",fg="black")
    labelReporteriaServiceCitasDetail.config(text="",fg="black")
    labelReporteriaIISCitas.config(text="IIS")
    labelReporteriaUDLCitas.config(text="UDL")
    #proceso de carga de los datos del servicio
    s=identifyService(f"{path}\Middleware\Appointment\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
    if(s!=None): 
      print(f"{s[0]}{s[1]}")
      labelReporteriaServiceCitas.config(text=f"{s[0]}",fg="green")
      labelReporteriaServiceCitasDetail.config(text=f"{s[1]}|{s[2]}",fg="green")
      if(s[1]=="Stopped"):
        botonReporteriaServiceCitas = tk.Button(frame20,text="Ejecutar", command=lambda:loadOptionService(1,botonReporteriaServiceCitas,f"{label20.cget('text')}\Middleware\Appointment\\bin\Sidesys.Services.ApplicationService.exe",labelReporteriaServiceCitas,frame20))
                
      if(s[1]=="Running"):
        botonReporteriaServiceCitas = tk.Button(frame20,text="Detener", command=lambda:loadOptionService(2,botonReporteriaServiceCitas,f"{label20.cget('text')}\Middleware\Appointment\\bin\Sidesys.Services.ApplicationService.exe",labelReporteriaServiceCitas,frame20))
      botonReporteriaServiceCitas.place(x=230,y=125)
    else:
      labelReporteriaServiceCitas.config(text=f"No existe el aplicativo e-Flow",fg="red")
      print(validateDirectory(f"{path}\\FrontEnd","Appointment"))
      if(validateDirectory(f"{path}\\FrontEnd","Appointment")==False): 
        labelReporteriaServiceCitas.config(text=f"No hay servicio instalado",fg="red")
        botonReporteriaServiceCitas = tk.Button(frame20,text="Instalar Servicio", command=lambda:loadOptionService(3,botonReporteriaServiceCitas,f"{label20.cget('text')}\Middleware\Appointment\\bin\Sidesys.Services.ApplicationService.exe",labelReporteriaServiceCitas,frame20))
        botonReporteriaServiceCitas.place(x=230,y=125)
    #Citas - IIS
    texto=''
    datosApp=findApp(f"{path}\\FrontEnd\\Appointment",logging,datetime)
    datosSite=findSite(f"{path}\\FrontEnd\\Appointment",logging,datetime)
    if(datosApp!=False):
      name,site,protocol=datosApp
      i=0
      while(i<len(name)):
        texto=f"{texto}Aplication {name[i]} {site[i]} {protocol[i]}\n"
        i=i+1
    if(datosSite!=False):
      name,site,protocol=datosSite
      i=0
      while(i<len(name)):
        texto=f"{texto}Site {name[i]} {site[i]} {protocol[i]}\n"
        i=i+1
    print(texto.replace("\\n","|"))
    labelReporteriaIISCitas.config(text=f"{texto}",fg="green")
    if(texto==''):
      logging.info(f' {datetime.datetime.now() }: No se encontro aplicacion o site asociado a este paquete')
      labelReporteriaIISCitas.config(text="No se encontro aplicacion o site asociado a este paquete",fg="red")
    #Citas - UDL
    textoUDL=''
    datosSOF=findUdls(f"{path}\\Middleware\\Appointment\\ConfigFiles","SOF",logging,datetime)
    datosusrSSP=findUdls(f"{path}\\Middleware\\Appointment\\ConfigFiles","SSP",logging,datetime)
    if(datosSOF!=False):textoUDL=f"{textoUDL}user:{datosSOF[1]} password:{datosSOF[0]} db:{datosSOF[2]} srv:{datosSOF[3]}\n"
    if(datosusrSSP!=False):textoUDL=f"{textoUDL}user:{datosusrSSP[1]} password:{datosusrSSP[0]} db:{datosusrSSP[2]} srv:{datosusrSSP[3]}\n"
    labelReporteriaUDLCitas.config(text=f"{textoUDL}",fg="green")
    if(textoUDL==''):
      logging.info(f' {datetime.datetime.now() }: Hubo un error al identificar los udls ')
      labelReporteriaUDLCitas.config(text="Revisar UDLS",fg="red")

    #Load Citas Parameter
    TextboxReporteriaCitasApplication.delete(0, tk.END)
    TextboxReporteriaCitasAppSpa.delete(0, tk.END)
    TextboxReporteriaCitasAttOpSpa.delete(0, tk.END)
    TextboxReporteriaCitasAppointmentWebIndex.delete(0, tk.END)
    TextboxReporteriaCitasAppointmentWebSetting.delete(0, tk.END)
    TextboxReporteriaCitasSTEWeb.delete(0, tk.END)
    TextboxReporteriaCitasServiceSSP.delete(0, tk.END)
    TextboxReporteriaCitasNME.delete(0, tk.END)
    TextboxReporteriaCitasAppointmentWebConfig.delete(0, tk.END)
    TextboxReporteriaCitasConfigFilesAppointment.delete(0, tk.END)
    TextboxReporteriaCitasConfigFilesAppoinmentWeb.delete(0, tk.END)
    TextboxReporteriaCitasSSPServiceMSMQ.delete(0, tk.END)
    TextboxReporteriaCitasDataExport.delete(0, tk.END)  
    
    Insert(TextboxReporteriaCitasApplication,Identify(f"{path}/FrontEnd/Appointment/bin/Application.config",'<OperationalPath>[\S|\\b|" "]+</OperationalPath>','<OperationalPath>[\S|\\b|" "]+</OperationalPath>',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasAppSpa,identifyBaseURL(f"{path}/FrontEnd/Appointment/appSpa/index.html",'<base href=[\S|\\b|" "]+','<base href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasAttOpSpa,identifyBaseURL(f"{path}/FrontEnd/Appointment/AttOpSpa/index.html",'<base href=[\S|\\b|" "]+','<base href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasAppointmentWebIndex,identifyBaseURL(f"{path}/FrontEnd/AppointmentWeb/index.html",'<base href=[\S|\\b|" "]+','<base href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasAppointmentWebSetting,identifyBaseURL(f"{path}/FrontEnd/AppointmentWeb/assets/settings.json",'"appointmentApiUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasSTEWeb,identifyBaseURL(f"{path}/FrontEnd/STE/Web.config",'<add key="AppointmentWS" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasServiceSSP,identifyBaseURL(f"{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="dataExportServer" value=[\S|\\b|" "]+/>','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasNME,identifyBaseURL(f"{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json",'"appointmentApiEndpoint":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasAppointmentWebConfig,identifyBaseURL(f"{path}/FrontEnd/AppointmentWeb/Web.config",'<add key="messageQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasConfigFilesAppointment,Identify(f"{path}/Middleware/Appointment/ConfigFiles/Appointment.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasConfigFilesAppoinmentWeb,Identify(f"{path}/Middleware/Appointment/ConfigFiles/Appointment.config",'<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasSSPServiceMSMQ,identifyBaseURL(f"{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="virtualQueueCallBackQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaCitasDataExport,Identify(f"{path}/Middleware/STE/ConfigFiles/DataExport.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime),logging,datetime)
    
  if(p==3):
    #Encuesta - SERVICE
    #limpia todos los label
    labelReporteriaServiceEncuesta.config(text="Service",fg="black")
    labelReporteriaServiceEncuestaDetail.config(text="",fg="black")
    labelReporteriaIISEncuesta.config(text="IIS")
    labelReporteriaUDLEncuesta.config(text="UDL")
    #proceso de carga de los datos del servicio
    s=identifyService(f"{path}\Middleware\OpinionPoll\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
    if(s!=None): 
      print(f"{s[0]}{s[1]}")
      labelReporteriaServiceEncuesta.config(text=f"{s[0]}",fg="green")
      labelReporteriaServiceEncuestaDetail.config(text=f"{s[1]}|{s[2]}",fg="green")
      if(s[1]=="Stopped"):botonReporteriaServiceEncuestas = tk.Button(frame21,text="Ejecutar", command=lambda:loadOptionService(1,botonReporteriaServiceEncuestas,f"{label21.cget('text')}\Middleware\OpinionPoll\\bin\Sidesys.Services.ApplicationService.exe",labelReporteriaServiceEncuesta,frame21))      
      if(s[1]=="Running"):botonReporteriaServiceEncuestas = tk.Button(frame21,text="Detener", command=lambda:loadOptionService(2,botonReporteriaServiceEncuestas,f"{label21.cget('text')}\Middleware\OpinionPoll\\bin\Sidesys.Services.ApplicationService.exe",labelReporteriaServiceEncuesta,frame21))
      botonReporteriaServiceEncuestas.place(x=230,y=125)
    else:
      labelReporteriaServiceEncuesta.config(text=f"No existe el aplicativo Encuesta",fg="red")
      print(validateDirectory(f"{path}\\FrontEnd","OpinionPoll"))
      if(validateDirectory(f"{path}\\FrontEnd","OpinionPoll")==False): 
        labelReporteriaServiceEncuesta.config(text=f"No hay servicio instalado",fg="red")
        botonReporteriaServiceEncuestas = tk.Button(frame21,text="Instalar Servicio", command=lambda:loadOptionService(3,botonReporteriaServiceEncuestas,f"{label21.cget('text')}\Middleware\OpinionPoll\\bin\Sidesys.Services.ApplicationService.exe",labelReporteriaServiceEncuesta,frame21))
        botonReporteriaServiceEncuestas.place(x=230,y=125)
    #Encuesta - IIS
    texto=''
    datosApp=findApp(f"{path}\\FrontEnd\\OpinionPoll",logging,datetime)
    datosSite=findSite(f"{path}\\FrontEnd\\OpinionPoll",logging,datetime)
  
    if(datosApp!=False):
      name,site,protocol=datosApp
      i=0
      while(i<len(name)):
        texto=f"{texto}Aplication {name[i]} {site[i]} {protocol[i]}\n"
        i=i+1
    if(datosSite!=False):
      name,site,protocol=datosSite
      i=0
      while(i<len(name)):
        texto=f"{texto}Site {name[i]} {site[i]} {protocol[i]}\n"
        i=i+1
    print(texto.replace("\\n","|"))
    labelReporteriaIISEncuesta.config(text=f"{texto}",fg="green")
    if(texto==''):
      logging.info(f' {datetime.datetime.now() }: No se encontro aplicacion o site asociado a este paquete')
      labelReporteriaIISEncuesta.config(text="No se encontro aplicacion o site asociado a este paquete",fg="red")
    #Encuesta - UDL
    textoUDL=''
    datosSOF=findUdls(f"{path}\\Middleware\\OpinionPoll\\ConfigFiles","SOF",logging,datetime)
    datosOpinionPoll=findUdls(f"{path}\\Middleware\\OpinionPoll\\ConfigFiles","OpinionPoll",logging,datetime)
    if(datosSOF!=False):textoUDL=f"{textoUDL}user:{datosSOF[1]} password:{datosSOF[0]} db:{datosSOF[2]} srv:{datosSOF[3]}\n"
    if(datosOpinionPoll!=False):textoUDL=f"{textoUDL}user:{datosOpinionPoll[1]} password:{datosOpinionPoll[0]} db:{datosOpinionPoll[2]} srv:{datosOpinionPoll[3]}\n"
    labelReporteriaUDLEncuesta.config(text=f"{textoUDL}",fg="green")
    if(textoUDL==''):
      logging.info(f' {datetime.datetime.now() }: Hubo un error al identificar los udls ')
      labelReporteriaUDLEncuesta.config(text="Revisar UDLS",fg="red")
    #Load Encuestas Parameter 
    TextboxReporteriaSTEWebConfig.delete(0, tk.END)
    TextboxReporteriaReportePoll.delete(0, tk.END)
    TextboxReporteriaOpinionPollIndex.delete(0, tk.END)
    TextboxReporteriaSettingPoll.delete(0, tk.END)
    TextboxReporteriaMiddlewareOpinionPoll.delete(0, tk.END)
    TextboxReporteriaMiddlewareSTE.delete(0, tk.END)
    

    Insert(TextboxReporteriaSTEWebConfig,identifyBaseURL(f"{path}/FrontEnd/STE/Web.config",'<add key="OpinionPollPath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaReportePoll,identifyBaseURL(f"{path}/FrontEnd/STE/Reportes/Poll/app/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaOpinionPollIndex,identifyBaseURL(f"{path}/FrontEnd/OpinionPoll/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaSettingPoll,identifyBaseURL(f"{path}/FrontEnd/OpinionPoll/assets/settings.json",'"pollApiBaseUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaMiddlewareOpinionPoll,Identify(f"{path}/Middleware/OpinionPoll/ConfigFiles/OpinionPoll.config",'<eFlow>[\S|\\b|" "]+</eFlow>','<eFlow>[\S|\\b|" "]+</eFlow>',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaMiddlewareSTE,Identify(f"{path}/Middleware/STE/ConfigFiles/OpinionPoll.config",'<Path>[\S|\\b|" "]+</Path>','<Path>[\S|\\b|" "]+</Path>',logging,datetime),logging,datetime)
    
  if(p==4):
    print("Virtual Queue")
  #Load Encuestas Parameter 
    TextboxReporteriaVQDB.delete(0, tk.END)
    TextboxReporteriaVQMSMQWebConfig.delete(0, tk.END)
    TextboxReporteriaVQMSMQMiddlewareSTE.delete(0, tk.END)
    

    Insert(TextboxReporteriaVQDB,identifyBaseURL(f"{path}/FrontEnd/VirtualQueue/web.config",'<add name="Default" connectionString="[\S|\\b|" "]+"','connectionString=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaVQMSMQWebConfig,identifyBaseURL(f"{path}/FrontEnd/VirtualQueue/web.config",'<add key="IncomingEventsReceiveQueuePath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
    Insert(TextboxReporteriaVQMSMQMiddlewareSTE,Identify(f"{path}/Middleware/STE/ConfigFiles/VirtualQueue.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime),logging,datetime)
   
  return path
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
  logging.info(f' {datetime.datetime.now() }: Borrando los campos de la tablas')
  for child in tree.get_children():
        tree.delete(child)
  path =path
  #if(validateService(Path.lower(),"Scheduling.config","middleware","ConfigFiles")):  
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {path}')
    path = path.replace("/", r"\ ".strip())
    path=path.rstrip()
    if(validateDirectory(f'{path}\\FrontEnd',"STE")==False):
      versionEflow=identifyVersion(f"{path}\\FrontEnd\STE\\bin\eflow.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      se=identifyService(f"{path}\\Middleware\\STE\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
      if(se!=None):labelReporteriaEflowService.config(fg= "green", text=f"{se[0]} | {se[1]} | {se[2]}")
      else:
        se=["No hay servicio instalado","None","none","none"]
        labelReporteriaEflowService.config(fg= "red", text=f"No hay servicio instalado")
      labelReporteriaEflow.config(fg= "green", text=f"e-Flow    {versionEflow}")     
      print("Existe e-Flow")
    else:
      se=["No hay servicio instalado","none","none","none"]
      versionEflow="None"
      labelReporteriaEflow.config(fg= "red", text=f"e-Flow")
    if(validateDirectory(f'{path}\\FrontEnd',"Appointment")==False):
      versionCitas=identifyVersion(f"{path}\\\FrontEnd\Appointment\\bin\Application.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      sa=identifyService(f"{path}\\Middleware\\Appointment\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
      if(sa!=None):labelReporteriaCitasService.config(fg= "green", text=f"{sa[0]} | {sa[1]} | {sa[2]}")
      else:
        sa=["No hay servicio instalado","none","none","none"]
        labelReporteriaCitasService.config(fg= "red", text=f"No hay servicio instalado")
      labelReporteriaCitas.config(fg= "green", text=f"Citas        {versionCitas}")      
      print("Existe Citas")
    else:
      sa=["No hay servicio instalado","none","none","none"]
      versionCitas="None"
      labelReporteriaCitas.config(fg= "red", text=f"Citas")  
    if(validateDirectory(f'{path}\\FrontEnd',"OpinionPoll")==False):      
      versionEncuesta=identifyVersion(f"{path}\\FrontEnd\OpinionPoll\\bin\OpinionPoll.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      sen=identifyService(f"{path}\\Middleware\\Appointment\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
      if(sen!=None):labelReporteriaEncuestaService.config(fg= "green", text=f"{sen[0]} | {sen[1]} | {sen[2]}")
      else:
        sen=["No hay servicio instalado","none","none","none"]
        labelReporteriaEncuestaService.config(fg= "red", text=f"No hay servicio instalado")
      labelReporteriaEncuesta.config(fg= "green", text=f"Encuesta v{versionEncuesta}")
      print("Existe encuesta")
    else:
      sen=["No hay servicio instalado","none","none","none"]
      versionEncuesta="None"
      labelReporteriaEncuesta.config(fg= "red", text=f"Encuesta")
    # Datos de ejemplo
    data = [
        ("Version",versionEflow, versionCitas, versionEncuesta),
        ("Nombre",se[0],sa[0],sen[0]),
        ("Estado",se[1],sa[1],sen[1]),
        ("Inicio",se[2],sa[2],sen[2]),
        ("Ruta",  se[3],sa[3],sen[3]),
    ]
    for item in data:
        tree.insert("", "end", values=item)
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
    if(identifyNME(Path,'"attentionPreferential": {\\n\s+"showButton": [\S|\\b|" "]+,','"showButton": [\S|\\b|" "]+,')):preferencialVar.set(1)
    else:preferencialVar.set(0)
    if(identifyNME(Path,'"announceAppointment": {\\n\s+"showAnnounceAppointment": [\S|\\b|" "]+,','"showAnnounceAppointment": [\S|\\b|" "]+,')):AnnounceAppointmentVar.set(1)
    else:AnnounceAppointmentVar.set(0)
    
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
  print(AnnounceAppointmentVar.get())
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
    configurarEmissionConfig(label15.cget("text"), preferencialVar.get(),AnnounceAppointmentVar.get(), loggin,datetime)
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
    configurarNodo(label16.cget("text"),TextboxNodeFont.get(),TextboxNodeVoice.get(),TextboxNodeHeaderColor.get(),TextboxNodeFooterColor.get(), TextboxNodeNumberSize.get(),TextboxNodeLang.get(),TextboxNodeW.get(),TextboxNodeUW.get(),TextboxNodeNumberTableHeaderColor.get(),TextboxNodeNumberTableHeaderSize.get(),TextboxNodeNumberTableHeaderfontColor.get(),TextboxNodeBannerBackgroundColor.get(),TextboxNodeBannerFontColor.get(),logging,datetime)    
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
def updateAppointment():
  print(label20.cget("text"))
  updateCitas(label20.cget("text"),TextboxReporteriaCitasAppSpa.get(),TextboxReporteriaCitasAttOpSpa.get(),TextboxReporteriaCitasApplication.get(),TextboxReporteriaCitasAppointmentWebIndex.get(),TextboxReporteriaCitasAppointmentWebSetting.get(),TextboxReporteriaCitasSTEWeb.get(),TextboxReporteriaCitasServiceSSP.get(),TextboxReporteriaCitasNME.get(),TextboxReporteriaCitasAppointmentWebConfig.get(),TextboxReporteriaCitasConfigFilesAppointment.get(),TextboxReporteriaCitasConfigFilesAppoinmentWeb.get(),TextboxReporteriaCitasSSPServiceMSMQ.get(),TextboxReporteriaCitasDataExport.get(),logging,datetime)
def updatePoll():
  print(label21.cget("text"))
  updateEncuestas(label21.cget("text"),TextboxReporteriaSTEWebConfig.get(),TextboxReporteriaReportePoll.get(),TextboxReporteriaOpinionPollIndex.get(),TextboxReporteriaSettingPoll.get(),TextboxReporteriaMiddlewareOpinionPoll.get(),TextboxReporteriaMiddlewareSTE.get(),logging,datetime)
def updateVirtualQueue():  
  print(label22.cget("text"))
  updatesVirtualQueue(label21.cget("text"),TextboxReporteriaVQDB.get(),TextboxReporteriaVQMSMQWebConfig.get(),TextboxReporteriaVQMSMQMiddlewareSTE.get(),logging,datetime)
  print("update Virtual Queue")

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
#Declaracion del Loggin
logging.basicConfig(filename=f'Logs\event {datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')
#Declaracion de la instancia de la aplicacion a utilizar
menu.title("Instalador de servicios Unicos V0.100")
menu.geometry(sizeVentana)
menu.config(relief="sunken") 
menu.config(bg="blue")          # color de fondo, background
menu.config(bd=25)  
menu.resizable(resizable, resizable)
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

menu_archivo
#------Creacion de los componentes para el Frame 1: MENU PRINCIPAL --------------------------------------------------------------------------------------------------
frameMenuPrincipal = Frame(menu)
frameMenuPrincipal.config(bg=colorMenuPrincipal)  
frameMenuPrincipal.config(width=425,height=350) 
frameMenuPrincipal.pack()
#Declaracion de los label
Titulo = tk.Label(frameMenuPrincipal,text="Menu Principal",font=fontMenuPrincipal,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
if(readValueSystem("<Vlvwhpd h-Iorz>\w<Vlvwhpd h-Iorz>")=="a"):buttonEflow = tk.Button(frameMenuPrincipal,width=100,height=41, image = eflowimg,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuEflow)).place(x=45,y=100)
if(readValueSystem("<Folhqw>\w<Folhqw>")=="a"):buttonClient = tk.Button(frameMenuPrincipal,width=100,height=41, image = client,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuClient)).place(x=157,y=100)
if(readValueSystem("<Vlvwhpd flwdv>\w<Vlvwhpd flwdv>")=="a"):buttonCitas = tk.Button(frameMenuPrincipal,width=100,height=41, image = citas,text="Citas", command=lambda: show_frame(frameMenuPrincipal,frameMenuCitas)).place(x=270,y=100)
if(readValueSystem("<Vlvwhpd h-Hqfxhvwd>\w<Vlvwhpd Hqfxhvwd>")=="a"):buttonEncuesta = tk.Button(frameMenuPrincipal,width=100,height=41, image = encuesta,text="Encuesta", command=lambda: show_frame(frameMenuPrincipal,frameMenuEncuesta)).place(x=45,y=175)
if(readValueSystem("<Uhsruwhv>\w<Uhsruwh>")=="a"):buttonReport = tk.Button(frameMenuPrincipal,width=100,height=41, image = report,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuReport)).place(x=157,y=175)
if(readValueSystem("<Dxwrpdwlcdgru>\w<Dxwrpdwlcdgru>")=="a"):buttonAutomatizacion = tk.Button(frameMenuPrincipal,width=100,height=41, image = automatizacion,text="Automatizacion", command=lambda: show_frame(frameMenuPrincipal,frameMenuAuto)).place(x=270,y=175)
if(readValueSystem("<PrghIuhh>\w<PrghIuhh>")=="a"):buttonCorreo = tk.Button(frameMenuPrincipal,width=100,height=41,image = correo,text="Modo Libre", command=lambda: show_frame(frameMenuPrincipal,frameMenuML)).place(x=45,y=250)

#------Creacion de los componentes para el frameMenuEflow: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuEflow = Frame(menu)
frameMenuEflow.config(bg=colorMenuEflow,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(frameMenuEflow,text="Menu e-Flow",font=fontMenuEflow,pady=12,bg=colorMenuEflow)
Titulo.place(x=160,y=30)
#Declaracion de los botones
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
frameMenuClient.config(bg=colorMenuClient,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(frameMenuClient,text="Menu Client",font=fontMenuClient,pady=12,bg=colorMenuClient)
Titulo.place(x=140,y=30)
label1 = tk.Label(frameMenuClient,text="",bg=colorMenuPrincipal) #se agregan las etiquetas al frame
label1.place(x=40,y=125)
buttonClientService = tk.Button(frameMenuClient,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuClient,frame)).place(x=45,y=100)
buttonClientBack = tk.Button(frameMenuClient,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuClient,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los frameMenuClient para el frameMenuCitas: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuCitas: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuCitas = Frame(menu)
frameMenuCitas.config(bg=colorMenuCita,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(frameMenuCitas,text="Menu Citas",font=fontMenuCita,pady=12,bg=colorMenuCita)
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
frameMenuEncuesta.config(bg=colorMenuEncuesta,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(frameMenuEncuesta,text="Menu Encuestas",font=fontMenuEncuesta,pady=12,bg=colorMenuEncuesta)
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
frameMenuReport.config(bg=colorMenuReporteria,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(frameMenuReport,text="Reportes",font=fontMenuReporteria,pady=12,bg=colorMenuReporteria)
Titulo.place(x=170,y=30)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte General", command=lambda: show_frame(frameMenuReport,frame18)).place(x=45,y=100)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte e-Flow", command=lambda: show_frame(frameMenuReport,frame19)).place(x=45,y=130)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte Citas", command=lambda: show_frame(frameMenuReport,frame20)).place(x=230,y=100)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte Encuestas", command=lambda: show_frame(frameMenuReport,frame21)).place(x=230,y=130)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte Virtual Queue", command=lambda: show_frame(frameMenuReport,frame22)).place(x=45,y=160)
buttonReportBack = tk.Button(frameMenuReport,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuReport,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuReport: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuAuto = Frame(menu)
frameMenuAuto.config(bg=colorMenuAutomatizacion,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(frameMenuAuto,text="Automatizacion del proceso",font=fontMenuAutomatizacion,pady=12,bg=colorMenuAutomatizacion)
Titulo.place(x=100,y=30)
buttonReporService = tk.Button(frameMenuAuto,width=20,height=1, text="Automatizador Basico", command=lambda: show_frame(frameMenuAuto,frame17)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuAuto,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuAuto,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#------Creacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ------------------------------------------------------------------------------------------------------------------------------------
frameMenuML = Frame(menu)
frameMenuML.config(bg=colorMenuPrincipal,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(frameMenuML,text="Correo",font=fontMenuPrincipal,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
buttonReporService = tk.Button(frameMenuML,width=20,height=1, text="Ver mis correo", command=lambda: show_frame(frameMenuML,frame)).place(x=45,y=100)
buttonEncuestaBack = tk.Button(frameMenuML,width=20,height=1, text="Back", command=lambda: show_frame(frameMenuML,frameMenuPrincipal)).place(x=230,y=270)
#------Finalizacion de los componentes para el frameMenuAuto: MENU PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------

#--------------------------Sub-Sub-menu IIS: MENU SECUNDARIO e-Flow ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
framesubMenuIIS = Frame(menu)
framesubMenuIIS.config(bg=colorMenuPrincipal,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(framesubMenuIIS,text="Sub menu IIS",font=fontMenuPrincipal,pady=12,bg=colorMenuPrincipal)
Titulo.place(x=140,y=30)
buttonAplicationIIS = tk.Button(framesubMenuIIS,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(framesubMenuIIS,frame2)).place(x=45,y=100)
buttonSiteIIS = tk.Button(framesubMenuIIS,width=20,height=1, text="Creador de site", command=lambda: show_frame(framesubMenuIIS,frame6)).place(x=230,y=100)
buttonEflowBack = tk.Button(framesubMenuIIS,width=20,height=1, text="Back e-Flow", command=lambda: show_frame(framesubMenuIIS,frameMenuEflow)).place(x=45,y=270)
buttonEflowBack = tk.Button(framesubMenuIIS,width=20,height=1, text="Back to Menu Principal", command=lambda: show_frame(framesubMenuIIS,frameMenuPrincipal)).place(x=230,y=270)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------Sub-Sub-menu NME: MENU SECUNDARIO e-Flow ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
framesubMenuNME = Frame(menu)
framesubMenuNME.config(bg=colorMenuPrincipal,width=425,height=350) 
#Declaracion de los label
Titulo = tk.Label(framesubMenuNME,text="Sub menu NME",font=fontMenuPrincipal,pady=12,bg=colorMenuPrincipal)
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
#Declaracion de la variable seleccion
#Declaracion de los radiunRadiobutton
R1 = Radiobutton(frame,text="Manual", variable=var, value=1, command=setStart,bg=colorframe1)
R2 = Radiobutton(frame, text="Automatico", variable=var, value=2,command=setStart,bg=colorframe1)
R1.place(x=0,y=40)
R2.place(x=0,y=60)
#Declaracion de los label
Titulo = tk.Label(frame,text="Instalador de servicios Unicos",font=fontMenuPrincipal,pady=12,bg=colorframe1)
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
Titulo2 = tk.Label(frame2,text="Creador de aplicaciones en IIS",font=fontMenuPrincipal,pady=24,bg=colorframe2)
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
Titulo3 = tk.Label(frame3,text="Configurador de udls",font=fontMenuPrincipal,pady=24,bg=colorframe3)
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
Titulo4 = tk.Label(frame4,text="Modificador de puertos",font=fontMenuPrincipal,pady=24,bg=colorframe4)
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
Titulo5 = tk.Label(frame5,text="Configurador de citas",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo6 = tk.Label(frame6,text="Creador de Sites en IIS",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo7 = tk.Label(frame7,text="Configurador de NCache",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo8 = tk.Label(frame8,text="Configurador de NME",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo9 = tk.Label(frame9,text="Configurador de Citas NME ",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
frame10 = Frame(menu) 
frame10.config(bg=colorframe5)  
frame10.config(width=425,height=350) 
Titulo10 = tk.Label(frame10,text="Configurador de horario procesamiento historico ",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo11 = tk.Label(frame11,text="Configuracion de un correo",font=fontMenuPrincipal,pady=24,bg=colorframe3)
Titulo11.place(x=40,y=0)
label11 = tk.Label(frame11,text="",bg=colorframe3)
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
Titulo12 = tk.Label(frame12,text="Configurador de Encuesta",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
frame13 = Frame(menu) 
frame13.config(bg=colorframe5)  
frame13.config(width=425,height=350) 
Titulo13 = tk.Label(frame13,text="Configurador de tiempo de sesion",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo14 = tk.Label(frame14,text="Configurador de NME por Site",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo15 = tk.Label(frame15,text="emission.config",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label15 = tk.Label(frame15,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame15
boton1 = tk.Button(frame15,text="Buscar", command=lambda:ExamineDirectoryNME(label15)).place(x=40,y=55)
label15.place(x=40,y=36) #se agregan las etiquetas al frame15
Titulo15.place(x=160,y=-10) #se agregan las etiquetas al frame15
boton4 = tk.Button(frame15,text="Modificar Emission.config", command=lambda:modifyNMEEmissionConfig(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame15,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame15,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame15,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame15,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame15, text="",image=confImg ,command=lambda: show_frame(frame15,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
labelPreferencial = tk.Label(frame15,text="Mostrar boton preferencial",bg=colorframe5).place(x=2,y=80)
preferencialTrue = Radiobutton(frame15,text="Si", variable=preferencialVar, value=1, command=setStart,bg=colorframe1,width=2)
preferencialFalse = Radiobutton(frame15, text="No", variable=preferencialVar, value=0,command=setStart,bg=colorframe1,width=2)
preferencialTrue.place(x=2,y=100)
preferencialFalse.place(x=2,y=120)
labelAppointment = tk.Label(frame15,text="Mostrar el boton de anunciar citas",bg=colorframe5).place(x=2,y=150)
AppointmentTrue = Radiobutton(frame15,text="Si", variable=AnnounceAppointmentVar, value=1, command=setStart,bg=colorframe1,width=2)
AppointmentFalse = Radiobutton(frame15, text="No", variable=AnnounceAppointmentVar, value=0,command=setStart,bg=colorframe1,width=2)
AppointmentTrue.place(x=2,y=170)
AppointmentFalse.place(x=2,y=190)
#------buttonAnnounceAppointmentVar de la Creacion de los componentes para el frame15----------------------------------------------------------

#------Creacion de los componentes para el frame15: FRAME DE Configurador emission.config----------------------------------------------------------
#Declaracion de los label al frame16
frame16 = Frame(menu) 
frame16.config(bg=colorframe5)  
frame16.config(width=425,height=350) 
Titulo16 = tk.Label(frame16,text="Nodo.xml",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label16 = tk.Label(frame16,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame15
boton1 = tk.Button(frame16,text="Buscar", command=lambda:Examine(2)).place(x=40,y=55)
label16.place(x=40,y=36) #se agregan las etiquetas al frame15
Titulo16.place(x=160,y=-10) #se agregan las etiquetas al frame15
labelNodeFont= tk.Label(frame16,text="GENERAL: Font-Family",bg=colorframe5)
TextboxNodeFont = tk.Entry(frame16)
labelNodeVoice= tk.Label(frame16,text="GENERAL: Voz",bg=colorframe5)
TextboxNodeVoice = tk.Entry(frame16)
labelNodeLang= tk.Label(frame16,text="GENERAL: Idioma",bg=colorframe5)
TextboxNodeLang = tk.Entry(frame16)
labelNodeHeaderColor= tk.Label(frame16,text="HEADER: Color",bg=colorframe5)
TextboxNodeHeaderColor = tk.Entry(frame16)
labelNodeFooterColor= tk.Label(frame16,text="FOOTER: Color",bg=colorframe5)
TextboxNodeFooterColor = tk.Entry(frame16)
labelNodeNumberSize= tk.Label(frame16,text="NumberTableBodyandNewNumber: Size",bg=colorframe5)
TextboxNodeNumberSize = tk.Entry(frame16)
labelNodeW= tk.Label(frame16,text="HEADER: Width",bg=colorframe5)
TextboxNodeW = tk.Entry(frame16)
labelNodeUW= tk.Label(frame16,text="HEADER: Unit Width",bg=colorframe5)
TextboxNodeUW = tk.Entry(frame16)
labelNodeFont.place(x=40,y=80)
TextboxNodeFont.place(x=40,y=100)
labelNodeVoice.place(x=40,y=120)
TextboxNodeVoice.place(x=40,y=140)
labelNodeLang.place(x=40,y=160)
TextboxNodeLang.place(x=40,y=180)
labelNodeFooterColor.place(x=40,y=200)
TextboxNodeFooterColor.place(x=40,y=220)
labelNodeNumberSize.place(x=200,y=80)
TextboxNodeNumberSize.place(x=200,y=100)
labelNodeHeaderColor.place(x=200,y=120)
TextboxNodeHeaderColor.place(x=200,y=140)
labelNodeW.place(x=200,y=160)
TextboxNodeW.place(x=200,y=180)
labelNodeUW.place(x=200,y=200)
TextboxNodeUW.place(x=200,y=220)
boton4 = tk.Button(frame16,text="Modificar nodo XML", command=lambda:modifyNode(logging)).place(x=40,y=265)
# Widgets para el frame2
button2 = tk.Button(frame16,width=16,height=1, text="Back to e-Flow", command=lambda: show_frame(frame16,frameMenuEflow)).place(x=275,y=270)
button8 = tk.Button(frame16,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame16,frameMenuPrincipal)).place(x=275,y=245)
button6 = tk.Button(frame16, text="",image=confImg ,command=lambda: show_frame(frame16,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
botonNext = tk.Button(frame16,text="==>", command=lambda: show_frame(frame16,frame16b)).place(x=375,y=150)

#------Fin de la Creacion de los componentes para el frame16----------------------------------------------------------

#------Creacion de los componentes para el frame15: FRAME DE Configurador emission.config----------------------------------------------------------
#Declaracion de los label al frame16
frame16b = Frame(menu) 
frame16b.config(bg=colorframe5)  
frame16b.config(width=425,height=350) 
Titulo16b = tk.Label(frame16b,text="Nodo.xml",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label16b = tk.Label(frame16b,text="",bg=colorframe5)
labelNodeNumberTableHeaderColor= tk.Label(frame16b,text="NumberTableHeader: Color",bg=colorframe5)
TextboxNodeNumberTableHeaderColor = tk.Entry(frame16b)
labelNodeNumberTableHeaderSize= tk.Label(frame16b,text="NumberTableHeader: Size",bg=colorframe5)
TextboxNodeNumberTableHeaderSize = tk.Entry(frame16b)
labelNodeNumberTableHeaderfontColor= tk.Label(frame16b,text="NumberTableHeader: font Color",bg=colorframe5)
TextboxNodeNumberTableHeaderfontColor = tk.Entry(frame16b)
labelNodeBannerBackgroundColor= tk.Label(frame16b,text="BANNER: Background Color",bg=colorframe5)
TextboxNodeBannerBackgroundColor = tk.Entry(frame16b)
labelNodeBannerFontColor= tk.Label(frame16b,text="BANNER: font Color",bg=colorframe5)
TextboxNodeBannerFontColor = tk.Entry(frame16b)
labelNodeNumberTableHeaderColor.place(x=40,y=80)
TextboxNodeNumberTableHeaderColor.place(x=40,y=100)
labelNodeNumberTableHeaderSize.place(x=40,y=120)
TextboxNodeNumberTableHeaderSize.place(x=40,y=140)
labelNodeBannerBackgroundColor.place(x=200,y=80)
TextboxNodeBannerBackgroundColor.place(x=200,y=100)
labelNodeBannerFontColor.place(x=200,y=120)
TextboxNodeBannerFontColor.place(x=200,y=140)
#Declaracion y agregacion de los botones al frame15
boton1 = tk.Button(frame16b,text="Buscar", command=lambda:Examine(2)).place(x=40,y=55)
label16b.place(x=40,y=36) #se agregan las etiquetas al frame15
Titulo16.place(x=160,y=-10) #se agregan las etiquetas al frame15
botonBack = tk.Button(frame16b,text="<==", command=lambda: show_frame(frame16b,frame16)).place(x=2,y=150)
# Widgets para el frame2

#------Fin de la Creacion de los componentes para el frame16----------------------------------------------------------

#------Creacion de los componentes para el frame17: Automatizador----------------------------------------------------------
#Declaracion de los label al frame17
frame17 = Frame(menu) 
frame17.config(bg=colorframe5)  
frame17.config(width=425,height=350) 
Titulo17 = tk.Label(frame17,text="Automatizador",font=fontMenuPrincipal,pady=24,bg=colorframe5)
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
Titulo18 = tk.Label(frame18,text="Reporteria",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label18 = tk.Label(frame18,text="",bg=colorframe5)
labelReporteriaEflow= tk.Label(frame18,text="e-Flow",bg=colorframe5)
labelReporteriaEflowService= tk.Label(frame18,text="",bg=colorframe5)
labelReporteriaCitas= tk.Label(frame18,text="Citas",bg=colorframe5)
labelReporteriaCitasService= tk.Label(frame18,text="",bg=colorframe5)
labelReporteriaEncuesta= tk.Label(frame18,text="Encuestas",bg=colorframe5)
labelReporteriaEncuestaService= tk.Label(frame18,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame18
boton1 = tk.Button(frame18,text="Buscar", command=lambda:ExamineDirectoryReporteria(label18)).place(x=40,y=55)
label18.place(x=40,y=36) #se agregan las etiquetas al frame18
# Crear el Treeview
tree = ttk.Treeview(frame18, columns=("","e-Flow", "Citas", "Encuestas"),height=5, show="headings")
# Configurar las columnas
tree.heading("", text="")
tree.heading("e-Flow", text="e-Flow")
tree.heading("Citas", text="Citas")
tree.heading("Encuestas", text="Encuestas")
# Ajustar el ancho de las columnas
tree.column("",width=60)
tree.column("e-Flow",width=100)
tree.column("Citas",width=100)
tree.column("Encuestas", width=100)
tree.place(x=10,y=100)
Titulo18.place(x=160,y=-10) #se agregan las etiquetas al frame18
# Widgets para el frame18
button2 = tk.Button(frame18,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame18,frameMenuReport)).place(x=280,y=270)
button8 = tk.Button(frame18,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame18,frameMenuPrincipal)).place(x=150,y=270)
button6 = tk.Button(frame18, text="",image=confImg ,command=lambda: show_frame(frame18,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
buttonExcel = tk.Button(frame18, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame18, text="",image=impresora ,command=lambda: show_frame(frame18,frameConfiguracionColoresPrincipales)).place(x=305,y=55)
#------Fin de la Creacion de los componentes para el frame18----------------------------------------------------------

#------Creacion de los componentes para el frame19: Reporteria e-Flow----------------------------------------------------------
#Declaracion de los label al frame19
frame19 = Frame(menu) 
frame19.config(bg=colorframe5)  
frame19.config(width=425,height=350) 
Titulo19 = tk.Label(frame19,text="Reporte e-Flow",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label19 = tk.Label(frame19,text="",bg=colorframe5)
labelReporteriaServiceEflow= tk.Label(frame19,text="Service",bg=colorframe5)
labelReporteriaServiceEflowDetail= tk.Label(frame19,text="",bg=colorframe5)
labelReporteriaIISEflow= tk.Label(frame19,text="IIS",bg=colorframe5,justify=tk.LEFT)
labelReporteriaUDLEflow= tk.Label(frame19,text="UDL",bg=colorframe5,justify=tk.LEFT)
label19 = tk.Label(frame19,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame18
boton1 = tk.Button(frame19,text="Buscar", command=lambda:ExamineDirectoryReportesAplicativos(1,label19)).place(x=40,y=55)
label19.place(x=40,y=36) #se agregan las etiquetas al frame19
labelReporteriaServiceEflow.place(x=40,y=106) #se agregan las etiquetas al frame19
labelReporteriaServiceEflowDetail.place(x=40,y=126) #se agregan las etiquetas al frame19
#botonReporteriaServiceEflow = tk.Button(frame19,text="Ejecutar", command=lambda:ExamineDirectoryReportesAplicativos(1,label19)).place(x=240,y=126)
labelReporteriaUDLEflow.place(x=40,y=150) #se agregan las etiquetas al frame19
labelReporteriaIISEflow.place(x=40,y=220) #se agregan las etiquetas al frame1
Titulo19.place(x=160,y=-10) #se agregan las etiquetas al frame19
# Widgets para el frame18
button2 = tk.Button(frame19,width=16,height=1, text="Back to Reportes", command=lambda:show_frame(frame19,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame19,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame19,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame19, text="",image=confImg ,command=lambda: show_frame(frame19,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
buttonExcel = tk.Button(frame19, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame19, text="",image=impresora ,command=lambda: show_frame(frame19,frameConfiguracionColoresPrincipales)).place(x=305,y=55)
#------Fin de la Creacion de los componentes para el frame19----------------------------------------------------------

#------Creacion de los componentes para el frame20: Reporteria Citas----------------------------------------------------------
#Declaracion de los label al frame20
frame20 = Frame(menu) 
frame20.config(bg=colorframe5)  
frame20.config(width=425,height=350) 
Titulo20 = tk.Label(frame20,text="Reporte Citas",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label20 = tk.Label(frame20,text="",bg=colorframe5)
labelReporteriaServiceCitas= tk.Label(frame20,text="Service",bg=colorframe5)
labelReporteriaServiceCitasDetail= tk.Label(frame20,text="",bg=colorframe5)
labelReporteriaIISCitas= tk.Label(frame20,text="IIS",bg=colorframe5,justify=tk.LEFT)
labelReporteriaUDLCitas= tk.Label(frame20,text="UDL",bg=colorframe5,justify=tk.LEFT)
label20 = tk.Label(frame20,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame18
boton1 = tk.Button(frame20,text="Buscar", command=lambda:ExamineDirectoryReportesAplicativos(2,label20)).place(x=40,y=55)
label20.place(x=40,y=36) #se agregan las etiquetas al frame20
labelReporteriaServiceCitas.place(x=120,y=106) #se agregan las etiquetas al frame20
labelReporteriaServiceCitasDetail.place(x=120,y=126) #se agregan las etiquetas al frame20
labelReporteriaUDLCitas.place(x=120,y=150) #se agregan las etiquetas al frame20
labelReporteriaIISCitas.place(x=120,y=180) #se agregan las etiquetas al frame20
Titulo20.place(x=160,y=-10) #se agregan las etiquetas al frame20
# Widgets para el frame18
button2 = tk.Button(frame20,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame20,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame20,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame20,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame20, text="",image=confImg ,command=lambda: show_frame(frame20,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
buttonRC1 = Button(frame20,bg="#000",fg="#FFF",width=15,height=1,text="Datos Basicos").place(x=0,y=100)
buttonRC2 = Button(frame20,width=15,height=1,text="Configuracion Citas", command=lambda:show_frame(frame20,frame20b)).place(x=0,y=150)
buttonRC3 = Button(frame20,width=15,height=1,text="MSMQ", command=lambda:show_frame(frame20,frame20c)).place(x=0,y=200)
buttonExcel = tk.Button(frame20, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame20, text="",image=impresora ,command=lambda: show_frame(frame18,frameConfiguracionColoresPrincipales)).place(x=305,y=55)
#------Fin de la Creacion de los componentes para el frame20----------------------------------------------------------

#------Creacion de los componentes para el frame20b: Reporteria Citas configuracion Citas----------------------------------------------------------
#Declaracion de los label al frame20b
frame20b = Frame(menu) 
frame20b.config(bg=colorframe5)  
frame20b.config(width=425,height=350) 
Titulo20b = tk.Label(frame20b,text="Reporte Citas: Configuraciones basicas",font=fontMenuPrincipal,pady=24,bg=colorframe5)
labelReporteriaCitasApplication= tk.Label(frame20b,text="Application.config",bg=colorframe5)
TextboxReporteriaCitasApplication = tk.Entry(frame20b)
labelReporteriaCitasAppSpa= tk.Label(frame20b,text="appSpa/index.html",bg=colorframe5)
TextboxReporteriaCitasAppSpa = tk.Entry(frame20b)
labelReporteriaCitasAttOpSpa= tk.Label(frame20b,text="AttOpSpa/index.html",bg=colorframe5)
TextboxReporteriaCitasAttOpSpa = tk.Entry(frame20b)
labelReporteriaCitasAppointmentWebIndex= tk.Label(frame20b,text="A.Web/index.html",bg=colorframe5)
TextboxReporteriaCitasAppointmentWebIndex = tk.Entry(frame20b)
labelReporteriaCitasAppointmentWebSetting= tk.Label(frame20b,text="settings.json",bg=colorframe5)
TextboxReporteriaCitasAppointmentWebSetting = tk.Entry(frame20b)
labelReporteriaCitasServiceSSP= tk.Label(frame20b,text="A.Service.exe.config",bg=colorframe5)
TextboxReporteriaCitasServiceSSP = tk.Entry(frame20b)
labelReporteriaCitasSTEWeb= tk.Label(frame20b,text="STE/Web.config'",bg=colorframe5)
TextboxReporteriaCitasSTEWeb = tk.Entry(frame20b)
labelReporteriaCitasNME= tk.Label(frame20b,text="emission.config.json",bg=colorframe5)
TextboxReporteriaCitasNME = tk.Entry(frame20b)

labelReporteriaCitasApplication.place(x=120,y=90)
TextboxReporteriaCitasApplication.place(x=120,y=110)
labelReporteriaCitasAppSpa.place(x=120,y=130)
TextboxReporteriaCitasAppSpa.place(x=120,y=150)
labelReporteriaCitasAttOpSpa.place(x=280,y=90)
TextboxReporteriaCitasAttOpSpa.place(x=280,y=110)
labelReporteriaCitasAppointmentWebIndex.place(x=280,y=130)
TextboxReporteriaCitasAppointmentWebIndex.place(x=280,y=150)
labelReporteriaCitasAppointmentWebSetting.place(x=120,y=170)
TextboxReporteriaCitasAppointmentWebSetting.place(x=120,y=190)
labelReporteriaCitasServiceSSP.place(x=120,y=210)
TextboxReporteriaCitasServiceSSP.place(x=120,y=230)
labelReporteriaCitasSTEWeb.place(x=280,y=170)
TextboxReporteriaCitasSTEWeb.place(x=280,y=190)
labelReporteriaCitasNME.place(x=280,y=210)
TextboxReporteriaCitasNME.place(x=280,y=230)
Titulo20b.place(x=65,y=-10) #se agregan las etiquetas al frame20
# Widgets para el frame18
button2 = tk.Button(frame20b,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame20b,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame20b,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame20b,frameMenuPrincipal)).place(x=150,y=270)
button6 = tk.Button(frame20b, text="",image=confImg ,command=lambda: show_frame(frame20b,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
button9 = tk.Button(frame20b,width=16,height=1, text="Actualizar datos", command=lambda: updateAppointment()).place(x=25,y=270)
buttonRC1 = Button(frame20b,width=15,height=1,text="Datos Basicos",command=lambda:show_frame(frame20b,frame20)).place(x=0,y=100)
buttonRC2 = Button(frame20b,width=15,height=1,text="Configuracion Citas",bg="#000",fg="#FFF").place(x=0,y=150)
buttonRC3 = Button(frame20b,width=15,height=1,text="MSMQ", command=lambda:show_frame(frame20b,frame20c)).place(x=0,y=200)
buttonExcel = tk.Button(frame20b, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame20b, text="",image=impresora ,command=lambda: show_frame(frame20b,frameConfiguracionColoresPrincipales)).place(x=305,y=55)
#------Fin de la Creacion de los componentes para el frame20b----------------------------------------------------------

#------Creacion de los componentes para el frame20b: Reporteria Citas MSMQ----------------------------------------------------------
#Declaracion de los label al frame20b
frame20c = Frame(menu)                                                                      
frame20c.config(bg=colorframe5)  
frame20c.config(width=425,height=350) 
Titulo20c = tk.Label(frame20c,text="Reporte Citas: MSMQ",font=fontMenuPrincipal,pady=24,bg=colorframe5)
Titulo20c.place(x=130,y=-10) #se agregan las etiquetas al frame20
labelReporteriaCitasAppointmentWebConfig= tk.Label(frame20c,text="A.Web/Web.config",bg=colorframe5)
TextboxReporteriaCitasAppointmentWebConfig = tk.Entry(frame20c)
labelReporteriaCitasConfigFilesAppointment= tk.Label(frame20c,text="Appointment.config out",bg=colorframe5)
TextboxReporteriaCitasConfigFilesAppointment = tk.Entry(frame20c)
labelReporteriaCitasConfigFilesAppoinmentWeb= tk.Label(frame20c,text="Appointment.config web",bg=colorframe5)
TextboxReporteriaCitasConfigFilesAppoinmentWeb = tk.Entry(frame20c)
labelReporteriaCitasSSPServiceMSMQ= tk.Label(frame20c,text="A.Service.exe.config",bg=colorframe5)
TextboxReporteriaCitasSSPServiceMSMQ = tk.Entry(frame20c)
labelReporteriaCitasDataExport= tk.Label(frame20c,text="DataExport.config",bg=colorframe5)
TextboxReporteriaCitasDataExport = tk.Entry(frame20c)

labelReporteriaCitasAppointmentWebConfig.place(x=120,y=90)
TextboxReporteriaCitasAppointmentWebConfig.place(x=120,y=110)
labelReporteriaCitasConfigFilesAppointment.place(x=120,y=130)
TextboxReporteriaCitasConfigFilesAppointment.place(x=120,y=150)
labelReporteriaCitasConfigFilesAppoinmentWeb.place(x=280,y=90)
TextboxReporteriaCitasConfigFilesAppoinmentWeb.place(x=280,y=110)
labelReporteriaCitasSSPServiceMSMQ.place(x=280,y=130)
TextboxReporteriaCitasSSPServiceMSMQ.place(x=280,y=150)
labelReporteriaCitasDataExport.place(x=120,y=170)
TextboxReporteriaCitasDataExport.place(x=120,y=190)
# Widgets para el frame18
button2 = tk.Button(frame20c,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame20c,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame20c,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame20c,frameMenuPrincipal)).place(x=275,y=240)
button9 = tk.Button(frame20c,width=16,height=1, text="Actualizar datos", command=lambda: updateAppointment()).place(x=25,y=270)
button6 = tk.Button(frame20c, text="",image=confImg ,command=lambda: show_frame(frame20c,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
buttonRC1 = Button(frame20c,width=15,height=1,text="Datos Basicos",command=lambda:show_frame(frame20c,frame20)).place(x=0,y=100)
buttonRC2 = Button(frame20c,width=15,height=1,text="Configuracion Citas", command=lambda:show_frame(frame20c,frame20b)).place(x=0,y=150)
buttonRC3 = Button(frame20c,width=15,height=1,text="MSMQ",bg="#000",fg="#FFF").place(x=0,y=200)
buttonExcel = tk.Button(frame20c, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame20c, text="",image=impresora ,command=lambda: show_frame(frame20c,frameConfiguracionColoresPrincipales)).place(x=305,y=55)

#------Fin de la Creacion de los componentes para el frame20c----------------------------------------------------------

#------Creacion de los componentes para el frame21: Reporteria Encuesta----------------------------------------------------------
#Declaracion de los label al frame21
frame21 = Frame(menu) 
frame21.config(bg=colorframe5)  
frame21.config(width=425,height=350) 
Titulo21 = tk.Label(frame21,text="Reporte Encuesta",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label21 = tk.Label(frame21,text="",bg=colorframe5)
labelReporteriaServiceEncuesta= tk.Label(frame21,text="Service",bg=colorframe5)
labelReporteriaServiceEncuestaDetail= tk.Label(frame21,text="",bg=colorframe5)
labelReporteriaIISEncuesta= tk.Label(frame21,text="IIS",bg=colorframe5,justify=tk.LEFT)
labelReporteriaUDLEncuesta= tk.Label(frame21,text="UDL",bg=colorframe5,justify=tk.LEFT)
label21 = tk.Label(frame21,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame18
boton21 = tk.Button(frame21,text="Buscar", command=lambda:ExamineDirectoryReportesAplicativos(3,label21)).place(x=40,y=55)
label21.place(x=40,y=36) #se agregan las etiquetas al frame21
labelReporteriaServiceEncuesta.place(x=120,y=106) #se agregan las etiquetas al frame21
labelReporteriaServiceEncuestaDetail.place(x=120,y=126) #se agregan las etiquetas al frame21
labelReporteriaUDLEncuesta.place(x=120,y=150) #se agregan las etiquetas al frame21
labelReporteriaIISEncuesta.place(x=120,y=180) #se agregan las etiquetas al frame21
Titulo21.place(x=145,y=-10) #se agregan las etiquetas al frame21
# Widgets para el frame18
button2 = tk.Button(frame21,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame21,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame21,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame21,frameMenuPrincipal)).place(x=275,y=240)
button6 = tk.Button(frame21, text="",image=confImg ,command=lambda: show_frame(frame21,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
buttonRE1 = Button(frame21,width=15,height=1,text="Datos Basicos",bg="#000",fg="#FFF").place(x=0,y=100)
buttonRE2 = Button(frame21,width=15,height=1,text="Configuracion",command=lambda:show_frame(frame21,frame21b)).place(x=0,y=150)
buttonExcel = tk.Button(frame21, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame21, text="",image=impresora ,command=lambda: show_frame(frame21,frameConfiguracionColoresPrincipales)).place(x=305,y=55)

#------Fin de la Creacion de los componentes para el frame21----------------------------------------------------------

#------Creacion de los componentes para el frame21b: Reporteria Encuesta configuracion basica----------------------------------------------------------
#Declaracion de los label al frame21b
frame21b = Frame(menu) 
frame21b.config(bg=colorframe5)  
frame21b.config(width=425,height=350) 
Titulo21b = tk.Label(frame21b,text="Reporte Encuesta: Configuraciones basicas",font=fontMenuPrincipal,pady=24,bg=colorframe5)
labelReporteriaSTEWebConfig= tk.Label(frame21b,text="STE/Web.config",bg=colorframe5)
TextboxReporteriaSTEWebConfig = tk.Entry(frame21b)
labelReporteriaReportePoll= tk.Label(frame21b,text="Reporte/index.html",bg=colorframe5)
TextboxReporteriaReportePoll = tk.Entry(frame21b)
labelReporteriaOpinionPollIndex= tk.Label(frame21b,text="O./index.html",bg=colorframe5)
TextboxReporteriaOpinionPollIndex = tk.Entry(frame21b)
labelReporteriaSettingPoll= tk.Label(frame21b,text="Setting.json",bg=colorframe5)
TextboxReporteriaSettingPoll = tk.Entry(frame21b)
labelReporteriaMiddlewareOpinionPoll= tk.Label(frame21b,text="M/O/OpinionPoll.config",bg=colorframe5)
TextboxReporteriaMiddlewareOpinionPoll = tk.Entry(frame21b)
labelReporteriaMiddlewareSTE= tk.Label(frame21b,text="M/S/OpinionPoll.config",bg=colorframe5)
TextboxReporteriaMiddlewareSTE = tk.Entry(frame21b)

labelReporteriaSTEWebConfig.place(x=120,y=90)
TextboxReporteriaSTEWebConfig.place(x=120,y=110)
labelReporteriaReportePoll.place(x=120,y=130)
TextboxReporteriaReportePoll.place(x=120,y=150)
labelReporteriaOpinionPollIndex.place(x=280,y=90)
TextboxReporteriaOpinionPollIndex.place(x=280,y=110)
labelReporteriaSettingPoll.place(x=280,y=130)
TextboxReporteriaSettingPoll.place(x=280,y=150)
labelReporteriaMiddlewareOpinionPoll.place(x=120,y=170)
TextboxReporteriaMiddlewareOpinionPoll.place(x=120,y=190)
labelReporteriaMiddlewareSTE.place(x=280,y=170)
TextboxReporteriaMiddlewareSTE.place(x=280,y=190)
Titulo21b.place(x=40,y=-10) #se agregan las etiquetas al frame21
# Widgets para el frame18
button2 = tk.Button(frame21b,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame21b,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame21b,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame21b,frameMenuPrincipal)).place(x=275,y=240)
button9 = tk.Button(frame21b,width=16,height=1, text="Actualizar datos", command=lambda: updatePoll()).place(x=25,y=270)
button6 = tk.Button(frame21b, text="",image=confImg ,command=lambda: show_frame(frame21b,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
buttonRE1 = Button(frame21b,width=15,height=1,text="Datos Basicos",command=lambda:show_frame(frame21b,frame21)).place(x=0,y=100)
buttonRE2 = Button(frame21b,width=15,height=1,text="Configuracion",bg="#000",fg="#FFF").place(x=0,y=150)
buttonExcel = tk.Button(frame21b, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame21b, text="",image=impresora ,command=lambda: show_frame(frame21b,frameConfiguracionColoresPrincipales)).place(x=305,y=55)
#------Fin de la Creacion de los componentes para el frame21b----------------------------------------------------------

#------Creacion de los componentes para el frame22: Reporteria Virtual Queue----------------------------------------------------------
#Declaracion de los label al frame22
frame22 = Frame(menu) 
frame22.config(bg=colorframe5)  
frame22.config(width=425,height=350) 
Titulo22 = tk.Label(frame22,text="Reporte Virtual Queue",font=fontMenuPrincipal,pady=24,bg=colorframe5)
label22 = tk.Label(frame22,text="",bg=colorframe5)
#Declaracion y agregacion de los botones al frame18
boton22 = tk.Button(frame22,text="Buscar", command=lambda:ExamineDirectoryReportesAplicativos(4,label22)).place(x=40,y=55)
label22.place(x=40,y=36) #se agregan las etiquetas al frame21
Titulo22.place(x=40,y=-10) #se agregan las etiquetas al frame21
labelReporteriaVQDB= tk.Label(frame22,text="DB Conection",bg=colorframe5)
TextboxReporteriaVQDB = tk.Entry(frame22,width=50)
labelReporteriaVQMSMQWebConfig= tk.Label(frame22,text="MSMQ/Web.config",bg=colorframe5)
TextboxReporteriaVQMSMQWebConfig = tk.Entry(frame22,width=50)
labelReporteriaVQMSMQMiddlewareSTE= tk.Label(frame22,text="MSMQ/MiddlewareSTE",bg=colorframe5)
TextboxReporteriaVQMSMQMiddlewareSTE = tk.Entry(frame22,width=50)

labelReporteriaVQDB.place(x=40,y=90)
TextboxReporteriaVQDB.place(x=40,y=110)
labelReporteriaVQMSMQWebConfig.place(x=40,y=130)
TextboxReporteriaVQMSMQWebConfig.place(x=40,y=150)
labelReporteriaVQMSMQMiddlewareSTE.place(x=40,y=170)
TextboxReporteriaVQMSMQMiddlewareSTE.place(x=40,y=190)
# Widgets para el frame18
button2 = tk.Button(frame22,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame22,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame22,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame22,frameMenuPrincipal)).place(x=275,y=240)
button9 = tk.Button(frame22,width=16,height=1, text="Actualizar datos", command=lambda: updateVirtualQueue()).place(x=25,y=270)
button6 = tk.Button(frame22, text="",image=confImg ,command=lambda: show_frame(frame22,frameConfiguracionColoresPrincipales)).place(x=375,y=55)
buttonExcel = tk.Button(frame22, text="",image=excel ,command=lambda: exportExcel(logging)).place(x=340,y=55)
buttonImpresora = tk.Button(frame22, text="",image=impresora ,command=lambda: show_frame(frame22,frameConfiguracionColoresPrincipales)).place(x=305,y=55)

#------Fin de la Creacion de los componentes para el frame21b----------------------------------------------------------
#------Creacion de los componentes para el Frame Configuracion----------------------------------------------------------
#Declaracion de los label al Frame Configuracion
frameConfiguracionColoresPrincipales = Frame(menu) 
frameConfiguracionColoresPrincipales.config(bg=colorframeC)  
frameConfiguracionColoresPrincipales.config(width=425,height=350) 
TituloC = tk.Label(frameConfiguracionColoresPrincipales,text="Configuracion de los colores principales",font=fontMenuPrincipal,pady=24,bg=colorframeC)
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
TituloC = tk.Label(frameConfiguracionColoresSecundarios,text="Configuracion de los colores secundario",font=fontMenuPrincipal,pady=24,bg=colorframeC)
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