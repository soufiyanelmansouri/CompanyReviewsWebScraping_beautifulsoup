# import libraries 

from curses.ascii import isdigit
from bs4 import BeautifulSoup
import requests
import datetime
import helper

i = 1
while i < 3: 
    # Connect to the Website and pull in data
    URL = f'https://www.trustpilot.com/review/aardy.com?page={i}'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)
    response = BeautifulSoup(page.content, "html.parser")
    soup =  BeautifulSoup(response.prettify(), "html.parser")

    # extracet data from html
    website = soup.find('span', class_="styles_suffix__2BIZf")
    reviews_count = soup.find('span', class_="typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-7__9Ut3K typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_text__W4hWi")
    starts = soup.find('p', class_="typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-7__9Ut3K typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3")
    
    # Clean up the data a little bit
    website = website.text.strip()
    reviews_count = reviews_count.text.strip()
    starts = starts.text.strip()
    reviews = soup.find_all('div', class_="paper_paper__1PY90 paper_square__lJX8a card_card__lQWDv card_noPadding__D8PcU styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ")

    # this method removes all white spaces
    reviews_count = helper.get_reviews_count(reviews_count)

    # print all data

    # this method get what people says about the product
    helper.extract_reviews(reviews)
    i += 1
    
print('Company web site: ',website)
print('Company reviews: ',reviews_count)
print('Company stars: ',starts)