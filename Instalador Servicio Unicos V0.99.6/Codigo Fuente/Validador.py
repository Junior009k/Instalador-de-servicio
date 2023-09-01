import re
from tkinter import messagebox as MessageBox
#Valida los servicios
def validateService(path,servicio, carpeta, subCarpeta):
  print(path)
  print(re.findall(carpeta,path))
  print(re.findall(subCarpeta,path))
  print(re.findall(servicio,path))
  print(path.lower())
  print(carpeta.lower())
  print(subCarpeta.lower())
  print(servicio.lower())
  path=path.lower()
  carpeta=carpeta.lower()
  subCarpeta=subCarpeta.lower()
  servicio=servicio.lower()
  bandera=False
  if(re.findall(carpeta,path) and re.findall(subCarpeta,path) and re.findall(servicio,path)):
    bandera=True
  if(re.findall(carpeta,path)==[] and (re.findall(subCarpeta,path)==[] or re.findall(subCarpeta,path)==[subCarpeta]) and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio])):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {carpeta}") 
    bandera=False
  if(re.findall(carpeta,path)==[carpeta] and re.findall(subCarpeta,path)==[]   and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio])):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {subCarpeta}") 
    bandera=False
  if( re.findall(carpeta,path)==[])and re.findall(subCarpeta,path)==[]   and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio]):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {subCarpeta} ni dentro de la carpeta de {carpeta}") 
    bandera=False
  if(re.findall(carpeta,path)==[carpeta] and re.findall(subCarpeta,path)==[subCarpeta] and re.findall(servicio,path)==[]):
    MessageBox.showerror("Error",f"Usted no esta seleccionando el archivo {servicio}") 
    bandera=False
  return bandera

#validateService("C:\Users\jaquino\OneDrive - Sidesys Srl\Documents\Sidesys\Banco BHD - e-Flow 4.1.3 - Custom 2.0\1. Proceso de Instalacion\Middleware\STE\ConfigFiles","STE","Middleware","ConfigFiles")

