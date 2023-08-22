# import geopy
# from geopy.geocoders import Nominatim
# import pandas as pd

# geolocator = Nominatim(user_agent="geoapiExercises")

# header = ["Location", "Latitude", "Longitude"]
# file_path = r"C:\Users\Sanket\Desktop\route-optmz\Vehicle route optimization\locations.xlsx"

# location = "Mumbai"

# location = geolocator.geocode(location)

# latitude = location.latitude
# longitude = location.longitude

# data = [[location, latitude, longitude]]

# df = pd.DataFrame(data, columns=header)

# df.to_excel(file_path, index=False)
import geopy
from geopy.geocoders import Nominatim
import pandas as pd

geolocator = Nominatim(user_agent="geoapiExercises")

header = ["Location", "Latitude", "Longitude","load"]
file_path = r"C:\Users\Sanket\Desktop\route-optmz\Vehicle route optimization\locations.xlsx"

data = []
loc = input("Enter a location (or enter 'q' to quit): ")
location = str(loc) + str(", India")
location = geolocator.geocode(location)
print(location.latitude)
# while True:
#     loc = input("Enter a location (or enter 'q' to quit): ")
#     location = str(loc) + str(", India")
#     load = input("Enter Weight of package  ")

#     if location.lower() == 'q':
#         break
#     if load.lower() == 'q':
#         break
#     location = geolocator.geocode(location)

#     latitude = location.latitude
#     longitude = location.longitude
#     load = load


#     data.append([location, latitude, longitude,load])

# df = pd.DataFrame(data, columns=header)

# df.to_excel(file_path, index=False)
