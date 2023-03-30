class Score:
    def __init__(self, value=0):
        self.value = value

    # Define a set of methods to provide operator functionality

    def __add__(self, other):
        new_value = self.value + other.value
        return Score(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Score(new_value)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value * other
        else:
            raise ValueError(f'invalid type {type(other)}')
        return Score(new_value)

    def __pow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value ** other.value
        else:
            raise ValueError(f'invalid type {type(other)}')
        return Score(new_value)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value / other
        else:
            raise ValueError(f'invalid type {type(other)}')
        return Score(new_value)

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value // other.value
        else:
            raise ValueError(f'invalid type {type(other)}')
        return Score(new_value)

    def __mod__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_value = self.value % other.value
        else:
            raise ValueError(f'invalid type {type(other)}')
        return Score(new_value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __str__(self):
        return 'Score[' + str(self.value) + ']'
