import logging
import random
from habit_tracker.logger import get_logger

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_round():
    roll1 = roll_dice()
    roll2 = roll_dice()
    return roll1, roll2

def round_winner(roll1, roll2):
    if roll1 > roll2:
        return "Player 1 wins!"
    elif roll2 > roll1:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

def game():
    rounds = {}
    for i in range(1,5):
        roll1, roll2 = play_round()
        rounds[f'Round {i}'] = (roll1, roll2, round_winner(roll1, roll2))
        print(rounds)
    return rounds

def game_winner(rounds):
    player1_wins = sum(1 for round in rounds.values() if round[2] == "Player 1 wins!")
    player2_wins = sum(1 for round in rounds.values() if round[2] == "Player 2 wins!")

    if player1_wins > player2_wins:
        return "Player 1 is the overall winner!"
    elif player2_wins > player1_wins:
        return "Player 2 is the overall winner!"
    else:
        return "The game is a tie!"

def print_game_results(rounds, logger):
    for round, result in rounds.items():
        logger.info(f"{round}: Player 1 rolled {result[0]}, Player 2 rolled {result[1]} - {result[2]}")

    logger.info(game_winner(rounds))

def main():
    logging.getLogger().setLevel(logging.DEBUG)

    logger = get_logger(__name__)

    player1 = input("Giocatore 1, inserisci il tuo nome: ")
    player2 = input("Giocatore 2, inserisci il tuo nome: ")
    logger.info(f"{player1} vs {player2} - Inizia il gioco dei dadi!")

    game_results = game()
    print_game_results(game_results, logger)

main()