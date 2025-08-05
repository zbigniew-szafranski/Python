# ### 🔴 Ćwiczenie
#
# # Narodowy Bank Polski udostępnia przez swoje API historyczne kursy walut. Otrzymałæś odpowiedź taką jak poniżej
#
# # Jest to kurs waluty USD z dnia 3 sierpnia 2021. Z tak zagnieżdżonej struktury wyciągnij kurs waluty (klucz "mid").
response = {
    "table": "A",
    "currency": "dolar amerykański",
    "code": "USD",
    "rates": [
        {
            "no": "148/A/NBP/2021",
            "effectiveDate": "2021-08-03",
            "mid": 3.8315,
        },
    ],
}
#
exchange_rate = response['rates'][0]['mid']
print('exchange rate', exchange_rate)