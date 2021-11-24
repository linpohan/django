# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:41:29 2021

@author: User
"""

import requests
from bs4 import BeautifulSoup
import db
#https://movies.yahoo.com.tw/chart.html?cate=us
url = 'https://movies.yahoo.com.tw/chart.html'
data = requests.get(url, 'html.parser')
data.encoding = 'UTF-8'
data = data.text
sp = BeautifulSoup(data)

rank = sp.find('div', class_ = 'rank_list table rankstyle1')
rank = rank.find_all('div', class_ = 'tr')

for row in rank:
    try:
        num = row.find('div', class_ = 'td').text
        if len(num) < 2:
            num = '0'+num
        title = row.find('div', class_ = 'rank_txt').text.strip()
        star = row.find('div', class_ = 'td starwithnum').text.strip()
        link = row.find('a').get('href')
        
        sql = "SELECT num,title,star,link FROM `rank` WHERE link='{}'".format(link)
        db.cursor.execute(sql)
        db.conn.commit()
        
        if db.cursor.rowcount == 0:
            sql = """
                INSERT INTO `rank`(num, title, star, link)
                VALUES('{}', '{}', '{}', '{}')
            """.format(num, title, star, link)
            db.cursor.execute(sql)
            db.conn.commit()        
        else:
            result = db.cursor.fetchone()
            if star != result[2]:
                sql = "UPDATE `rank` SET star='{}' WHERE num='{}'".format(star,result[0])
                db.cursor.execute(sql)
                db.conn.commit()  
            elif title != result[1]:
                sql = "UPDATE `rank` SET title='{}' WHERE num'{}'".format(title,result[0])
                db.cursor.execute(sql)
                db.conn.commit() 
            else:
                link != result[3]
                sql = "UPDATE `rank` SET link='{}' WHERE num'{}'".format(link,result[0])
                db.cursor.execute(sql)
                db.conn.commit()
        
    except:
        try:
            num = row.find('div', class_ = 'td').text
            if len(num) < 2:
                num = '0'+num
            title = row.find('h2').text.strip()
            star = row.find('h6').text.strip()
            link = row.find('a').get('href')
            
            sql = "SELECT id,star,num FROM `rank` WHERE link='{}'".format(link)
            db.cursor.execute(sql)
            db.conn.commit()
            
            if db.cursor.rowcount == 0:
                sql = """
                    INSERT INTO `rank`(num, title, star, link)
                    VALUES('{}', '{}', '{}', '{}')
                """.format(num, title, star, link)
                db.cursor.execute(sql)
                db.conn.commit()        
            else:
                result = db.cursor.fetchone()
                if star != result[2]:
                    sql = "UPDATE `rank` SET star='{}' WHERE num='{}'".format(star,result[0])
                    db.cursor.execute(sql)
                    db.conn.commit()  
                elif title != result[1]:
                    sql = "UPDATE `rank` SET title='{}' WHERE num'{}'".format(title,result[0])
                    db.cursor.execute(sql)
                    db.conn.commit() 
                else:
                    link != result[3]
                    sql = "UPDATE `rank` SET link='{}' WHERE num'{}'".format(link,result[0])
                    db.cursor.execute(sql)
                    db.conn.commit()
        except Exception as e:
            print(e)

db.conn.close()