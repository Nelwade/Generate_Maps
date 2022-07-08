from email.policy import default
import pandas as pd
import folium
from folium.plugins import MarkerCluster

df = pd.read_excel("new_database.xlsx", skiprows=0)
center = [-0.023559, 37.9061928]
map_kenya = folium.Map(location=center, zoom_start=5)

tooltip = "More Information!"

marker_cluster = MarkerCluster().add_to(map_kenya)

def marker(accident, color):
    location = [accident['LATITUDE'], accident['LONGITUDE']]
    folium.Marker(
        location, 
        popup = f'DATE OF OCCURENCE: {accident["OCCURENCE DATE"]}\n\n\
            REGISTRATION: {accident["REGISTRATION"]}\n\n\
            TYPE OF FLIGHT: {accident["TYPE OF FLIGHT"]}\n\
            PHASE OF FLIGHT: {accident["PHASE OF FLIGHT"]}\n\
            FATAL INJURIES: {accident["FATAL INJURIES"]}\n\
            SERIOUS INJURIES: {accident["SERIOUS INJURIES"]}\n\
            MINOR INJURIES: {accident["MINOR INJURIES"]}\n\
            DAMAGE: {accident["DAMAGE"]}\n\
            TYPE OF OCCURENCE: {accident["TYPE OF OCCURRENCE"]}\n\
            AIRCRAFT TYPE: {accident["AIRCRAFT TYPE"]}\n\
            ENGINE TYPE: {accident["ENGINE TYPE"]}\n\
            PROBABLE CAUSE: {accident["CAUSE"]}', 
        tooltip=tooltip,
        icon=folium.Icon(color=color)
        ).add_to(marker_cluster)
    

for index, accident in df.iterrows():
    try:
        if accident["FATAL INJURIES"] > 0:
            marker(accident, color="red")
        else:
            marker(accident, color="blue")
    except ValueError:
        continue

map_kenya.save("index1.html")