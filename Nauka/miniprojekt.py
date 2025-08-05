# count_a = input("Podaj tekst: ")
# counter = 0
# for a in count_a:
#     if a.isalpha() and a == "a" or a =="A":
#         counter += 1
# print("Ten tekst ma liter a: ", counter)

# 2. Napisz program, który sprawdzi, czy nawiasy są poprawnie sparowane - czyli czy jest tyle samo nawiasów otwierających `(` co zamykających `)`. Na przykład:

#     "bla() bla (bla bla (bla))" jest w porządku.
#     "bla ( bla" nie jest w porządku, bo brakuje zamykającego nawiasu
#     "bla ) bla (" nie jest w porządku, bo zaczyna się od zamykającego nawiasu
#     podpowiedź: wystarczy w odpowiedni sposób zliczać ile było nawiasów otwierających i zamykających

# nawias = input("podaj tekst: ")
# counter_o = 0
# counter_c = 0
# kolejnosc = ""
# for naw in nawias:
#     if naw == "(":
#         counter_o+=1
#     if naw == ")":
#         counter_c+=1
#     if naw == "()":    # zastanowić się nad tym
#         kolejnosc = "kolejność ok"
#     if naw == ")(":    # zastanowić się nad tym
#         kolejnosc = "zła kolejność"
#     if counter_o == counter_c:
#         beznaw = "nawiasy się zgadzają"
#     elif counter_o > counter_c:
#         count_n = counter_o - counter_c
#         beznaw = f"brak {count_n} nawiasu zamykającego"
#     elif counter_o < counter_c:
#         count_n = counter_c - counter_o
#         beznaw = f"brak {count_n} nawiasu otwerającego"
#     else:
#          beznaw="brak nawiasu"

# print("Ilość nawiasów otwierających: ", counter_o)
# print("ilość nawiasów zamykających: ", counter_c)
# print(beznaw)
# print(kolejnosc)

# 3. Napisz program, który sprawdza pojedynczy ruch w grę "kamień, papier, nożyce". Program przyjmuje Twój ruch oraz ruch przeciwnika. Następnie wyświetla, czy wygrałeś, czy zremisowałeś, czy przegrałeś. Podpowiedź: nie potrzebujemy pętli for. Zamiast tego potrzebujemy wiele rozgałęzień warunkowych if-else.

# print("Kamień, papier, nożyce")
# print('------------------------')
# print("ZASADY GRY: ")
# print("Kmień tępi nożyce")
# print("Papier zawija kamień")
# print("Nożyce tną papier")
# print("-------------------------")

# player_one = input("GRACZ 1 Podaj jedno z trzech (kamień, papier, nożyce): ")
# player_two = input("GRACZ 2 Podaj jedno z trzech (kamień, papier, nożyce): ")
# rock = "kamień"
# paper = "papier"
# scizors = "nożyce"
# print(f"Gracz 1: {player_one}, Gracz 2: {player_two}")


# if player_one == rock and player_two==rock and player_one == paper and player_two == paper and player_one == scizors and player_two == scizors:

#     if player_one == rock and player_two == rock:
#         result = "remis"
#     elif player_one == paper and player_two == paper:
#         result = "remis"
#     elif player_one == scizors and player_two == scizors:
#         result = 'remis'
#     elif (player_one == paper and player_two == rock) or (player_one == scizors and player_two == paper) or (player_one == rock and player_two == scizors):
#         result = "zwycięża GRACZ 1"
#     elif (player_one == scizors and player_two == rock) or (player_one == paper and player_two == scizors) or (player_one == rock and player_two == paper):
#         result = "zwycięża GRACZ 2"
# else:
#     result = "nie podano poprawnej nazwy"
# print(result)

# text = input("Podaj tekst: ")
# level = 0
# for char in text:
#     if char == '(':
#         level += 1
#     elif char == ')':
#         level -= 1
#     if level < 0:
#         print("Ups, wygląda na to, że zamykasz nawias zanim go otworzyłeś")
# if level > 0:
#     print("Ups, brakuje jednego lub kilku nawiasów zamykających")

# 3. Napisz program, który sprawdza pojedynczy ruch w grę "kamień, papier, nożyce". Program przyjmuje Twój ruch oraz ruch przeciwnika. Następnie wyświetla, czy wygrałeś, czy zremisowałeś, czy przegrałeś. Podpowiedź: nie potrzebujemy pętli for. Zamiast tego potrzebujemy wiele rozgałęzień warunkowych if-else.

print("Kamień, papier, nożyce")
print('------------------------')
print("ZASADY GRY: ")
print("Kmień tępi nożyce")
print("Papier zawija kamień")
print("Nożyce tną papier")
print("-------------------------")

user_choice = input("Twój ruch: ")
computer_choice = input("Ruch przeciwnika: ")
print(f"Gracz wybrał: {user_choice}, przeciwnik wybrał: {computer_choice}")
choice = ['kamień', 'papier', 'nożyce']

if user_choice in choice and computer_choice in choice:
    if user_choice == computer_choice:
        result = "remis"
    else:
        if user_choice == "kamień":
            if computer_choice == "nożyce":
                result = "wygrałeś"
            else:
                result = "przegrałeś"
        elif user_choice == "papier":
            if computer_choice == "kamień":
                result = "wygrałeś"
            else:
                result = "przegrałeś"
        elif user_choice == "nożyce":
            if computer_choice == "papier":
                result = "wygrałeś"
            else:
                result = "przegrałeś"
else:
    result = "Błąd w danych"


print(result)
