import subprocess
import datetime
import os

def createAplicationIIS(name, Path,loggin):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion De la creacion de la aplicacion {name} ')
    comando_ps =f'''
                 Import-Module WebAdministration
                 New-Item 'IIS:\Sites\Default Web Site\{name}' -physicalPath '{Path}' -type Application
                '''

    resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
    print(resultado)
    loggin.info(f' {datetime.datetime.now() }: {resultado} ')
    if(validateDirectory(name,loggin)):
        loggin.info(f' {datetime.datetime.now() }: Creando la aplicacion...')
        return True
    else:
        loggin.error(f' {datetime.datetime.now() }: Error al crear la aplicacion {name}, valide que sea administrador')
        return False
    
def createSiteIIS(name, Path,loggin,port):
    loggin.info(f' {datetime.datetime.now() }: Inicializacion De la creacion del site {name} ')
    comando_ps =f'''
                 Import-Module WebAdministration
                 New-IISSite -Name {name} -BindingInformation "*:{port}:" -PhysicalPath "{Path}"
                '''

    resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
    print(resultado)
    loggin.info(f' {datetime.datetime.now() }: {resultado} ')
    loggin.info(f' {datetime.datetime.now() }: {name} Se creo el site correctamente')
# New-IISSite -Name "TestSite" -BindingInformation "*:8080:" -PhysicalPath "$env:systemdrive\inetpub\testsite"
#New-IISSite -Name "pRUEBA" -BindingInformation "*:855:" -PhysicalPath "C:\"
def validateDirectory(name,loggin):

    # Verifica si la carpeta existe
    if os.path.exists(f"C:/Users/{name}") and os.path.isdir(f"C:/Users/{name}"):
        loggin.info(f' {datetime.datetime.now() }: La carpeta {name}  existe')
    else:
        loggin.error(f' {datetime.datetime.now() }: La carpeta {name} no existe')
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
