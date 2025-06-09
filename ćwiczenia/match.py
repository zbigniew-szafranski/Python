import argparse

# def get_day(day: int):
#     match day:
#         case 1: return "Poniedziałek"
#         case 2: return "Wtorek"
#         case 3: return "Środa"
#         case 4: return "Czwartek"
#         case 5: return "Piątek"
#         case 6: return "Sobota"
#         case 7: return "Niedziela"
#         case _: return "Błąd"
# day_number = int(input("Podaj numer dnia: "))
# print(get_day(day_number))

print("KALKULATOR")

def calculate(first: int,operator: str, second: int):
    match operator:
        case "+": return first + second
        case "-": return first - second
        case "*": return first * second
        case "/":
            if second == 0:
                return "Nie możesz dzielić przez zero"
            return first / second
        case _: return "Niewłaściwy operator"

parser = argparse.ArgumentParser(description="Kalkulator")
parser.add_argument("first", type=int, help="Pierwsza liczba")
parser.add_argument("operator", choices=['+', '-', '*', '/'], type=str, help="Operator")
parser.add_argument("second", type=int, help="Druga liczba")
args = parser.parse_args()
print(calculate(args.first, args.operator, args.second))


