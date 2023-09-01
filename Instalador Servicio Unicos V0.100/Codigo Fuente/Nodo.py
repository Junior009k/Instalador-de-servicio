from funcionesAuxiliares import *
import logging
import datetime
def configurarNodo(path,font,voz,headerColor,footerColor,fontSizeNumber,lang,W,UW,NumberHeaderColor,NumberHeaderSize,NumberHeaderFontColor,bannerBColor, bannerFColor,logging,datetime):
    
    replaceCadenaInSection(path,'"node":{[\S|\s]+"header"','fontFamily":"[\S|\\b|" "]+"', f'fontFamily":"{font}"',logging,datetime)
    replaceCadenaInSection(path,'"node":{[\S|\s]+"header"','voice":"[\S|\\b|" "]+', f'voice":"{voz}"',logging,datetime)
    replaceCadenaInSection(path,'"header":{[\S|\s]+"logo"','backgroundColor":"[\S|\\b|" "]+', f'backgroundColor":"{headerColor}"',logging,datetime)
    replaceCadenaInSection(path,'"footer":{[\S|\s]+"alignContent"','backgroundColor":"[\S|\\b|" "]+', f'backgroundColor":"{footerColor}"',logging,datetime)
    replaceCadenaInSection(path,'"numbersTableBody":{[\S|\s]+"columnTask"','fontSize":"[\S|\\b|" "]+', f'fontSize":"{fontSizeNumber}"',logging,datetime)
    replaceCadenaInSection(path,'"numberNews":{[\S|\s]+"panel"','fontSize":"[\S|\\b|" "]+', f'fontSize":"{fontSizeNumber}"',logging,datetime)
    replaceCadenaInSection(path,'"node":{[\S|\s]+"header"','lang":"[\S|\\b|" "]+"',f'lang":"{lang}"',logging,datetime)
    replaceCadenaInSection(path,'"header":{[\S|\s]+"text"','width":"[\S|\\b|" "]+"',f'width":"{W}"',logging,datetime)
    replaceCadenaInSection(path,'"header":{[\S|\s]+"text"','unitWidth":"[\S|\\b|" "]+"',f'unitWidth":""{UW}""',logging,datetime)
    replaceCadenaInSection(path,'"numbersTableHeader":{[\S|\s]+"columnTask"','backgroundColor":"[\S|\\b|" "]+"',f'backgroundColor":"{NumberHeaderColor}"',logging,datetime)
    replaceCadenaInSection(path,'"numbersTableHeader":{[\S|\s]+"columnTask"','fontSize":"[\S|\\b|" "]+"',f'fontSize":"{NumberHeaderSize}"',logging,datetime)
    replaceCadenaInSection(path,'"numbersTableHeader":{[\S|\s]+"columnTask"','fontColor":"[\S|\\b|" "]+"',f'fontColor":"{NumberHeaderFontColor}"',logging,datetime)
    replaceCadenaInSection(path,'"banner":{[\S|\s]+"fontColor"','backgroundColor":"[\S|\\b|" "]+"',f'backgroundColor":"{bannerBColor}"',logging,datetime)
    replaceCadenaInSection(path,'"banner":{[\S|\s]+}','fontColor":"[\S|\\b|" "]+"',f'fontColor":"{bannerFColor}"',logging,datetime)
#configurarNodo("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\\FrontEnd\STE\\view_configuration\\PROMERICA\\xml\\PROMERICA-vtnodo.xml","font","vASDFDFASLAGSD","hcolor","fcolor", "sizenumber",logging,datetime)    
#IdentifyJSON("C:\\Entornos\\Banco Promerica - 01\\PRODUCCION\\FrontEnd\STE\\view_configuration\\PROMERICA\\xml\\PROMERICA-vtnodo.xml",'"numbersTableHeader":{[\S|\s]+"columnTask"','fontSize":"[\S|\\b|" "]+',logging,datetime)