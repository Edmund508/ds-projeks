import time
import requests
from bs4 import BeautifulSoup

baselink = "https://www.sudzibas.lv"

usrinput = input("Ievadiet kompanijas nosaukumu: ")
categorylink = "/category/mebeles-iekartas/22"
page = requests.get(baselink + categorylink)
counter = 0
if page.status_code == 200:
    pageCode = BeautifulSoup(page.content, "html.parser")
    next = pageCode.find_all('a', string = " nākamā")
    while(True):
        found = pageCode.find_all('b', string = usrinput)
        for i in found:
            parent = i.find_parent('a')
            href = parent.get('href')
            new_url = baselink + href
            sid = href.split("-")
            nextpage = requests.get(new_url)
            time.sleep(2)
            if nextpage.status_code == 200:
                next_page_code = BeautifulSoup(nextpage.content, "html.parser")
                name = sid[len(sid) - 1] + ".txt"
                file = open(name, "w")
                theme = next_page_code.find_all(itemprop = "about")
                for t in theme:
                    file.write(t.text + "\n" + "\n")
                text = next_page_code.find_all(itemprop = "reviewBody")
                for t in text:
                    file.write(t.text + "\n" + "\n")
                date = next_page_code.find_all(itemprop = "datePublished")
                for t in date:
                    file.write(t.text)
                file.close()
                counter += 1
        if(next == []):
            break
        href = next[0].get('href')
        page = requests.get(baselink + categorylink + href)
        time.sleep(2)
        if page.status_code == 200:
            pageCode = BeautifulSoup(page.content, "html.parser")
            next = pageCode.find_all('a', string = " nākamā")
    print("Sudzību skaits: " + str(counter))