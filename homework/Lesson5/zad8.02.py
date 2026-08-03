#Zadanie 8 - 

owoce = ["Jabłko", "Banan", "Gruszka" , "Czereśnia"] 

pytanie = input("Podaj owoc: ") 

for owoc in owoce: 
    if pytanie.lower() == owoc.lower() :
       print("Znaleziono owoc!")
       break 
else: 
    print("Nie ma tego na liście") 
