from bs4 import BeautifulSoup
import requests


url= "https://en.wikipedia.org/wiki/Aviation_accidents_and_incidents#Statistics"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.5993.90 Safari/537.36"
}


source= requests.get(url, headers=headers)
soup= BeautifulSoup(source.text, "lxml")
print(source.status_code)

crash_dict=[]

tables= soup.find_all("table")

for table in tables:

    header=[th.text.strip() for th in table.find_all("th")]

    if any("Number of incidents" in h for h in header):
        rows= table.find_all("tr")
        for row in rows[1:]:
            tds= row.find_all("td")

            if len(tds)<3:
                continue

            year= tds[0].text.strip()
            deaths=tds[1].text.strip()
            incidents= tds[2].text.strip()
            
            crash_dict.append({
                "year":year,
                "deaths": deaths,
                "incidents": incidents
                })
        break


for crash in crash_dict:
    print(crash)




            





