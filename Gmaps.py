
# Copyright 2014 Google Inc. All rights reserved.
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
import googlemaps
gmaps = googlemaps.Client('AIzaSyBrowh9H67Od1WmEL7bVLNAzO1O7BDSYwY')
geocode_result = gmaps.geocode('1600 Pennsylvania Av, Washington DC')
#print(geocode_result)
reverse_geocode_result = gmaps.reverse_geocode((40.7134104, -74.0411325))
#reverse_geocode_result=gmaps.address_to_latlng('149 Essex St, Jersey City, NJ')
address = reverse_geocode_result
#f = open("test.txt","w")
#f.write(address)
#print(vars(address))
#print(address['postal'])
x=address[0][0]
#y=x[0]
print(len(x))
#f.close()