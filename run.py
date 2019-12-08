from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from getpass import getpass
import time

chrome_options = Options()
    
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=chrome_options)
driver.get('https://msi.co1.qualtrics.com/jfe/form/SV_01ahxHyi7TdhU3j')

time.sleep(60)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID1-2-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

Select(driver.find_element_by_id('QR~QID3')).select_by_visible_text('United States of America')
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID4-3-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID77-5-label').click()
time.sleep(1)

driver.find_element_by_id('QID77-2-label').click()
time.sleep(1)

driver.find_element_by_id('QID77-3-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_xpath('//label[@for="QR~QID7~1~34"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~2~33"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~3~33"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~4~34"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~5~34"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~6~36"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~7~35"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~8~36"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID7~9~36"]').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID8-2-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID79-2-label').click()
time.sleep(1)

driver.find_element_by_id('QID79-4-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID36-3-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID37-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID38-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_xpath('//label[@for="QR~QID39~1~1"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID39~2~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID39~3~3"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID39~4~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID39~5~1"]').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_xpath('//label[@for="QR~QID40~1~1"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID40~2~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID40~3~3"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID40~4~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID40~5~1"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID40~6~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID40~7~3"]').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_xpath('//label[@for="QR~QID41~1~1"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID41~2~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID41~3~3"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID41~4~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID41~5~1"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID41~6~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID41~7~3"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID41~8~2"]').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID42-2-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID43-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QR~QID44~1~TEXT').send_keys('500')
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID47-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID48-79-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID82-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID45-47-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_xpath('//label[@for="QR~QID46~10"]').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QR~QID49').send_keys('Better Documentation.')
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID50-4-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_xpath('//label[@for="QR~QID51~1~4"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID51~8~3"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID51~9~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID51~10~4"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID51~11~3"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID51~12~2"]').click()
time.sleep(1)

driver.find_element_by_xpath('//label[@for="QR~QID51~13~4"]').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID53-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID54-4-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID55-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID56-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID57-12-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID58-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QID61-1-label').click()
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QR~QID62').send_keys('hi@shivamgoyal.co')
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(2)

driver.find_element_by_id('QR~QID63').send_keys('hi@shivamgoyal.co')
time.sleep(1)

driver.find_element_by_id('NextButton').click()
time.sleep(5)

print('YaY! You just filled the survey.')
driver.close()