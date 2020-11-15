from geopy.geocoders import Nominatim

def geocoding(place):
    geolocateor = nominatim(user_agent="my-application")
    location = geolocateor.geocode(place, timeout=10)
    if location is None:
        return
    else:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude