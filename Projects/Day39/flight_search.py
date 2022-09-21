import requests
import time
from data_manager import DataManager

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com"
        self.header = {"apikey": "amIF7atU6eswxqmG_uVttSLSHyM3HYBt"}



    def get_city_code(self, cities):
        #cities = ["Natal", "Fortaleza"]
        self.cities_codes = []
        for self.city in cities:

            self.parameters = {"term": self.city,
                               "active_only": "true",
                               }
            response = requests.get(url=f"{self.endpoint}/locations/query", headers=self.header, params=self.parameters)
            city_code = response.json()
            print(city_code['locations'][0]["code"])
            c_code = city_code['locations'][0]["code"]
            self.cities_codes.append(c_code)
        return self.cities_codes

    def search_flight(self, fly_from, date_from, date_to, min_price):
        self.search_parameters = {
            "fly_from": fly_from,
            "date_from": date_from,
            "date_to": date_to,
            "price_from": 0,
            "price_to": min_price,

        }
        response = requests.get(url=f"{self.endpoint}/search", headers=self.header, params=self.search_parameters)
        flight_dados = response.json()



        my_flight = {
           flight_dados["data"][position]["price"]: [f"{flight_dados['data'][position]['flyFrom']}",
                                                    f"{flight_dados['data'][position]['flyTo']}",
                                                    f"{flight_dados['data'][position]['cityFrom']}",
                                                    f"{flight_dados['data'][position]['cityTo']}",
                                                    f"{time.strftime('%d/%m/%Y', time.localtime(flight_dados['data'][position]['dTime']))}"]
                                                    for position in range(len(flight_dados['data'])-1)

        }


        res = list(my_flight.keys())[0]

        print(f"Price Alert:{res}, fly from: {my_flight[res][2]}-{my_flight[res][0]} "
              f"to {my_flight[res][3]}-{my_flight[res][1]} from {my_flight[res][4]}")













#datma = DataManager()

#flight_search = FlightSearch()
#flight_search.search_flight(fly_from="NYC", date_from="28/04/2022", date_to="28/12/2022", min_price=100)



