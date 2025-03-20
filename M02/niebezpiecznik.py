# Jesteś konsultantem działającym dla Niebezpiecznika - polskiego lidera cyberbezpieczeństwa. Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami. 
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.

user_password = input("Podaj hasło: ")
has_lower = False
has_upper = False
has_space = False
has_special = False

for char in user_password:
    if char.islower():
        has_lower = True
    if char.isupper():
        has_upper = True
    if char.isspace():
        has_space = True
    if char.isalnum():
        has_special = True
errors = []

if len(user_password) < 8:
    errors.append("Hasło powinno składać się z co najmniej 8 znaków.")
if not has_lower:
    errors.append("Hasło powinno zawierać conajmniej jedną małą literę")
if not has_upper:
    errors.append("Hasło powinno zawierać jedną dużą literę")
if has_space:
    errors.append("Hasło nie może zawierać spacji")
if not has_special:
    errors.append("Hasło powinno zawierać znak specjalny")

if errors:
    print("\n".join(errors))
else:
    print("Hasło jest bezpieczne")