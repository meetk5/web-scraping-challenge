from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd

def scrape_info():
    executable_path = {"executable_path": "/Users/meetkamalkaursahni/Documents/chromedriver"}
    browser = Browser("chrome", **executable_path)

    url = 'https://redplanetscience.com/'

    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    title = soup.select_one("div.content_title")
    news_title = title.text

    body = soup.select_one("div.article_teaser_body")
    news_body = body.text

    url2 = "https://spaceimages-mars.com/"

    browser.visit(url2)
    html2 = browser.html
    soup2 = bs(html2, 'html.parser')

    image_url = soup2.select_one("img.fancybox-image")['src']

    url3 = 'https://galaxyfacts-mars.com/'

    table = pd.read_html(url3)

    df = table[0]

    new_header = df.iloc[0] #grab the first row for the header.
    df.columns = new_header #make the header the new column names
    df = df[1:]

    html = df.to_html()

    html.replace('\n', '')

    df.to_html('table.html', index=False)

    url4 = "https://marshemispheres.com/"

    browser.visit(url4)
    html = browser.html
    soup4 = bs(html, 'html.parser') 

    link1 = "https://marshemispheres.com/cerberus.html"
    link2 = "https://marshemispheres.com/schiaparelli.html"
    link3 = "https://marshemispheres.com/syrtis.html"
    link4 = "https://marshemispheres.com/valles.html"

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": link4},
    {"title": "Cerberus Hemisphere", "img_url": link1},
    {"title": "Schiaparelli Hemisphere", "img_url": link2},
    {"title": "Syrtis Major Hemisphere", "img_url": link3},
    ]
    
    # Store data in a dictionary
    html_data = {
        "news_title": news_title,
        "news_body": news_body,
        "image_url": image_url,
        "hemisphere_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return html_data

