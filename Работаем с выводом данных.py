nazvanie = str(input())
ves_tovara = float(input())
cena_tovara = float(input())
dengi_pokupately = int(input())
print('        Чек')
print(nazvanie + ' - ' + str(ves_tovara) + ' кг' + ' - ' + str(cena_tovara) + " руб/кг")
print('Итого: ' + str(ves_tovara * cena_tovara) + ' руб')
print('Внесено: ' + str(dengi_pokupately) + ' руб')
print('Сдача: ' + str(dengi_pokupately - (ves_tovara * cena_tovara)) + ' руб')
