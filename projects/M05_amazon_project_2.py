import click
import requests
from lxml.html import fromstring
import sys

# Configure console output encoding to support UTF-8
sys.stdout.reconfigure(encoding='utf-8')


def download_page(url: str) -> bytes:
    """
    Fetches the HTML content of a given URL.

    :param url: The URL of the webpage to download.
    :return: The raw HTML content as bytes.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.content


def parse_html(content: bytes):
    """
    Parses the given HTML content into a DOM object.

    :param content: Raw HTML content.
    :return: Parsed DOM object.
    """
    return fromstring(content)


def normalize_text(text: str) -> str:
    """
    Cleans and normalizes text by stripping whitespace
    and replacing newlines with spaces.

    :param text: The raw text to normalize.
    :return: The cleaned and normalized text.
    """
    return text.strip().replace("\n", " ")


def extract_and_print_products(dom, xpath1: str, xpath2: str):
    """
    Extracts products and prices (or any paired data) from two XPath queries and displays them line by line.

    :param dom: Parsed DOM object.
    :param xpath1: XPath query to extract products.
    :param xpath2: XPath query to extract prices (or related information).
    """
    # Extract results from both XPath queries
    products = dom.xpath(xpath1)
    normalized_products = [normalize_text(product) for product in products]

    prices = dom.xpath(xpath2)
    normalized_prices = [normalize_text(price) for price in prices]

    # Determine the number of pairs to iterate over
    max_length = max(len(normalized_products), len(normalized_prices))

    # Fill missing data with placeholders if lengths don't match
    if len(normalized_products) < max_length:
        normalized_products += ["No Product"] * (max_length - len(normalized_products))
    if len(normalized_prices) < max_length:
        normalized_prices += ["No Price"] * (max_length - len(normalized_prices))

    # Combine products and prices into pairs and print each pair on a new line
    for product, price in zip(normalized_products, normalized_prices):
        print(f"{product} - {price}")



@click.command()
@click.argument("url")
@click.argument("xpath1")
@click.argument("xpath2")
def main(url: str, xpath1: str, xpath2: str):
    """
    Main function to download, parse, and print pairs of information (e.g., products and prices)
    line by line from two XPath queries.

    :param url: The URL of the webpage to scrape.
    :param xpath1: First XPath query to extract products.
    :param xpath2: Second XPath query to extract prices.
    """
    try:
        # Download and parse HTML content
        html_content = download_page(url)
        dom = parse_html(html_content)

        # Extract and print product-price pairs
        extract_and_print_products(dom, xpath1, xpath2)

    except requests.RequestException as e:
        print(f"Error fetching data from the URL: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")



if __name__ == "__main__":
    main()
