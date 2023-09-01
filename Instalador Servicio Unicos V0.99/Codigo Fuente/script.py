from os import system
import psutil
import logging
import datetime
def installService(name,path,start,loggin):
    logging.info(f' {datetime.datetime.now() }: Inicializacion De La instalacion del servicio')
    system('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    print('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    if(validateExistService(name)):
        logging.info(f' {datetime.datetime.now() }: El servicio {name} se ha instalado exitosamente')
        logging.info(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return True
    else:
        logging.error(f' {datetime.datetime.now() }: El servicio {name} no se ha instalado ')
        logging.error(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return False

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

#"C:\Users\jaquino\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" main.py script.py Validador.py funcionesAuxiliares.py configuracionCitas.py db.py iis.py --onefile --name "Instalador servicio"
#"C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe" main.py script.py Validador.py funcionesAuxiliares.py configuracionCitas.py db.py iis.py NME.py NCache.py code.py --onefile --name "Instalador servicio"
#C:\Users\jaquino\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip