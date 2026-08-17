# Zadanie 7 -  Tylko samogłoski 

# Poproś użytkownika o zdanie. Użyj pętli for oraz instrukcji continue ,
# aby wyświetlić tylko samogłoski z tego zdania. (Wskazówka: if litera not in
# "aeiouy": continue ).

zdanie = input("Podaj dowolne słowo/zdanie: ")
samogłoski = "aeiouy"

for litera in zdanie:
    if litera.lower() not in samogłoski:
        continue
    print(litera) 


       

