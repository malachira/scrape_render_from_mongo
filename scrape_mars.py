import time
from bs4 import BeautifulSoup as bs
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    browser = init_browser()

    # create surf_data dict that we can insert into mongo

    #First, scrape the news
    mars_data = {}

    # Visit mars.nasa.gov to scrape news
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    result = soup.find("li", class_="slide")

    news_title = result.find("div",class_="content_title").text
    news_p = result.find("div",class_="article_teaser_body").text
    mars_data["news_title"] = news_title
    mars_data["news_para"] = news_p

    #Scrape images
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    img_html = browser.html
    soup = bs(img_html, "html.parser")

    img_results = soup.find("div", class_="carousel_items").find("article")["style"]
    featured_image_url = "https://www.jpl.nasa.gov"+ img_results.split("'")[1]

    mars_data["img_link"] = featured_image_url

    # print(mars_data)
    return mars_data

# if __name__ == "__main__":
#     scrape()