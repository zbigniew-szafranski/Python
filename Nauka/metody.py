### 🔴 Ćwiczenie: 

# Napisz program, który pyta użytkownika jak się nazywa, a następnie generuje dla niego username (nazwę użytkownika) małymi literami i nie zawierający spacji. 
# 1. Jeśli użytkownik przedstawi się wieloma słowami (np. imieniem i nazwiskiem), wówczas spacje należy ZASTĄPIĆ podkreśleniami. Na przykład, przedstawiam się jako "Jan Kowalski" i generowany jest username jan_kowalski. 
# 2. Do zamiany spacji na podkreślenia musisz użyć metody, która NIE została przedstawiona w tej lekcji - Twoim zadaniem jest wyszukać ją korzystając z Ctrl+Space.

user = input("Jak się nazywasz: ")
user = user.replace(" ", "_")
user = user.lower()
print(user)
