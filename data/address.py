# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:56:04 2021

@author: User
"""

import requests
from bs4 import BeautifulSoup
import db


url = 'https://movies.yahoo.com.tw/theater_list.html'
data = requests.get(url, 'html.parser')
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data, 'html.parser')

address = sp.find('div', id = 'content_l')
address = address.find_all('li')
    
for row in address:
    try:
        title = row.find('div', class_ = 'name').text.strip()
        add = row.find('div', class_ = 'adds').text
        url = row.find('div', class_ = 'name').find('a').get('href')
        tel = row.find('div', class_ = 'tel').text.strip()

        sql = "SELECT id FROM `address` WHERE url='{}'".format(url)
        db.cursor.execute(sql)
        db.conn.commit()
        
        if db.cursor.rowcount == 0:
            sql="""
                INSERT INTO `address`(`title`, `add`, `url`, `tel`)
                VALUES('{}', '{}', '{}', '{}')
            """.format(title, add, url, tel)
            
            db.cursor.execute(sql)
            db.conn.commit()
    except Exception as e:
        print(e)

        
db.conn.close()
        