#from bs4 import BeautifulSoup
import bs4
from urllib.request import urlopen
#pass the URL
num = input("Enter from which year you want:")
#s='http://www.imdb.com/search/title?release_date=2005,num&title_type=feature&user_rating=1.0,10'
#print('http://www.imdb.com/search/title?release_date=2005,',num,'&title_type=feature&user_rating=1.0,10')
s='http://www.imdb.com/search/title?release_date=2005,'+num+'&title_type=feature&user_rating=1.0,10'
url = urlopen(s)
#read the source from the URL
readHtml = url.read()
#close the url
url.close()
#passing HTML to scrape it
soup = bs4.BeautifulSoup(readHtml, 'html.parser')

tableClassResults = soup.find("table", { "class" : "results" })
for row in tableClassResults.find_all('tr'):
    print("\n")
    title=row.find_all('td',{"class":"title"})
    for titletd in title:
        rating_rating=titletd.find(class_="rating-rating")
        ratingValue=rating_rating.find(class_="value")
        if ratingValue > 8:
            print("Title:"+titletd.a.string)
            print("Year:"+titletd.find(class_="year_type").string)
            genreClass=titletd.find(class_="genre")
            print("Genries:")
            for eachGenre in genreClass.find_all('a'):
                print("\t"+eachGenre.string)
            print("Run Time:"+titletd.find(class_="runtime").string)
            #rating_rating=titletd.find(class_="rating-rating")
           #ratingValue=rating_rating.find(class_="value")
            print("Rating:"+ratingValue.string)
