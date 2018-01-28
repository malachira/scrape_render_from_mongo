from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    mars_data = {}

    browser = init_browser()
    # create surf_data dict that we can insert into mongo

    # Visit the following URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    results = soup.find_all("li", class_="slide")

    for result in results:
        try:
            news_title = result.find("div",class_="content_title").text
            news_p = result.find("div",class_="article_teaser_body").text
            mars_data["title"] = news_title
            mars_data["para"] = news_p
        except Exception as e:
            print(e)

    return mars_data
