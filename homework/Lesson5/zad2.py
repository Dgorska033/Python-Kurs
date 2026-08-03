# Zadanie 2 - Kalkulator zniżek 

ticket_price = 100 
procent = 50 

student = input("Czy jesteś studentem? tak/ nie: ") 
age = int(input("Ile masz lat?: ")) 

discount = ticket_price - (ticket_price * (procent / 100))

if age < 18 or student == "tak" : 
     print(f"Twoja cena to: {discount}") 
else: 
    print(f"Twoja cena to: {ticket_price}")     

# w poleceniu było użyj or i and, natomiast nie widzę tutaj zastosoawania do and, użyłam tylko or 
