from os import system
import psutil
import logging
import datetime
def instalarServicio(name,path,start,loggin):
    logging.info(f' {datetime.datetime.now() }: Inicializacion De La instalacion del servicio')
    system('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    print('sc create "'+name+'"  binpath="'+path+'" obj=localsystem start='+str(start)+' ')
    if(validarExistenciaDelServicio(name)):
        logging.info(f' {datetime.datetime.now() }: El servicio {name} se ha instalado exitosamente')
        logging.info(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return True
    else:
        logging.error(f' {datetime.datetime.now() }: El servicio {name} no se ha instalado exitosamente')
        logging.info(f' {datetime.datetime.now()}: Finalizacion de la instalacion del servicio')
        return False

def instalarCounter(name,path):
    system('')


def validarExistenciaDelServicio(name):
    '''
    Check if there is any running process that contains the given name processName.
    '''
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