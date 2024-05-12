from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from notifypy import Notify
import os
from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client["amazon"]
collection=db["prices"]

# options.add_argument("--headless")
def get_data():
    options=Options()
    with open("products.txt") as f:
        products=f.readlines()
    driver=webdriver.Chrome(options=options)
    i=0
    for product in products:
        driver.get(f"https://www.amazon.in/dp/{product}")
        # i+=1
        page_source=driver.page_source
        with open(f"data/{product.strip()}.html","w",encoding="utf-8") as f:
            f.write(page_source)
def extract_data():
    files=os.listdir("data")
    for file in files:
        print(file)
        with open(f"data/{file}",encoding="utf-8") as f:
            content=f.read()
        soup=BeautifulSoup(content,'html.parser')
        title=soup.title.getText().split(":")[0]
        time=datetime.now()


        # print(soup.title)
        price=soup.find(class_="a-price-whole")
        priceInt=price.getText()
        table=soup.find(id="productDetails_detailBullets_sections1")
        asin=table.find(class_="prodDetAttrValue").getText().strip()

        print(priceInt,asin,title,time)
        collection.insert_one({"priceInt":priceInt,"asin":asin,"title":title,"time":time})

        with open("finaldata.txt","a") as f:
            f.write(f"{priceInt}~~{asin}~~{title}~~{time}\n")
            





if __name__=="__main__":
    notification=Notify()
    notification.title="Extracting Data"
    notification.message="Extracting data from amazon"
    notification.send()
    get_data()
    extract_data()


    
