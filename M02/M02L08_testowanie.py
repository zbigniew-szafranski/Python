### 🔴 Czy warto testować?

# 👉 Po napisaniu programu zawsze przetestuj go! - nie chcesz wsiąść do bolidu z nieprzetestowanymi hamulcami.
# 👉 Testowanie manualne (ręczne) vs testowanie automatyczne (piszesz program, który testuje za Ciebie - program testuje inny program).
# 👉 Koniecznie wyrób sobie nawyk myślenia, co może pójść nie tak. Zostań hackerem, który próbuje złośliwie wykorzystać Twój program niezgodnie z przeznaczeniem. Testuj nie tylko typowe przypadki (happy path), ale także przypadki brzegowe (sad path).

# Na przykład, w jednym z poprzednich ćwiczeń napisałæś program generujący nazwy użytkownika bez spacji i małymi literami. Co gdy użytkownik:
# - nie poda nic (po prostu wciśnie enter?)
# - użyje tabulacji zamiast spacji
# - użyje znaków specjalnych
# - poda zbyt długą nazwę użytkownika
# - poda "    Jan Kowalski" (tak, spacje na początku)
# - istnieje już użytkownik o danej nazwie

### 🔴 Ćwiczenie

# Bazując na rozwiązaniu poprzedniego ćwiczenia, zmodyfikuj program tak, że jeżeli użytkownik poda kilka znaków, wówczas wyświetl błąd, że użytkownik powinien podać tylko jeden znak. W przeciwnym przypadku program powinien działać tak samo jak do tej pory.