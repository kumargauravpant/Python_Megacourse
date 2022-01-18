import folium
import pandas

volData = pandas.read_csv("volcanoes.txt")
name = list(volData["NAME"])
lat = list(volData["LAT"])
lon = list(volData["LON"])

map = folium.Map(location=[12.947227, 77.675838], zoom_start=6)

fg = folium.FeatureGroup(name="My Map")

for lt,ln,nme in zip(lat,lon,name):
    #fg.add_child(folium.Marker(location=[12.946565, 77.675871], popup="Home", icon=folium.Icon(color='green')))
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=nme, color='green'))

map.add_child(fg)

map.save("MyMap.html")


