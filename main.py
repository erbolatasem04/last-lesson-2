import config
from bs4 import BeautifulSoup
import requests
import json

response = requests.get(config.URL,headers=config.HEADERS)

html = response.text

def get_data(html):
    soup = BeautifulSoup(html, "lxml").find("section", {"class": "a-list a-search-list a-list-with-favs"}).find_all("div", {"class": "a-card__inc"})
    unprocessed_data = []
    # Перебираем карточки по одной, card это одна карточка товара
    for card in soup:


        name = card.find("a", {"class": "a-card__title"})
        address = card.find("div", {"class": "a-card__subtitle"})
        price = card.find("div",{"class":"a-card__price"})
        description = card.find("div",{"class": "a-card__text-preview"})


        fields = [ name , price, address, description]
        if not all(fields):
            continue
        unprocessed_data.append(
    {
        "name": name.get_text(strip=True),
        "address": address.get_text(strip=True),
        "price": price.get_text(strip=True),
        "description": description.get_text(strip=True),

    }
    )

    return unprocessed_data




def main():
    data = []
    unprocessed_data = get_data(html)
    data.extend(unprocessed_data)

    with open("item.json","w", encoding = "utf-8" ) as file:
        json.dump(data, file, indent=4,ensure_ascii = False)
main()

print("hello")