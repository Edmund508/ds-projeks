import requests
from bs4 import BeautifulSoup

baselink = "https://www.sudzibas.lv"

print("Izvēlies kategoriju:")
print("1. Atpūta un izklaide")
print("2. Auto un transports")
print("3. Bērni")
print("4. Bizness un finanses")
print("5. Būvniecība")
print("6. Ceļojumi")
print("7. Drošība")
print("8. Dzīvnieki")
print("9. Elektronika un tehnika")
print("10. Iepazīšanās")
print("11. Internets")
print("12. Izglītība")
print("13. Jurisprudence un konsultācijas")
print("14. Karjera un darbs")
print("15. Māksla un daiļrade")
print("16. Mēbeles un iekārtas")
print("17. Nekustamais īpašums")
print("18. Pakalpojumi")
print("19. Pārejas")
print("20. Politika un valsts struktūras")
print("21. Reklāma")
print("22. Reliģija")
print("23. Skaistumkopšana")
print("24. Sports")
print("25. Telekomunikācijas")
print("26. Televīzija un radio")
print("27. Tirdzniecība")
print("28. Veselība un medicīna")
usrinput = int(input("Ievadiet kategorijas numuru: "))
match usrinput:
    case 1:
        categorylink = "/category/atputa-izklaide/1"
    case 2:
        categorylink = "/category/auto-transports/2"
    case 3:
        categorylink = "/category/berni/39"
    case 4:
        categorylink = "/category/bizness-finanses/4"
    case 5:
        categorylink = "/category/buvnieciba/5"
    case 6:
        categorylink = "/category/celojumi/6"
    case 7:
        categorylink = "/category/drosiba/7"
    case 8:
        categorylink = "/category/dzivnieki/8"
    case 9:
        categorylink = "/category/elektronika-un-tehnika/34"
    case 10:
        categorylink = "/category/iepazisanas/11"
    case 11:
        categorylink = "/category/internets/9"
    case 12:
        categorylink = "/category/izglitiba/10"
    case 13:
        categorylink = "/category/jurisprudence-konsultacijas/13"
    case 14:
        categorylink = "/category/karjera-darbs/16"
    case 15:
        categorylink = "/category/maksla-dailrade/21"
    case 16:
        categorylink = "/category/mebeles-iekartas/22"
    case 17:
        categorylink = "/category/nekustamais-ipasums/12"
    case 18:
        categorylink = "/category/pakalpojumi/265290"
    case 19:
        categorylink = "/category/parejas/28"
    case 20:
        categorylink = "/category/politika-valsts-strukturas/27"
    case 21:
        categorylink = "/category/reklama/29"
    case 22:
        categorylink = "/category/religija/30"
    case 23:
        categorylink = "/category/skaistumkopsana/18"
    case 24:
        categorylink = "/category/sports/31"
    case 25:
        categorylink = "/category/telekomunikacijas/15"
    case 26:
        categorylink = "/category/televizija-radio/33"
    case 27:
        categorylink = "/category/tirdznieciba/36"
    case 28:
        categorylink = "/category/veseliba-medicina/35"
    case _:
        print("Nepareizs kategorijas numurs")
        exit()
page = requests.get(baselink + categorylink)
counter = 0
usrinput = input("Ievadiet kompanijas nosaukumu: ")
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
        if page.status_code == 200:
            pageCode = BeautifulSoup(page.content, "html.parser")
            next = pageCode.find_all('a', string = " nākamā")
    print("Sudzību skaits: " + str(counter))