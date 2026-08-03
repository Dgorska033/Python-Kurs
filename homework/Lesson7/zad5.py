#Zadanie 5 
# Iloczyn elementów: Użyj funkcji reduce() , aby obliczyć iloczyn (wynik mnożenia)
# wszystkich liczb w liście [1, 2, 3, 4, 5] 

from functools import reduce # reduce() znajduje się w module functools, więc trzeba go zaimportować

lista = [1, 2, 3, 4, 5]

iloczyn = reduce(lambda a,b : a*b , lista) # a jest dotychczasowym wynikiem, a b kolejną liczbą:
# reduce() bierze całą listę i stopniowo „redukuje” ją do jednej wartości.
# bierze dwie wartości i je mnoży, „redukuje” wiele elementów do jednego wyniku.

print(iloczyn) 

"""
1* 2 = 2    
2 * 3 = 6   
6 * 4 = 24    
24 * 5 = 120
"""