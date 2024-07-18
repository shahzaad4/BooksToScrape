from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://books.toscrape.com/"
driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/index.html")

soup=BeautifulSoup(driver.page_source,'html.parser')

books_data = []

def scrape_data(soup):
    items= soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for item in items:
        title= item.h3.a['title']
        price=item.find('p',class_="price_color").text
        stock=item.find('p',class_="instock availability").text
        
        rating_class= item.p['class']
        rating_dict={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
        rating=rating_dict[rating_class[1]]
        books_data.append([title,price,stock,rating])
    
        

while True:
    scrape_data(soup)
    
    try:
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
        time.sleep(2)
        
        next_button=driver.find_element(By.CSS_SELECTOR,"#default > div > div > div > div > section > div:nth-child(2) > div > ul > li.next > a")
        next_button.click()
        time.sleep(2)
    except (NoSuchElementException, ElementNotInteractableException):
        break
    
df=pd.DataFrame(books_data,columns=['Title','Price','Stock Availability','Rating'])
df.to_csv('books_data.csv',index=True)
print(df)