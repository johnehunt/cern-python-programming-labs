from os import path

from constants import LOWSCORE_FILENAME, DEFAULT_MAX_GUESS


def load_highscore():
    guess_count = DEFAULT_MAX_GUESS
    if path.isfile(LOWSCORE_FILENAME):
        with open(LOWSCORE_FILENAME, 'r') as file:
            input_string = file.readline()
            guess_count = int(input_string)
    print('The current best guess count is', guess_count)
    return guess_count


def check_highscore_update(best_guess_count, player):
    if player.guess_count < best_guess_count:
        print(player.name, 'you have the current best guess count')
        with open(LOWSCORE_FILENAME, 'w') as file:
            file.write(str(player.guess_count))
