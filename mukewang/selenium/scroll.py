from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")

driver = webdriver.Chrome(chrome_options=option, executable_path="drivers/chromedriver")

driver.get("https://www.jd.com")

driver.set_window_size(600, 800)

js = "window.scrollTo(20000, 10000)"

driver.execute_script(js)