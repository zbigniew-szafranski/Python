# 2. Kalkulator wieku psa. Napisz program, który na podstawie wieku psa podanego przez użytkownika wyliczy jego wiek w latach ludzkich. 
# Pierwsze dwa lata życia psa zawsze odpowiadają ok. 10,5 ludzkich lat (1 psi rok = 10.5 ludzkich lat, 
# 2 psie lata = 21 ludzkich lat)
# każdy kolejny rok życia psa to ok. 4 ludzkie lata.

print('KALKULATOR WIEKU PSA')
dog_year = input("Podaj wiek psa: ")

if dog_year.isalpha():
    print('Została podana litera - Podaj liczbę')
elif dog_year.isspace():
    print('Został podany biały znak- Podaj liczbę')
    
else:
    dog_year_float = float(dog_year)

    if dog_year_float <= 0:
        print('Wiek musi być większy od zera')
    elif 0 < dog_year_float <=2:
        human_age = dog_year_float*10.5
        print("Piesek ma ludzkich:",human_age, "lat")
    elif dog_year_float >2:
        human_age = 21+((dog_year_float-2)*4) 
        print("Piesek ma ludzkich:",human_age, "lat")