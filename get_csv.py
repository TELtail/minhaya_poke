import chromedriver_binary # nopa
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


driver.get('https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E4%B8%80%E8%A6%A7')






loop_flag = True
i = 1
time.sleep(2)

while loop_flag:
    send_button = driver.find_element(By.XPATH,f'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[{str(i)}]/td[2]/a')
    pokemon_name = send_button.get_attribute("title")
    print(pokemon_name)
    send_button.click() #送信ボタンを押す
    driver.back()
    i+=1
driver.save_screenshot(f"./test.png") #スクショ
#driver.quit()