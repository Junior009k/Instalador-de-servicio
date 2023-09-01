
from Validador import *
import win32com.client
import datetime
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
   # Crear una instancia del objeto ADODB.Stream
    print(f"{path} + {name}.udl")
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

    # Modificar las propiedades de conexión
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
    # Abrir el objeto Stream en modo escritura
    stream.Open()
    stream.WriteText(new_content)
    # Guardar el archivo UDL
    #loggin.info(f' {datetime.datetime.now()} : {new_content} '}
    stream.SaveToFile(f'{path}\{name}.udl', 2) # 2 = overwrite

    # Cerrar el objeto Stream
    stream.Close()

#gestionaUDL("RDSTAC001/SQLEXPRESS","aerodom2","C:\Entorno\JurisdiccionInmobiliaria\Middleware\SE\ConfigFiles")
