# Zadanie 8 - Obliczanie wieku psa

dogAge = float(input("Podaj wiek psa w latach ludzkich: ")) 

if dogAge > 40 :
    print("Żaden pies nie żyje tak długo ") 

else: 
    if dogAge <= 1 : 
       dogAgeinHuman = dogAge * 15 
    elif 2 >= dogAge > 1 : 
       dogAgeinHuman = 15 + (dogAge - 1) * 9
    elif 3 <= dogAge <= 40 : 
       dogAgeinHuman = 24 + (dogAge - 2) * 5

    print(f"Wiek psa w latach ludzkich to: {dogAgeinHuman}")  
    
    




        
     
