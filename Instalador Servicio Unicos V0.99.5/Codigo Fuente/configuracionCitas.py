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
                '"appointmentApiUrl": "[\S|\\b]+",', 
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
    
#configurarCitas("C:\SidesysCitas","192.168.104.92","SegurosReservasCitas","STE","SegurosReservas", logging,datetime)