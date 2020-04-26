""" Model for aircraft flights"""
from pprint import pprint as pp
class Flight:

    def __init__(self, number):
        # Checking the Class-Invariant : Truth about the object that endure for the life of the object
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

class Aircraft:
    """ To know the type of Aircraft for seating bookings"""
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        # In production code validate if the seats and rows are not negative.
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        # Returns a tuple containing the range to iterate over the rows, and a string of seats for column (seat label)
        return (range(1,self._num_rows+1),"ABCDEFGHJK"[:self._num_seats_per_row])



a1 = Aircraft("G-EUPT","Airbus A319", num_rows=22, num_seats_per_row=6)
print(f"Model is : {a1.model()}")

print(f"Registration of aircraft : {a1.registration()}")

print(f"Seating plan is : {a1.seating_plan()}")


"""Output:

Model is : Airbus A319
Registration of aircraft : G-EUPT
Seating plan is : (range(1, 23), 'ABCDEF')


"""
