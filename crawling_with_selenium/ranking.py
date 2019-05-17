import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(data, 'html.parser')
news_title = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k')
title_array = []
for title in news_title:
    title_array.append(title.get_text())

a = 0
print("네이버 검색 순위")
for i in title_array:
    a += 1 
    print(str(a)+". "+i)