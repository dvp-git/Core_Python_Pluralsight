# Creating a Seat booking system ( With Re-location mechanism)

from pprint import pprint as pp

class Flight():
    """ A model for a Flight"""
    def __init__(self, number, aircraft):

        if not number[:2].isupper():
            raise ValueError(f"Invalid flight number in {number}")

        if not number[:2].isalpha():
            raise ValueError(f"Invalid Airline code in {number}")

        if int(number[2:]) not in range(9999):
            raise ValueError(f"Invalid Route code i {number}")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        # self._seating = [None] + [{seat:None for seat in "ABCDEFGH"[:self._aircraft._num_seats_per_row+1]}for _ in range(self._aircraft._num_seats_per_row+1)]
        self._seating = [None] + [{seat:None for seat in seats}for _ in rows]

    def number(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft.model


    def allocate_seat(self,seat_number, passenger):
        """A method that allocates the passenger to seat number of the form 15"""
        row,seat_letter = seat_number[:-1],seat_number[-1]

        rows,seats = self._aircraft.seating_plan()
        if seat_letter not in seats:
            raise ValueError(f"Invalid sear letter in {seat_number}")

        try:
            row = int(row)
        except ValueError:
            raise ValueError(f"Invalid seat number in {seat_number}")

        if row not in rows:
            raise ValueError(f"Row is not present in {seat_number}")

        if self._seating[row][seat_letter] is not None:
            raise ValueError(f"Seat {seat_number} already occupied")

        self._seating[row][seat_letter] = passenger


    def _parse_seat(self, seat_number):
        """ A method to get the seat_number details in seat_row,seat_letter form

        Args:
            seat_number : The seat number of the form '12F'

        Returns:
            seat_row    : The row number of the seat
            seat_letter : The seat lettter of the seat
        """
        seat_row, seat_letter =  seat_number[:-1],seat_number[-1]
        rows,seats = self._aircraft.seating_plan()

        if seat_letter not in seats:
            raise ValueError(f"Invalid sear letter in {seat_number}")

        try:
            seat_row = int(seat_row)
        except ValueError:
            raise ValueError(f"Invalid seat number in {seat_number}")

        if seat_row not in rows:
            raise ValueError(f"Row is not present in {seat_number}")

        return seat_row,seat_letter


    def relocate_seat(self, from_seat , to_seat):
        """A method to relocate the passenger from from_seat to to_seat

        Args:
            from_seat   : The seat from which a passenger needs to be relocated
            to_seat     : The seat to which a passenger needs to be shifted to

        Returns:
            None
        """
        from_seat_row,from_seat_letter = self._parse_seat(from_seat)
        to_seat_row,to_seat_letter = self._parse_seat(to_seat)
        if self._seating[from_seat_row][from_seat_letter] is None:
            raise ValueError(f"No passenger in {from_seat}")


        if self._seating[to_seat_row][to_seat_letter] is not None:
            raise ValueError(f"Seat {to_seat} is already occupied")

        self._seating[to_seat_row][to_seat_letter] = self._seating[from_seat_row][from_seat_letter]
        self._seating[from_seat_row][from_seat_letter] = None


    def seats_available(self):
        sum = 0
        for row in self._seating:
            if row is not None:
                for seat in row.values():
                    if seat == None:
                        sum = sum + 1
        return sum
        # OR
        # return sum(sum(1 for s in row.values() if s is None)for row in self._seating if row is not None)



class Aircraft():
    """A model for Aircraft"""
    def __init__(self, registration, model, num_rows , num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1,self._num_rows+1), "ABCDEFGH"[:self._num_seats_per_row]

f1 = Flight("SN0020",Aircraft("AirBus AG","AG1234",20,6))
print(f1._aircraft._num_rows)
print(f1._aircraft.seating_plan())
pp(f1._seating)


# Testing the code
f1 = Flight("BA758",Aircraft("G-EUPT","Airbus A319", num_rows=22, num_seats_per_row=7))

print("Testing the Seating arrangement of the flight  \n")
pp(f1._seating)


f1.allocate_seat('12A',"Guido Van Rossum")
pp(f1._seating)

# f1.allocate_seat('12A',"Rasmus Lerdorf")
# pp(f1._seating)  #---> Results it ValueError: 12A is already taken

f1.allocate_seat('15F',"Bjarne Stroustup")
pp(f1._seating)

# f1.allocate_seat("E27","Yukihiro Matsumoto")
# pp(f1._seating)  #--> ValueError: Invalid seat letter in E27

# f1.relocate_seat('13A','15B')
# pp(f1._seating)  # --> ValueError: No passenger in 13A

f1.relocate_seat('15F','15B')
pp(f1._seating)

print("Seats availble :")
print(f1.seats_available())





"""Output:
20
(range(1, 21), 'ABCDEF')
[None,
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}]
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
  'B': 'Bjarne Stroustup',
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
 {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}]
152
"""
