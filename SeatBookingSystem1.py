# Creating a Seat booking system

from pprint import pprint as pp

""" Model for aircraft flights"""
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
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{seat:None for seat in seats}for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        # Directly get the aircraft model, rather than reach through Flight and delgate aircraft object directly. Another way\
        # of doing this is f1._aircraft.model()
        return self._aircraft.model()

    def allocate_seat(self,seat,passenger_name):
        """A method to allocate the seat to the passenger

        Args:
            seat: A seat number such as 05A
            passenger_name: The name of the passenger

        Return:
            ValueError: If the seat is unavailable.
        """

        # Extract the row number for referancing the lst index
        row = seat[:2]

        # Extract the seat number for referacing the dictionary key.
        seat_letter = seat[-1]

        # Get the plan for comparison checks, if the input seat is valid
        rows,seat_letters = self._aircraft.seating_plan()

        # Entered input not in list of seat_letters
        if seat_letter not in seat_letters:
            raise ValueError(f"Invalid seat letter in {seat}")

        # Convert the row number to integer for indexing, if no possible raise ValueError
        try:
            row = int(row)
        except ValueError:
            raise ValueError(f"Invalid row in {seat}")

        # Check if the obtained row is in given list of rows = range(self._num_rows+1). Eg: Range supportcontainer protocol
        # >>> l = 2
        # >>> l in range(1,100)
        #     True
        if row not in rows:
            raise ValueError(f"Invalid row. Row {row} is not present")

        # Check if the seat is already occupied
        if self._seating[row][seat_letter] is not None:
            raise ValueError(f"{seat} is already taken")

        #Allocate the seat
        self._seating[row][seat_letter] = passenger_name


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


# Testing the code
f1 = Flight("BA758",Aircraft("G-EUPT","Airbus A319", num_rows=22, num_seats_per_row=7))

print("Testing the Seating arrangement of the flight  \n")
pp(f1._seating)


f1.allocate_seat('12A',"Guido Van Rossum")
pp(f1._seating)

# f1.allocate_seat('12A',"Rasmus Lerdorf")
# pp(f1._seating)  ---> Results it ValueError: 12A is already taken

f1.allocate_seat('15F',"Bjarne Stroustup")
pp(f1._seating)

# f1.allocate_seat("E27","Yukihiro Matsumoto")
# pp(f1._seating)  --> ValueError: Invalid seat letter in E27

"""Output:
Testing the Seating arrangement of the flight

[None,
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}]
[None,
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': 'Guido Van Rossum',
  'B': None,
  'C': None,
  'D': None,
  'E': None,
  'F': None,
  'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}]
[None,
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': 'Guido Van Rossum',
  'B': None,
  'C': None,
  'D': None,
  'E': None,
  'F': None,
  'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None,
  'B': None,
  'C': None,
  'D': None,
  'E': None,
  'F': 'Bjarne Stroustup',
  'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}]

"""
