import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class MessengerBot:
    def __init__(self, email, password, headless=False):
        self.email = email
        self.password = password
        
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
            
        self.driver = webdriver.Chrome(options=chrome_options)
        if not headless:
            self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.messenger.com/")
        
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'összes elfogadása')]"))
            )
            cookie_button.click()
        except:
            pass

        try:
            email_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            email_field.send_keys(self.email)
            
            pass_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "pass"))
            )
            pass_field.send_keys(self.password)
            
            login_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "loginbutton"))
            )
            login_button.click()
        except:
            pass

    def verify_login(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_changes("https://www.messenger.com/")
            )
        except:
            pass

    def search_user(self, name):
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='search']"))
            )
            search_input.send_keys(name)
        except:
            pass

    def select_first_result(self):
        try:
            first_result = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//div[@role='button']"))
            )
            first_result.click()
        except:
            pass

    def send_message(self, message):
        try:
            msg_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Üzenet írása' and @role='textbox']"))
            )
            msg_box.send_keys(message)
            time.sleep(1)
            msg_box.send_keys(Keys.RETURN)
        except:
            pass

    def close(self):
        self.driver.quit()

def main():
    bot = None
    try:
        bot = MessengerBot("teszt.bercel@gmail.com", "NagyonTitkosJelszo123", headless=False)
        bot.login()
        bot.verify_login()
        bot.search_user("Teszt Elek")
        bot.select_first_result()
        bot.send_message("Szia! Ez egy automatikus teszt uzenet a python bottol xd.")
        time.sleep(5)
    finally:
        if bot:
            bot.close()

if __name__ == "__main__":
    main()