from CoronaContryScraper import CoronaScraper

scraper = CoronaScraper()

scraper.updateContent()
df = scraper.getCountryDf()
print (df)
scraper.populateCountries(df)

for country in scraper.countries:
    print(country.name)
    print(country.cases)
    print(country.critical)
    print(country.deaths)