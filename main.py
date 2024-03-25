import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
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
        self.customer_name = customer_name
        self.hotel_object = hotel_object
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation here are your booking data
        Name: {self.customer_name}
        hotel name:{self.hotel.name}
        """
        return content



print(df)
hotel_id = input("Enter the id of the hotel")
hotel = Hotel(hotel_id)


if hotel.available():
    hotel.book()
    name = input("Enter your name")
    reservation = Reservation(customer_name=name, hotel_object=hotel)
    print(reservation.generate())
else:
    print("Hotel is not free")