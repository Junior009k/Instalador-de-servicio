from funcionesAuxiliares import *

def updatesVirtualQueue(path,uri,MSMQFrontEnd,MSMQMiddleware,loggin,datetime):
    #"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/VirtualQueue/web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/VirtualQueue/web.config','<add name="Default" connectionString="[\S|\\b|" "]+"','connectionString=[\S|\\b|" "]+',f'connectionString={uri}',loggin,datetime)
  
   #"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/VirtualQueue/web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/VirtualQueue/web.config','<add key="IncomingEventsReceiveQueuePath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+"',f'value="{MSMQFrontEnd}"',loggin,datetime)

    #"C:/Entornos/Senasa - 03/PRODUCCION/Middleware/STE/ConfigFiles/VirtualQueue.config"
   replaceCadenaInSection(f'{path}/Middleware/STE/ConfigFiles/VirtualQueue.config','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',f'<OutgoingEventsSendQueuePath>{MSMQMiddleware}</OutgoingEventsSendQueuePath>',loggin,datetime)


#updatesVirtualQueue("C:/Entornos/Senasa - 03/PRODUCCION","uri","MSMQFrontEnd","MSMQMiddleware",logging,datetime)

#VirtualQueue
#identifyBaseURL(f"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/VirtualQueue/web.config",'<add name="Default" connectionString="[\S|\\b|" "]+"','connectionString=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Senasa - 03/PRODUCCION/FrontEnd/VirtualQueue/web.config",'<add key="IncomingEventsReceiveQueuePath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime)
#Identify(f"C:/Entornos/Senasa - 03/PRODUCCION/Middleware/STE/ConfigFiles/VirtualQueue.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime)
