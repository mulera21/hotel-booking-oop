import pandas

df = pandas.read_csv("hotels.csv")


class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass


class Reservation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter the id of the hotel")
hotel = Hotel(id)


if hotel.availabel():
    hotel.book()
    name = input("Enter your name")
    reservation = Reservation(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not free")