import subprocess
import datetime
import os
import re
import logging

def createAplicationIIS(name, Path,loggin):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion De la creacion de la aplicacion {name} ')
    resultado=consultaPowershell(f" New-Item 'IIS:\Sites\Default Web Site\{name}' -physicalPath '{Path}' -type Application",loggin,datetime)
    loggin.info(f' {datetime.datetime.now() }: {resultado} ')
    if(validateDirectory(name,loggin)):
        loggin.info(f' {datetime.datetime.now() }: Creando la aplicacion...')
        return True
    else:
        loggin.error(f' {datetime.datetime.now() }: Error al crear la aplicacion {name}, valide que sea administrador')
        return False

def createSiteIIS(name, Path,loggin,port):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion De la creacion del site {name} ')
    print(f'New-IISSite -Name {name} -BindingInformation "*:{port}:" -PhysicalPath "{Path}"')
    resultado=consultaPowershell(f'New-IISSite -Name {name} -BindingInformation "*:{port}:" -PhysicalPath "{Path}"',loggin,datetime)
    loggin.info(f' {datetime.datetime.now() }: {resultado} ')
    loggin.info(f' {datetime.datetime.now() }: {name} Se creo el site correctamente')

#Busca informacion de la aplicacion
def findApp(path,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }:buscando site que coincidan con la ruta {path}')
    #print(consultaPowershell("Get-WebApplication | select physicalPath",loggin,datetime))
    #print(consultaPowershell("Get-WebApplication | select path",loggin,datetime))#name
    #print(consultaPowershell("Get-WebApplication | select applicationPool",loggin,datetime))#siteName
    #print(consultaPowershell("Get-WebApplication | select enabledProtocols",loggin,datetime))#protocols
    #patron=re.findall(f'[\S]+:[" "|\\b|\S]+' , resultado.stdout)
    patron=  re.findall(f'\\n[\\b|\S|" "]+'   , consultaPowershell("Get-WebApplication | select physicalPath"    ,loggin,datetime))
    patronDetail=re.findall(f'\\n[\\b|\S|" "]+' , consultaPowershell("Get-WebApplication | select path,applicationPool,enabledprotocols",loggin,datetime))
    #name=    re.findall(f'\\n[\\b|\S|" "]+'   , consultaPowershell("Get-WebApplication | select path"            ,loggin,datetime))
    #site=   re.findall(f'\\n[\\b|\S|" "]+'   , consultaPowershell("Get-WebApplication | select applicationPool" ,loggin,datetime))
    #protocol=re.findall(f'\\n[\\b|\S|" "]+'   , consultaPowershell("Get-WebApplication | select enabledprotocols",loggin,datetime))
    nameA=[]
    siteA=[]
    protocolA=[]
    #print(path)
    #print(patron)
    #print(len(patron))
    i=0
    while(i<len(patron)):
        if(re.findall(path.replace("\\","/"),patron[i].replace("\\","/"))):
            nameA.append(re.split("[\s+|""]+",patronDetail[i])[1])
            siteA.append(re.split("[\s+|""]+",patronDetail[i])[2])
            protocolA.append(re.split("[\s+|""]+",patronDetail[i])[3])
        i=i+1
    if(len(nameA)==0 and len(siteA)==0 and len(protocolA)==0):return False
    return nameA,siteA, protocolA

#Busca Informacion del site
def findSite(path,loggin,datetime):
    #print(path)
    
    loggin.info(f' {datetime.datetime.now() }:buscando site que coincidan con la ruta {path}')
    #print(consultaPowershell("Get-WebSite | select id,physicalPath",loggin,datetime))
    #print(consultaPowershell("Get-WebSite | select name",loggin,datetime))#name
    #print(consultaPowershell("Get-WebSite | select state",loggin,datetime))#Started
    #print(consultaPowershell("Get-WebSite | select enabledprotocols",loggin,datetime))#enabledprotocols

    #patron=re.findall(f'[\S]+:[" "|\\b|\S]+' , resultado.stdout)
    #patron=re.findall(f'[" "|\\b|\S]+' , resultado.stdout)
    #patron=re.findall(f'[\s|\S]+' , resultado.stdout)
    #patron=re.findall(f'[" "|\\b|\S]+\s+[1-9]+\s+ S[\\b|\S|" "]+http[\\b|\S|" "]+' , resultado.stdout)
    patron=re.findall(f'\\n[\\b|\S|" "]+' , consultaPowershell("Get-WebSite | select id,physicalPath",loggin,datetime))
    patronDetail=re.findall(f'\\n[\\b|\S|" "]+' , consultaPowershell("Get-WebSite | select name,state,enabledprotocols",loggin,datetime))
    #name=re.findall(f'\\n[\\b|\S|" "]+' , consultaPowershell("Get-WebSite | select name",loggin,datetime))
    #state=re.findall(f'\\n[\\b|\S|" "]+' , consultaPowershell("Get-WebSite | select state",loggin,datetime))
    #protocol=re.findall(f'\\n[\\b|\S|" "]+' , consultaPowershell("Get-WebSite | select enabledprotocols",loggin,datetime))
    #print(path)
    #print(patron)
    #print(len(patron))
    nameA=[]
    stateA=[]
    protocolA=[]
    i=0
    while(i<len(patron)):
        # print(patron[i])
        if(re.findall(path.replace("\\","/"),patron[i].replace("\\","/"))):
            ##print(re.split("[\s+|""]+",patronDetail[i]))
            nameA.append(re.split("[\s+|""]+",patronDetail[i])[1])
            stateA.append(re.split("[\s+|""]+",patronDetail[i])[2])
            protocolA.append(re.split("[\s+|""]+",patronDetail[i])[3])
        i=i+1
    if(len(nameA)==0 and len(stateA)==0 and len(protocolA)==0):return False
    return nameA,stateA,protocolA
#valida el directorio en el IIS        
def validateDirectory(name,loggin):

    # Verifica si la carpeta existe
    if os.path.exists(f"C:/Users/{name}") and os.path.isdir(f"C:/Users/{name}"):
        loggin.info(f' {datetime.datetime.now() }: La carpeta {name}  existe')
    else:
        loggin.error(f' {datetime.datetime.now() }: La carpeta {name} no existe')

#Consulta Powershell 
def consultaPowershell(consulta,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }:empezando la consulta en poweshell')
    loggin.info(f' {datetime.datetime.now() }:{consulta}')
    comando_ps =f'''Import-Module WebAdministration
                 {consulta}'''
    resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
    if(len(resultado.stderr)>0):loggin.error(f' {datetime.datetime.now() }:error al realizar la consulta en powershell {resultado.stderr}')
    return resultado.stdout

#[0]eater eggs
def ko(event,k):
    bandera=True
    #upupdowndownleftrightabstart
    #38-38-40-40-37-39-65-66-13
    if(event.keycode==38 and k<2):
        print(f"arriba {k}")
        bandera=False
    if(event.keycode==40 and k>=2 and k<4):
        print(f"abajo {k}")
        bandera=False
    if(event.keycode==37 and k>=4 and k<5):
        print(f"Izquierda {k}")
        bandera=False
    if(event.keycode==39 and k>=5 and k<6):
        print(f"Derecha {k}")
        bandera=False
    if(event.keycode==65 and k>=6 and k<7):
        print(f"A {k}")
        bandera=False
    if(event.keycode==66 and k>=7 and k<8):
        print(f"B {k}")
        bandera=False
    if(event.keycode==13 and k>=8 and k<9):
        print(f"START {k}")
        bandera=False
    if((event.keycode not in [38,40,37,39,65,66,13]) or bandera):
        print("Ups no completaste el acertijo")
        return 0
    return k+1


#createAplicationIIS("hola","C:\Entornos",logging)   
#createSiteIIS("hola","C:\Entornos",logging,"801") 
#print(findApp("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\\FrontEnd\\Appointment",logging,datetime))
#print(findSite("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\\FrontEnd\\STE",logging,datetime))
#print(findSite("C:\\",logging,datetime))