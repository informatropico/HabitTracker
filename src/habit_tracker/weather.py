import logging
import requests
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

city = input("Inserisci il nome di una città per conoscere le condizioni meteorologiche: ")

if city and city.strip():
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?key=5934c0cf258e46df80385357261505&q={city}&aqi=no').json()

    if response.get('error'):
        logger.warning(f"Errore: {response['error']['message']}")
        exit()
    
    location = response.get('location', {})
    temp_c = response.get('current', {}).get('temp_c')
    condition = response.get('current', {}).get('condition', {}).get('text')

    if temp_c and condition:
        logger.info(f"Ho trovato: {location.get('name')}, {location.get('country')}")
        logger.info(f"Le condizioni meteorologiche a {city} sono: {temp_c}°C con {condition}.")
    else:
        logger.warning(f"Non sono riuscito a recuperare le condizioni meteorologiche per {location.get('name')}.")
else:
    logger.warning("Non hai inserito il nome di una città.")