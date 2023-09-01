from funcionesAuxiliares import *
import logging
import datetime
import os

# ...
def configurarMail(path,ssl,server,port,senderaccount, password,logging, datetime):
    if(ssl==0):ssl="False"
    if(ssl==1):ssl="True"
    
    #"C:\Sides\MiddleWare\STE\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/STE/ConfigFiles/MailServers.config',
    '<ServerName>[\S|\\b|" "]+</ServerName>',f'<ServerName>{server}</ServerName>',logging,datetime)
    #"C:\Sides\MiddleWare\STE\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/STE/ConfigFiles/MailServers.config',
    '<SSL>[\S|\\b|" "]+</SSL>',f'<SSL>{ssl}</SSL>',logging,datetime)
    #"C:\Sides\MiddleWare\STE\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/STE/ConfigFiles/MailServers.config',
    '<Port>[\S|\\b|" "]+</Port>',f'<Port>{port}</Port>',logging,datetime)
    #"C:\Sides\MiddleWare\STE\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/STE/ConfigFiles/MailServers.config',
    '<SenderAccount>[\S|\\b|" "]+</SenderAccount>',f'<SenderAccount>{senderaccount}</SenderAccount>',logging,datetime)
    #"C:\Sides\MiddleWare\STE\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/STE/ConfigFiles/MailServers.config',
    '<UserName>[\S|\\b|" "]+</UserName>',f'<UserName>{senderaccount}</UserName>',logging,datetime)
    #"C:\Sides\MiddleWare\STE\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/STE/ConfigFiles/MailServers.config',
    '<Password>[\S|\\b|" "]+</Password>',f'<Password>{password}</Password>',logging,datetime)
    
    #"C:\Sides\MiddleWare\Appointment\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/Appointment/ConfigFiles/MailServers.config',
    '<ServerName>[\S|\\b|" "]+</ServerName>',f'<ServerName>{server}</ServerName>',logging,datetime)
    #"C:\Sides\MiddleWare\Appointment\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/Appointment/ConfigFiles/MailServers.config',
    '<SSL>[\S|\\b|" "]+</SSL>',f'<SSL>{ssl}</SSL>',logging,datetime)
    #"C:\Sides\MiddleWare\Appointment\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/Appointment/ConfigFiles/MailServers.config',
    '<Port>[\S|\\b|" "]+</Port>',f'<Port>{port}</Port>',logging,datetime)
    #"C:\Sides\MiddleWare\Appointment\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/Appointment/ConfigFiles/MailServers.config',
    '<SenderAccount>[\S|\\b|" "]+</SenderAccount>',f'<SenderAccount>{senderaccount}</SenderAccount>',logging,datetime)
    #"C:\Sides\MiddleWare\Appointment\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/Appointment/ConfigFiles/MailServers.config',
    '<UserName>[\S|\\b|" "]+</UserName>',f'<UserName>{senderaccount}</UserName>',logging,datetime)
    #"C:\Sides\MiddleWare\Appointment\ConfigFiles\MailServers.config"
    replaceCadena(f'{path}/MiddleWare/Appointment/ConfigFiles/MailServers.config',
    '<Password>[\S|\\b|" "]+</Password>',f'<Password>{password}</Password>',logging,datetime)
    
#configurarMail("C:\Sides",1,"192.168.104.92","545","junior009k@gmail.com","123456",logging, datetime)

#configurarMail("C:\SidesysCitas",1,"192.168.104.92","545","junior009k@gmail.com","123456",logging, datetime)
