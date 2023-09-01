from os import system
import psutil
import datetime
import win32com.client
import re 

#See encarga de indentificar el servicio
def identifyService(path,logging,datetime):
    logging.info(f' {datetime.datetime.now() }: Empezando a identificar el servicio de la ruta {path}')
    services = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    service_locator = services.ConnectServer(".", "root\cimv2")
    service_query = "SELECT * FROM Win32_Service"
    service_list = service_locator.ExecQuery(service_query)
    print(path)
    print(path.replace('\\', r"/"))
    path2=path.replace('\\', r"/")
    for service in service_list:
        try:
            if(path==service.PathName or path2==service.PathName):
                print(f"Nombre: {service.Name}")
                print(f"Estado: {service.State}")
                print(f"Tipo de inicio: {service.StartMode}")
                print(f"Descripción: {service.Description}")
                print(f"Ruta del archivo ejecutable: {service.PathName}")
                logging.info(f' {datetime.datetime.now() }: Nombre: {service.Name}')
                logging.info(f' {datetime.datetime.now() }: Estado: {service.State}')
                logging.info(f' {datetime.datetime.now() }: Tipo de inicio: {service.StartMode}')
                logging.info(f' {datetime.datetime.now() }: Descripción: {service.Description}')
                logging.info(f' {datetime.datetime.now() }: Ruta del archivo ejecutable: {service.PathName}')
                return service.Name,service.State, service.StartMode, service.PathName
        except Exception as e:
            logging.info(f' {datetime.datetime.now() }: error al identificar los servicios {e}')
#identifyService("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\Middleware\\STE\\bin\Sidesys.Services.ApplicationService.exe", logging, datetime)
def installService(name,path,start,loggin):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion De La instalacion del servicio')
    system('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    loggin.info(f' {datetime.datetime.now() }: create "{name}"  binpath="{path}" obj=localsystem start={str(start)} ')
    print('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    if(validateExistService(name)):
        loggin.info(f' {datetime.datetime.now() }: El servicio {name} se ha instalado exitosamente')
        loggin.info(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return True
    else:
        loggin.error(f' {datetime.datetime.now() }: El servicio {name} no se ha instalado ')
        loggin.error(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return False

#identifyService("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\Middleware\\STE\\bin\Sidesys.Services.ApplicationService.exe", logging, datetime)
def manageService(p,name,path,loggin):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion del manejador de servicio')
    print(p)
    print(name)
    print(path)
    #Ejecuta el servicio
    if(p==1):
        system(f'sc start "{name}"')
        loggin.info(f'sc start "{name}"')
        print(f'sc start "{name}"')   
    if(p==2):
        system(f'sc stop "{name}"')
        loggin.info(f'sc stop "{name}"')
        print(f'sc stop "{name}"')  

def instalarCounter(name,path):
    system('')


def validateExistService(name):
    #Itera los servicios
    for proc in psutil.win_service_iter():
        try:
            # Valida los nombres de lo servicios 
            if name.lower() in proc.name().lower():
                print(proc.name())
                return True;
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

#"C:\Users\jaquino\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" main.py script.py Validador.py funcionesAuxiliares.py configuracionCitas.py db.py iis.py NME.py NCache.py code.py Encuesta.py RHI.py mail.py consola.py nodo.py Reporte.py --onefile --name "Instalador servicio"
#"C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" main.py script.py Validador.py funcionesAuxiliares.py configuracionCitas.py db.py iis.py NME.py NCache.py code.py Encuesta.py RHI.py mail.py consola.py --onefile --name "Instalador servicio"
#C:\Users\jaquino\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip