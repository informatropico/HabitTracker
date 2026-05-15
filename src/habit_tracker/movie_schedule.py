import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

current_movies = { 'The Grinch': ['11:00am', '2:00pm', '5:00pm'],
                   'The Polar Express': ['12:00pm', '3:00pm', '6:00pm'],
                   'Elf': ['1:00pm', '4:00pm', '7:00pm'],
                   'Home Alone': ['10:00am', '1:00pm', '4:00pm'],
                   'A Christmas Carol': ['11:30am', '2:30pm', '5:30pm'],
                   'The Nightmare Before Christmas': ['12:30pm', '3:30pm', '6:30pm'],
                   'The Gladiator': ['1:30pm', '4:30pm', '7:30pm'],
                   'The Lion King': ['10:30am', '1:30pm', '4:30pm'],
                   'The Lord of the Rings': ['11:15am', '2:15pm', '5:15pm'],
                   'The Matrix': ['12:15pm', '3:15pm', '6:15pm'] }

logger.info("Ecco i film attualmente in programmazione:")

# Itera sui film e stampa i loro titoli (for movie in current_movies.items() per ottenere anche gli orari)
for movie in current_movies: 
    logger.info(f"{movie}")

movie_choice = input("Scegli un film dalla lista: ")

if movie_choice in current_movies:
    logger.info(f"Orari disponibili per {movie_choice}: {', '.join(current_movies[movie_choice])}")
else:
    logger.warning(f"{movie_choice} non è in programmazione.")