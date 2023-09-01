from funcionesAuxiliares import *
import logging
import datetime

def identifyVersion(path,patron,logging,datetime):
    return Identify(path,patron,patron, logging, datetime)



#print(identifyVersion("C:\Entornos\Clinica San Rafael\Centro Medico San Rafael\CMSR - eFlow 4.1.3\Despliegue\Entregable\\1. Proceso de Intalacion\FrontEnd\STE\\bin\eflow.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime))
#print(identifyVersion("C:\Entornos\Superintendencia - 04\PRODUCCION\FrontEnd\Appointment\\bin\Application.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime))
#print(identifyVersion("C:\Entornos\Senasa - 03\PRODUCCION\FrontEnd\OpinionPoll\\bin\OpinionPoll.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime))