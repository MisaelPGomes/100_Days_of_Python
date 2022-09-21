from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData

#This file will need to use the DataManager,
# FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

"""Program Requirements
1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet
with International Air Transport Association (IATA) codes for each city.
Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later
for all the cities in the Google Sheet.

3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
with the Twilio API.

4. The SMS should include the departure airport IATA code,
destination airport IATA code, departure city, destination city, flight price and flight dates. e.g."""

flight_search = FlightSearch()
data_manager = DataManager()
flight_data = FlightData()

cities = data_manager.get_city()

codes = flight_search.get_city_code(cities)

min_price = data_manager.get_min_price()

flight_data.store_cities(cities)
flight_data.store_lower_price(min_price)

flight_data.create_dict(codes, min_price)






#print(codes)
#print(type(codes))


for i in range(len(codes)):
    code = codes[i]
    id = i+2
    data_manager.put_city_code(code, id)



for code in flight_data.dictionary:
    flight_search.search_flight(code, flight_data.tomorrow, flight_data.six_months, flight_data.dictionary[code])
    #print(flight_data.dictionary[code])
    #print(type(code))