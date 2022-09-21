import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = "https://api.sheety.co/efa26c7a2f09c24a4779fd46dc2b0fcf/flightDeals/prices"

    def get_city(self):
        self.cities = []
        self.response = requests.get(url=self.endpoint)
        self.city = self.response.json()

        for position in self.city["prices"]:
            self.cities.append(position["city"])
        return self.cities

    def get_min_price(self):
        self.min_prices = []
        self.response_pice = requests.get(url=self.endpoint)
        self.min_price = self.response.json()

        for position in self.min_price["prices"]:
            self.min_prices.append(position["lowestprice"])
        return self.min_prices

    def put_city_code(self, code, id):
        self.id = id
        self.message = {
            "price": {
                "iata": code,
            }
        }

        self.sheet_code = requests.put(url=f"{self.endpoint}/{self.id}", json=self.message)
        self.sheet_response = self.sheet_code.json()
        print(self.sheet_response)


datamanager = DataManager()
#datamanager.get_city()
#tests = ["PAR", "LON", "FR"]


#for i in range(len(tests)):
 #   test = tests[i]
  #  id = i+2
   # datamanager.put_city_code(test, id)
