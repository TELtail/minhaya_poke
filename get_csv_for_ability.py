import chromedriver_binary # nopa
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import csv
import re

def check_dont_need_text(text_str,check_text):
    if check_text in text_str:
        text_str = text_str.replace(check_text,"")
    
    return text_str

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


driver.get('https://wiki.xn--rckteqa2e.com/wiki/%E3%81%A8%E3%81%8F%E3%81%9B%E3%81%84%E4%B8%80%E8%A6%A7')

skip_ability = []

check_text_list = ["(X)","(Y)","(ピカブイ)","(B2W2)","(ソード)","(シールド)","[dex 1]","B2W2・Y)","BW/B2W2)","X・シールド)","Yまで)"," ","(漢字)","×","○"]

with open("ability.csv","w",newline="", encoding='utf_8_sig') as zukan_csv_file:
    writer = csv.writer(zukan_csv_file)


    time.sleep(2)

    for i in range(267):
        send_button = driver.find_element(By.XPATH,f'//*[@id="mw-content-text"]/div/table/tbody/tr[{str(i+1)}]/td[2]/a')
        ability_name = send_button.get_attribute("title") #特性名取得
        print(i,ability_name)
        send_button.click() #送信ボタンを押す
        if len(driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[1]/div[3]/div[4]/div/dl')) != 1:
            skip_ability.append(ability_name)
            driver.back()
            time.sleep(0.5)
            continue
        poke_scripts = driver.find_elements(By.XPATH,'/html/body/div/div[1]/div[1]/div[3]/div[4]/div/dl/dd') #説明一覧取得
        candidate_list = []
        for scr in poke_scripts:
            text_str = scr.text #説明文を取得
            if re.search("[一-鿐]",text_str): #漢字が入っている説明のみを取得
                for check_text in check_text_list:
                    text_str = check_dont_need_text(text_str,check_text)
                candidate_list.append(text_str) #(漢字)を排除
        
        for selected_text in random.sample(candidate_list,min(1,len(candidate_list))): #テキスト数は最大で5個まで
            print(selected_text)
            writer.writerow([selected_text,ability_name]) #csvに書き込み
        
        driver.back()
        time.sleep(0.5)

    print(skip_ability)
    driver.quit()


