# Illustrates creating a history with information
# on the result of each guess i.e. was it higher or lower

import random

# Set up some global 'constants'
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = 'Please guess a number between ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + ': '

# Set up variables to be used in the game
game_over = False

while not game_over:

    # Initialise the history of guesses
    history = []

    # Initialise the number to be guessed
    number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    # Start the game
    print('Welcome to the number guess game')

    # Obtain their initialise guess
    guess = 0
    while number_to_guess != guess and count_number_of_tries != MAX_NUMBER_OF_GUESSES:

        # Set up a message to user variable
        message_to_user = ''

        guess = int(input(GUESS_PROMPT))

        # Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if guess == -1:
            print('The number to guess is', number_to_guess)
            continue
        elif number_to_guess == guess:
            message_to_user = 'Correct Guess'
        elif count_number_of_tries + 1 == MAX_NUMBER_OF_GUESSES:
            message_to_user = 'Max number of guesses made'
        elif guess + 1 == number_to_guess or guess -1 == number_to_guess:
            message_to_user = 'Sorry wrong number - you were out by 1'
        elif guess < number_to_guess:
            message_to_user = "Sorry wrong number\nYour guess was lower than the number"
        elif guess > number_to_guess:
            message_to_user = 'Sorry wrong number\nYour guess was higher than the number'

        print(message_to_user)

        # Add the guess to the history and increment number of attempts
        history.append((guess, message_to_user))

        # Obtain their next guess and increment number of attempts
        count_number_of_tries += 1

    # Check to see if they did guess the correct number
    if number_to_guess == guess:
        print('Well done you won!')
        print(f'You took {count_number_of_tries} goes to complete the game')
    else:
        print("Sorry - you loose")
        print(f'The number you needed to guess was {number_to_guess}')

    # Present the guess history
    print('Your guesses were:')
    print(history)

    total = 0
    lowest_value = 9999
    highest_value = 0
    for item in history:
        total = total + item[0]
        if lowest_value > item[0]:
            lowest_value = item [0]
        if highest_value < item[0]:
            highest_value = item[0]

    print(f'The lowest value entered: {lowest_value}')
    print(f'The highest value entered: {highest_value}')
    print(f'Average value is: {total / len(history)}')


    play_again = input("Do you want to play again? ")
    if play_again.lower() == 'n' or play_again.lower() == 'no':
        game_over = True

print('Game Over')
