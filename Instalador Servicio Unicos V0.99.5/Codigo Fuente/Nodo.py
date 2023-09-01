from funcionesAuxiliares import *
import logging
import datetime
def configurarNodo(path,font,voz,headerColor,footerColor,fontSizeNumber,logging,datetime):
    
    replaceCadenaInSection(path,'"node":{[\S|\s]+"header"','fontFamily":"[\S|\\b|" "]+"', f'fontFamily":"{font}"',logging,datetime)
    replaceCadenaInSection(path,'"node":{[\S|\s]+"header"','voice":"[\S|\\b|" "]+', f'voice":"{voz}"',logging,datetime)
    replaceCadenaInSection(path,'"header":{[\S|\s]+"logo"','backgroundColor":"[\S|\\b|" "]+', f'backgroundColor":"{headerColor}"',logging,datetime)
    replaceCadenaInSection(path,'"footer":{[\S|\s]+"alignContent"','backgroundColor":"[\S|\\b|" "]+', f'backgroundColor":"{footerColor}"',logging,datetime)
    replaceCadenaInSection(path,'"numbersTableBody":{[\S|\s]+"columnTask"','fontSize":"[\S|\\b|" "]+', f'fontSize":"{fontSizeNumber}"',logging,datetime)
    replaceCadenaInSection(path,'"numberNews":{[\S|\s]+"panel"','fontSize":"[\S|\\b|" "]+', f'fontSize":"{fontSizeNumber}"',logging,datetime)
    
#configurarNodo("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\\FrontEnd\STE\\view_configuration\\PROMERICA\\xml\\PROMERICA-vtnodo.xml","font","vASDFDFASLAGSD","hcolor","fcolor", "sizenumber",logging,datetime)    
