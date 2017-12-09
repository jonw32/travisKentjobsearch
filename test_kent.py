from selenium import webdriver
import time

#driver = webdriver.Chrome(executable_path="chromedriver")
driver = webdriver.PhantomJS()
driver.get("http://jobs.kent.edu/cw/en-us/listing/")
driver.find_element_by_id('search-keyword').send_keys("Chemistry")
time.sleep(2)

content = driver.find_element_by_id('search-results-contnt')
assert content != None

print("Success The Search Works!!")

for con in content:
    print(con.text)