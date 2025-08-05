### 🔴 Ćwiczenie

# Wejdź na stronę Leroy Merlin na dowolną stronę z listą produktów. Otwórz narzędzia deweloperskie. Skopiuj XPATH nazw produktów. Następnie zmodyfikuj ten XPATH tak, aby znajdował nazwy wszystkich produktów, a nie tylko jednego.
import requests
from lxml.html import parse
from lxml.html import fromstring

# Pobieranie zawartości strony
url = "https://www.kaufland.pl/"
response = requests.get(url)

# Sprawdzanie statusu odpowiedzi
if response.status_code == 200:
    page = fromstring(response.content)  # Parsowanie HTML za pomocą lxml
    print(page)
else:
    print(f"Błąd podczas pobierania strony, kod statusu: {response.status_code}")
# html_tree = fromstring(page)
# text_content = html_tree.text_content()
# print(text_content)

print(page.xpath('/html/body/div[3]/main/div[1]/div/div/div[4]/div[2]/div[1]/div/div/div[3]/div/div/a/div[1]/div[2]/h4'))
# from playwright.sync_api import sync_playwright
#
# url = "https://www.kaufland.pl/"
#
# with sync_playwright() as p:
#     # Uruchamianie przeglądarki
#     browser = p.chromium.launch(
#         headless=True)  # Możesz ustawić headless=False, aby zobaczyć działanie w oknie przeglądarki
#     page = browser.new_page()
#
#     # Przejdź do strony Kaufland
#     page.goto(url)
#
#     # Zaczekaj na załadowanie produktów
#     page.wait_for_selector('//div[@class="o-overview-list"]')
#
#     # Pobierz produkty
#     products = page.locator('//div[@class="o-overview-list"]/div/div/div/div/a/div[1]/div[2]/h4')
#
#     for i in range(products.count()):
#         print(products.nth(i).text_content())
#
#     # Zamknięcie przeglądarki
#     browser.close()


