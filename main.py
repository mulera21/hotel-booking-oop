import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        pass

    def book(self):
        """book a hotel by changing its availability"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
        pass

    def available(self):
        """checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return  False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        pass


print(df)
hotel_id = input("Enter the id of the hotel")
hotel = Hotel(hotel_id)


if hotel.available():
    hotel.book()
    name = input("Enter your name")
    reservation = Reservation(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not free")