from funcionesAuxiliares import *
import logging
import datetime

def identifyHour(path, logging, datetime):
    #"C:\Sides\MiddleWare\STE\ConfigFiles\Scheduling.config"
    print("estoy identificando a que hora se corre el historico")
    return Identify(path + "/Middleware/STE/ConfigFiles/Scheduling.config",'<Description>Procesamiento de Reportes \S+</Description>\\n\s+<Scheduling type="Sidesys.eFlow.SystemTools.Scheduling.TaskLoader.StartingAtGivenTimeBasedExecTimeConfig">\\n\s+<StartingHour>\S+</StartingHour>\\n\s+<StartingMinutes>\S+</StartingMinutes>',"<StartingHour>\S+</StartingHour>", logging,datetime)
   
    

def identifyMinute(path, logging, datetime):
    print("estoy identificando a que minuto se corre el historico")
    return Identify(path + "/Middleware/STE/ConfigFiles/Scheduling.config",'<Description>Procesamiento de Reportes \S+</Description>\\n\s+<Scheduling type="Sidesys.eFlow.SystemTools.Scheduling.TaskLoader.StartingAtGivenTimeBasedExecTimeConfig">\\n\s+<StartingHour>\S+</StartingHour>\\n\s+<StartingMinutes>\S+</StartingMinutes>',"<StartingMinutes>\S+</StartingMinutes>", logging,datetime)

def configurarHorario(path,hour, minute,logging, datetime):
    
   
    if(len(hour)<2):
        print(hour)
        hour="0" + str(hour)
        print(hour)
    if(len(minute)<2):
       print(minute)
       minute="0" + minute
       print(minute)

        
    
    replaceCadenaInSection(path + "/Middleware/STE/ConfigFiles/Scheduling.config",'<Description>Procesamiento de Reportes \S+</Description>\\n\s+<Scheduling type="Sidesys.eFlow.SystemTools.Scheduling.TaskLoader.StartingAtGivenTimeBasedExecTimeConfig">\\n\s+<StartingHour>\S+</StartingHour>\\n\s+<StartingMinutes>\S+</StartingMinutes>',"<StartingHour>\S+</StartingHour>", f"<StartingHour>{hour}</StartingHour>",logging,datetime)
    replaceCadenaInSection(path + "/Middleware/STE/ConfigFiles/Scheduling.config",'<Description>Procesamiento de Reportes \S+</Description>\\n\s+<Scheduling type="Sidesys.eFlow.SystemTools.Scheduling.TaskLoader.StartingAtGivenTimeBasedExecTimeConfig">\\n\s+<StartingHour>\S+</StartingHour>\\n\s+<StartingMinutes>\S+</StartingMinutes>',"<StartingMinutes>\S+</StartingMinutes>", f"<StartingMinutes>{minute}</StartingMinutes>",logging,datetime)

    "C:\Entornos\ONAPI\Frontend\STE\Web.config"

#identifyHour("C:\Sides",logging,datetime)
#identifyMinute("C:\Sides",logging,datetime)
#configurarHorario("C:\Sides","2","01",logging,datetime)
#\\n\s+<Scheduling type="Sidesys.eFlow.SystemTools.Scheduling.TaskLoader.StartingAtGivenTimeBasedExecTimeConfig">\\n\s+<StartingHour>22</StartingHour>\\n\s+<StartingMinutes>00</StartingMinutes>