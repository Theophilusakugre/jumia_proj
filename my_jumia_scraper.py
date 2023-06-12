# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:50:39 2022

@author: MTL9
"""


from selenium import webdriver
import pandas as pd
import time

chromedriver = "C:/Users/MTL9/Downloads/chromedriver_win32 (2)/chromedriver.exe"

driver=webdriver.Chrome(chromedriver)

url='https://www.jumia.com.gh'

driver.get(url)

popp=driver.find_element_by_xpath('//*[@id="pop"]/div/section/button')
popp.click()

what_iam_searching=driver.find_element_by_xpath('//*[@id="fi-q"]')
what_iam_searching.send_keys('headset')
ok_search=driver.find_element_by_xpath('//*[@id="search"]/button')
ok_search.click()
time.sleep(3)

name=[]
price=[]
old_price=[]
rating=[]
name_info=driver.find_elements_by_class_name('name')
for i in name_info:
    name.append(i.text)
price_info=driver.find_elements_by_class_name('prc') 
for i in price_info:
    price.append(i.text)
old_info=driver.find_elements_by_class_name('s-prc-w')
for i in old_info:
    old_price.append(i.text)
ratin=driver.find_elements_by_class_name('rev')
for i in ratin:
    rating.append(i.text)

driver.quit()

#time.sleep(5)
df=pd.DataFrame.from_dict({'name':name,'price':price,'old price':old_price,'rating':rating},orient='index')
df.transpose(inplace=True)
df.to_csv('jumia_details.csv',index=False)
print(df)
