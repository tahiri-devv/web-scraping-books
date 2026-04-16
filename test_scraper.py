import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# telecharger page web
url = "https://books.toscrape.com"
page = 1

while url:
    print(f"\n📄 Page {page}")

    response = requests.get(url, verify=False)

    # afficher le status
    print("Statut de la connexion :", response.status_code)

    # on lit le contenu html
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    # on recupere le titre de la page
    titre = soup.find("title")
    print("Titre de la page :", titre.text.strip())

    # on recupere les 5 premiers livres
    livres = soup.find_all("article", class_="product_pod")
    print("\nLes 5 premiers livres :")

    for livre in livres[:5]:
        nom = livre.find("h3").find("a")["title"]
        prix = livre.find("p", class_="price_color").text
        print(f" - {nom} -> {prix}")

    # passer a la page suivante
    next_btn = soup.find("li", class_="next")

    if next_btn and page < 3:  # limite pour tester
        next_page = next_btn.find("a")["href"]
        url = urljoin(url, next_page)
        page += 1
        print("\n➡️ Page suivante...\n")
    else:
        url = None
        print("\n✅ Fin du scraping")