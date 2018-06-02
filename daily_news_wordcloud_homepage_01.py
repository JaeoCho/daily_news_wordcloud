import urllib.request
from bs4 import BeautifulSoup
import re
import os
import date_time_check

DATE = date_time_check

def plus_zero(num):
	if num < 10:
		return '0'+str(num)
	else:
		return str(num)

Url = urllib.request.urlopen("https://www.nytimes.com/section/sports")
soup = BeautifulSoup(Url, 'html.parser')

link_list=[]

today_year = DATE.YEAR
today_month = DATE.MONTH
today_day = DATE.DAY

for link in soup.find_all('a'):
    if str(today_year)+"/"+plus_zero(today_month)+"/"+plus_zero(today_day) in link.get('href'):
        if link.get('href') in link_list:
            a=1
        else:
            link_list.append(link.get('href'))

for i in link_list:
    print(i)