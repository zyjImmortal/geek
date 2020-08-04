from typing import List

from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")

driver = webdriver.Chrome(chrome_options=option, executable_path="drivers/chromedriver")

driver.get("https://www.sohu.com/")

# driver.set_window_size(600, 800)
#
# js = "document.getElementById('train_date').removeAttribute('readonly')"
#
# driver.execute_script(js)
#
# driver.find_element_by_id('train_date').clear()
# time.sleep(2)
# driver.find_element_by_id("train_date").send_keys("2020-04-05")
#
# alert = driver.switch_to.alert
#
# alert.accept()
# alert.dismiss()
# alert.send_keys("")

window = driver.current_window_handle  # 获取当前窗口的句柄

driver.find_element_by_link_text("新闻").click()


# windows = driver.window_handles # 获取所有当前浏览器句柄
# for current_window in windows:
#     if current_window != window:
#         driver.switch_to.window(current_window)  # 切换新打开window
#
# time.sleep(2)

# driver.switch_to_window(windows[-1])
# driver.switch_to.window(windows[-1])

# 验证码


