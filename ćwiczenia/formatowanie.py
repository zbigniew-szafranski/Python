# import logging
# from decimal import Decimal
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# def format_message(name, age, saldo):
#     message_percent = "Hello %s. You are %d years old and your balance is $%.2f."%(name, age, saldo)
#
#     message_str_format = "Hello {}. You are {} years old and your balance is ${}.".format(name, age, saldo)
#
#     message_f_string = f"Hello {name}. You are {age} years old and your balance is ${saldo}."
#
#     logging.debug(f"Message percent: {message_percent}")
#     logging.warning(f"Message str format: {message_str_format}")
#     logging.info(f"Message f string: {message_f_string}")
#
#     return message_percent, message_str_format, message_f_string
#
# format_message("aga", 24, 121.121)

# Napisz funkcję compare_types, która porównuje wynik działania na liczbach typu float i decimal, demonstrując różnicę w precyzji. 

# from decimal import Decimal


# def compare_types():
#     float_result = 0.1 + 0.2
#     decimal_result = Decimal('0.1') + Decimal('0.2')
#     print("Float result:", float_result)
#     print("Decimal result:", decimal_result)
#     print("Are they equal?", float_result == decimal_result)
#
# compare_types()

# Przeprowadź eksperyment ilustrujący problem z precyzją typu float, wykorzystując przykład sumowania bardzo małych liczb. Jaki powinien być wynik? A jaki jest w rzeczywistości?
# Aby uzyskać ten efekt napisz pętlę, która np. 10 000 krotnie zsumuje 0.0001. Ile powinno wynosić 10 000 * 0.0001?

# def float_precision_issue():
#     sum_ = 0.0
#     for i in range(10000):
#         sum_ += 0.0001
#     print("Expected result: 1.0")
#     print("Actual result:", sum_)
# float_precision_issue()

# Napisz funkcję search_emails, która przyjmuje tekst i za pomocą wyrażeń regularnych znajduje w nim wszystkie adresy e-mail. Funkcja powinna zwracać listę znalezionych adresów.
import re

email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
def search_emails(text):
    return email_pattern.findall(text)

text = "My email is zbig@wp.pl and my phone number is +380987654321 and other ibihiz@wp.pl and @op"
emails = search_emails(text)
print(emails)