import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import config

# ورود به جابینجا
def login_jobinja(driver):
    driver.get("https://jobinja.ir/login")
    time.sleep(2)

    # وارد کردن ایمیل
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(config.JOBINJA_EMAIL)

    # وارد کردن پسورد
    pass_input = driver.find_element(By.NAME, "password")
    pass_input.send_keys(config.JOBINJA_PASSWORD)
    pass_input.send_keys(Keys.RETURN)

    time.sleep(3)

# شروع ربات
def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    login_jobinja(driver)

    print("ورود موفق! (اینجا بعدا میریم سمت ارسال رزومه)")

    driver.quit()

if __name__ == "__main__":
    main()
