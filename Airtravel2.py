# Law of Delimeter: Never call methods on objects returned from the other calls.

""" Model for aircraft flights"""
from pprint import pprint as pp
class Flight:
    """A flight wiht a particular passenger aircraft"""
    def __init__(self, number, aircraft):
        # Checking the Class-Invariant : Truth about the object that endure for the life of the object
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()  # Directly get the aircraft model, rather than reach through Flight and delgate aircraft object directly. Another way\
                                       # of doing this is f1._aircraft.model()


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


f1 = Flight("BA758",Aircraft("G-EUPT","Airbus A319", num_rows=22, num_seats_per_row=6))
print(f"Model using Law of Demeter is : {f1.aircraft_model()}")

# f1 = Flight("BA758",Aircraft("G-EUPT","Airbus A319", num_rows=22, num_seats_per_row=6))
# print(f"Model is {f1._aircraft.model()}")



"""Output:

Model is : Airbus A319
Registration of aircraft : G-EUPT
Seating plan is : (range(1, 23), 'ABCDEF')


"""
