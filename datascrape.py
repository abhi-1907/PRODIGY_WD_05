import requests
from bs4 import BeautifulSoup
import csv


csvfile = "itemdata.csv"

print("Enter the item: ")
item = input()
url = "https://www.limeroad.com/search/"+item
alldata = requests.get(url)

parseddata = BeautifulSoup(alldata.text,'html.parser')

imagedata = parseddata.find_all('a',attrs={'class':'c9 dB fs11 w140 oH tdN ttC wsN pt4 toE'})
itemname = []

print(imagedata)

for span in imagedata:
    name=span.find('span')
    itemname.append(name.text.strip())

itemprice = []

prices = parseddata.find_all('div',attrs={'class':'dIb vM c3 fs14'})
for price in prices:
    itemprice.append(price.text.strip())

itemrating = []

ratings = parseddata.find_all('div',attrs = {'class' : 'dIb vM lh12 fwB fs11'})
for rating in ratings:
    itemrating.append(rating.text.strip())


length=min(len(itemname),len(itemprice),len(itemrating))


with open(csvfile, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Rating"])
    for i in range(length):
        writer.writerow([itemname[i],itemprice[i],itemrating[i]])

print("Data written to", csvfile)
