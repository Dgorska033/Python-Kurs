# Zadanie nr 9 - Identyfikator po zmianie

x = 10 
print(f"ID x to: {id(x)}") 

# ID x to: 140708245203672

x = x + 1 
print(f"ID x to: {id(x)}") 

# ID x to: 140708245203704 

# Indetyfiaktor się zmienił ponieważ drugie x, bo zmieniłam wartość x 