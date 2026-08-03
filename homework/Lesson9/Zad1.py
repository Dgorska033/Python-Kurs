# Zadanie 1
# Dziennik użytkownika: Napisz program, który w pętli prosi użytkownika o wpisanie jednej
# linii tekstu. Każda wpisana linia powinna być dopisywana (tryb 'a' ) do pliku
# dziennik.txt . Program kończy działanie, gdy użytkownik wpisze "koniec"

def dziennik(): 

    while True: 
        notka = input("Jak ci minął dzień lub wpisz (koniec): ")
        if notka.lower() == "koniec": 
            print("Dziękuję za skorzystanie")
            break 

        with open("dziennik.txt", "a") as plik: 
            plik.write(notka + "\n")


dziennik()
    

           
               

            
