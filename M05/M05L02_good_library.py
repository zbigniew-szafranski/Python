# Zerknij najpierw do pliku M05L02_name.

print(f"M05L02_good_library.__name__ =", __name__)

# Tutaj definiowane są funkcje, z których chcemy korzystać w M05L02_main

def generate_username(name):
    return name.lower().replace(' ', '_')

# Poniższy kod jest wykonywany TYLKO, gdy uruchamiasz ten plik, ale nie wtedy, gdy go importujesz - i tak powinno być!

if __name__ == "__main__":
    name = input("Podaj imię i nazwisko: ")
    username = generate_username(name)
    print(f"Twój username: {username}")