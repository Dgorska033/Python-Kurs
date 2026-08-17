# Wyrażenie logiczne 

prawo_jazdy = input("Czy masz prawo jazdy? (tak/nie): ") 

age = int(input("Podaj swój wiek: ")) 

czy_może_proawdzić = age >= 18 and prawo_jazdy.lower() == "tak"

print(czy_może_proawdzić)

