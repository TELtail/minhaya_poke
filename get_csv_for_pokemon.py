import chromedriver_binary # nopa
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import csv

def check_dont_need_text(text_str,check_text):
    if check_text in text_str:
        text_str = text_str.replace(check_text,"")
    
    return text_str

# WebDriver のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


driver.get('https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E4%B8%80%E8%A6%A7')

check_text_list = ["(X)","(Y)","(ピカブイ)","(B2W2)","(ソード)","(シールド)","[dex 1]","B2W2・Y)","BW/B2W2)","X・シールド)","Yまで)"," "]

with open("zukan.csv","w",newline="", encoding='utf_8_sig') as zukan_csv_file:
    writer = csv.writer(zukan_csv_file)


    time.sleep(2)

    for i in range(1,979):
        send_button = driver.find_element(By.XPATH,f'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[{str(i)}]/td[2]/a')
        try: #フォルム違いを排除
            driver.find_element(By.XPATH,f'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[{str(i)}]/td[2]/small')
            time.sleep(0.5)
            continue
        except:
            pass
        pokemon_name = send_button.get_attribute("title") #ポケモン名取得
        print(pokemon_name)
        send_button.click() #送信ボタンを押す
        poke_scripts = driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div/dl[1]/dd') #図巻説明一覧取得
        candidate_list = []
        for scr in poke_scripts:
            text_str = scr.text #図巻説明文を取得
            if pokemon_name not in text_str and "(漢字)" in text_str: #(漢字)の文字が入っていて、そのポケモンの名前自体が入っていない図巻説明のみを取得
                text_str = text_str.replace("(漢字)","")
                for check_text in check_text_list:
                    text_str = check_dont_need_text(text_str,check_text)
                candidate_list.append(text_str) #(漢字)を排除
        
        for selected_text in random.sample(candidate_list,min(5,len(candidate_list))): #テキスト数は最大で5個まで
            print(selected_text)
            writer.writerow([selected_text,pokemon_name]) #csvに書き込み
        
        driver.back()
        time.sleep(0.5)

    driver.save_screenshot(f"./test.png") #スクショ
    driver.quit()


