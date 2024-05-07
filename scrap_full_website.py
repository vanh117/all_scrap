from bs4 import BeautifulSoup
import requests
root = "https://subslikescript.com"
website = f"{root}/movies_letter-A"
results = requests.get(website)
content = results.text
soup = BeautifulSoup(content, "lxml")
# pagination
pagination = soup.find("ul", class_ = "pagination")
pages = pagination.find_all("li", class_ = "page-item")
last_pages =  pages[-2].text


links = []
for page in range(1, int(last_pages)+1): 
    # dòng lặp này để lấy tất cả: do int+1 sẽ lấy từ 1 --> int aka all      
    # https://subslikescript.com/movies_letter-A?page=2
    
    results = requests.get(f"{website}?page={page}") #để giống format)
    content = results.text
    soup = BeautifulSoup(content, "lxml")
    

    box = soup.find('article', class_="main-article")
    links = []
    for link in box.find_all("a", href = True):
        links.append(link["href"])
        
    print(links)
    for link in links:
        try:
            print(link)
            
            results = requests.get(f"{root}/{link}")
            content = results.text
            soup = BeautifulSoup(content, "lxml")
            title = box.find("h1").get_text()
            transcript = box.find("div", class_ = "full-script").get_text(strip=True, separator= " ")
            with open(f'{title}.txt', 'w' ) as file:
                file.write(transcript)
        except:
            print("link not working: ")
            print(link)
            pass
            
            #nếu 1 link nó không có đủ thông tin thì bỏ qua
        
        
    # title = box.find("h1").get_text()
