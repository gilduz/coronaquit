import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome('chromedriver', options=chrome_options)

# url = 'https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/'
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR30F8lYP3jG7YOq8es0PBpJIE5yvRVZffOyaqC0GgMBN6yt0Q-NI8pxS7hd1F9dYXnowSC6zpZmW9D/pubhtml'
driver.get(url)
content = driver.page_source

data_date_time = datetime.now().strftime('%Y-%m-%d %H:%M')
print(data_date_time)

dfs = pd.read_html(content)

len(dfs)
print(dfs[0])

df_intl=dfs[0]
df_intl  = df_intl.drop(df_intl .columns[0], axis=1)
df_intl  = df_intl.drop(list(range(6)), axis=0)
df_intl  = df_intl.drop([7,8], axis=1)
num_cols = len(df_intl.columns)

columns = ['d'] * num_cols
columns[0] ='Country'
columns[1] ='Cases'
columns[2] = 'Deaths'
columns[3] = 'Serious'
columns[4] = 'Critical'
columns[5] = 'Recovered'
df_intl.columns=columns
co3umns=columns
co4umns=columns
print(df_intl)