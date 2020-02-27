from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://192.168.1.120:8000/portals-web/login.jsp")
driver.implicitly_wait(4)

driver.find_element_by_name("userId").clear()
driver.find_element_by_name("userId").send_keys("admin")
driver.find_element_by_name("passwd").clear()
driver.find_element_by_name("passwd").send_keys("123456")
driver.find_element_by_link_text("登录").click()
