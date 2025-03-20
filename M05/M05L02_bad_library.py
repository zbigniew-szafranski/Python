# Zerknij najpierw do pliku M05L02_name.

print(f"M05L02_bad_library.__name__ =", __name__)

# Tutaj definiowane są funkcje, z których chcemy korzystać w M05L02_main

def generate_username(name):
    username = name.lower().replace(' ', '_')
    return username

# Jednocześnie poniżej jest kod, który powinien być wykonywany TYLKO, gdy uruchamiasz ten plik, ale nie gdy go importujesz. Póki co jednak ten kod JEST wykonywany, gdy go importujesz.

name = input("Podaj imię i nazwisko: ")
username = generate_username(name)
print(f"Twój username: {username}")