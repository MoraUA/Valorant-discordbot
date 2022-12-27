from selenium import webdriver
from fake_useragent import UserAgent


userAgent = UserAgent()
def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={userAgent.random}")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(executable_path='D:\\python\\chromedrivers\\chromedriver.exe', options=options)
    return driver
    





