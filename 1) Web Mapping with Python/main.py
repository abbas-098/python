import folium
import pandas as pd

# Loading the text file
data = pd.read_csv("volcanoes(America).csv")

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# obtaining lists of data
latitude = list(data["Latitude"])
longitude = list(data["Longitude"])
elevation = list(data["Elev"])
name = list(data["Volcano Name"])
typev = list(data["Type"])

# Function to decide the colour depending on the elevation
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

# latitutde, longitude
for lt, ln, el, nm, typ in zip(latitude,longitude,elevation,name,typev):
    fg.add_child(folium.CircleMarker(location = [lt,ln],radius=6, 
    popup="Elevation: " + str(el) + "m" + "\n" + "Name: " + nm + "\n" +  "Type: " + typ ,fill_color = color_producer(el), 
    color = "grey", fill_opacity = 0.7))


map.add_child(fg)


map.save("Map1.html")