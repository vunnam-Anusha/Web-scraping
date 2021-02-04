
import time
import numpy as np
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option=Options()
driver=webdriver.Chrome(options=option,executable_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.1\\bin\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()

baseurl = 'https://www.google.com/maps/dir///@15.8271193,80.3511221,14z/data=!4m2!4m1!3e0'

driver.get(baseurl)

# this is the data frame from where we pull the data for the loop execution
import pandas as pd
df=pd.read_excel("D:\\FlipKart\\Clustering\\Jharkard\\InputData.xlsx",sheet_name="14")
df
#df=pd.read_excel("D:\\FlipKart\\Clustering\\Bihar\\IP1.xlsx")
df["3pl"]=df["3pl"].astype(str).str.split('.', expand = True)[0]
df["3pl1"]=df["3pl1"].astype(str).str.split('.', expand = True)[0]
# this will the file of pincodes from where we need to give the inputes
#u need to give ur own path like from where we need to read this csv file
df.head(10)
df.tail(10)


# creating a new data fraem to append the values into the new data frame
dist_1=pd.DataFrame()

print(dist_1) # this will show u the no of columns and no or index bu t as of now it is an empty data frame no columns and index(rows)

import time



for i in range(1,4):  # the range is 0,
    for j in range(0,24): # the range is 0,400

        source=driver.find_element_by_class_name("tactile-searchbox-input").send_keys(str(df["3pl"][i]))
        destination=driver.find_element_by_xpath("//*[@id='sb_ifc51']/input").send_keys(str(df["3pl1"][j]))
        #time.sleep(1)
        try:

            search=driver.find_element_by_xpath("//*[@id='directions-searchbox-1']/button[1]").click()

            time.sleep(4)

            disclick=driver.find_element_by_xpath("//*[@id='section-directions-trip-0']/div[1]/div[1]/div[4]/button").click()

            time.sleep(1)

            distance=driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[2]/span").text
            print(distance)
            dist_1.loc[str(i),str(j)] =distance

            #time.sleep(1)
            driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[1]/button").click()
            source = driver.find_element_by_class_name("tactile-searchbox-input").clear()
            #time.sleep(1)
            destination = driver.find_element_by_xpath("//*[@id='sb_ifc51']/input").clear()
            #time.sleep(1)

        except Exception as e:
            i+1
            distance ="NO roadway found"
            dist_1.loc[str(i), str(j)] = distance
            source = driver.find_element_by_class_name("tactile-searchbox-input").clear()
            #time.sleep(1)
            destination = driver.find_element_by_xpath("//*[@id='sb_ifc51']/input").clear()
            #time.sleep(1)


 #dist_1.to_excel("D:\FlipKart\Clustering\OdishaClustering\Clustering\book.xlsx" ,index=None)
 dist_1.to_excel("D:\\FlipKart\\Clustering\\Jharkard\\IP14.xlsx",index=None)


