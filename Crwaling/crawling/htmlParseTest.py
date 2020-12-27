import urllib
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os

soup = BeautifulSoup(urllib.request.urlopen('https://movie.naver.com/movie/bi/mi/point.nhn?code=36944').read(),"html.parser")
review_list = []
title = soup.find('h3', class_='h_movie').find('a').text


html=""

s = requests.Session()
r = s.get("https://movie.naver.com/movie/bi/mi/point.nhn?code=36944")
soup1 = BeautifulSoup(r.content, "html.parser")
iframe_src = soup1.select_one("#pointAfterListIframe").attrs["src"]
r = s.get(f"https://movie.naver.com{iframe_src}")
soup1 = BeautifulSoup(r.content, "html.parser")
'''
f = open("test.html",'w',-1, "utf-8")
f.write(html)
f.close()
'''
div = soup1.find('div', class_='score_result')

data_list = div.select("ul > li")
    
for review in data_list:
    start = review.find("div", class_="star_score").text.strip()
    reply = review.find("div", class_="score_reple")
    comment = reply.find("p").text
#    print(comment)
#    dts=reply.select("dt > em")
    if len(reply.select("dt > em")) ==0:
        continue
     
    date = reply.select("dt > em")[1].text.strip()
    button = review.find("div", class_="btn_area")
    sympathy = button.select("strong")
    good = sympathy[0].text
    bad = sympathy[1].text
 #   print("date:"+date+
 #         "\ncomment:"+comment.strip())
    review_list.append(Review(comment.strip(),date, start, good, bad))