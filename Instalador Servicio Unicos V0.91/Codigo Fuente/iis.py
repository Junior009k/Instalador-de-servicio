import subprocess
import datetime
import os

def creacionAplicacion(name, Path,loggin):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion De la creacion de la aplicacion {name} ')
    comando_ps =f'''
                 Import-Module WebAdministration
                 New-Item 'IIS:\Sites\Default Web Site\{name}' -physicalPath '{Path}' -type Application
                '''

    resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
    if(validarDirectorio(name,loggin)):
        loggin.info(f' {datetime.datetime.now() }: Creando la aplicacion...')
        return True
    else:
        loggin.error(f' {datetime.datetime.now() }: Error al crear la aplicacion {name}, valide que sea administrador')
        return False

def validarDirectorio(name,loggin):

    # Verifica si la carpeta existe
    if os.path.exists(f"C:/Users/{name}") and os.path.isdir(f"C:/Users/{name}"):
        loggin.info(f' {datetime.datetime.now() }: La aplicacion se creo exitosamente')
    else:
        loggin.error(f' {datetime.datetime.now() }: La carpeta {name} no existe')