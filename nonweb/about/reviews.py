# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:50:20 2022

@author: nonnon519
"""
import db
from requests import session
import json

s = session()
stopRes = ")]}'\n[null,null,null," #空值所出現的內容

pretext = ")]}\'" # 為了資安而設計的特殊字元
count = 0
pagetext =''
lisT = []

url = "https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3776617829798604783!2y4821236543880116526!2m2!1i{}0!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s8RorYp_5DsqlwAPMsrWQBw!7e81"


rQ = s.get(url.format(pagetext)).text
while rQ.startswith(stopRes) is not True:
    
    
    pagetext = str(count)
    rQ = s.get(url.format(pagetext)).text
 
    text = rQ.replace(pretext,'')

    soup = json.loads(text)
    need = soup[2]
    lisT.append(need)
    count += 1
    
    if count == 15:
        break
    
for i in lisT :
    for j in i :
        print("username:"+ str(j[0][1]))
        auther = str(j[0][1])
        #print("time:"+ str(j[1]))
        review_date = str(j[1])
        #print("comment:"+ str(j[3]))
        comment = str(j[3])
        #print("grade:"+str(j[4]))
        grade = str(j[4])
        print("-------------------------------------------------------")
        
        sql = "select id,grade from reviews where auther='{}'".format(auther)
        db.cursor.execute(sql)
        db.conn.commit()
        
        if db.cursor.rowcount == 0:
            sql = "insert into reviews(auther,review_date,comment,grade) values('{}','{}','{}','{}')".format(auther,review_date,comment,grade)
            db.cursor.execute(sql)
            db.conn.commit()
        else:
            result = db.cursor.fetchone()
            if grade != result[1]:
                sql = "update reviews set grade='{}' where id='{}'".format(grade,result[0])
                db.cursor.execute(sql)
                db.conn.commit()
db.conn.close()


