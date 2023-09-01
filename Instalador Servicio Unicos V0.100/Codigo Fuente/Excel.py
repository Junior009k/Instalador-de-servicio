import re

import pandas as pd


# Datos de ejemplo (puedes reemplazar estos datos con tus propios datos)
def registrarReporte(path,eflow,citas,encuesta, datetime, logging):
    print(path)
    logging.info(f' {datetime.datetime.now() }: Se comienza la exportacion del excel en la siguiente ruta {path}')
    logging.info(f' {datetime.datetime.now() }: Datos exportado {eflow}')
    logging.info(f' {datetime.datetime.now() }: Datos exportado {citas}')
    logging.info(f' {datetime.datetime.now() }: Datos exportado {encuesta}')
    
    
    data = {
        'Sistema': ['version', 'nombre', 'Estado', 'Inicio', 'ruta'],
        'e-Flow':  eflow,
        'Citas':citas,
        'Encuesta':encuesta,
        
    }
    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(data)
    # Exportar el DataFrame al archivo de Excel
    df.to_excel(path, index=False)
    logging.info(f' {datetime.datetime.now() }: Los datos han sido exportados a {path}')