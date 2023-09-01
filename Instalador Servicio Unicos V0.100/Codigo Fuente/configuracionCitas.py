from funcionesAuxiliares import *
import logging
import datetime

def configurarCitas(path,server,citas,eflow,msmq,loggin,datetime): 
    #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\appSpa\index.html"
    replaceCadena(f'{path}/FrontEnd/Appointment/appSpa/index.html',
                '<base href="\S+">', 
                f'<base href="http://{server}/{citas}/appSpa/"> ',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\AttOpSpa\index.html"
    replaceCadena(f'{path}/FrontEnd/Appointment/AttOpSpa/index.html',
               '<base href="\S+">', 
                f'<base href="http://{server}/{citas}/AttOpSpa/">" ',loggin,datetime)
     
    #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\bin\Application.config"
    replaceCadena(f'{path}/FrontEnd/Appointment/bin/Application.config',
                '<OperationalPath>[\S|\s]+</OperationalPath>', 
                f'<OperationalPath>http://{server}/{citas}/POC/POCView.aspx</OperationalPath>',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\FrontEnd\STE\Web.config"
    replaceCadena(f'{path}/FrontEnd/STE/Web.config',
                '<add key="AppointmentWS" value="[\S|\s]+/Appointment.asmx"', 
                f'<add key="AppointmentWS" value="http://{server}/{citas}/Appointment.asmx"',loggin,datetime)
     
    #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\index.html"
    replaceCadena(f'{path}/FrontEnd/AppointmentWeb/index.html',
                '<base href="\S+" />', 
                f'<base href="http://{server}/{citas}web/" />',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\Web.config" cola de mensajeria web 
    replaceCadena(f'{path}/FrontEnd/AppointmentWeb/Web.config',
                '<add key="messageQueuePath" value="\S+" />', 
                   f'<add key="messageQueuePath" value="FormatName:DIRECT=TCP:{server}\private$\{msmq}" />',loggin,datetime)
    

    #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\assets\settings.json"
    replaceCadena(f'{path}/FrontEnd/AppointmentWeb/assets/settings.json',
                '"appointmentApiUrl": "[\S|\\b|" "]+",', 
                f'"appointmentApiUrl": "http://{server}/{citas}webservice",',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config" OutgoingEventsSendQueuePath>
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config',
                '<OutgoingEventsSendQueuePath>[\S|\s]+</OutgoingEventsSendQueuePath>', 
                f'<OutgoingEventsSendQueuePath>FormatName:DIRECT=TCP:{server}\private$\{msmq}</OutgoingEventsSendQueuePath>',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config" cola de mensajeria web 
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config',
                '<MSMQWebChannel>[\S|\s]+</MSMQWebChannel>', 
             f'<MSMQWebChannel>FormatName:DIRECT=TCP:{server}\private$\{msmq}</MSMQWebChannel>',loggin,datetime)
    
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\bin\Sidesys.Services.ApplicationService.exe.config" e-Flow 
    replaceCadena(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config',
                '<add key="dataExportServer" value="\S+"/>', 
                f'<add key="dataExportServer" value="http://{server}/{eflow}"/>',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\bin\Sidesys.Services.ApplicationService.exe.config" cola de mensajeria
    replaceCadena(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config',
                '<add key="virtualQueueCallBackQueuePath" value="\S+" />', 
                f'<add key="virtualQueueCallBackQueuePath" value="FormatName:DIRECT=TCP:{server}\private$\{msmq}" />',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\STE\ConfigFiles\DataExport.config"
    replaceCadena(f'{path}/Middleware/STE/ConfigFiles/DataExport.config',
                '<OutgoingEventsSendQueuePath>\S+</OutgoingEventsSendQueuePath>', 
                f'<OutgoingEventsSendQueuePath>FormatName:DIRECT=TCP:{server}\private$\{msmq}</OutgoingEventsSendQueuePath>',loggin,datetime)


from funcionesAuxiliares import *

def updateCitas(path,appSpa,AttOpSpa,app,awi,setting,steweb,steMiddleware,nmecitas,MSMQawi,MSMQMAout,MSMQMAweb,MSMQMService, MSMQMDataExport,loggin,datetime): 
   print("configurar Citas")
   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\appSpa\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/appSpa/index.html','<base href=[\S|\\b|" "|[<,>]]+','href="[\S|\\b|" "]+"',f'href="{appSpa}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\AttOpSpa\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/AttOpSpa/index.html','<base href=[\S|\\b|" "]+','href="[\S|\\b|" "]+"',f'href="{AttOpSpa}"',loggin,datetime)
    
   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\bin\Application.config"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/bin/Application.config','<OperationalPath>[\S|\\b|" "]+</OperationalPath>','<OperationalPath>[\S|\\b|" "]+</OperationalPath>',f'<OperationalPath>{app}</OperationalPath>',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentWeb/index.html','<base href=[\S|\\b|" "]+','href="[\S|\\b|" "]+"',f'href="{awi}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\assets\settings.json"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentWeb/assets/settings.json','"appointmentApiUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+"',f':"{setting}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\STE\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/STE/Web.config','<add key="AppointmentWS" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+"',f'value="{steweb}"',loggin,datetime)

   #""C:\Entorno\Seguros Reservas\Middleware\Appointment\bin\Sidesys.Services.ApplicationService.exe.config" e-Flow 
   replaceCadenaInSection(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config','<add key="dataExportServer" value=[\S|\\b|" "]+/>','value=[\S|\\b|" "]+"',f'value="{steMiddleware}"',loggin,datetime)

   #C:\Sides\Frontend\STE\SPA\assets\configuration\emission.config.json
   replaceCadenaInSection(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json','"appointmentApiEndpoint": [\S|\\b|" "]+"',':[\S|\\b|" "]+"',f':"{nmecitas}"',loggin,datetime)

   #C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentWeb/Web.config','<add key="messageQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+"',f'value="{MSMQawi}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',f'<OutgoingEventsSendQueuePath>{MSMQMAout}</OutgoingEventsSendQueuePath>',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>',f'<MSMQWebChannel>{MSMQMAweb}</MSMQWebChannel>',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config','<add key="virtualQueueCallBackQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+"',f'value="{MSMQMService}"',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/STE/ConfigFiles/DataExport.config','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',f'<OutgoingEventsSendQueuePath>{MSMQMDataExport}</OutgoingEventsSendQueuePath>',loggin,datetime)




#updateCitas(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/","http://rdstac001/Citas","http://rdstac001/Citas","http://rdstac001/ CitasApp","http://rdstac001/ CitasIndex","http://rdstac001/ CitaswebService","http:RDSTAC001/Citas/Appointment","http://RDSTAC002/STE","http://rdstac001/ CitaswebService",".\Appointment",".\Appointmentout",".\AppointmentWeb",".\Appointmentout",".\AppointmentWeb",logging,datetime)
#configurarCitas("C:\SidesysCitas","192.168.104.92","SegurosReservasCitas","STE","SegurosReservas", logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/Appointment/appSpa/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/Appointment/AttOpSpa/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/AppointmentWeb/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/AppointmentWeb/assets/settings.json",'"appointmentApiUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/STE/Web.config",'<add key="AppointmentWS" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="dataExportServer" value=[\S|\\b|" "]+/>','value=[\S|\\b|" "]+',logging,datetime)
identifyBaseURL(f"C:\Entornos\Superintendencia - 04\PRODUCCION/FrontEnd/STE/SPA/assets/configuration/emission.config.json",'"appointmentApiEndpoint":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/AppointmentWeb/Web.config",'<add key="messageQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime)
#Identify(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/Appointment/ConfigFiles/Appointment.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime)
#Identify(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/Appointment/ConfigFiles/Appointment.config",'<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION//Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="virtualQueueCallBackQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime)
#Identify(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/STE/ConfigFiles/DataExport.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime)

