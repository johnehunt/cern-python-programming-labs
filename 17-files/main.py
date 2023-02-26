import random
import traceback
from functools import reduce

from constants import MIN_VALUE, MAX_VALUE, MAX_NUMBER_OF_GUESSES, GUESS_PROMPT
from utils import get_user_yes_or_no
from player import Player
from file_utils import load_highscore, check_highscore_update

# Set up global variables
# Low score dictionary
low_score_dictionary = {}
# current player
current_player = None
# Best guess global
best_guess_count = None


class NumberGuessGameException(Exception):
    """ Class representing errors in the number guess game"""

    def __init__(self, msg):
        super().__init__(msg)


def welcome_message():
    print('Welcome to the number guess game')


def display_instructions():
    response = get_user_yes_or_no('Do you want to see the instructions?: ')
    if response == 'y':
        print(GUESS_PROMPT)
        print("You can play as many times as you like")


def game_over_message():
    print('Game Over')
    print('Low Score table:')
    for key in low_score_dictionary:
        print(f'\t{key.name} = {low_score_dictionary[key]}')

    print('-' * 25)
    analyse_low_score_table()


def check_current_user():
    global current_player
    check_new_user = 'n'
    if current_player is not None:
        user_prompt = f'The current user is {current_player.name}, do you wish to enter a new name (y/n): '
        check_new_user = input(user_prompt).lower()

    if check_new_user == 'y' or current_player is None:
        name = input('Please input your name: ')
        if name == '':
            raise NumberGuessGameException('Invalid Name')
        current_player = Player(name)


def get_user_guess(prompt):
    user_input_int = None
    invalid_input = True
    while invalid_input:
        user_input = input(prompt)
        if user_input == '-1':
            return -1
        if not user_input.isdigit():
            print('Input must be a positive number')
        else:
            user_input_int = int(user_input)
            if user_input_int < MIN_VALUE or user_input_int > MAX_VALUE:
                print(f'Number must be in range {MIN_VALUE} and {MAX_VALUE}')
            else:
                invalid_input = False
    return user_input_int


def update_low_score_table(user, count_number_of_tries):
    previous_low_score = low_score_dictionary.get(user, 1000)
    if previous_low_score > count_number_of_tries:
        low_score_dictionary[current_player] = count_number_of_tries


def analyse_low_score_table():
    low_score_length = len(low_score_dictionary)
    print(f'Number of scores in low score table: {low_score_length}')
    func = lambda total, item: total + item[1]
    low_score_total = reduce(func, low_score_dictionary.items(), 0)
    low_score_average = low_score_total / low_score_length
    print(f'Average of low scores: {low_score_average}')
    # Filter scores
    scores_above_three = list(filter(lambda item: item[1] > 2, low_score_dictionary.items()))
    print(f'Scores above 3 {scores_above_three}')
    scores_in_ascending_order = sorted(low_score_dictionary.items(), key=lambda item: item[1])
    print(f'Scores in ascending order {scores_in_ascending_order}')
    scores_in_descending_order = sorted(low_score_dictionary.items(),
                                        reverse=True,
                                        key=lambda item: item[1])
    print(f'Scores in descending order {scores_in_descending_order}')
    # chain HOF for filter and sorting
    scores_in_ascending_order_above_three = sorted(filter(lambda item: item[1] > 2, low_score_dictionary.items()),
                                                   key=lambda item: item[1])
    print(f'Scores in ascending order above three {scores_in_ascending_order_above_three}')
    scores_in_descending_order_above_three = sorted(filter(lambda item: item[1] > 2, low_score_dictionary.items()),
                                                    reverse=True,
                                                    key=lambda item: item[1])
    print(f'Scores in descending order above three {scores_in_descending_order_above_three}')


def play_game():
    best_guess_count = load_highscore()

    # Set up main game loop variable
    game_over = False
    while not game_over:

        # Initialise the number to be guessed
        number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

        # display instructions if required
        display_instructions()
        # Check the current user setting
        check_current_user()

        # Initialise the players history of guesses
        current_player.history = []

        # Obtain their initialise guess
        guess = 0
        while number_to_guess != guess and current_player.guess_count != MAX_NUMBER_OF_GUESSES:

            # Set up a message to user variable
            message_to_user = ''

            guess = current_player.make_a_guess()

            # Check to see they have not exceeded the maximum
            # number of attempts if so break out of loop otherwise
            # give the user come feedback
            if guess == -1:
                print('The number to guess is', number_to_guess)
                continue
            elif number_to_guess == guess:
                message_to_user = 'Correct Guess'
            elif current_player.guess_count == MAX_NUMBER_OF_GUESSES:
                message_to_user = 'Max number of guesses made'
            elif guess + 1 == number_to_guess or guess - 1 == number_to_guess:
                message_to_user = 'Sorry wrong number - you were out by 1'
            elif guess < number_to_guess:
                message_to_user = "Sorry wrong number\nYour guess was lower than the number"
            elif guess > number_to_guess:
                message_to_user = 'Sorry wrong number\nYour guess was higher than the number'

            print(message_to_user)

            # Add the guess to the history and increment number of attempts
            current_player.add_guess((guess, message_to_user))

        # Check to see if they did guess the correct number
        if number_to_guess == guess:
            print('Well done you won!')
            print(f'You took {current_player.guess_count} goes to complete the game')
            check_highscore_update(best_guess_count, current_player)
        else:
            print("Sorry - you loose")
            print(f'The number you needed to guess was {number_to_guess}')

        update_low_score_table(current_player.name, current_player.guess_count)

        # Present the guess history
        print('Your guesses were:')
        # current_player.print_history()
        for guess in current_player:
            print(guess)

        # Print the length fo the player
        print('The length of the player history is', len(current_player))

        play_again = input("Do you want to play again? ")
        if play_again.lower() == 'n' or play_again.lower() == 'no':
            game_over = True


def main():
    try:
        welcome_message()
        play_game()
        game_over_message()
    except NumberGuessGameException as exp:
        print('A problem was encountered within the program')
        print(exp)
        # printing stack trace
        traceback.print_exc()


if __name__ == "__main__":
    main()
