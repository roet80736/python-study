from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://192.168.1.120:29002/login?from=%2F")
driver.implicitly_wait(3)

# 登录
# above = driver.find_element_by_id("lbNormal")
# ActionChains(driver).move_to_element(above).perform()
# driver.implicitly_wait(3)
driver.find_element_by_id("j_username").clear()
driver.find_element_by_name("j_username").send_keys("admin")
driver.find_element_by_name("j_password").clear()
driver.find_element_by_name("j_password").send_keys("admin")
driver.find_element_by_xpath('/html/body/div/div/form/div[4]/input').click()
driver.find_element_by_link_text("退出").click()
driver.quit()
