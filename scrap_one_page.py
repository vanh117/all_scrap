from bs4 import BeautifulSoup
import requests
root = "https://subslikescript.com"
website = f"{root}/movies"
results = requests.get(website)
content = results.text
soup = BeautifulSoup(content, "lxml")


box = soup.find('article', class_="main-article")
links = []
for link in box.find_all("a", href = True):
    links.append(link["href"])
    
print(links)
for link in links:
    website = f"{root}/{link}"
    results = requests.get(website)
    content = results.text
    soup = BeautifulSoup(content, "lxml")
    title = box.find("h1").get_text()
    transcript = box.find("div", class_ = "full-script").get_text(strip=True, separator= " ")
    with open(f'{title}.txt', 'w' ) as file:
        file.write(transcript)
    
# title = box.find("h1").get_text()
