# Napisz program, który wczytuje listę wydatków z pliku expenses.txt (plik zawiera same wielkości wydatków jako liczby), a następnie wyświetla ich sumę.

with open('M03/expenses.txt') as stream:
    numbers =  stream.read()
content = numbers.split()
print(content)
int_content=[]
total_sum= ""
for nummber in content:
        int_content.append(float(nummber))
        total_sum = sum(int_content)
print(total_sum)