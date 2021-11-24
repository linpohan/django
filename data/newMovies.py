# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:03:31 2021

@author: User
"""

import requests
from bs4 import BeautifulSoup
import db

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
data = requests.get(url)
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data, 'html.parser')

newMovies = sp.find('ul', class_ = 'release_list')
newMovies = newMovies.find_all('li')

for row in newMovies:
    title = row.find('div', class_ = 'release_info').find('a').text.strip()
    img = row.find('div', class_ = 'release_foto').find('img').get('src')
    url = row.find('div', class_ = 'release_info').find('a').get('href')
    content = row.find('span', class_ = 'jq_text_overflow_180 jq_text_overflow_href_list').text.strip()
    date = row.find('div', class_ = 'release_movie_time').text    
    print(date)
#     sql = "SELECT id FROM newmovie WHERE url='{}'".format(url)
#     db.cursor.execute(sql)
#     db.conn.commit()
    
#     if db.cursor.rowcount == 0:
#         sql = """
#             INSERT INTO newmovie(title, img, url, content, date)
#             VALUES('{}', '{}', '{}', '{}', '{}')
#         """.format(title, img, url, content, date)
#         db.cursor.execute(sql)
#         db.conn.commit()
        
# db.conn.close()
    