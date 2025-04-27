from M05_amazon_project import extract_and_print_products

from lxml.html import fromstring


def test_extract_products():
    html = """
    <div>
        <div class="product">Title</div>
        <div class="product">Subtitle</div>
    </div>
    """
    dom = fromstring(html)
    xpath = "//div[@class='product']"
    got = extract_and_print_products(dom, xpath)
    expected = ["Title", "Subtitle"]
    assert got == expected


def test_extract_products_empty():
    html = """
    <div>
        <span>Other someone</span>
    </div>
    """
    dom = fromstring(html)
    xpath = "//div[@class='non-existent']"
    got = extract_and_print_products(dom, xpath)
    expected = []
    assert got == expected

def test_extract_products_empty_text():
    html = """
    <div>
        <div class="product"></div>
        <div class="product"></div>
    </div>
    """
    dom = fromstring(html)
    xpath = "//div[@class='product']"
    got = extract_and_print_products(dom, xpath)
    expected = []
    assert got == expected