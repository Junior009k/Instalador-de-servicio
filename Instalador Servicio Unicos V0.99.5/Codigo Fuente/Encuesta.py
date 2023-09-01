from funcionesAuxiliares import *
import logging
import datetime

def configurarEncuesta(path,server,encuesta,eflow,loggin,datetime): 
    #"C:\SidesysEncuesta\FrontEnd\STE\Web.config"
    replaceCadena(f'{path}/FrontEnd/STE/Web.config',
                f'<add key="OpinionPollPath" value="[\S|\\b]+"', 
                f'<add key="OpinionPollPath" value="http://{server}/{encuesta}"',loggin,datetime)

    #"C:\SidesysEncuesta\FrontEnd\STE\Reportes\Poll\app\index.html"
    replaceCadena(f'{path}/FrontEnd/STE/Reportes/Poll/app/index.html',
               '<base href="[\S|\s]+/Reportes/Poll/app/"', 
                f'<base href="http://{server}/{encuesta}/Reportes/Poll/app/"',loggin,datetime)
     
    #"C:\SidesysEncuesta\FrontEnd\OpinionPoll\index.html"
    replaceCadena(f'{path}/FrontEnd/OpinionPoll/index.html',
                '<base href="\S+" />', 
                f'<base href="http://{server}/{encuesta}/" />',loggin,datetime)
    
    #"C:\SidesysEncuesta\FrontEnd\OpinionPoll\assets\settings.json"
    replaceCadena(f'{path}/FrontEnd/OpinionPoll/assets/settings.json',
                '"pollApiBaseUrl": "[\S|\\b]+",', 
                f'"pollApiBaseUrl": "http://{server}/{encuesta}/",',loggin,datetime)
     
    #"C:\SidesysEncuesta\Middleware\OpinionPoll\ConfigFiles\OpinionPoll.config"
    replaceCadena(f'{path}/Middleware/OpinionPoll/ConfigFiles/OpinionPoll.config',
                '<eFlow>[\S|\s]+</eFlow>', 
                f'<eFlow>http://{server}/{eflow}/</eFlow>',loggin,datetime)

    #"C:\SidesysEncuesta\Middleware\STE\ConfigFiles\OpinionPoll.config"
    replaceCadena(f'{path}/Middleware/STE/ConfigFiles/OpinionPoll.config',
                '<Path>[\S|\s]+</Path>', 
                   f'<Path>http://{server}/{encuesta}/</Path>',loggin,datetime)
   
    
    
#configurarEncuesta("C:\SidesysEncuesta","192.168.104.95","SegurosReservasPoll","STE", logging,datetime)