from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def scrape_info():
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser("chrome", **executable_path)

    url = 'https://redplanetscience.com/'

    browser.visit(url)

    time.sleep(5)
    
    html = browser.html
    soup = bs(html, 'html.parser')

    title = soup.select_one("div.content_title")
    news_title = title.text

    body = soup.select_one("div.article_teaser_body")
    news_body = body.text

    url2 = "https://spaceimages-mars.com/"

    browser.visit(url2)
    time.sleep(2)
    html2 = browser.html
    soup2 = bs(html2, 'html.parser')

    image_url = soup2.find('img', class_='headerimage fade-in')['src']

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

    # Create an empty list to hold dictionaries of hemisphere title with the image url string
    hemisphere_image_urls = []
    hemisphere_list = soup4.find_all('div', class_='item')
    for item in hemisphere_list:
    
        url = 'https://marshemispheres.com/'
    
        title = item.find('h3').text
        title = title.replace('Enhanced', '')
        link = item.find('a')['href']
        full_link = url + link
    
        executable_path = {'executable_path': 'chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)
        browser.visit(full_link)
        time.sleep(5)
        html = browser.html
        soup = bs(html, 'html.parser')
        
        
        downloads = soup.find('div', class_='downloads')
        image = downloads.find('a')['href']
    
        entry = {title: image}
        hemisphere_image_urls.append(entry)
    
        # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_body": news_body,
        "image_url": image_url,
        "hemisphere_urls": hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return html_data

