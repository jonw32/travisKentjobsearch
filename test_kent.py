from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("http://jobs.kent.edu/cw/en-us/listing/")
driver.find_element_by_id('search-keyword').send_keys("Chemistry")
time.sleep(2)

content = driver.find_element_by_id('search-results-content')
assert content != None

print("Sucess! Your searchBar returns values")