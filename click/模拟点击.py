# 先安装python3、python3-pip、chromium-driver(会安装各种依赖)，然后输入pip3 install selenium安装selenium库

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')


browser = webdriver.Chrome(options=options)
browser.get("http://www.baidu.com/") # 利用认证系统的跳转特性直接跳转到认证界面

username_='username' # 输入用户名
password_='password' # 输入密码

username = browser.find_element_by_xpath('//*[@id="username"]')
password = browser.find_element_by_xpath('//*[@id="password"]')
username.clear()
username.send_keys(username_)
password.clear()
password.send_keys(password_)


login_btn = browser.find_element_by_xpath('//*[@id="login"]')
login_btn.click()

try:
    # 页面一直循环，直到 id="myDynamicElement" 出现
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="logout-dm"]'))
    )
    print("fff")
finally:
    browser.quit()

browser.quit()
