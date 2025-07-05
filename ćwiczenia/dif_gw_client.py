import pandas as pd

# Wczytanie plików
df1 = pd.read_excel('/home/ibhiz/PycharmProjects/Python/ćwiczenia/klienci_all.xlsx', dtype={'nr_klienta': str, 'telefon': str}, engine='openpyxl')
df2 = pd.read_excel('/home/ibhiz/PycharmProjects/Python/ćwiczenia/klienci_teraz.xlsx', dtype={'nr_klienta': str, 'telefon': str}, engine='openpyxl')

# Czyszczenie numerów klientów
df1['nr_klienta'] = df1['nr_klienta'].str.strip().str.replace(r'\s+', '', regex=True)
df2['nr_klienta'] = df2['nr_klienta'].str.strip().str.replace(r'\s+', '', regex=True)

# Znajdujemy rekordy z klienci_all, których nie ma w klienci_teraz
roznica = df1[~df1['nr_klienta'].isin(df2['nr_klienta'])]
roznica = roznica[['nr_klienta', 'nazwa', 'adres', 'telefon', 'mail']]

# Zapisujemy wynik
roznica.to_excel('/home/ibhiz/PycharmProjects/Python/ćwiczenia/roznica.xlsx', index=False, engine='openpyxl')
print(f"Znaleziono {len(roznica)} rekordów, które są w klienci_all, ale nie ma ich w klienci_teraz")