# tripadvisor Scrapper - use this one to scrape hotels

# importing libraries
from bs4 import BeautifulSoup
import urllib
import os
import urllib.request
import re
import json

# creating CSV file to be used

file = open(os.path.expanduser(r"newfile.txt"), "r")
with open("newfile.txt") as f:
    WebSites = f.readlines()
#print(content[1])
#    b"Organization,Address,Website" + b"\n")

# List the first page of the reviews (ends with "#REVIEWS") - separate the websites with ,
#WebSites = [
#   content[0], content[2]]
#print(type(WebSites))
#Checker = "REVIEWS"
# looping through each site until it hits a break
for theurl in WebSites:
    thepage = urllib.request.urlopen(theurl)
    print(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    titleTag = soup.html.head.title # Searching for the title - practice code
#    print(titleTag.string)
    x=soup.findAll(attrs={"script": ""})
    data = json.loads(soup.find('script', type='application/ld+json').text)
    for i in range(0,2):
    	print(data['itemListElement'][i]['url'])
#    y= json.dumps(data)
#    print(y)
 #   print(data)
#for i in range(0,9):
#    print(type(data['itemListElement'][i]['url']))
#print(data['itemListElement'][i]['url'])
file.close()