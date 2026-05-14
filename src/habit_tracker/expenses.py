import logging
import random
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)
logger = get_logger(__name__)

number_of_expenses = int(input("Quante spese vuoi inserire? "))

expenses = []
for i in range(number_of_expenses):
    expenses.append(random.uniform(0.01, 500.00))

total_expenses = sum(expenses)

logger.info(f"Le spese totali sono: {total_expenses:.2f} euro.")
