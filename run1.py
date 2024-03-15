# import folium package
import folium
import geocoder
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/mappp')
def maps1():
    g = geocoder.ip('me')
    print(g.latlng)
    #print(g.latlng[0])

    #my_map3 = folium.Map(location = [g.latlng[0], g.latlng[1]],
    #                                        zoom_start = 15)
    
    # Pass a string in popup parameter
    #folium.Marker([g.latlng[0], g.latlng[1]],
    #            popup = ' Geeksforgeeks.org ').add_to(my_map3)
    
    
    #my_map3.save(" my_map3.html ")
    return g.latlng

