### 🔴 Konwertowanie string na datę

# Na końcu tego modułu w naszym projekcie program będzie pytać użytkownika o datę. Tak wpisaną datę trzeba skonwertować ze stringa na datetime.

# Teoretycznie możemy użyć do tego metody datetime.strptime(format). Jednak w ten sposób wymuszamy na użytkowniku, aby podał datę w określonym przez nas formacie. Chcemy jednak pozwolić użytkownikowi na podanie daty w dowolnym formacie. Ta metoda się do tego nie nada.

# Podpowiedź: nie znajdziemy takiej funkcjonalności ani w module datetime, ani nigdzie indziej w standardowej bibliotece.

# Jednak jest to typowy problem, więc może ktoś go już rozwiązał...

### 🔴 Ćwiczenie

# Znajdź w Google (w szczególności na StackOverflow) w jaki sposób możesz skonwertować string podany przez użytkownika na obiekt datetime. Użytkownik może podać datę w różnych formatach - powinniśmy być jak najbardziej elastyczni.

date_1_as_str = '2021 8 28'
date_2_as_str = '28 Aug 21  12:00'