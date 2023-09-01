import re 
from script import * 

def show_frame(frame1,frame2):
    frame1.pack_forget()
    frame2.pack()
def show_Configuration(frame1,frame2,frame3,frame4,frame5,frameMenuPrincipal,frameC):
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frameMenuPrincipal.pack_forget()
    frameC.pack()

def fixWord(word):
    print(word.split("'",2))
    p="'"
    if("('" in word):
        print(f"arreglamos la palabra {word.split(p,2)[1]}")
        return word.split(p,2)[1]
    return word

#Esta funcion se encargara de reemplazar la cadena de texto
def replaceCadena(path,patron, service,loggin,datetime):
    #Loggin para capturar la ruta del archivo a reemplazar
    loggin.info(f' {datetime.datetime.now() }: Se comienza a modificar el  archivo {path}')
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())
        
        #imprime la ruta y el patron:PRUEBA
        print(path)
        print(patron)
        
        #abre el archivo solo para lectura, indicandolo con la "r"
        content=open(path,"r").read()
        #print(content)

        #imprime el resultado del findall, esto es para saber si logro encontrar el patron en el contenido 
        print(re.findall(patron, content))
        #Almacena ese valor en la variable, old, para saber el valor antiguo
        old = re.findall(patron, content)
        
        #Imprime el antiguo valor y el valor por el cual se reemplazara
        print(old[0])
        print(service)

        #redefinimos el nuevo contenido del archivo, reemplazando el antiguo valor por el nuevo
        content=content.replace(old[0],service)
        
        #un print del contenido, al ser tan extenso no se recomienda usarlo 
        #print(content)
        #Se vuelve abrir el archivo pero esta vez con permiso de escritura
        #tener cuidado ya que esto sobreescribe el documento seleccionado.
        open(path,"w").write(content)

        #Si el proceso sale exitoso, se imprime "exitoso" y captura la ruta, nombre del antiguo y nuevo texto reemplazarlo  
        print("Exitoso")
        loggin.info(f' {datetime.datetime.now() }: Ha sido modificado el  archivo {path} de forma exitosa')
        loggin.info(f' {datetime.datetime.now() }: Se cambio la cadena de texto {old[0]}')
        loggin.info(f' {datetime.datetime.now() }: por la cadena de texto {service}')
    except:
        #si ocurre una excepcion, se imprimira esto
        print("Espacio en blanco detectado")
        loggin.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')


#Esta funcion se encarga de remplazar un patron de un nombre con un nombre especifico en una seccion especifica
def replaceCadenaInSection(path,patron,SecondPatron, service,loggin,datetime):
    #Loggin para capturar la ruta del archivo a reemplazar
    loggin.info(f' {datetime.datetime.now() }: Se comienza a modificar el  archivo {path}')

    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:

        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #imprime la ruta y el patron:PRUEBA
        print(path)
        #print(patron)

        #Abre el documento, especificado en la ruta(path)
        content=open(path,"r").read()

        #imprime el contenido del archivo y el resultado de la busqueda del patron en el contenido:PRUEBA
        #print(content)
        #print(re.findall(patron, content))

        #Almacena ese valor en la variable, old, para saber el valor antiguo
        old = re.findall(patron, content)
        
        #Imprime el valor antiguo
        #print(old[0])

        #Realmacenar  el valor de la segunda busquedad del patron, pero esta vez buscara no en el archivo sino en la seccion anteriormente almacenada
        old=re.findall(SecondPatron, old[0])
        
        #Imprime el antiguo valor y el valor por el cual se reemplazara
        print(old[0])
        print(service)

        #redefinimos el nuevo contenido del archivo, reemplazando el antiguo valor por el nuevo
        content=content.replace(old[0],service)

        #un print del contenido, al ser tan extenso no se recomienda usarlo 
        #print(content)
        #Se vuelve abrir el archivo pero esta vez con permiso de escritura
        #tener cuidado ya que esto sobreescribe el documento seleccionado.
        open(path,"w").write(content)
        
        #Si el proceso sale exitoso, se imprime "exitoso" y captura la ruta, nombre del antiguo y nuevo texto reemplazarlo  
        print("Exitoso")
        loggin.info(f' {datetime.datetime.now() }: Ha sido modificado el  archivo {path} de forma exitosa')
        loggin.info(f' {datetime.datetime.now() }: Se cambio la cadena de texto {old[0]}')
        loggin.info(f' {datetime.datetime.now() }: por la cadena de texto {service}')
        
    except Exception as e:
        #si ocurre una excepcion, se imprimira esto_
        print(f"Espacio en blanco detectado {e}")
        loggin.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')

def Identify(path,patron,secondPatron, logging, datetime):
    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #Imprime la ruta del archivo
        print(path)

        #abre el archivo solo como lectura
        content=open(f"{path}","r").read()

        #imprime el contenido
        #print(content)

        #asigna el patron encontrado a la variable patron 
        patron=re.findall(f'{patron}' , content)

        #imprime el patron
        print(patron)

        #Una vez idemtificado el patron, este lo divide en tres string 
        #[String1>][PATRON][<String2]
        patron=re.findall(f"{secondPatron}",patron[0])[0].split(">",3)[1].split("<",2)[0]
        #patron=re.findall(f"{secondPatron}",patron[0])[0].split('"',3)[1].split('"',2)[0]
        print(patron)
        return patron
    except Exception as e:
        print(f"Espacio en blanco detectado: {e}")
        logging.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')
def IdentifyJSON(path,patron,secondPatron, logging, datetime):
    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #Imprime la ruta del archivo
        print(path)

        #abre el archivo solo como lectura
        content=open(f"{path}","r").read()

        #imprime el contenido
        #print(content)
        print(secondPatron)
        #asigna el patron encontrado a la variable patron 
        patron=re.findall(f'{patron}' , content)

        #imprime el patron
        print(patron)

        #Una vez idemtificado el patron, este lo divide en tres string 
        #[String1:][PATRON][,String2]
        patron=re.findall(f"{secondPatron}",patron[0])[0].split(":",2)[1].split(",",2)[0].strip()
        
        #imprime el patron
        print(patron)

        #Retorna el patron
        return patron
    except Exception as e:
        print(f"Espacio en blanco detectado: {e}")
        logging.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')
def identifyBaseURL(path,patron,secondPatron, logging, datetime):
    #Se abre el try, ya que puede dar problema al usar old[0], esta excepcion se produce cuando no logra encontrar el patron 
    try:
        #remplaza el / por el \, y eliminina el espacion
        path=path.replace("/", r"\ ".strip())

        #Imprime la ruta del archivo
        print(path)

        #abre el archivo solo como lectura
        content=open(f"{path}","r").read()

        #imprime el contenido
        #print(content)

        #asigna el patron encontrado a la variable patron 
        patron=re.findall(f'{patron}' , content)

        #imprime el patron
        print(patron)

        #Una vez idemtificado el patron, este lo divide en tres string 
        #[String1>][PATRON][<String2]
        #patron=re.findall(f"{secondPatron}",patron[0])[0].split(">",3)[1].split("<",2)[0]
        patron=re.findall(f"{secondPatron}",patron[0])[0].split('"',3)[1].split('"',2)[0]
        print(patron)
        return patron
    except Exception as e:
        print(f"Espacio en blanco detectado: {e}")
        logging.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')
def loadImagen(img,PI,loggin, datetime):
    try:
        return PI(file=img)
    except Exception as e:
        loggin.info(f' {datetime.datetime.now() }: No se ha encontrado la img {img}')
        loggin.info(f' {datetime.datetime.now() }: {e}')

def Insert(tb,function,loggin,datetime):
    try:
        tb.insert(0,function)
    except Exception as e:
        loggin.error(f' {datetime.datetime.now() }: No se ha cargado el dato')
        loggin.error(f' {datetime.datetime.now() }: {e}')

#def isEmpty(logging):
 #   if( Textboxdb.get()==""):
 #       logging.error(f' {datetime.datetime.now() }: No se puede modificar los UDLS sin especificar el nombre de la base de datos')
  #      MessageBox.showerror("Error","No se puede modificar los UDLS sin especificar el nombre de la base de datos")
 #       bandera=False
