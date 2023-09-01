from funcionesAuxiliares import *
import logging
import datetime

def configurarNME(path,server,eflow,eflowApi,loggin,datetime): 
    #"C:\Sides\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/Sidesys.eFlow.Emission.API/Web.config',
                '<add key="eFlowServiceUrl" value="http://[\S|\\b|" "]+/Services/EmissionService.svc"', 
                f'<add key="eFlowServiceUrl" value="http://{server}/{eflow}/Services/EmissionService.svc"',loggin,datetime)
    #"C:\Sides\Frontend\STE\SPA\assets\configuration\emission.config.json"
    replaceCadena(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',
                '"emissionApiEndpoint": "[\S|\\b|" "]+",', 
                f'"emissionApiEndpoint": "http://{server}/{eflowApi}",',loggin,datetime)
def configurarNMESite(path,server,eflow,eflowApi,loggin,datetime): 
    #"C:\Sides\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/Sidesys.eFlow.Emission.API/Web.config',
                '<add key="eFlowServiceUrl" value="http://[\S|\\b|" "]+/Services/EmissionService.svc"', 
                f'<add key="eFlowServiceUrl" value="http://{server}:{eflow}/Services/EmissionService.svc"',loggin,datetime)
    #"C:\Sides\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/Sidesys.eFlow.Emission.API/Web.config',
                ' <add key="AllowedCrossOrigins" value="[\S|\\b|" "]+"', 
                f'<add key="AllowedCrossOrigins" value="http://{server}:{eflow}"',loggin,datetime)    
    #"C:\Sides\Frontend\STE\SPA\assets\configuration\emission.config.json"
    replaceCadena(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',
                '"emissionApiEndpoint": "[\S|\\b|" "]+",', 
                f'"emissionApiEndpoint": "http://{server}:{eflowApi}",',loggin,datetime)
 
def configurarNMECitas(path,server,citaswebservice,loggin,datetime): 
    #"C:\Entornos\Superintendencia - 03\PRODUCCION\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',
    '"appointmentApiEndpoint": "[\S|\\b|" "]+",', 
    f'"appointmentApiEndpoint": "http://{server}/{citaswebservice}",',loggin,datetime)

def configurarEmissionConfig(path, preferencial, loggin,datetime):
    if(preferencial==1):preferencial='true'
    else:preferencial='false'
    replaceCadenaInSection(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json','"attentionPreferential": {[\S|\s]+"showIcon"','"showButton":[\S|\\b|" "]+,', f'"showButton": {preferencial},',logging,datetime)
#configurarEmissionConfig("C:\Entornos\Superintendencia - 04\PRODUCCION",1, logging, datetime)   
def identifyNME(path):
    if(IdentifyJSON(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json','"attentionPreferential": {\\n\s+"showButton": [\S|\\b|" "]+,','"showButton": [\S|\\b|" "]+,',logging,datetime)=="true"):
        return True
    else:
        return False
#print(identifyNME("C:\Entornos\Superintendencia - 04\PRODUCCION"))
#configurarNMESite("C:\Entornos\Superintendencia - 04\PRODUCCION","192.168.104.42","80","81",logging,datetime)
#configurarNME("C:\Entornos\Superintendencia - 04\PRODUCCION","192.168.104.42","ste","steAPI",logging,datetime)
#configurarNMECitas("C:\Entornos\Superintendencia - 04\PRODUCCION","192.168.104.42","AppointmentWebService",logging,datetime)