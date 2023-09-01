from funcionesAuxiliares import *
import logging
import datetime

def configurarNME(path,server,eflow,eflowApi,loggin,datetime): 
    #"C:\Sides\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/Sidesys.eFlow.Emission.API/Web.config',
                '<add key="eFlowServiceUrl" value="http://\S+/Services/EmissionService.svc"', 
                f'<add key="eFlowServiceUrl" value="http://{server}/{eflow}/Services/EmissionService.svc"',loggin,datetime)
    #"C:\Sides\Frontend\STE\SPA\assets\configuration\emission.config.json"
    replaceCadena(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',
                '"emissionApiEndpoint": "http://\S+",\\n\s+"appointmentEnabled": true,', 
                f'"emissionApiEndpoint": "http://{server}/{eflowApi}",\n      "appointmentEnabled": true,',loggin,datetime)

#configurarNaNME("C:\Sides","192.168.104.42","ste","steAPI",logging,datetime)