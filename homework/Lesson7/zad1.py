# Zadanie 7

# Filtrowanie słów: Mając listę słów slowa = ["jabłko", "banan", "kiwi", "gruszka",
# "truskawka"] , użyj list comprehension, aby stworzyć nową listę zawierającą tylko te
# słowa, które mają więcej niż 5 liter

slowa = ["jabłko", "banan", "kiwi", "gruszka","truskawka"]

slowa_v2 = [x for x in slowa if len(x) > 5] # weź x → dla każdego x w slowa → jeśli długość x jest większa niż 5
print(slowa_v2)
