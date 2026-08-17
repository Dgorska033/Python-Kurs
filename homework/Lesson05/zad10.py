# Zadanie 10 -  Mini-projekt: Prosty kalkulator walut

# Zdefiniuj kursy w słowniku, np. kursy = {"USD": 4.0, "EUR": 4.3} .
# W pętli while True zapytaj użytkownika o kwotę w PLN i walutę (USD/EUR).
# Użyj if-elif-else , aby sprawdzić wybraną walutę i obliczyć wynik.
# Sformatuj wynik do dwóch miejsc po przecinku, używając f-stringa.
# Zapytaj użytkownika, czy chce kontynuować. Jeśli odpowie "nie", użyj break

kursy = {"USD": 3.8, 
         "EUR": 4.3
        } 

while True: 
    kwota = (float(input("Podaj kwotę w PLN: ")))
    waluta = input("Podaj walutę na jaką chcesz przeliczyć (USD/EUR): ") 

    if "EUR" == waluta  : 
       EUR = kwota / 4.3
       print(f"Twoja kwota w Euro to {EUR:.2f}")        
    elif "USD" == waluta : 
        USD = kwota / 3.8
        print(f"Twoja kwota w dolarch to {USD:.2f}")    
    else:
        print("Brak waluty na liście") 
    
    kontynuacja = input("Czy chcesz kontynuować: (tak/nie): ") 
    if kontynuacja == "nie": 
        print("Dziękuję za skorzystanie z kantoru") 
        break  
