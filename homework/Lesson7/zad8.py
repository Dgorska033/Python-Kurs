# Zadanie 8
# Łączenie map i filter: Mając listę liczb [-5, 2, 8, -1, 0, 10] , użyj filter do
# wybrania tylko liczb dodatnich, a następnie map do obliczenia ich kwadratów. Zrób to w
# jednej linijce

liczby = [-5, 2, 8, -1, 0, 10]

liczby_v2 = list(map(lambda liczba: liczba ** 2, filter(lambda liczba: liczba > 0, liczby)))
print( liczby_v2)

# filter() zostawia tylko liczby większe od 0
# map() podnosi każdą z nich do kwadratu
# list() zamienia wynik na zwykłą listę

