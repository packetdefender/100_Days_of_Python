from bs4 import BeautifulSoup as bs
import requests
# Going to use the ycombinator main hacker news web site

request = requests.get("https://news.ycombinator.com")
webpage = request.text

soup = bs(webpage, "html.parser")

# stories = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
articles = soup.find_all(name="a", class_="titlelink")

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_upvote = max(article_upvotes)
highest_upvote_position = article_upvotes.index(highest_upvote)
print(article_texts[highest_upvote_position], article_links[highest_upvote_position], highest_upvote)

# print(article_texts)
# print(article_links)
# print(article_upvotes)


























# with open("website.html") as file:
#     webpage = file.read()
#
# soup = bs(webpage, "html.parser")
# # print(soup.a.string)
# all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
# # 	print(tag.get('href'))
#
# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h3", class_="heading")
#
# company_url = soup.select_one(selector="p a")
# # print(company_url.get('href'))
#
# name = soup.select_one(selector='#name')
# # print(name)
#
# headings = soup.select(selector=".heading")
# # print(headings)
