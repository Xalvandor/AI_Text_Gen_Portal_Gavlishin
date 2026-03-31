import requests
import bs4
import csv


url = "https://www.scrapethissite.com/pages/simple/"
#scrapes raw data from site
response = requests.get(url)
#parses data
soup = bs4.BeautifulSoup(response.text, "html.parser")
#finds specific html with country data
countries = soup.find_all("div", class_="col-md-4 country")
#blank list for parsed data
country_list = []

#loops through each country and creates a dictionary with each relevant data point
for country in countries:
   country_info = {
       'Name': country.find("h3", class_="country-name").text.strip(),
       'Capital': country.find("span", class_="country-capital").text.strip(),
       'Population': country.find("span", class_="country-population").text.strip(),
       'Area': country.find("span", class_="country-area").text.strip(),
   }
   #appends to parsed country list
   country_list.append(country_info)

#writes data to csv file
filename = "countries.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Capital', 'Population', 'Area'])
    writer.writeheader()
    for country in country_list:
        writer.writerow(country)
