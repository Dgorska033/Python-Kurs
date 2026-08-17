# # Zadanie 8 -  Wyszukiwarka w liście: 

# Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr","Kasia"] .
# Poproś użytkownika o podanie imienia do wyszukania. 
# Użyj pętli for z instrukcją break oraz blokiem else , aby:
# Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę.
# Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia na
# liście."

pytanie = input("Podaj imię do wyszukania: ") 
imiona = ["Anna", "Jan", "Piotr", "Kasia"]

for imie in imiona: 
    if pytanie.lower() == imie.lower() : 
        print("Znaleziono!") 
        break 
else:
    print("Nie znaleziono imienia na liście") 
      

    
   

    
