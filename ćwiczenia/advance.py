import reprlib
import pprint
import textwrap
import locale

print(reprlib.repr(set('Zbigniew')))

t = [[[['black', 'cyan'], 'white',['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width=30)

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))

print(locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8'))
conv = locale.localeconv()
x= 1234567.8
print(locale.format_string("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
