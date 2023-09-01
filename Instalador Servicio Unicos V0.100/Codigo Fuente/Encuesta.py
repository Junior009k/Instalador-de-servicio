from funcionesAuxiliares import *

def configurarEncuesta(path,server,encuesta,eflow,loggin,datetime): 
    #"C:\SidesysEncuesta\FrontEnd\STE\Web.config"
    replaceCadena(f'{path}/FrontEnd/STE/Web.config',
                f'<add key="OpinionPollPath" value="[\S|\\b|" "]+"', 
                f'<add key="OpinionPollPath" value="http://{server}/{encuesta}"',loggin,datetime)

    #"C:\SidesysEncuesta\FrontEnd\STE\Reportes\Poll\app\index.html"
    replaceCadena(f'{path}/FrontEnd/STE/Reportes/Poll/app/index.html',
               '<base href="[\S|\s]+/Reportes/Poll/app/"', 
                f'<base href="http://{server}/{encuesta}/Reportes/Poll/app/"',loggin,datetime)
     
    #"C:\SidesysEncuesta\FrontEnd\OpinionPoll\index.html"
    replaceCadena(f'{path}/FrontEnd/OpinionPoll/index.html',
                '<base href="[\S|\\b|" "]+ />', 
                f'<base href="http://{server}/{encuesta}/" />',loggin,datetime)
    
    #"C:\SidesysEncuesta\FrontEnd\OpinionPoll\assets\settings.json"
    replaceCadena(f'{path}/FrontEnd/OpinionPoll/assets/settings.json',
                '"pollApiBaseUrl":[\S|\\b|" "]+",', 
                f'"pollApiBaseUrl": "http://{server}/{encuesta}/",',loggin,datetime)
     
    #"C:\SidesysEncuesta\Middleware\OpinionPoll\ConfigFiles\OpinionPoll.config"
    replaceCadena(f'{path}/Middleware/OpinionPoll/ConfigFiles/OpinionPoll.config',
                '<eFlow>[\S|\s]+</eFlow>', 
                f'<eFlow>http://{server}/{eflow}/</eFlow>',loggin,datetime)

    #"C:\SidesysEncuesta\Middleware\STE\ConfigFiles\OpinionPoll.config"
    replaceCadena(f'{path}/Middleware/STE/ConfigFiles/OpinionPoll.config',
                '<Path>[\S|\s]+</Path>', 
                   f'<Path>http://{server}/{encuesta}/</Path>',loggin,datetime)

def updateEncuestas(path,steweb,pollReporte,pollIndex,setting,pollMiddleware,steMiddleware,loggin,datetime): 
   print("configurar Citas")
   #"C:\SidesysEncuesta\FrontEnd\STE\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/STE/Web.config','<add key="OpinionPollPath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+"',f'value="{steweb}"',loggin,datetime)
  
   #C:\SidesysEncuesta\FrontEnd\STE\Reportes\Poll\app\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/STE/Reportes/Poll/app/index.html','<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+"',f'href="{pollReporte}"',loggin,datetime)

   #C:\SidesysEncuesta\FrontEnd\OpinionPoll\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/OpinionPoll/index.html','<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+"',f'href="{pollIndex}"',loggin,datetime)

   #C:\SidesysEncuesta\FrontEnd\OpinionPoll\assets\settings.json"
   replaceCadenaInSection(f'{path}/FrontEnd/OpinionPoll/assets/settings.json','"pollApiBaseUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+"',f': "{setting}"',loggin,datetime)

   #"C:\SidesysEncuesta\Middleware\OpinionPoll\ConfigFiles\OpinionPoll.config"
   replaceCadenaInSection(f'{path}/Middleware/OpinionPoll/ConfigFiles/OpinionPoll.config','<eFlow>[\S|\s]+</eFlow>','<eFlow>[\S|\s]+</eFlow>',f'<eFlow>{pollMiddleware}</eFlow>',loggin,datetime)

   #"C:\SidesysEncuesta\Middleware\STE\ConfigFiles\OpinionPoll.config"
   replaceCadenaInSection(f'{path}/Middleware/STE/ConfigFiles/OpinionPoll.config','<Path>[\S|\s]+</Path>','<Path>[\S|\s]+</Path>',f'<Path>{steMiddleware}</Path>',loggin,datetime)

#updateEncuestas("C:\Entornos\Cerilab - 05\PRODUCCION","steweb","PollReporte","pollIndex","setting","pollMiddleware","STEiddleware",logging,datetime)


#identifyBaseURL(f"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/STE/Web.config",'<add key="OpinionPollPath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/STE/Reportes/Poll/app/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/OpinionPoll/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/OpinionPoll/assets/settings.json",'"pollApiBaseUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime)
#Identify(f"C:/Entornos/Senasa - 03/PRODUCCION/Middleware/OpinionPoll/ConfigFiles/OpinionPoll.config",'<eFlow>[\S|\s]+</eFlow>','<eFlow>[\S|\s]+</eFlow>',logging,datetime)
#Identify(f"C:/Entornos/Senasa - 03/PRODUCCION/Middleware/STE/ConfigFiles/OpinionPoll.config",'<Path>[\S|\\b|" "]+</Path>','<Path>[\S|\\b|" "]+</Path>',logging,datetime)


#configurarEncuesta("C:\SidesysEncuesta","192.168.104.95","SegurosReservasPoll","STE", logging,datetime)