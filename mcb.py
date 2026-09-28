import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "teszt.bercel@gmail.com"
PASSWORD = "NagyonTitkosJelszo123"

def main():
    print("Bongeszo inditasa...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.messenger.com/")
    
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'összes elfogadása')]"))
        )
        cookie_button.click()
        print("Sutik elfogadva!")
    except:
        print("Nincs suti ablak vagy nem talalhato.")

    try:
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(EMAIL)
        print("Email beirva!")
        
        pass_field = driver.find_element(By.ID, "pass")
        pass_field.send_keys(PASSWORD)
        print("Jelszo beirva!")
        
        login_button = driver.find_element(By.ID, "loginbutton")
        login_button.click()
        print("Bejelentkezes gombra kattintva!")
    except:
        print("Hiba a mezok vagy a gomb keresesekor.")
        
    time.sleep(10)
    
    driver.quit()
    print("Bongeszo bezarva.")

if __name__ == "__main__":
    main()