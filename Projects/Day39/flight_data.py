import datetime


# today = datetime.datetime.today()
# tomorrow_day = today.day + 1
# six_months = today + datetime.timedelta(days=180)


# print(today.strftime(f"{tomorrow_day}/%m/%Y"))
# print(six_months.strftime("%d/%m/%Y"))
# six = six_months.strftime("%d/%m/%Y")


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.cities = None
        self.lower_price = None
        self.dictionary = None
        self.now = datetime.datetime.today()
        self.tomorrow_day = self.now.day + 1
        self.tomorrow = self.now.strftime(f"{self.tomorrow_day}/%m/%Y")
        self.six_months = (self.now + datetime.timedelta(days=180)).strftime("%d/%m/%Y")

    def store_cities(self, cities):
        self.cities = cities

    def store_lower_price(self, price):
        self.lower_price = price

    def create_dict(self, cities, price):
        self.dictionary = dict(zip(cities, price))



flightdata = FlightData()

#print(flightdata.six_months)
#print(flightdata.cities)
#flightdata.store_cities(["for", "nat"])
#print(flightdata.cities)
print(flightdata.dictionary)
