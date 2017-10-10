import time
from selenium import webdriver
from decouple import config

HOME = config('HOME')
driver = webdriver.Chrome(executable_path=HOME + '/chromedriver/chromedriver')
driver.maximize_window()
time.sleep(0.5)

url = 'http://www.imdb.com/chart/top'
driver.get(url)
