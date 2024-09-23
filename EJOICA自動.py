from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
import time  

# ギフトIDのリスト  
gift_ids = [     
    "コード1",
    "コード2",
    "コード3",
    # 必要な数だけコードを追加してください
]  

# 取得したクレームコードを保存するリスト  
claim_codes = []  

# WebDriverの初期化（Chromeの場合）  
driver = webdriver.Chrome()  

for gift_id in gift_ids:  
    try:  
        # サイトにアクセス  
        driver.get("https://atgift.jp/user/item/ejoica/")  

        # 「登録サイトはこちら」をクリック  
        register_link = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.CLASS_NAME, "btnMain"))  
        )  
        register_link.click()  

        # 新しいタブに切り替え  
        driver.switch_to.window(driver.window_handles[-1])  

        # IDを入力  
        gift_id_input = WebDriverWait(driver, 10).until(  
            EC.presence_of_element_located((By.ID, "giftID"))  
        )  
        gift_id_input.clear()  
        gift_id_input.send_keys(gift_id)  

        # 「同意して次へ」をクリック  
        next_button = driver.find_element(By.XPATH, "//img[@alt='同意して次へ']")  
        next_button.click()  

        # 「登録サイトへ」をクリック  
        register_site_button = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='登録サイトへ']"))  
        )  
        register_site_button.click()  

        # メールアドレスを入力  
        email_input = WebDriverWait(driver, 10).until(  
            EC.presence_of_element_located((By.ID, "mailID"))  
        )  
        email_input.clear()  
        email_input.send_keys("sue.satoshi2@gmail.com")  

        # ページの読み込みを待機  
        WebDriverWait(driver, 10).until(  
            lambda d: d.execute_script('return document.readyState') == 'complete'  
        )  

        # 「次へ」ボタンを探してクリック  
        next_button = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='次へ']"))  
        )  
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)  
        driver.execute_script("arguments[0].click();", next_button)  

        # 「交換する」ボタンを探してクリック  
        exchange_button = WebDriverWait(driver, 10).until(  
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='交換する']"))  
        )  
        driver.execute_script("arguments[0].scrollIntoView(true);", exchange_button)  
        driver.execute_script("arguments[0].click();", exchange_button)  

        # クレームコードを取得  
        claim_code_element = WebDriverWait(driver, 10).until(  
            EC.presence_of_element_located((By.ID, "claimCode"))  
        )  
        claim_code = claim_code_element.text.strip()  
        claim_codes.append((gift_id, claim_code))  
        print(f"ギフトID {gift_id} のクレームコード: {claim_code}")  

        # クリップボードにコピー（オプション）  
        # import pyperclip  
        # pyperclip.copy(claim_code)  
        # print("クレームコードがクリップボードにコピーされました。")  

        # タブを閉じて最初のタブに戻る  
        driver.close()  
        driver.switch_to.window(driver.window_handles[0])  

    except Exception as e:  
        print(f"ギフトID {gift_id} の処理中にエラーが発生しました: {e}")  
        # タブを閉じて最初のタブに戻る  
        driver.close()  
        driver.switch_to.window(driver.window_handles[0])  
        continue  

# すべてのクレームコードをまとめて出力  
print("\n取得したクレームコード一覧:")  
for gift_id, code in claim_codes:  
    print(f"ギフトID: {gift_id} -> クレームコード: {code}")  

# ブラウザを閉じる前に少し待機  
time.sleep(5)  

# ブラウザを閉じる  
driver.quit()
