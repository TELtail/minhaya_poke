import chromedriver_binary # nopa
from selenium import webdriver
import time

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get('https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E4%B8%80%E8%A6%A7')


time.sleep(1)
#driver.quit()