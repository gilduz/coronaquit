from coronavirusStats.coronavirus import Coronavirus
from coronavirusStats.coronavirus import CoronaData
scraper = Coronavirus()

data = scraper.get_data()
print ("Ciao")
print (data)
scraper.closeDriver()

