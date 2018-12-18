from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Controllers.html_checker import HtmlChecker

import time

SOLS_LOGIN = "https://solss.uow.edu.au/sid/sols_login_auth.do_login"
CHROMEDRIVER_LOC = "./chromedriver"
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
CHROME_OPTIONS.add_argument("--disable-dev-shm-usage")
CHROME_OPTIONS.add_argument("--no-sandbox")

# To be removed


def login(user_usn: str, user_pw: str) -> HtmlChecker:
    driver = webdriver.Chrome(options=CHROME_OPTIONS, executable_path=CHROMEDRIVER_LOC)
    driver.get(SOLS_LOGIN)
    driver.save_screenshot("Login.png")

    user = driver.find_element_by_name("p_username")
    pw = driver.find_element_by_name("p_password")
    loginBtn = driver.find_element_by_xpath("//input[@value='Login']")
    user.send_keys(user_usn)
    pw.send_keys(user_pw)
    loginBtn.click()
    time.sleep(10)
    return navigateLogin(driver)


def navigateLogin(driver: webdriver) -> HtmlChecker:
    driver.save_screenshot("Post_Login.png")
    resultBtn = driver.find_element_by_xpath("//a[@data-id='21']")
    resultBtn.click()
    time.sleep(10)
    driver.save_screenshot("Results.png")
    pageSource = driver.page_source
    HtmlObj = HtmlChecker(pageSource)
    driver.quit()
    return HtmlObj
