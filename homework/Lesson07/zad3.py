# Zadanie 3 
# Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion imiona =
# ["anna", "piotr", "kasia"] w listę imion pisanych wielką literą

imiona = ["anna", "piotr", "kasia"]

duze_imiona = list(map(lambda imiona: imiona.title(), imiona)) 
# map musi mieć dwa arguemnty: co zrobić z danym arugemntem i na końcu "imiona" > to znaczy skąd brać dane argumenty
print(duze_imiona)
