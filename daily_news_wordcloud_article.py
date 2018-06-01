import urllib.request
from bs4 import BeautifulSoup
import re

Url = urllib.request.urlopen("https://www.nytimes.com/2018/05/31/sports/nba-finals-cavs-warriors-score.html")	#20180531일자 스포츠 headline 뉴스
soup = BeautifulSoup(Url, 'html.parser')
soup = soup.find(id="story")
soup = soup.get_text().lower()
soup = re.split("[^a-z]+|\n+",soup)			# 소문자 단어들만 구분 -->don't('don','t')해결이 필요함, 광고 부분은 word cloud에 영향을 미치지 않다고 가정

print(soup)									# 글자들을 나열
