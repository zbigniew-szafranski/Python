### 🔴 Ćwiczenie: System numerowania zdjęć w aparacie

# Wyobraź sobie, że tworzysz oprogramowanie dla aparatu fotograficznego.
# Aparat zapisuje zdjęcia w formacie "IMG_XXXX.jpg", gdzie XXXX to czterocyfrowy numer zdjęcia
# (np. "IMG_0001.jpg", "IMG_0002.jpg" itd.)
# 
# Napisz funkcję generate_photo_name(existing_photos: list[str]) -> str, która:
# 1. Otrzymuje listę nazw już istniejących zdjęć
# 2. Zwraca nazwę dla nowego zdjęcia w odpowiednim formacie
# 3. Numer musi być zawsze 4-cyfrowy (uzupełniony zerami z przodu)
# 4. Należy użyć pierwszego wolnego numeru
#
# Przykłady:
# - Dla pustej listy → "IMG_0001.jpg"
# - Dla ["IMG_0001.jpg"] → "IMG_0002.jpg"
# - Dla ["IMG_0001.jpg", "IMG_0002.jpg", "IMG_0004.jpg"] → "IMG_0003.jpg"
#
# Dodatkowo:
# - Napisz testy sprawdzające różne przypadki
# - Co się stanie gdy numery się wyczerpią (> 9999)?

def generate_photo_name(existing_photos: list[str]) -> str:
    if not existing_photos:
        return "IMG_0001.jpg"
        
    # Tworzymy zbiór istniejących numerów
    existing_numbers = set()
    for photo in existing_photos:
        number = int(photo.split('_')[-1].split('.')[0])
        existing_numbers.add(number)
    
    # Znajdujemy pierwszy wolny numer
    new_number = 1
    while new_number in existing_numbers:
        new_number += 1
        
    # Sprawdzamy przekroczenie zakresu
    if new_number > 9999:
        raise ValueError("Przekroczono maksymalny numer zdjęcia (9999)")
        
    return f"IMG_{new_number:04d}.jpg"
print(generate_photo_name(["IMG_0001.jpg", "IMG_0002.jpg", "IMG_0004.jpg"]))
