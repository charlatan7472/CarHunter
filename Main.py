__author__ = 'jheider'

import requests
import DesiredOptions
import QueryBuilder
import bs4

site_name = "http://www.autotrader.com"
#search_string = '/cars-for-sale/searchresults.xhtml?' \
         #       '&zip=32202&extColorsSimple=BLACK%2CBLUE&exteriorColorSimple1=BLACK&exteriorColorSimple2=BLUE&searchRadius=0&doorCodes=4&featureCodes=1078%2C1132&makeCode1=RAM&trim1=RM1500%7CSport&mmt=%5BRAM%5BRM1500%5BRM1500%7CSport%5D%5D%5B%5D%5D&maxMileage=45000&vehicleStyleCodes=TRUCKS&minPrice=0&maxPrice=35000&listingTypes=used%2Ccertified&startYear=2012&endYear=2015&sellerTypes=d&mod_bookmark_id=102332494&lastExec=1433529371000'
my_options = DesiredOptions.DesiredOptions()
QueryBuilder.set_search_string("www.autotrader.com", my_options)



# def CreateAutoTraderSearch()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

response = requests.get(site_name, headers=headers)

#print response.text
