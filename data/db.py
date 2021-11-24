# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:41:27 2021

pip install PyMySQL
AppServ
CMD : mysql -u root -p

@author: USER
"""

import pymysql

conn = pymysql.connect(
                        host = '127.0.0.1', #本地端,localhost
                        user = 'root',
                        passwd = 'Auo780502',
                        db = 'movies'
)

cursor = conn.cursor() #資料集






