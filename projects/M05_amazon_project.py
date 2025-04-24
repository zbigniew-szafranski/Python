# Napisz dla Amazona program, który automatycznie wyciąga wybrane informacje z wybranych stron internetowych, na przykład nazwy produktów ze stron Leroy Merlin. Użytkownik podaje jedynie adres strony oraz ścieżkę xpath, którą może łatwo skopiować w przeglądarce.

# 1. Użyj biblioteki click, aby łatwiej było Ci odczytać url oraz xpath.

# 2. Podziel kod na funkcje tak, aby można było go łatwo testować.

# 3. Napisz kilka testów. Zacznij od tzw. happy path, tzn. najprostszego przypadku, a następnie przetestuj przypadki brzegowe.

# 4. Wyciągając z HTML tekst, usuń białe znaki z początku i końca (poszukaj odpowiedniej metody na stringach) oraz zamień znaki końca linii na spacje.

# 5. Wyświetl każdy znaleziony element HTML w osobnej linii.

# 6. Użyj docstringów, aby udokumentować Twój kod. Jakie informacje Twoim zdaniem warto tam zawrzeć?

# Hint: W razie problemów z cudzysłowami w XPATH pod Windows, możesz zamienić je na apostrofy, np.:
#     "//div[@id='wartosc']"
# zamiast
#     '//div[@id="wartosc"]'

# https://www.kaufland.pl/oferta/aktualny-tydzien/przeglad.category=01_Mi%C4%99so__Dr%C3%B3b__W%C4%99dliny.html

# Podpowiedź: zwróć uwagę, aby @click.command() oraz @click.argument(...) znalazły się nad odpowiednią funkcją - powinno to być tuż nad main():
#
# @click.command()
# @click.argument(...)
# def main(...):
# url_kaufland = "https://sklep.kaufland.pl/asortyment/swieze-artykuly.html"
# pattern = "//div[contains(@class, 'k-product-tile__title')]/text()"

import click
import requests
from lxml.html import fromstring


@click.command()
@click.argument("url")
@click.argument("xpath")

def main(url, xpath):
    repsonse = requests.get(url)
    dom = fromstring(repsonse.content)
    products = dom.xpath(xpath)
    for product in products:
        print(product.strip())
main()

