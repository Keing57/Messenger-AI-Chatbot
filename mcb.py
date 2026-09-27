import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    print("Bongeszo inditasa...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.messenger.com/")
    
    try:
        cookie_button = driver.find_element(By.XPATH, "//button[contains(text(), 'összes elfogadása')]")
        cookie_button.click()
        print("Sutik elfogadva!")
        time.sleep(2)
    except:
        print("Nincs suti ablak vagy nem talalhato.")

    try:
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("teszt.bercel@gmail.com")
        print("Email beirva!")
        
        pass_field = driver.find_element(By.ID, "pass")
        pass_field.send_keys("NagyonTitkosJelszo123")
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