import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np

class CoronaCountry(object):
    name = None
    cases = None
    deaths = None
    serious = None
    critical = None

    def __init__(self, name):
        self.name = name

    def populateFromRow(self, row):
        self.cases = (row['Cases'])
        self.deaths = (row['Deaths'])
        self.serious = (row['Serious'])
        self.critical = (row['Critical'])

class CoronaScraper(object):
    
    chrome_options = None
    countries = []
    pageContent = None
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR30F8lYP3jG7YOq8es0PBpJIE5yvRVZffOyaqC0GgMBN6yt0Q-NI8pxS7hd1F9dYXnowSC6zpZmW9D/pubhtml'
    driver = None

    def __init__(self):
        pass
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)

    def updateContent(self):
        self.driver.get(self.url)
        self.pageContent = self.driver.page_source
        #data_date_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        
    def getCountryDf(self):
        dfs = pd.read_html(self.pageContent)

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
        return df_intl

    def populateCountries(self, df):
        self.countries = []
        for index, row in df.iterrows():
            if ((str(row['Country']) != 'nan') and (row['Country'] != 'TOTAL') and (row['Country'] != 'Queque')):
                country = CoronaCountry(str(row['Country']))
                country.populateFromRow(row)
                self.countries.append(country)

