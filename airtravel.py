# Complex is better than complicated; Flight class is more complex but none of the client of flight needs to know about the aircraft model details 
class Flight:
    """A flight with a particular aircraft model"""

    # if an initialisation method is provided, it will be called as part of the process of creating a new instance object of the type/class by the Python runtime!
    # this is an initializer not a constructor; the purpose of it is to configure an object that already exists by the time it's called. 
    # In python the actual ctor is provided by the python runtime which checks whether an initializer exists and call it if it does. 
    def __init__(self, number, aircraft):

        #class invariants
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}''".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        # everything is public in Python!
        self._number = number # don't need to pre-create an attribute on the type
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        # using a dict comprehension within a list comprehension to get all rows in the seating; each element in the seating is a dict of seats. 
        self._seating = [None] + [{str(row) + letter : None for letter in seats} for row in rows]
    
    # private/implementation details by convention begin with _ 
    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter
        
        Args:
            seat: A seat designator such as 12A

        Returns:
            A tuple containing an integer of row number and a string for seat letter
        """
        rows, seats = self._aircraft.seating_plan()
        rowNumber = seat[:-1]
       
        try:
            row = int(rowNumber)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(rowNumber))
        if row not in rows:
            raise ValueError("Invalide row number for seat {}".format(row))
        seatLetter = seat[-1]
        if seatLetter not in seats:
            raise ValueError("Invalide seat number in seat {}".format(seat))

        return row, seatLetter # return a tuple where () is optional 

    

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger
        
        Args:
            seat : a seat designator such as '12C' or '21F'.
            passenger: The passenger name
        
        Rarises:
            ValueError: If the seat if unavailable.
        """
        row, _ = self._parse_seat(seat)
        if self._seating[row][seat] is not None:
            raise ValueError("Seat {} is occupied already".format(seat))
        
        #allocate the seat! 
        self._seating[row][seat] = passenger


    def change_seat(self, from_seat, to_seat):
        """Change a passenger from one seat to another seat
        
        Args:
            from_seat: The current seat of the passenger
            to_seat: The seat to change to

        """
        from_row, _ = self._parse_seat(from_seat)
        if self._seating[from_row][from_seat] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))
        
        to_row, _ = self._parse_seat(to_seat)
        if self._seating[to_row][to_seat] is not None:
            raise ValueError("Seat {} is already occupied".format(to_seat))
        
        # everything is passed by reference so it's better NOT to cache the passenger name in case it's a mutable object
        self._seating[to_row][to_seat] = self._seating[from_row][from_seat]
        self._seating[from_row][from_seat] = None
        
    
    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is not None)
                    for row in self._seating if row is not None) # since the first row is always None 
    
# instance methods, can be called on the objects rather than type, must always take the 1st parameter and by convention it's called self. 
    def number(self):
        return self._number
    

    def airline(self):
        return self._number[:2]

    # Law of Demeter: The principle of least knowledge --- you should never call methods on objects you receive from other calls! e.g. only talk to your friend!
    def aircraft_model(self):
        return self._aircraft.model() # delegate the call to aircraft object 


"""Model for an aircraft"""
class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row  

    
    def registration(self):
        return self._registration


    def model(self):
        return self._model


    def seating_plan(self):
        """
        Returns:
            A tuple of possible seats range iterators and number of seats per row
        """
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])


def main():
    from pprint import pprint as pp
    a = Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=7)
    print(a.seating_plan())
    print(a.model())
    print(a.registration())
    f = Flight('BA038', Aircraft('H-EUFJG', 'Boeing 777', num_rows= 20, num_seats_per_row = 6))
    #pp(f._seating)
    f.allocate_seat('10A', 'Rita')
    f.allocate_seat('10B', 'Mandy')
    f.allocate_seat('10C', 'Tony')
    pp(f._seating)
    f.change_seat('10C', '5A')
    pp(f._seating)
    


if __name__ == '__main__':
    main()