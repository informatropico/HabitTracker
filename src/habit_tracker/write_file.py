import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

acronym = input("Inserisci un acronimo da inserire: ")
meaning = input("Inserisci il significato dell'acronimo: ")
file_path = "src\\resources\\acron.txt"

with open(file_path, "a") as file: # mode "a" per appendere al file esistente, "w" per sovrascrivere, "r" per leggere
    file.write(f"{acronym} - {meaning}\n")