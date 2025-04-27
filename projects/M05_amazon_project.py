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
# pattern = "//div[@class='k-product-tile__text']"
# pattern dla castoramy = "//div[@data-test-id='product-tile-title']"
# url_sinsay = "https://www.sinsay.com/pl/pl/dom/dashboard-home?brick=B_Podstrona_Home_H&place=home"
# pattern dla sinsay = "//div[@class='product-name-main']"

# -*- coding: utf-8 -*-

import click
import requests
from lxml.html import fromstring
import sys


def download_page(url):
    """
    Fetches the HTML content of a given URL.

    :param url: The URL of the webpage to download.
    :return: The raw HTML content as string.
    """
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def parse_html(content):
    """
    Parses the given HTML content into a DOM object.

    :param content: Raw HTML content.
    :return: Parsed DOM object.
    """
    return fromstring(content)


def normalize_text(text):
    """
    Cleans and normalizes text by stripping whitespace
    and replacing newlines with spaces.

    :param text: The raw text to normalize.
    :return: The cleaned and normalized text.
    """
    return text.strip().replace("\n", " ")

def extract_and_print_products(dom, xpath):
    """
    Extracts elements matching the given XPath and prints each one.
    Returns the list of combined texts.

    :param dom: Parsed DOM object.
    :param xpath: XPath query to extract elements from the DOM.
    :return: A list of product texts.
    """
    products = dom.xpath(xpath)
    product_list = []

    for product in products:
        texts = product.xpath('.//text()')
        combined_text = " ".join(normalize_text(text) for text in texts if text.strip())
        if combined_text:
            print(combined_text)
            product_list.append(combined_text)

    return product_list


@click.command()
@click.argument("url")
@click.argument("xpath")

def main(url: str, xpath):
    """
    Main function to download, parse, and extract product names
    from a webpage using a specified XPath.

    :param url: The URL of the webpage to scrape.
    :param xpath: The XPath query used to locate product names.
    """
    try:
        html_content = download_page(url)
        dom = parse_html(html_content)
        product_list = extract_and_print_products(dom, xpath)
    except requests.RequestException as e:
        print(f"Error fetching data from the URL: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")


if __name__ == "__main__":
    main()