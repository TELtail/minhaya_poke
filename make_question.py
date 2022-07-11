import csv
import time
import pyautogui as p
import pyperclip


with open('zukan.csv', 'r' ,encoding="utf_8") as f:
    zukan_data = csv.reader(f)
    

    for one_row in zukan_data:
        zukan_script, pokemon_name = one_row[0],one_row[1]
        p.click(518,941) #問題追加ボタン
        p.click(209,210) #問題欄
        time.sleep(0.5)
        pyperclip.copy(zukan_script)
        p.hotkey("ctrl","v")
        p.click(224,349) #解答欄
        time.sleep(0.5)
        pyperclip.copy(pokemon_name)
        p.hotkey("ctrl","v")
        p.click(86,423) #自動生成
        p.click(448,593) #ok
        time.sleep(1)
        p.click(177,559) #保存
        time.sleep(0.5)
        p.click(448,593) #ok
        time.sleep(2)
        
        