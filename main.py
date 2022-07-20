from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests


URL = "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"
WEB_FILE = "data.html"
# Use HTMLSession() to initialize the GET requests and the .get() function from requests to call the URL to scrape.
# To make sure that there is no error,
# add a try and except statement to return an error in case the code doesn’t work.


def get_webpage():
    try:
        session = HTMLSession()
        response = session.get(URL)

    except requests.exceptions.RequestException as e:
        print(e)
    finally:
    # The structure of the requests-HTML parsing call goes like this: variable.attribute.function(*selector*, parameters)
    # The variable is the instance that was created using the .get(url) function. In this case, response.
    # The attribute is the type of content that I want to extract (html / lxml). In this case, html.
        with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
            fp.write(response.html.html)

def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_webpage()
    else:
        pass
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")

get_webpage()
read_web_file()

soup = read_web_file()
all_titles = soup.findAll(name="strong")
title_texts = []
title_index = []
index = 100
for title in all_titles:
    text = title.getText()
    title_index.append(index)
    title_texts.append(text)
    index -= 1

final_titles = [text for text in title_texts if int(title_texts.index(text))%2 == 0]

top_100_movies_list = []
n = 1
for movie in final_titles[::-1]:
    top_100_movies_list.append(f"{n}). {movie}")
    n +=1

# Create the text file:
with open ("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in top_100_movies_list:
        file.write(f"{movie}\n")
