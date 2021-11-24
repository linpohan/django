# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:03:27 2021

@author: User
"""

import requests
from bs4 import BeautifulSoup
import db

for num in range(1,8):
    url = 'https://movies.yahoo.com.tw/movie_comingsoon.html?page={}'.format(num)
    data = requests.get(url, 'html.parser')
    data.encoding = 'UTF-8'
    data = data.text
    sp = BeautifulSoup(data)
    
    comingMovies = sp.find('ul', class_ = 'release_list')
    comingMovies = comingMovies.find_all('li')
    
    for row in comingMovies:
        title = row.find('div', class_ = 'release_info').find('a').text.strip()
        img = row.find('div', class_ = 'release_foto').find('img').get('src')
        url = row.find('div', class_ = 'release_info').find('a').get('href')
        content = row.find('span', class_ = 'jq_text_overflow_180 jq_text_overflow_href_list').text.strip()
        date = row.find('div', class_ = 'release_movie_time').text
        
        sql = "SELECT id FROM comingmovie WHERE url='{}'".format(url)
        db.cursor.execute(sql)
        db.conn.commit()
        try:
            if db.cursor.rowcount == 0:
                sql = """
                    INSERT INTO comingmovie(title, img, url, content, date)
                    VALUES('{}', '{}', '{}', '{}', '{}')
                """.format(title, img, url, content, date)
                db.cursor.execute(sql)
                db.conn.commit()
        except Exception as e:
            print(e)
            
            
db.conn.close()
        