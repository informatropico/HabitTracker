import random
import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

computer_wins = 0
user_wins = 0

for _ in range(5):
    computer_choice = random.choice(["rock", "paper", "scissor"])
    user_choice = input("Scegli tra rock, paper o scissor: ").lower()

    if user_choice == computer_choice:
        logger.info(f"Pareggio! Entrambi avete scelto {user_choice}.")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissor" and computer_choice == "paper"):
        logger.info(f"Hai vinto! Hai scelto {user_choice} e il computer ha scelto {computer_choice}.")
        user_wins += 1
    else:
        logger.info(f"Hai perso! Hai scelto {user_choice} e il computer ha scelto {computer_choice}.")
        computer_wins += 1

logger.info(f"Risultato finale - Utente: {user_wins}, Computer: {computer_wins}")

if user_wins > computer_wins:
    logger.info("Complimenti, hai vinto la partita!")
elif computer_wins > user_wins:
    logger.info("Mi dispiace, hai perso la partita!")
else:
    logger.info("La partita è finita in pareggio!")