import logging
import datetime

logging.basicConfig(filename=f'Logs\event {datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')