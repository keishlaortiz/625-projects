"""
Class to store the information about a city (name, latitute and longitude)
"""
class City(object):
    def __init__(self,name,lat,lon):
        self._name = name
        self._lat = lat
        self._lon = lon

    @property
    def name(self):
        return self._name

    @property
    def latitude(self):
        return self._lat

    @property
    def longitude(self):
        return self._lon
    
    
    