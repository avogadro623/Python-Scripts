# Copyright 2014 Google Inc. All rights reserved.
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
import googlemaps
import csv
gmaps = googlemaps.Client('AIzaSyBrowh9H67Od1WmEL7bVLNAzO1O7BDSYwY')
tf= 'Python Sample\ZIP_CODES.txt'
with open(tf) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    zips = []
    cities = []
    states = []
    for row in readCSV:
        zip = row[0]
        city = row[3]
        state = row[4]
    #    print(state)
        if state == 'NJ':
        	zips.append(zip)
        	cities.append(city)
        	states.append(state)
    #print(zips)
#n_zips=len(zips)
#print(n_zips)
for i in range(1,5):
    directions= gmaps.distance_matrix('07302', zips[i], departure_time='now', traffic_model='pessimistic', mode='walking')
    #print(len(directions))
    m_p=directions['rows'][0]['elements'][0]['duration']['text']
    directions= gmaps.distance_matrix('07302', zips[i], departure_time='now', traffic_model='optimistic')
    m_o=directions['rows'][0]['elements'][0]['duration']['text']
    print("The duration from "+cities[0]+" to "+cities[i]+"("+zips[i]+") is pessimistic "+m_p+" and optimistic is "+m_o)
 #   p=max(m)
 #   print(p)