import win32com.client
import re
# Crear una instancia del objeto ADODB.Stream
stream = win32com.client.Dispatch('ADODB.Stream')

# Establecer los atributos del objeto Stream
stream.Type = 2 # Texto
stream.Charset = 'utf-16le'

# Abrir el archivo UDL en modo lectura
stream.Open()
stream.LoadFromFile('SOF.udl')

# Leer el contenido del archivo UDL
content = stream.ReadText(-1)

# Cerrar el objeto Stream
stream.Close()

# Modificar las propiedades de conexión
contentS=content.split('\n',2)[2]
print(contentS)
#1Password 2 n/a 3User id 4 initialcatalog 5Data source 
print(contentS.split(';',4))
print(f"""
       1){contentS.split(';',4)[0]}
       2){contentS.split(';',4)[1]}
       3){contentS.split(';',4)[2]}
       4){contentS.split(';',4)[3]} 
       5){contentS.split(';',4)[4]} 
        """)
new_content = content.replace(contentS.split(';',4)[4], 'Data Source=myNewServerAddress')
new_content = new_content.replace(contentS.split(';',4)[3], 'Initial Catalog=myNewDatabase')
new_content = new_content.replace(contentS.split(';',4)[2], 'User ID=myNewUsername')
new_content = new_content.replace(contentS.split(';',4)[0], 'Password=myNewPassword')
# Abrir el objeto Stream en modo escritura
stream.Open()
stream.WriteText(new_content)

# Guardar el archivo UDL
stream.SaveToFile('SOF.udl', 2) # 2 = overwrite

# Cerrar el objeto Stream
stream.Close()
