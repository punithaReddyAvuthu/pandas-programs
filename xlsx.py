import json
with open("C:\\Users\\punit\\OneDrive\\Documents\\top100cities_weather_data.csv.xlsx") as cities_file:
        cities_data = json.load(cities_file)
        print(cities_data)