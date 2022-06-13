import requests
from bs4 import BeautifulSoup

Url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
R = requests.get(Url)
Soup = BeautifulSoup(R.text, "html5lib")
List = Soup.find("tbody", {"class": "lister-list"}).find_all("tr")

for Movie in List:

    Name = Movie.find("td", {"class": "titleColumn"}).a.text
    Date = Movie.find("td", {"class": "titleColumn"}).span.text.strip("()")
    Rating = Movie.find(
        "td", {"class": "ratingColumn imdbRating"}).text.strip()
    print(f"Movie --> {Name}  Date --> {Date}  Rating --> {Rating}")
