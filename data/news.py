# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 09:06:49 2021

@author: User
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import db

path = 'D:/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

url = 'https://movies.yahoo.com.tw/tagged/movieheadline'
driver.get(url)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

sp = BeautifulSoup(driver.page_source, 'html.parser')

news = sp.find('ul', class_ = 'news_list')
news = news.find_all('li', class_ = 'news_content')

for row in news:
    title = row.find('h2', class_ = 'text_truncate_2').text
    img = row.find('img').get('src')
    img = img.split('--/')[-1]
    content = row.find('span', class_ = 'jq_text_overflow_150 jq_text_overflow_link').text.strip()
    link = row.find('a').get('href')
    date = row.find('div', class_ = 'day').text
    
    sql = "SELECT id FROM new WHERE link='{}'".format(link)
    db.cursor.execute(sql)
    db.conn.commit()
    
    if db.cursor.rowcount == 0:
        sql="""
            INSERT INTO new(title, img, content, link, date)
            VALUES('{}', '{}', '{}', '{}', '{}')
        """.format(title, img, content, link, date)
        
        db.cursor.execute(sql)
        db.conn.commit()
            
db.conn.close()
    
driver.close()
