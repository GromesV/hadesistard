from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait 
import selenium.webdriver.support.expected_conditions as EC

import os
import time
import paths


USERNAME = 'ASDFADF'
PASSWORD = 'ADFADF'

def f(param):
    return driver.find_element(By.XPATH, param)



def sel(path, index):
    selectlogin = f(path)
    sel = Select(selectlogin)
    sel.select_by_index(index)


s = Service(r"D:\chromedriver\chromedriver.exe")


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options, service=s)
driver.get('https://support.heroesandgenerals.com')
f(paths.usernamepath).send_keys(USERNAME)
f(paths.passwordpath).send_keys(PASSWORD)
f(paths.submitloginpath).click()
f(paths.usernamepath).send_keys(USERNAME)
f(paths.passwordpath).send_keys(PASSWORD)
f(paths.submitloginpath).click()
driver.get('https://handg.kayako.com/Tickets/Submit')
f('/html/body/div[1]/div/a').click()
time.sleep(10)
element = f(paths.techsupportpath)
driver.execute_script("arguments[0].scrollIntoView();", element)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, paths.techsupportpath))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, paths.actiongamepath))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, paths.nextpath))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, paths.steampath))).click()
sel(paths.selectloginpath, 1)
sel(paths.joinbattlespath, 3)
sel(paths.actiongamecrashpath, 1)
os.system("dxdiag /t D:\diag.txt")
time.sleep(30)
cf = f(paths.dxdiagfileuploadpath)
cf.send_keys(r"D:\diag.txt")
sel(paths.errmsgpath, 2)
sel(paths.opsystempath, 3)
f(paths.subjectpath).send_keys('My game has crashed :( ')
f(paths.agreepath).click()