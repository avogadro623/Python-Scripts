# tripadvisor Scrapper - use this one to scrape hotels

# importing libraries
from bs4 import BeautifulSoup
import urllib
import os
import urllib.request
import re
import json

# creating CSV file to be used

file = open(os.path.expanduser(r"~/Desktop/TripAdvisorList1.csv"), "w")
#    b"Organization,Address,Website" + b"\n")

# List the first page of the reviews (ends with "#REVIEWS") - separate the websites with ,
WebSites = [
    "https://www.tripadvisor.com/Restaurants-g28951-New_Jersey.html"]
#Checker = "REVIEWS"
# looping through each site until it hits a break
file = open("newfile.txt", "w")
for theurl in WebSites:
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    titleTag = soup.html.head.title # Searching for the title - practice code
    print(titleTag.string)
    x=soup.findAll("div",{"class":"geo_name"})
    for div in x:
        print((div.find('a')['href']))
        file.write('https://www.tripadvisor.com'+ div.find('a')['href'] + '\n')
 #   print(data)
 #   print(x)
file.close()
file.close()