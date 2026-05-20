import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

file_path = "src\\resources\\acron.txt"

def find_acronym(look_up = None):
    if look_up is None:
        look_up = input("Inserisci un acronimo da cercare: ")
    try:
        with open(file_path, "r") as file:
            for line in file:
                if look_up in line:
                    return line.strip()
        return None
    except FileNotFoundError:
        logger.error("File non trovato.")
        return   

def add_acronym():
    acronym = input("Inserisci un acronimo da inserire: ")
    meaning = input("Inserisci il significato dell'acronimo: ")
    
    if not find_acronym(acronym):
        with open(file_path, "a") as file:
            file.write(f"{acronym} - {meaning}\n")
            return True
    else:
        logger.warning(f"Acronimo '{acronym}' già presente nel file.")
        return False

def main():
    result = add_acronym()
    if result:
        logger.info("Acronimo aggiunto con successo.")
    
    result = find_acronym()
    if result:
        logger.info(f"Acronimo trovato: {result}")
    else:
        logger.warning("Acronimo non trovato.")

if __name__ == "__main__":
    main()