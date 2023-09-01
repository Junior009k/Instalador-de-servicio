
import re
#print(content)
port="1421"
patron= '<endpoint name="MiddleWare" address="net.tcp://localhost:\w*/ApplicationService/" '
service= f'<endpoint name="MiddleWare" address="net.tcp://localhost:{port}00/ApplicationService/" '




def changePort(path,port,loggin,datetime):
    #puertos {path}\Middleware\bin\servicemodelConfig\{service.config} tcp middleware
    loggin.info(f' {datetime.datetime.now() }: Se inicia con el proceso de cambio de puerto')
    replacePort(f'{path}/Middleware/STE/bin/serviceModelConfig/services.config',
                '<endpoint name="MiddleWare" address="net.tcp://localhost:\w*/ApplicationService/" ', 
                f'<endpoint name="MiddleWare" address="net.tcp://localhost:{port}00/ApplicationService/" ',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{service.config} Design Time Adress middleware
    replacePort(f'{path}/Middleware/STE/bin/serviceModelConfig/services.config',
                'add baseAddress="http://localhost:\w*/Design_Time_Addresses/Sidesys.Services/ApplicationService/"', 
                f'add baseAddress="http://localhost:{port}2/Design_Time_Addresses/Sidesys.Services/ApplicationService/"',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{Cliente.config} clientNode en el middleware
    replacePort(f'{path}/Middleware/STE/bin/serviceModelConfig/client.config',
                'address="net.tcp://localhost:\w*/ApplicationServiceNode/"', 
                f'address="net.tcp://localhost:{port}01/ApplicationServiceNode/"',loggin,datetime)
    #puertos {path}\MiddlewareNode\bin\servicemodelConfig\{service.config} tcp middlewareNode
    replacePort(f'{path}/MiddlewareNode/STE/bin/serviceModelConfig/services.config',
                '<endpoint name="MiddleWareNode" address="net.tcp://localhost:\w*/ApplicationServiceNode/" ', 
                f'<endpoint name="MiddleWareNode" address="net.tcp://localhost:{port}01/ApplicationServiceNode/" ',loggin,datetime)
    #puertos {path}\MiddlewareNode\bin\servicemodelConfig\{service.config} Design Time Adress middlewareNode
    replacePort(f'{path}/MiddlewareNode/STE/bin/serviceModelConfig/services.config',
                'add baseAddress="http://localhost:\w*/Design_Time_Addresses/Sidesys.Services/ApplicationServiceNode/"', 
                f'add baseAddress="http://localhost:{port}3/Design_Time_Addresses/Sidesys.Services/ApplicationServiceNode/"',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{Cliente.config} clientNode en el middlewareNode
    replacePort(f'{path}/MiddlewareNode/STE/bin/serviceModelConfig/client.config',
                'address="net.tcp://localhost:\w*/ApplicationServiceNode/"', 
                f'address="net.tcp://localhost:{port}9/ApplicationServiceNode/"',loggin,datetime)
    #puertos {path}\Frontend\ConfigFiles\Client.config tcp middleware
    replacePort(f'{path}/Frontend/STE/ConfigFiles/client.config',
                '<endpoint name="MiddleWare" address="net.tcp://localhost:\w*/ApplicationService/"', 
                f'<endpoint name="MiddleWare" address="net.tcp://localhost:{port}00/ApplicationService/" ',loggin,datetime)
    #puertos {path}\Frontend\ConfigFiles\Client.config  tcp middlewareNode
    replacePort(f'{path}/Frontend/STE/ConfigFiles/client.config',
                '<endpoint name="MiddleWareNode" address="net.tcp://localhost:\w*/ApplicationServiceNode/"', 
                f'<endpoint name="MiddleWareNode" address="net.tcp://localhost:{port}01/ApplicationServiceNode/" ',loggin,datetime)
    
#changePort("C:\sidesysT","041") 
    
#replacePort(content,patron, service)
def validatePort(port):
    if(len(port)!=3):return True
    else:return False
#print(validatePort(port))

#Esta funcion es una extencion del modulo portService.py
def replacePort(path,patron, service,loggin,datetime):
    path=path.replace("/", r"\ ".strip())
    print(path)
    content=open(path,"r").read()
    old = re.findall(patron, content)
    print(old[0])
    print(service)
    content=content.replace(old[0],service)
    #print(content)
    open(path,"w").write(content)
    print("Exitoso")
    loggin.info(f' {datetime.datetime.now() }: Ha sido modificado el puerto del archivo {path}')


#validateDirectory("C:\sidesysT","Middleware")
#validateDirectory("C:\sidesysT","MiddlewareNode")
#validateDirectory("C:\sidesysT","FrontEnd")