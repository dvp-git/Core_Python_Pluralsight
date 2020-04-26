# Creating a Seat booking system ( With Re-location mechanism and make_flight along with CardPrinter()

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
        row,seat_letter = self._parse_seat(seat_number)  # Using the _parse_seat method

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


    def make_boarding_cards(self, card_printer):
        # Make the flight print the card using cardprinter and passing each passenger, seat in sorted border
        # _passenger_seats is an implementation detail which gives the passenger and seat number
        for passenger,seat in sorted(self._passenger_seats()):
            card_printer(passenger,seat,self._number,self._aircraft.model())


    def _passenger_seats(self): # A generator function yielding the passenger and seat number only if occupied
        """ Iterable series of passenger seat allocations"""
        rows, seats = self._aircraft.seating_plan()
        for row in rows:
            for seat in seats:
                passenger = self._seating[row][seat]
                if passenger is not None:
                    yield (passenger, f"{row}{seat}")


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


# Tell! Don't ask, Make the Flight class tell the card_printer what to do.
def card_printer(passenger, seat, flight_number, aircraft):
    output = f"| Name : {passenger}"\
             f"| Flight : {flight_number}"\
             f"| Seat : {seat}"\
             f"| Aircraft : {aircraft}"\
             "|"
    banner = "+" + (len(output) - 2) * "-" + "+"
    border = "|" + (len(output) - 2) * " " + "|"
    lines = [banner, border , output, border, banner]
    card = "\n".join(lines)
    print(card)
    print("\n")





def main():
    f1 = Flight("SN0020",Aircraft("AirBus AG","AG1234",20,6))
    print(f1._aircraft._num_rows)
    print(f1._aircraft.seating_plan())
    pp(f1._seating)
    f1.make_boarding_cards(card_printer)



if "__main__" == __name__ :
    main()

# Testing the code
# f1 = Flight("BA758",Aircraft("G-EUPT","Airbus A319", num_rows=22, num_seats_per_row=7))
#
# print("Testing the Seating arrangement of the flight  \n")
# pp(f1._seating)
#
#
# f1.allocate_seat('12A',"Guido Van Rossum")
# pp(f1._seating)
#
# # f1.allocate_seat('12A',"Rasmus Lerdorf")
# # pp(f1._seating)  #---> Results it ValueError: 12A is already taken
#
# f1.allocate_seat('15F',"Bjarne Stroustup")
# pp(f1._seating)
#
# # f1.allocate_seat("E27","Yukihiro Matsumoto")
# # pp(f1._seating)  #--> ValueError: Invalid seat letter in E27
#
# # f1.relocate_seat('13A','15B')
# # pp(f1._seating)  # --> ValueError: No passenger in 13A
#
# f1.relocate_seat('15F','15B')
# pp(f1._seating)
#
# print("Seats availble :")
# print(f1.seats_available())

def make_flight():
    f = Flight("BA759",Aircraft("G-EUPT","Airbus A319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A","Guido Van Rossum")
    f.allocate_seat("15F","Bjarne Stroustrup")
    f.allocate_seat("15E","Anders Hejlsberg")
    f.allocate_seat("1C","John McCarthy")
    f.allocate_seat("1D","Rich Mickey")
    return f










"""Output:
>>> from MakeFlightCardPrinter import *
>>> f = make_flight()
>>> f = make_flight()
>>> f.make_boarding_cards(card_printer)
+----------------------------------------------------------------------------+
|                                                                            |
| Name : Anders Hejlsberg| Flight : BA759| Seat : 15E| Aircraft : Airbus A319|
|                                                                            |
+----------------------------------------------------------------------------+


+-----------------------------------------------------------------------------+
|                                                                             |
| Name : Bjarne Stroustrup| Flight : BA759| Seat : 15F| Aircraft : Airbus A319|
|                                                                             |
+-----------------------------------------------------------------------------+


+----------------------------------------------------------------------------+
|                                                                            |
| Name : Guido Van Rossum| Flight : BA759| Seat : 12A| Aircraft : Airbus A319|
|                                                                            |
+----------------------------------------------------------------------------+


+------------------------------------------------------------------------+
|                                                                        |
| Name : John McCarthy| Flight : BA759| Seat : 1C| Aircraft : Airbus A319|
|                                                                        |
+------------------------------------------------------------------------+


+----------------------------------------------------------------------+
|                                                                      |
| Name : Rich Mickey| Flight : BA759| Seat : 1D| Aircraft : Airbus A319|
|                                                                      |
+----------------------------------------------------------------------+
"""
