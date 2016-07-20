# Complex is better than complicated; Flight class is more complex but none of the client of flight needs to know about the aircraft model details 
class Flight:
    """A flight with a particular aircraft model"""

    # if an initialisation method is provided, it will be called as part of the process of creating a new instance object of the type/class by the Python runtime!
    # this is an initializer not a constructor; the purpose of it is to configure an object that already exists by the time it's called. 
    # In python the actual ctor is provided by the python runtime which checks whether an initializer exists and call it if it does. 
    def __init__(self, number, aircraft):# thanks to duck typing, as long as it passes in an object with satisfying attributes it's fine!

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
        return sum( # sum of available seats of all rows 
                    sum(1 for s in row.values() if s is None) # sum of available seats per row 
                    for row in self._seating if row is not None) # since the first row is always None
 
    
    # instance methods, can be called on the objects rather than type, must always take the 1st parameter and by convention it's called self. 
    def number(self):
        return self._number
    

    def airline(self):
        return self._number[:2]

    # Law of Demeter: The principle of least knowledge --- you should never call methods on objects you receive from other calls! e.g. only talk to your friend!
    def aircraft_model(self):
        return self._aircraft.model() # delegate the call to aircraft object

    
    def _passenger_seats(self):
        """An interable series of passengers seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for seat in seat_letters:
                passenger = self._seating[row][str(row) + seat]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, seat))


    def make_boarding_cards(self, card_printer):
        flight_number = self.number()
        model = self.aircraft_model()
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, flight_number, model)


"""Model for an aircraft"""
class Aircraft: # abstract base class used for sharing implementation details. 

    # all methods in base class are shared including __init__()
    def __init__(self, registration):
        self._registration = registration  

    
    def num_seats(self):
        # hence it cannot be instantiated alonoe!
        rows, row_seats = self.seating_plan() # it depends on seating_plan() method which must be defined in a derived class 
        return len(rows) * len(row_seats)


    def registration(self):
        return self._registration


#duck tpying of Aircraft. In statically typed language like C#, runtime ploymorphism is achieved through class based inheritance.
# This is not the case in Python because no Python method call or attributes lookups are NOT bound to actual objects until the point at 
# which they are called (known as late binding) means we can attempt ploymorphism with any object (rather than just the base/sub classes!)
# and will succeed if the object fits. Although inheritance in Python can be used to facilitate polymorphism, after all derived class will have 
# the same interface as the base classes, inheritance in Python is most useful in sharing implementation between classes.
# Thanks to duck typing, inheritance is less used in python which is a good thing because inheritance is very tight coupling between classes. 
class AirbusA319(Aircraft): 
    def __init__(self, registration):
        self._registration = registration
    

    def registration(self):
        return self._registration
    

    def model(self):
        return "AirbusA319"
    

    def seating_plan(self):
        return range(1, 23), "ABCDEF"

class Boeing777(Aircraft):
    def __init__(self, registration):
        self._registration = registration
    

    def registration(self):
        return self._registration
    

    def model(self):
        return "Boeing777"
    

    def seating_plan(self):
        return range(1, 56), "ABCDEFGHJK"


def main():
    from pprint import pprint as pp
    # a = Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=7)
    # print(a.seating_plan())
    # print(a.model())
    # print(a.registration())

    f = Flight('BA038', Boeing777('H-EUFJG'))
    #pp(f._seating)
    f.allocate_seat('10A', 'Rita')
    f.allocate_seat('10B', 'Mandy')
    f.allocate_seat('10C', 'Tony')
    #pp(f._seating)
    f.change_seat('10C', '5A')
    f.allocate_seat('22D', 'Mat')
    f.allocate_seat('32F', 'Andrew')
    #pp(f._seating)
    f.make_boarding_cards(console_card_printer)

    # use duck typing of aircraft into flight type
    fa = Flight("CA100", AirbusA319("G-FUNT"))
    fa.allocate_seat('10A', 'Mike Smith')
    fa.allocate_seat('4B', 'Chris Longden')
    fa.allocate_seat('20D', 'Andrew Eagen')
    fa.allocate_seat('19E', 'Paul Hawkings')
    print(fa.aircraft_model())
    print(fa.num_available_seats())
    fa.make_boarding_cards(console_card_printer)

    fb = Flight('BA007', Boeing777('F-GDSK'))
    fb.allocate_seat('3E', 'Mina Radman')
    fb.allocate_seat('8B', 'Andy')
    fb.allocate_seat('18D', 'Ben Li')
    fb.allocate_seat('20F', 'Ning')
    print(fb.aircraft_model())
    print(fb.num_available_seats())
    fb.make_boarding_cards(console_card_printer)

# don't always need to define class! sometimes functional ways are better!
# Ploymorphism is the concept of allowing objects of different type through an uniform interface; it can be applied to functions and complex objects.
# This function is ploymorphic because it can be used by different object types acting like a common interface.
# Ploymorphism in Python is achieved through duck typing e.g. a object fitness for prupose is only determined at runtime (e.g. at time of use!)
# Duck typing is the cornerstone of Python object system, unlike other statically typed languaged where compiler determines whether an object can be used.
# In Python, whether an object can be used is purely dependent on the attributes an object has at the time of use. 
# Duck typing and ploymorphism are very important in Python and collection protocols (iterable, iterator, sequences) are built upon these two.
def console_card_printer(passenger_name, seat, flight_number, aircraft_model):
    content = '| Name: {}' \
              '  Flight: {}' \
              '  Seat: {}   Aircraft:{} |'.format(passenger_name, flight_number, seat, aircraft_model)
    banner = '+' + '-' * (len(content) - 2) + '+'
    border = '|' + ' ' * (len(content) - 2) + '|'
    lines = [banner, border, content, border, banner]
    card = '\n'.join(lines) # convert list of string into a single string
    print(card)
    print() # another empty line  



if __name__ == '__main__':
    main()
    #console_card_card_printer('Rita Liu', 'CA938', '22E', 'Airbus A330')
