
from Validador import *
from funcionesAuxiliares import *
import win32com.client
import datetime
import logging 
import re

def manageUDL(server,database,path,loggin):
    loggin.info(f' {datetime.datetime.now() }: Comenzando a modificar el udl')
    server=server.replace("/", r"\ ".strip())
    if(validateService(path,"STE","Middleware","ConfigFiles")):
        loggin.info(f' {datetime.datetime.now() }: Comenzando a modificar el udl de STE')
        #name,user,password,server,database
        #e-Flow
        createsUDL("SOF","SOF","SOF",server,database,path,loggin)
        createsUDL("STE","usr_STE","usr_STE",server,database,path,loggin)
        createsUDL("STE_HD","usr_STE","usr_STE",server,database,path,loggin)
        createsUDL("STE_ServerGroup","usr_STE","usr_STE",server,database,path,loggin)
    elif(validateService(path,"Appointment","Middleware","ConfigFiles")):
        loggin.info(f' {datetime.datetime.now() }: Comenzando a modificar el udl de SSP')
        #Citas
        createsUDL("SOF","SOF","SOF",server,database,path,loggin)
        createsUDL("SSP","usr_SSP","usr_SSP",server,database,path,loggin)
    elif(validateService(path,"OpinionPoll","Middleware","ConfigFiles")):
        #Encuesta
        loggin.info(f' {datetime.datetime.now() }: Comenzando a modificar el udl de OpinionPoll')
        createsUDL("SOF","SOF","SOF",server,database,path,loggin)
        createsUDL("OpinionPoll","usr_STE","usr_STE",server,database,path,loggin) 
    else:
        loggin.error(f' {datetime.datetime.now() }: No se encontraron los udls')
        print("No se encontraron los udls")

def createsUDL(name,user,password,server,database,path,loggin):
  
    print(f"{path} {name}")
    # Modificar las propiedades de conexión
    content=openUdl(path,name)
    contentS=content.split('\n',2)[2]
   # print(contentS)
    #1Password 2 n/a 3User id 4 initialcatalog 5Data source 
   # print(contentS.split(';',4))
    print(f"""
           1){contentS.split(';',4)[0]}
           2){contentS.split(';',4)[1]}
           3){contentS.split(';',4)[2]}
           4){contentS.split(';',4)[3]} 
           5){contentS.split(';',4)[4]} 
            """)
    loggin.info(f''' {datetime.datetime.now() }
           1){contentS.split(';',4)[0]}
           2){contentS.split(';',4)[1]}
           3){contentS.split(';',4)[2]}
           4){contentS.split(';',4)[3]} 
           5){contentS.split(';',4)[4]} 
            ''')
    new_content = content.replace(contentS.split(';',4)[4], f'Data Source={server}')
    new_content = new_content.replace(contentS.split(';',4)[3], f'Initial Catalog={database}')
    new_content = new_content.replace(contentS.split(';',4)[2], f'User ID={user}')
    new_content = new_content.replace(contentS.split(';',4)[0], f'Password={password}')
     
    loggin.info(f''' {datetime.datetime.now() }
           1)La nueva clave es {password}
           2)La nueva base de datos es {database}
           3)El nuevo usuario es {user}
           4)El nuevo servidor es {server} 
            ''')
    stream = win32com.client.Dispatch('ADODB.Stream')
    # Abrir el objeto Stream en modo escritura
    stream.Open()
    stream.WriteText(new_content)
    # Guardar el archivo UDL
    #loggin.info(f' {datetime.datetime.now()} : {new_content} '}
    stream.SaveToFile(f'{path}\{name}.udl', 2) # 2 = overwrite

    # Cerrar el objeto Stream
    stream.Close()

def findUdls(path,name,loggin,datetime):
    try:
        content=openUdl(path,name).split('\n',2)[2]
        return content.split(';',4)[0].split("=",2)[1],content.split(';',4)[2].split("=",2)[1],content.split(';',4)[3].split("=",2)[1],content.split(';',4)[4].split("=",2)[1]
    except Exception as e: 
        logging.error(f' {datetime.datetime.now() }: No se ha identificado correctamente el udl, por favor revisarlos')
        logging.error(f' {datetime.datetime.now() }: {e}')
        return False
def openUdl(path,name):
     # Crear una instancia del objeto ADODB.Stream
    stream = win32com.client.Dispatch('ADODB.Stream')

    # Establecer los atributos del objeto Stream
    stream.Type = 2 # Texto
    stream.Charset = 'utf-16le'

    # Abrir el archivo UDL en modo lectura
    stream.Open()
    stream.LoadFromFile(f'{path}\{name}.udl')

    # Leer el contenido del archivo UDL
    content = stream.ReadText(-1)
#
    # Cerrar el objeto Stream
    stream.Close()

    return content

#print(findUdls("C:\Instalador de Servicio\Instalador Servicio Unicos V0.99.6\Codigo Fuente","SOF",logging,datetime))
#gestionaUDL("RDSTAC001/SQLEXPRESS","aerodom2","SOF.udl")
#createsUDL("SOF","SOF","SOF","192.168.104.92","RDSTAC001","C:\Instalador de Servicio\Instalador Servicio Unicos V0.99.6\Codigo Fuente",logging)