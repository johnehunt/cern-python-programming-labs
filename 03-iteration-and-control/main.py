import random

# Set up some global 'constants'
MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = 'Please guess a number between ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + ': '

# Set up variables to be used in the game
game_over = False

while not game_over:
    # Initialise the number to be guessed
    number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    # Start the game
    print('Welcome to the number guess game')

    # Obtain their initialise guess
    guess = 0
    while number_to_guess != guess:
        guess = int(input(GUESS_PROMPT))

        # Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if guess == -1:
            print('The number to guess is', number_to_guess)
            continue
        elif count_number_of_tries + 1 == MAX_NUMBER_OF_GUESSES:
            break
        elif guess + 1 == number_to_guess or guess -1 == number_to_guess:
            print('Sorry wrong number - you were out by 1')
        elif guess < number_to_guess:
            print('Sorry wrong number')
            print('Your guess was lower than the number')
        elif guess > number_to_guess:
            print('Sorry wrong number')
            print('Your guess was higher than the number')

        # Obtain their next guess and increment number of attempts
        count_number_of_tries += 1

    # Check to see if they did guess the correct number
    if number_to_guess == guess:
        print('Well done you won!')
        print(f'You took {count_number_of_tries} goes to complete the game')
    else:
        print("Sorry - you loose")
        print(f'The number you needed to guess was {number_to_guess}')

    play_again = input("Do you want to play again? ")
    if play_again.lower() == 'n' or play_again.lower() == 'no':
        game_over = True

print('Game Over')
