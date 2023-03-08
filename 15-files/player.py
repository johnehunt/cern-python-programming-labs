# Module used to define player class
from datetime import date
from datetime import datetime

from constants import MIN_VALUE, MAX_VALUE, GUESS_PROMPT

print('Loading Player Information')


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


class Score:
    def __init__(self, value):
        self.value = value
        self.today = date.today()
        self.time = datetime.now()

    def __add__(self, other):
        return Score(self.value + other.value)

    def __sub__(self, other):
        return Score(self.value - other.value)

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


class Player:
    """ Class to represent a player within the number guess game """

    def __init__(self, name):
        self.name = name
        self.guess_count = 0
        self.history = []

    def __repr__(self):
        return f'Player {self.name} - history {self.history}'

    def increment_count(self):
        self.guess_count = self.guess_count + 1

    def add_guess(self, guess):
        self.history.append(guess)

    def print_history(self):
        formatted_history = list(map(lambda guess: f'\t guess: {guess}', self.history))
        for guess in formatted_history:
            print(guess)

    def make_a_guess(self):
        guess = get_user_guess(GUESS_PROMPT)
        if guess != -1:
            self.increment_count()
        return guess

    # Implement the length Protocol
    def __len__(self):
        return len(self.history)

    # Makes this class Iterable
    def __iter__(self):
        return self.history.__iter__()
