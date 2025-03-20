### 🔴 XPATH

# HTML to bardzo pozagnieżdżana struktura. Dobrze byłoby móc odwołać się do konkretnego elementu. Nie wystarczy wskazać tylko jaki to tag (np. DIV), ale też musimy jakoś odnaleźć go w gąszczu innych.

# W tym celu wymyślono XPATH, który określa pewien wzorzec (pattern), jakiego tagu szukamy. To trochę tak jak korzystając z glob.glob można było podać wzorzec w stylu "katalog/*.txt". 

# Do znajdowania elementów służy metoda .xpath(). Zwraca ona LISTĘ wszystkich pasujących tagów:

from lxml.html import fromstring

html = """
  <html>
    <body>
      <h1>Nagłówek</h1>
      <p class="klasa" id="main-p">Akapit tekstu. 
        <b>Wytłuszczony fragment</b>
      </p>
      <p>Kolejny nagłówek</p>
    </body>
  </html>
"""

dom = fromstring(html)

print(dom.xpath('/html/body/p'))

# Jednak zazwyczaj nie będziemy podawać takiej "ścieżki bezwględnej", tylko względną. W tym celu trzeba rozpocząć ją od dwóch slashy //

print(dom.xpath('//p'))

# Czasami interesuje nas tylko tag, którego konkretny atrybut ma konkretną wartość. Tak jest najczęściej z atrybutem ID, ponieważ powinien on być unikalny w obrębie całej strony, więc świetnie nadaje się do wskazywania elementów.

# Poniżej szukamy tylko akapitów, których atrybut class jest równy "klasa":

print(dom.xpath('//p[@class="klasa"]'))

### 🔴 Ćwiczenie

# W poprzednim ćwiczeniu znajdź pierwszy wytłuszczony fragment tekstu w akapicie main-p i zwróć go jako string.