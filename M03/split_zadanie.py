# Napisz program, który wczytuje listę wydatków z pliku expenses.txt (plik zawiera same wielkości wydatków jako liczby), a następnie wyświetla ich sumę.

with open('M03/expenses.txt') as stream:
    numbers =  stream.read()
content = numbers.split()
print(content)
int_content=[]
for nummber in content:
    int_content.append(float(nummber))
    suma = sum(int_content)    
print(suma)