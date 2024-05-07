from bs4 import BeautifulSoup
import requests
website = "https://subslikescript.com/movie/The_Breach-14229154"
results = requests.get(website)
content = results.text
soup = BeautifulSoup(content, "lxml")
# print(soup.prettify) --> từ đầu đến dòng này chạy được

box = soup.find("article", class_ = "main-article")
title = box.find("h1").get_text()
transcript = box.find("div", class_ = "full-script").get_text(strip=True, separator= " ")
with open(f'{title}.txt', 'w' ) as file:
    file.write(transcript)
    

