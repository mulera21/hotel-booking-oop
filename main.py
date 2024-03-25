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
    def generate(self):
        pass


print(df)
id = input("Enter the id of the hotel")
hotel = Hotel(id):
if hotel.availabel():
    hotel.book()