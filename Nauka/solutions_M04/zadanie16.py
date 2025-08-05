### 🔴 Ćwiczenie

# Korzystając z oficjalnej dokumentacji na temat typu datetime, znajdź metodę na skonwertowanie datetime na string w formacie np. "2021.08.28 12.34.56"
# Dokumentacja: https://docs.python.org/3/library/datetime.html#datetime.datetime
from datetime import datetime
formatted_time = datetime.strftime(datetime.now(), '%A %Y/%m/%d %H.%M.%S')
print(formatted_time)