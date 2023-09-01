from db import *
from funcionesAuxiliares import *
from tkinter import *
from tkinter import messagebox as MessageBox,font
import tkinter as tk

logging.basicConfig(filename=f'Logs\event {datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)

#===========================CONSTANTE DEL FRONTEND================================
#
menu = tk.Tk()

#======Carga de imagen=======
icono = tk.PhotoImage(file="img\icon-16.png")
eflowimg= loadImagen("img\eflow.png",PhotoImage,logging,datetime)
client= loadImagen("img\client.png",PhotoImage,logging,datetime)
citas= loadImagen("img\citas.png",PhotoImage,logging,datetime)
encuesta= loadImagen("img\Encuesta.png",PhotoImage,logging,datetime)
report= loadImagen("img\\report.png",PhotoImage,logging,datetime)
automatizacion= loadImagen("img\\automatizacion.png",PhotoImage,logging,datetime)
imagen= loadImagen("img\sidesys.gif",PhotoImage,logging,datetime)
confImg= loadImagen("img\conf.png",PhotoImage,logging,datetime)
correo= loadImagen("img\correo.png",PhotoImage,logging,datetime)
excel= loadImagen("img\Excel-icon.png",PhotoImage,logging,datetime)
impresora= loadImagen("img\impresora.png",PhotoImage,logging,datetime)
imagen= loadImagen("img\sidesys.gif",PhotoImage,logging,datetime)
confImg =loadImagen("img\conf.png",PhotoImage,logging,datetime)
#========Configuracion de la aplicacion=======
k = tk.Label(menu,text="0")
sizeVentana=IdentifyJSON(f'appsetting.json',"Ventana[\s|\S]+}",'"size":[\S|" "|\\b]+',logging,datetime).replace('"', r'')
if(IdentifyJSON(f'appsetting.json',"Ventana[\s|\S]+}",'"resizable":[\S|" "|\\b]+',logging,datetime).replace('"', r'')=="False"):resizable=False
else:resizable=True
#========Carga de colores=======
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
colorframe1=getColor(1,"codigo")
colorframe2=getColor(2,"codigo")
colorframe3=getColor(3,"codigo")
colorframe4=getColor(4,"codigo")
colorframe5=getColor(5,"codigo")
colorframeC="#555"

#===Colores Menu principal y secundarios===
colorMenuPrincipal=IdentifyJSON(f'appsetting.json',"Menu Principal[\s|\S]+}",'"BackgroundColor": "[\S|" "|\\b]+"',logging,datetime).replace('"', r'')
colorMenuEflow=IdentifyJSON(f'appsetting.json',"Menu e-Flow[\s|\S]+}",'"BackgroundColor":[\S|" "|\\b]+',logging,datetime).replace('"', r'')
colorMenuClient=IdentifyJSON(f'appsetting.json',"Menu Client[\s|\S]+}",'"BackgroundColor":[\S|" "|\\b]+',logging,datetime).replace('"', r'')
colorMenuCita=IdentifyJSON(f'appsetting.json',"Menu Citas[\s|\S]+}",'"BackgroundColor":[\S|" "|\\b]+',logging,datetime).replace('"', r'')
colorMenuEncuesta=IdentifyJSON(f'appsetting.json',"Menu Encuestas[\s|\S]+}",'"BackgroundColor":[\S|" "|\\b]+',logging,datetime).replace('"', r'')
colorMenuReporteria=IdentifyJSON(f'appsetting.json',"Menu Reportes[\s|\S]+}",'"BackgroundColor":[\S|" "|\\b]+',logging,datetime).replace('"', r'')
colorMenuAutomatizacion=IdentifyJSON(f'appsetting.json',"Menu Automatizacion[\s|\S]+}",'"BackgroundColor":[\S|" "|\\b]+',logging,datetime).replace('"', r'')
#===Fuentes Menu principal y secundarios==
fontMenuPrincipal=font.Font(family=IdentifyJSON(f'appsetting.json',"Menu Principal[\s|\S]+}",'"font":[\S|" "|\\b]+',logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuEflow=font.Font(family=IdentifyJSON(f'appsetting.json',"Menu e-Flow[\s|\S]+}",'"font":[\S|" "|\\b]+',logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuClient=font.Font(family=IdentifyJSON(f'appsetting.json',"Menu Client[\s|\S]+}",'"font":[\S|" "|\\b]+',logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuCita=font.Font(family=IdentifyJSON(f'appsetting.json',"Menu Citas[\s|\S]+}",'"font":[\S|" "|\\b]+',logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuEncuesta=font.Font(family=IdentifyJSON(f'appsetting.json',"Menu Encuestas[\s|\S]+}",'"font":[\S|" "|\\b]+',logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuReporteria=font.Font(family=IdentifyJSON(f'appsetting.json',"Menu Reportes[\s|\S]+}",'"font":[\S|" "|\\b]+',logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuAutomatizacion=font.Font(family=IdentifyJSON(f'appsetting.json',"Menu Automatizacion[\s|\S]+}",'"font":[\S|" "|\\b]+',logging,datetime).replace('"', r''), size=12, weight="bold")

#=======Variables auxiliares para frames

#Frame 1
var = IntVar()

#Frame 10 RHI
hour=IntVar()
minute=IntVar()

#Frame 11 Mail
varMail=IntVar()

#Frame 13 Console 
minuteSesion=IntVar()

#Frame 15 Emission.config 
preferencialVar=IntVar()
preferencialVar.set(0)
AnnounceAppointmentVar=IntVar()
AnnounceAppointmentVar.set(0)

