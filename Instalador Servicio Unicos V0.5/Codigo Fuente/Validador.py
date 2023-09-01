import re
from tkinter import messagebox as MessageBox
def validarServicioEflow(path,servicio, carpeta, subCarpeta):
  print(re.findall(carpeta,path))
  print(re.findall(subCarpeta,path))
  print(re.findall(servicio,path))
  bandera=False
  if(re.findall(carpeta,path) and re.findall(subCarpeta,path) and re.findall(servicio,path)):
    bandera=True
  if(re.findall(carpeta,path)==[] and (re.findall(subCarpeta,path)==[] or re.findall(subCarpeta,path)==[subCarpeta]) and re.findall(servicio,path)==[]):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {carpeta}") 
    bandera=False
  if(re.findall(carpeta,path)==[carpeta] and re.findall(subCarpeta,path)==[]   and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio])):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {subCarpeta}") 
    bandera=False
  if( re.findall(carpeta,path)==[])and re.findall(subCarpeta,path)==[]   and (re.findall(servicio,path)==[] or re.findall(servicio,path)==[servicio]):
    MessageBox.showerror("Error",f"Usted no esta dentro de la carpeta {subCarpeta} ni dentro de la carpeta de {carpeta}") 
    bandera=False
  if(re.findall(carpeta,path)==[carpeta] and re.findall(subCarpeta,path)==[subCarpeta] and re.findall(servicio,path)==[]):
    MessageBox.showerror("Error",f"Usted no esta seleccionando el sarchivo {servicio}") 
    bandera=False
  return bandera




