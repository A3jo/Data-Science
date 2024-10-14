import requests
from bs4 import BeautifulSoup
def getdata(url):
 r = requests.get(url)
 return r.content
htmldata = getdata("https://sjcetpalai.ac.in")
soup = BeautifulSoup(htmldata,'html.parser')
print("SJC22MCA-2007 : ANJALA MICHAEL")
print("Batch : MCA 2022-24")
links = soup.find_all("a")
print("Total number of links : ",len(links))
for link in links:
 if link.get("href") != "":
  print("Link :",link.get("href"),"Text :",link.string)