import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

age = input("Inserisci la tua età: ")
decades = int(age) // 10
years = int(age) % 10
logger.info(f"Hai vissuto {decades} decadi e {years} anni.")