import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MessengerBot:
    def __init__(self, email, password):
        print("Bongeszo inditasa...")
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.messenger.com/")
        
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'összes elfogadása')]"))
            )
            cookie_button.click()
            print("Sutik elfogadva!")
        except:
            print("Nincs suti ablak vagy nem talalhato.")

        try:
            email_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_field.send_keys(self.email)
            print("Email beirva!")
            
            pass_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "pass"))
            )
            pass_field.send_keys(self.password)
            print("Jelszo beirva!")
            
            login_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "loginbutton"))
            )
            login_button.click()
            print("Bejelentkezes gombra kattintva!")
        except:
            print("Hiba a mezok vagy a gomb keresesekor.")

    def verify_login(self):
        print("Bejelentkezes ellenorzese...")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_changes("https://www.messenger.com/")
            )
            print("Sikeres tovabblepes a bejelentkezo oldalrol!")
        except:
            print("Nem valtozott az URL, valoszinuleg hibasak a belepesi adatok (teszt).")

    def close(self):
        self.driver.quit()
        print("Bongeszo bezarva.")

def main():
    bot = MessengerBot("teszt.bercel@gmail.com", "NagyonTitkosJelszo123")
    bot.login()
    bot.verify_login()
    bot.close()

if __name__ == "__main__":
    main()