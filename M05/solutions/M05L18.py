### 🔴 Ćwiczenie

# Rozwiń program z M05L16 tak, aby mając listę `elements` dla każdego jej elementu wywołać metodę .text_content() i tak uzyskane stringi zebrać w jedną, nową listę. Następnie wyświetl tą listę, każdy element w osobnej linii.


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
elements = dom.xpath('//p')

texts = [e.text_content().replace('\n', ' ') for e in elements]
for text in texts:
    print('-', text)