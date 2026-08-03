# Zadanie - Wstęp do parku rozrywki 


height = int(input("Podaj wzrost (cm): "))

if height >= 160:
     access = True 

else: 
     guardian = input ("Czy jest z Tobą opiekun?: ") 
    
    
     if guardian == "tak": 
        access = True 

     else: 
        access = False 

if access == True:
    print("Masz dostęp do parku rozrywki") 

elif access == False:
    print("Nie masz dostępu do parku rozrywki")





