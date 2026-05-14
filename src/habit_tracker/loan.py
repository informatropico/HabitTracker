import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)
logger = get_logger(__name__)

money_owed = float(input("Quanto denaro devi restituire? ")) # Inserisci l'importo che devi restituire
logger.info(f"Devi restituire {money_owed:.2f} euro.")

apr = float(input("Qual è il tasso di interesse annuale (in percentuale)? ")) # Inserisci il tasso di interesse annuale
logger.info(f"Il tasso di interesse annuale è {apr:.2f}%.")

payment = float(input("Quanto puoi pagare ogni mese? ")) # Inserisci l'importo che puoi pagare ogni mese
logger.info(f"Puoi pagare {payment:.2f} euro ogni mese.")

monthly_rate = (apr / 100) / 12
months = 0

while money_owed > payment:
    interest = money_owed * monthly_rate
    money_owed += interest
    money_owed -= payment
    months += 1
    logger.debug(f"Mese {months}: Interesse = {interest:.2f}, Denaro pagato = {payment:.2f}, Denaro dovuto = {money_owed:.2f}")

last_interest = money_owed * monthly_rate
last_payment = money_owed + last_interest
money_owed += last_interest
money_owed -= last_payment
logger.info(f"Mese {months + 1}: Interesse = {last_interest:.2f}, Denaro pagato = {last_payment:.2f}, Denaro dovuto = {money_owed:.2f}")

logger.info(f"Il prestito sarà restituito in {months + 1} mesi.")
