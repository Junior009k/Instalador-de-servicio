import requests
import json

async def make_request():
    # Hacer la solicitud HTTP
    response = await requests.get('https://ejemplo.com/api/data')
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Obtener los datos JSON de la respuesta
        data = response.json()
        
        # Trabajar con los datos obtenidos
        for item in data['results']:
            print('Nombre:', item['nombre'])
            print('Edad:', item['edad'])
            print('Email:', item['email'])
            print('---')
    else:
        print('Error en la solicitud:', response.status_code)

# Ejecutar la solicitud de forma asíncrona
asyncio.run(make_request())