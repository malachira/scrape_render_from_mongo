import time
from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    mars_news = {}

    browser = init_browser()
    # create surf_data dict that we can insert into mongo

    # Visit the following URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    result = soup.find("li", class_="slide")

    news_title = result.find("div",class_="content_title").text
    news_p = result.find("div",class_="article_teaser_body").text
    mars_news["title"] = news_title
    mars_news["para"] = news_p

    return mars_news

# if __name__ == "__main__":
#     scrape()