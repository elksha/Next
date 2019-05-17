from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

word = input('검색어를 입력해주세요.')

driver = webdriver.Chrome('./chromedriver')
driver.get(f'https://search.naver.com/search.naver?where=realtime&sm=tab_nmr&query={word}')

more_button = driver.find_element_by_class_name('_moreBtn')

for _ in range(3):
    more_button.click()
    sleep(1)

tweets = driver.find_elements_by_css_selector('#realTimeSearchBody > div.rt_wrap.rt_typ2 > div:nth-child(1) > ul:nth-child(1) > li > dl > dd:nth-child(2) > a')

texts = [tweet.text for tweet in tweets]

with open('result.txt', 'w', encoding='utf-8') as f:
    for text in texts:
        f.write(text+'\n')

driver.quit()