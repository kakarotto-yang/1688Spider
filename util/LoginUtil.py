# 模拟登录
import json
import time

from selenium.webdriver.common.by import By
from browserUtil import create_chrome_driver

browser = create_chrome_driver()
browser.get('https://login.taobao.com/?redirect_url=https%3A%2F%2Flogin.1688.com%2Fmember%2Fjump.htm%3Ftarget%3Dhttps%253A%252F%252Flogin.1688.com%252Fmember%252FmarketSigninJump.htm%253FDone%253D%25252F%25252Fdetail.1688.com%25252Foffer%25252F626336974071.html&style=tao_custom&from=1688web')

# 隐式等待
browser.implicitly_wait(10)

# 获取页面元素模拟用户输入和点击行为
username_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-id')
username_input.send_keys('your')  # 填写用户名

password_input = browser.find_element(By.CSS_SELECTOR, '#fm-login-password')
password_input.send_keys('your')  # 填写对应的密码

# 登录按钮
login_button = browser.find_element(By.CSS_SELECTOR, '#login-form > div.fm-btn > button')
login_button.click()

# 显示等待
# wait_obj = WebDriverWait(browser, 10)
# wait_obj.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.m-userinfo')))
time.sleep(30)

# 获取登录的cookie数据，并且写入文件
with open('1688.json', 'w') as file:
    json.dump(browser.get_cookies(), file)

