from bs4 import BeautifulSoup as bs
import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
webpage = response.text
soup = bs(webpage, 'html.parser')

all_titles = soup.find_all(name="h3", class_="title")
all_titles_text = [title.getText() for title in all_titles]
sorted_titles = all_titles_text[::-1]

with open("top_100.txt", "w") as file:
    for title in sorted_titles:
        file.write(title + "\n")




