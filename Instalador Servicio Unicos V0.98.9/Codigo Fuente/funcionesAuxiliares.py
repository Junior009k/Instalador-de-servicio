import re 

def show_frame(frame1,frame2):
    frame1.pack_forget()
    frame2.pack()

def show_Configuration(frame1,frame2,frame3,frameC):
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frameC.pack()

def fixWord(word):
    print(word.split("'",2))
    p="'"
    if("('" in word):
        print(f"arreglamos la palabra {word.split(p,2)[1]}")
        return word.split(p,2)[1]
    return word

#Esta funcion es una extencion del modulo portService.py
def replaceCadena(path,patron, service,loggin,datetime):
    try:
        path=path.replace("/", r"\ ".strip())
    
        print(path)
        #print(patron)
        content=open(path,"r").read()
        #print(content)
        print(re.findall(patron, content))
        old = re.findall(patron, content)
        print(old[0])
        print(service)
        content=content.replace(old[0],service)
        #print(content)
        open(path,"w").write(content)
        print("Exitoso")
        loggin.info(f' {datetime.datetime.now() }: Se cambio la cadena de texto {old[0]}')
        loggin.info(f' {datetime.datetime.now() }: por la cadena de texto {service}')
        loggin.info(f' {datetime.datetime.now() }: Ha sido modificado el  archivo {path} de forma exitosa')
    except:
        print("Espacio en blanco detectado")
        loggin.info(f' {datetime.datetime.now() }: El path no ha podido ser cambiado, asegurese que dentro del campo ha modificar no halla espacio en blanco')
#def isEmpty(logging):
 #   if( Textboxdb.get()==""):
 #       logging.error(f' {datetime.datetime.now() }: No se puede modificar los UDLS sin especificar el nombre de la base de datos')
  #      MessageBox.showerror("Error","No se puede modificar los UDLS sin especificar el nombre de la base de datos")
 #       bandera=False