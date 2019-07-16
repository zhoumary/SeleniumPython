from selenium import webdriver
import time
import selenium.webdriver.chrome.service as service

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.baidu.com')     # set up the destination
time.sleep(5)   # Let the user actually see something!
search_box = driver.find_element_by_name('wd')  # find elements by id/name/tag_name/class_name/css_selector/linke_text/xpath/partial_link_text
search_box.send_keys('ChromeDriver')    # post data in the above element
search_box.submit()     # submit data in form
time.sleep(5)   # Let the user actually see something!

driver.quit()
