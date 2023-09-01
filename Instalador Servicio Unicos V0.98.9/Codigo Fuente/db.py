import sqlite3

import logging
import datetime
#1Rojo 2Verde 3Azul
conn=sqlite3.connect("Configuracion.db")


cursor=conn.cursor()
conn.commit()

def getColor(id,field):
    cursor.execute(f'''
    Select {field} from estadoColor as e
    JOIN Frame f on e.frame= f.id
    JOIN Color c on  e.color= c.id
    where f.id={id};
    ''')
    results = cursor.fetchall()
    for row in results:
        print(f"1-{row}")
        return (row[0])
def getIdColor(id,field):
    cursor.execute(f'''
    Select {field} from color
    where descripcion="{id}";
    ''')
    results = cursor.fetchall()
    for row in results:
        #print(f"1-{row}")
        return (row[0])
    
def getColors():
    cursor.execute(f'''
    Select descripcion from color;
    ''')
    results = cursor.fetchall()
    print(results)
    return results
    
def setColor(id,color,loggin,now):
    conn2=sqlite3.connect("Configuracion.db")
    cursor2=conn2.cursor()
    print(f"setColor({id},{color})")
    loggin.info(f"{now}: actualizando la tabla estadoColor en el frame {id} actualiza el valor del campo idColor con {color})")
    cursor2.execute(f'''
    UPDATE estadoColor set color={color} where estadoColor.Frame={id};
    ''')
    conn2.commit()

def setConfiguration(Frame1,Frame2,Frame3,Frame4,Frame5,loggin,now):
    i="id"
    loggin.info(f"{now}: Estableciendo color {Frame1[0]} al frame {Frame1[1]} id del color {getIdColor(Frame1[0],i)}")
    loggin.info(f"{now}: Estableciendo color {Frame2[0]} al frame {Frame2[1]} id del color {getIdColor(Frame2[0],i)}")
    loggin.info(f"{now}: Estableciendo color {Frame3[0]} al frame {Frame3[1]} id del color {getIdColor(Frame3[0],i)}")
    loggin.info(f"{now}: Estableciendo color {Frame4[0]} al frame {Frame4[1]} id del color {getIdColor(Frame4[0],i)}")
    loggin.info(f"{now}: Estableciendo color {Frame5[0]} al frame {Frame5[1]} id del color {getIdColor(Frame5[0],i)}")
    print(f"Estableciendo color {Frame1[0]} al frame {Frame1[1]} id del color {getIdColor(Frame1[0],i)}")
    print(f"Estableciendo color {Frame2[0]} al frame {Frame2[1]} id del color {getIdColor(Frame2[0],i)}")
    print(f"Estableciendo color {Frame3[0]} al frame {Frame3[1]} id del color {getIdColor(Frame3[0],i)}")
    print(f"Estableciendo color {Frame4[0]} al frame {Frame4[1]} id del color {getIdColor(Frame4[0],i)}")
    print(f"Estableciendo color {Frame5[0]} al frame {Frame5[1]} id del color {getIdColor(Frame5[0],i)}")
    setColor(Frame1[1],int(getIdColor(Frame1[0],i)),loggin,now)
    setColor(Frame2[1],int(getIdColor(Frame2[0],i)),loggin,now)
    setColor(Frame3[1],int(getIdColor(Frame3[0],i)),loggin,now)
    setColor(Frame4[1],int(getIdColor(Frame4[0],i)),loggin,now)
    setColor(Frame5[1],int(getIdColor(Frame5[0],i)),loggin,now)

#getColor(4,"codigo")
#setColor(4,4,logging, datetime)

    
