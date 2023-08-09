from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Nastaran\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("http://localhost:3000")

time.sleep(3)
driver.find_element_by_id("loginbtn").click()
time.sleep(3)

driver.find_element_by_link_text("Signup/Login as a candidate").click()

driver.find_element_by_css_selector("input.whsOnd.zHQkBf").send_keys("saragary30@gmail.com")
time.sleep(3)
driver.find_element_by_xpath("//span[text()='Next']").click()
# saragary30@gmail.com
time.sleep(3)
driver.find_element_by_css_selector("input.whsOnd.zHQkBf").send_keys("SG1234!ara")
# time.sleep(2)
# driver.find_element_by_xpath("//span[text()='Next']").click()
