# Znajdź w Google (w szczególności na StackOverflow) w jaki sposób możesz skonwertować string podany przez użytkownika na obiekt datetime. Użytkownik może podać datę w różnych formatach - powinniśmy być jak najbardziej elastyczni.
date_1_as_str = '2021 8 28'
date_2_as_str = '28 Aug 21  12:00'

from dateutil import parser
date_1 = parser.parse(date_1_as_str)
date_2 = parser.parse(date_2_as_str)
print(date_1)
print(date_2)

