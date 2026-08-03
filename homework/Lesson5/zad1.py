# Zadanie 1 - Analiza wieku 

age = int(input("Provide your age in years: ")) 

if 0 <= age <= 1 : 
    print("Infant") 
elif 2 <= age <= 12 : 
    print("Child") 
elif 13 <= age <= 17 : 
    print("Teenager") 
elif 18 <= age <= 64 : 
    print("Adult") 
elif age >= 65 : 
    print("Senior citizen") 
else: 
    print("Wrong value") 

