from funcionesAuxiliares import *
import logging
import datetime

def configurarNCache(path,server,cache,loggin,datetime): 
    #"C:\Sides\Frontend\STE\ConfigFiles\ServiceBus.NCache.config""
    replaceCadena(f'{path}/FrontEnd/STE/ConfigFiles/ServiceBus.NCache.config',
                'ServerName="\S+"', 
                f'ServerName="{server}"',loggin,datetime)
    #"C:\Sides\Frontend\STE\ConfigFiles\ServiceBus.NCache.config""
    replaceCadena(f'{path}/FrontEnd/STE/ConfigFiles/ServiceBus.NCache.config',
                'CacheName ="\S+"', 
                f'CacheName ="{cache}"',loggin,datetime)

   #""C:\Sides\MiddleWare\STE\bin\ServiceBus.NCache.config"""
    replaceCadena(f'{path}/MiddleWare/STE/bin/ServiceBus.NCache.config',
                 'ServerName="\S+"', 
                f'ServerName="{server}"',loggin,datetime)
    
    #""C:\Sides\MiddleWare\STE\bin\ServiceBus.NCache.config"""
    replaceCadena(f'{path}/MiddleWare/STE/bin/ServiceBus.NCache.config',
                'CacheName ="\S+"', 
                f'CacheName ="{cache}"',loggin,datetime)
#configurarNCache("C:\Sides","192.168.104.42","myC5654he",logging,datetime)

