### 🔴 Praca z HTMLem

# Biblioteka requests pozwala nam pobrać kod strony (HTML), jednak jest on jedynie stringiem. Chcemy go SPARSOWAĆ, czyli zamienić string w pozagnieżdżaną strukturę tagów.

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

# Do tego służy moduł lxml.html, który należy doinstalować:

# $ pip install lxml

### 🔴 Ćwiczenie

# Znajdź w module lxml.html funkcjonalność odpowiedzialną za sprasowanie HTMLa, czyli przekształcenie go ze stringa na zagnieżdżoną strukturę reprezentowaną przez klasę lxml.html.HtmlElement. Jak znajdziesz tą informację? Gdzie znajduje się dokumentacja lxml?