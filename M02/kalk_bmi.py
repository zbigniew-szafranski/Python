# 1. Napisz kalkulator BMI. Użytkownik podaje wagę i wzrost, a program wyświetla wynik wraz z komentarzem. BMI jest liczone jako waga podzielona przez wzrost w metrach do kwadratu. Jeśli BMI jest między 18.5 a 25, to napisz, że jest ono w normie. W przeciwnym razie napisz, że jest to niedowaga lub nadwaga, a dla BMI > 30 otyłość.

print('KALKULATOR BMI')
weight = str(input('Podaj wagę w kilogramach: '))

if weight.isalpha():
    print("Podano literę")
elif weight.isspace():
    print('Podano biały znak')    
else:
    weight2=float(weight)
    hight = str(input('Podaj wzrost w centymetrach: '))

    if hight.isalpha():
        print('Podano literę')
    elif hight.isspace():
        print('Podano biały znak') 
    else:
        hight2 =float(hight)/100
        bmi = weight2/(hight2**2)
      
        if bmi < 18:
            print('Twoje BMI wynosi: ', round(bmi,2))
            print('Niedowaga')

        elif 18.5< bmi<24.9:
            print('Twoje BMI wynosi: ', round(bmi,2))
            print('Jesteś w normie')
        elif 25< bmi <29.9:
            print('Twoje BMI wynosi: ', round(bmi,2))
            print('Nadwaga')
        else:
            print('Twoje BMI wynosi: ', round(bmi,2))
            print('Masz otyłość')

# nie poradziłem sobie z przypadkiem co jeśli użytkownik naciśnie enter