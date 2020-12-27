import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

class Review:
    def __init__(self,comment,date,star,good,bad):
        self.comment = comment
        self.date = date
        self.star = star
        self.good = good
        self.bad = bad
        
    
    def show(self):
        print("내용:" + self.comment+
              "\n날짜: "+self.date+
              "\n별점: "+self.star+
              "\n좋아요: "+self.good+
              "\n싫어요: "+self.bad)

def crawl(url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read(),"html.parser")
   
   # parentPath=url[0:url.find("/movie/bi")-1]
    parentPath=url.split("/movie/bi")[0]
    #https://stackoverflow.com/questions/54522364/python-beautifulsoup-scrape-web-content-inside-iframes
    #iframe 불러오는 부분 참고
    s = requests.Session()
    r = s.get(url)
    soup1 = BeautifulSoup(r.content, "html.parser")
    iframe_src = soup1.select_one("#pointAfterListIframe").attrs["src"]
    r = s.get(f"{parentPath}{iframe_src}")
    soup1 = BeautifulSoup(r.content, "html.parser")
    
    review_list = []
    title = soup.find('h3', class_='h_movie').find('a').text
    div = soup1.find('div', class_='score_result')
    data_list = div.select("ul > li")
    
    for review in data_list:
        start = review.find("div", class_="star_score").text.strip()
        reply = review.find("div", class_="score_reple")
        comment = reply.find("p").text
#        print(comment)
#        dts=reply.select("dt > em")
        if len(reply.select("dt > em")) ==0:
            continue
        date = reply.select("dt > em")[1].text.strip()
        
        button = review.find("div", class_="btn_area")
        sympathy = button.select("strong")
        good = sympathy[0].text
        bad = sympathy[1].text
        review_list.append(Review(comment.strip(),date, start, good, bad))
        
    return title, review_list

'''
title, review_list = crawl("https://movie.naver.com/movie/bi/mi/point.nhn?code=36944")
print("제목:" + title)
for review in review_list:
    review.show() 
'''

def get_summary(review_list):
    star_list = []
    good_list = []
    bad_list = []
    
    for review in review_list:
        star_list.append(int(review.star))
        good_list.append(int(review.good))
        bad_list.append(int(review.bad))
    
    star_series = pd.Series(star_list)
    good_series = pd.Series(good_list)
    bad_series = pd.Series(bad_list)
       
    summary = pd.DataFrame({
        'Star': star_series,
        'Good': good_series,
        'Bad': bad_series,
        'Score': good_series / (good_series+bad_series)
        })
    
    return summary

def movie_compare(review_lists):
    count = 1
    x = []
    y = []
    for movie, review_list in review_lists:
        x.append(count)
        summary = get_summary(review_list)
        summary = summary[summary['Score']>0.8]
        y.append(summary['Star'].mean())
        count += 1
        
    plt.bar(x,y)
    plt.title('영화 평점 비교',fontproperties=font_name)
    plt.xlabel('영화 번호',fontproperties=font_name)
    plt.ylabel('신뢰성 별점 평균',fontproperties=font_name)
    plt.show()
    
movie_code_list = [136900,167657,174321,184859,194811]
review_lists = []

for i in movie_code_list:
    title, review_list = crawl("https://movie.naver.com/movie/bi/mi/point.nhn?code="+str(i))
    summary = get_summary(review_list)
    print("[%s ]" % (title))
    print(summary)
    review_lists.append((title, review_list))
    
font_location = 'C:/Windows/Fonts/malgunsl.ttf' # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()

    
movie_compare(review_lists)

    