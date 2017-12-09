from selenium import webdriver
import time

#driver = webdriver.Chrome(executable_path="chromedriver")
driver = webdriver.PhantomJS()
driver.get("http://jobs.kent.edu/cw/en-us/listing/")
driver.find_element_by_id('search-keyword').send_keys("Chemistry")
time.sleep(2)

content = driver.find_element_by_id('search-results-content')
assert content != None

rows = content.find_elements_by_css_selector('td')
print("Success The Search Works!! Here is What We Found")

for row in rows:
    print(row.text)