import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

def read_acronyms_with_dict(file_path: str, look_up: str):
    with open(file_path, "r") as file: # mode "a" per appendere al file esistente, "w" per sovrascrivere, "r" per leggere
        # Legge tutto il contenuto del file e lo divide in linee (potrebbe essere oneroso per file grandi)
        lines = file.readlines() # or with open("src\\resources\\acron.txt") as file: for line in file:
        acronyms = {}
        for line in lines: # or for line in file:
            line = line.strip()
            if line:
                parts = line.split("-")
                if len(parts) == 2:
                    acronym = parts[0].strip()
                    meaning = parts[1].strip()
                    acronyms[acronym] = meaning

    return acronyms.get(look_up)

def read_acronyms_efficiently(file_path: str, look_up: str):
    with open(file_path, "r") as file: # mode "a" per appendere al file esistente, "w" per sovrascrivere, "r" per leggere
        for line in file:
            if look_up in line:
                return line.strip()
    return None

def main():
    look_up = input("Inserisci un acronimo da cercare: ")
    file_path = "src\\resources\\acron.txt"
    meaning = read_acronyms_with_dict(file_path, look_up)
    if meaning:
        logger.info(f"Il significato di '{look_up}' è: {meaning}")
    else:
        logger.warning(f"Acronimo '{look_up}' non trovato.")    
    
    meaning_efficient = read_acronyms_efficiently(file_path, look_up)
    if meaning_efficient:
        logger.info(f"Il significato di '{look_up}' (ricerca efficiente) è: {meaning_efficient}")
    else:        
        logger.warning(f"Acronimo '{look_up}' non trovato (ricerca efficiente).")


if __name__ == "__main__":
    main()

   