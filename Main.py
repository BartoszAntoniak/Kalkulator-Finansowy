def Menu():
    
    print('Kalkulator Lokat v0.1')
    print('Przy wpisywaniu wartości niecałkowitych używaj kropek zamiast przecinków')
    print()
    print('Menu Główne')
    print()
    print('Kalkulator Lokat Pekao -> 1')
    print('Standardowy Kalkulator Lokat -> 2')
    print('Oszczędzanie -> 3')
    menu = input()
    menu = int(menu)

    if menu == 1:
        KalkulatorLokatPekao()
        return Menu()
    elif menu == 2:
        KalkulatorLokat()
        return Menu()
    elif menu == 3:
        Oszczedzanie()
        return Menu()
    else: 
        koniec = input()

def KalkulatorLokatPekao():
    
    Lokata = ['1 - 10 dni  0,45%' , '2 - 30 dni  0,60%' , '3 - 60 dni  0,60%' , '4 - 90 dni  0,60%' , '5 - 120 dni  0,80%' , '6 - 180 dni  0,80%' , '7 - 360 dni  1,20%']
    LokataWartosc = [0,1,2,3,4,5,6]
    Czas = [0.027 , 0.083 , 0.166 , 0.25 , 0.333 , 0.5 , 1]
    Oprocentowanie = [0.0045 , 0.006 , 0.006 , 0.006 , 0.008 , 0.008 , 0.012]

    for i in Lokata[0:7]:
        print(i)
    print()
    print('Wybierz lokatę')
    wybor = input()
    print('Podaj wartość wkładu pieniężnego')
    K0 = input()

    wybor = int(wybor)
    K0 = float(K0)
    n = Czas[wybor - 1]
    r = Oprocentowanie[wybor - 1]
    m = 1

    Kbrutto = K0 * (1 + (r / m)) ** (n * m)
    Belka = 0.19
    Zysk = Kbrutto - K0
    ZyskN = Zysk * (1 - Belka)
    Podatek = Zysk - ZyskN
    Knetto = K0 + ZyskN
    round(Knetto, 2)
    
    print('Wartość na koniec lokaty ' + str("%.2f" % Knetto) + 'zł')
    print('Zysk z lokaty ' + str("%.2f" % ZyskN) + 'zł')
    print('Wysokość podatku Belki ' + str(Belka*100) + '%')
    print('Podatek ' + str("%.2f" % Podatek) + 'zł')
    print()
    
    koniec = input()
    return

def KalkulatorLokat():
    print('Podaj wartość wkładu pieniężnego')
    K0 = input()
    print('Na jaki okres [podaj w latach]')
    n = input()
    print('Liczba okresów kapitalizacji w ciągu roku')
    m = input()
    print('Jaka jest roczna stopa procentowa [podaj w postaci dziesiętnej]')
    r = input()

    K0 = float(K0)
    n = float(n)
    m = float(m)
    r = float(r)

    Kbrutto = K0 * (1 + (r / m)) ** (n * m)
    Belka = 0.19
    Zysk = Kbrutto - K0
    ZyskN = Zysk * (1 - Belka)
    Podatek = Zysk - ZyskN
    Knetto = K0 + ZyskN

    print('Wartość na koniec lokaty ' + str("%.2f" % Knetto) + 'zł')
    print('Zysk z lokaty ' + str("%.2f" % ZyskN) + 'zł')
    print('Wysokość podatku Belki ' + str(Belka*100) + '%')
    print('Podatek ' + str("%.2f" % Podatek) + 'zł')
    print()
    koniec = input()
    return

def Oszczedzanie():
    print('Podaj kwotę oszczędzaną co miesiąc')
    kwota_oszczednosci=input()
    print('Podaj ile miesięcy chcesz oszczędzać')
    ilosc_miesiecy=input()

    kwota_oszczednosci=float(kwota_oszczednosci)
    ilosc_miesiecy=int(ilosc_miesiecy)
    zaoszczedzone=kwota_oszczednosci*ilosc_miesiecy
    print('Po ' + str(ilosc_miesiecy) + ' miesiącach zaoszczędzisz ' + str(zaoszczedzone) + ' złotych')
    koniec=input()
    
Menu()



