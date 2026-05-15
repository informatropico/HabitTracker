import logging
import requests
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

response = requests.get('http://api.open-notify.org/astros.json')

if response.status_code == 200:
    data = response.json()

    print(data)


    logger.info(f"Ci sono attualmente {data['number']} persone nello spazio.")
    for person in data['people']:
        logger.info(f"{person['name']} è a bordo della {person['craft']}.")