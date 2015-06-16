__author__ = 'jheider'

class DesiredOptions(object):
    def __init__(self):
        self.zip_code = "32250"     #required
        self.ext_colors = ["Black", "Blue"]
        self.doors = "4"
        self.search_radius = "0"    #required
        self.max_mileage = "45000"
        self.min_price = "0"
        self.max_price = "35000"
        self.make = "Ram"           #required
        self.model = "1500"         #required
        self.trim = "Sport"
        self.listing_types = ["Used", "Certified"]
        self.min_year = "2012"
        self.max_year = "2015"
        self.features = ["Leather Seats", "Quad Cab", "Sunroof"]

    def zipcode(self):
        return self.zip_code

    def external_colors(self):
        return self.ext_colors

    def number_of_doors(self):
        return self.doors

    def search_radius(self):
        return self.search_radius

    def max_mileage(self):
        return self.max_mileage

    def min_price(self):
        return self.min_price

    def max_price(self):
        return self.max_price

    def make(self):
        return self.make

    def model(self):
        return self.model

    def trim(self):
        return self.trim

    def listing_types(self):
        return self.listing_types

    def min_year(self):
        return self.min_year

    def max_year(self):
        return self.max_year

    def features(self):
        return self.features
