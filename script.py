from geopy.geocoders import Nominatim
import pandas

nom = Nominatim()

result = nom.geocode("3995 23rd St, San Francisco, CA 94114")

# Need to specifically mention unlike specifed in video
print(result.latitude, "is the latitude.")
print(result.longitude, "is the longitude")


df = pandas.read_csv("supermarkets.csv")

df["Address"] = df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]

df["Coordinates"] = df["Address"].apply(nom.geocode)

df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)


print(df)