from funcionesAuxiliares import *
import logging
import datetime


"C:\Entornos\ONAPI\Middleware\STE\ConfigFiles\IDE.config"
def identifyMinuteSesion(path, logging, datetime):
    print("estoy identificando a que minuto se corre el historico")
    minutos=(int(Identify(path + "/Middleware/STE/ConfigFiles/IDE.config",'<SessionTimeOut>\S+</SessionTimeOut>',"<SessionTimeOut>\S+</SessionTimeOut>", logging,datetime))/1000)/60
    print(minutos)
    return minutos
def configurarMinuteConsole(path, minute,logging, datetime):
    print(minute)
    "C:\Entornos\ONAPI\Middleware\STE\ConfigFiles\IDE.config"
    replaceCadena(f'{path}/Middleware/STE/ConfigFiles/IDE.config',
            '<SessionTimeOut>\S+</SessionTimeOut>', 
         f'<SessionTimeOut>{int(minute)*60*1000}</SessionTimeOut>',logging,datetime)
    #"C:\SidesysEncuesta\FrontEnd\STE\Web.config"
    replaceCadena(f'{path}/FrontEnd/STE/Web.config',
            '<forms name="CookieSesionIniciada" loginUrl="\S+" timeout="\w+"', 
         f'<forms name="CookieSesionIniciada" loginUrl="Default.aspx" timeout="{minute}"',logging,datetime)

    

    
    

#identifyHour("C:\Sides",logging,datetime)
#identifyMinuteSesion("C:\Sides",logging,datetime)
#configurarMinuteConsole("C:\Sides",30,logging,datetime)
#\\n\s+<Scheduling type="Sidesys.eFlow.SystemTools.Scheduling.TaskLoader.StartingAtGivenTimeBasedExecTimeConfig">\\n\s+<StartingHour>22</StartingHour>\\n\s+<StartingMinutes>00</StartingMinutes>