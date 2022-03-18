# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:53:21 2022

@author: nonnon519
"""
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


myHeader = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}


class Website(ABC):
 
    def __init__(self, search):
        self.search = search  # 食譜名稱屬性
 
    @abstractmethod
    def scrape(self):  # 爬取食譜抽象方法
        pass
 
class Icook(Website):
    
    def scrape(self):
        
        result = []  # 回傳結果
        
        if self.search :
            url = "https://icook.tw/search/"+ self.search
            rQ = requests.get(url,headers = myHeader).text
            souP = BeautifulSoup(rQ,"html.parser")

            for mySoup in souP.find_all("li","browse-recipe-item"):
                title = mySoup.a.article.find_all("div")[1].div.h2.text.strip()
                auther = mySoup.a.article.find_all("div")[1].div.span.text.strip()
                need = mySoup.a.article.find_all("div")[1].div.p.text.strip()
                #time =  mySoup.a.article.find_all("div")[1].ul.li.text.strip()
                url = "https://icook.tw"+ mySoup.a["href"]
    
                dicT=dict(titlE=title,autheR=auther,neeD=need,uRl=url)
                result.append(dicT)
               
        return result

