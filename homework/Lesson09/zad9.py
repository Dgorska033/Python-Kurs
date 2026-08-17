# Zadanie 9 
# Prosty arkusz kalkulacyjny: Używając openpyxl , stwórz plik finanse.xlsx . W
# pierwszej kolumnie umieść nazwy wydatków (np. "Czynsz", "Jedzenie"), a w drugiej ich
# wartości. W komórce poniżej wartości oblicz i wstaw sumę wszystkich wydatków, używając
# formuły Excela (np. =SUM(B1:B2) )

from openpyxl import Workbook 

wb = Workbook()
ws = wb.active  # Aktywny arkusz
ws.title = "Finanse"

ws.append(["Czynsz", 1700]) # A1 + B1 jako dane
ws.append(["Jedzenie", 1800]) # A2 + B2 jako dane
ws.append(["Suma wydatków", "=SUM(B1:B2)"]) # C1 + C2 >> podliczenie

wb.save("Finanse.xlsx") 

