from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get('www.baidu.com')
print(browser.current_url)
