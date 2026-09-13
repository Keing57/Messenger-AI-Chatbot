import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    print("Bongeszo inditasa...")
    driver = webdriver.Chrome()
    driver.get("https://www.messenger.com/")
    
    try:
        email_field = driver.find_element(By.ID, "email")
        print("Email mezo megvan!")
        
        pass_field = driver.find_element(By.ID, "pass")
        print("Jelszo mezo is megvan!")
    except:
        print("Valamelyik beviteli mezo hianyzik.")
        
    time.sleep(5)
    
    driver.quit()
    print("Bongeszo bezarva.")

if __name__ == "__main__":
    main()