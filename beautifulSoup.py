#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

for num  in range (10,2000,10):
    print(num)
    url = "https://www.tripadvisor.in/Attraction_Review-g297685-d478221-Reviews-or"+str(num)+"-Sarnath-Varanasi_Varanasi_District_Uttar_Pradesh.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    mydivs =soup.findAll("div", {"class": "ui_column is-9"})

    for div in mydivs:
            title=div.find("span", {"class": "noQuotes"})
            if title is not None:
                title_text=title.text
            review=div.find("p", {"class": "partial_entry"})
            if review is not None:
                review_text=review.text
            final_data=title_text+" "+review_text
            mylist=[]
            mylist.append(final_data)
            print(mylist)
            f = open('sarnath.csv','a')
            f.write(str(mylist)+'\n') 
