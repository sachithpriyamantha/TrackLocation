import geocoder
import folium

g = geocoder.ip("#####")

myAddress = g.latlng
print(myAddress)

my_map1 = folium.Map(location=myAddress,
                     zoom_start=12)


folium.CircleMarker(location=myAddress,
                    radius=50, popup="###").add_to(my_map1)

folium.Marker(myAddress,
              popup="####").add_to(my_map1)
my_map1.save("my_map.html ")


