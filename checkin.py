import requests
from bs4 import BeautifulSoup
page=requests.get("https://weather.com/en-IN/weather/tenday/l/c417d372b0f3169f3861ec453441ccf2d73cbdc5ad0be8d35904f1b6a8d929e1")
content=page.content
soup=BeautifulSoup(content,"html.parser")
l=[]
nw
all=soup.find("div",{"class":"locations-title ten-day-page-title"}).find("h1").text


table=soup.find_all("table",{"class":"twc-table"})
for items in table:
	for i in range(len(items.find_all("tr"))-1):
		d = {}
		try:
			d["day"]=items.find_all("span",{"class":"date-time"})[i].text
			d["date"]=items.find_all("span",{"class":"day-detail"})[i].text
			d["desc"]=items.find_all("td",{"class":"description"})[i].text
			d["temp"]=items.find_all("td",{"class":"temp"})[i].text
			d["precip"]=items.find_all("td",{"class":"precip"})[i].text
			d["wind"]=items.find_all("td",{"class":"wind"})[i].text
			d["humidity"]=items.find_all("td",{"class":"humidity"})[i].text
		except:
			d["day"]="None"
			d["date"]="None"
			d["desc"]="None"
			d["temp"]="None"
			d["precip"]="None"
			d["wind"]="None"
			d["humidity"]="None"
		#print("")
		l.append(d)

import pandas
df = pandas.DataFrame(l)
#print(df)
#print(df["wind"][0])
for xl in range(0, 15):
    res=[int(nw) for nw in df["wind"][xl].split() if nw.isdigit()]
    #print(res[0])
    if res[0]>5:
     print("Extend Checkin timings of Today +",xl,"th Day by",res[0]-5,"hours")
    else:
     print("No change in Today +",xl,"th Day Checkin timings")
    #print (df["wind"][xl])
df.to_csv("output.csv")
