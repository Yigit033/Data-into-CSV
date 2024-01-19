import requests
import csv

from requests.api import head

url = "http://api.coincap.io/v2/assets"


# header for rwquest

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json" 
}

response = requests.request("GET", url,headers=headers,data={})   
myjson = response.json()

yigitData= []

# yigitData.append(myjson['data'][50]["symbol"])

csvHeaders = ["Symbol","Name","Price"]

for x in myjson['data']:
  listing = [x["symbol"], x["name"],x["priceUsd"]]
  yigitData.append(listing)  



with open("crypto.cvs", "w",encoding="UTF-8", newline= "") as f:
  writer = csv.writer(f)
  writer.writerow(csvHeaders)
  writer.writerow(yigitData)


print("DONE")


# print(yigitData)