# Zadanie 2 - Indetyfikator obiektu

a = 256 
b = 256 
c = 256 

print(f"ID a: {id(a)}")
print(f"ID b: {id(b)}")
print(f"ID c: {id(c)}")

#Python wyświetla to samo ID dla wszystkich zmiennych 

d = 2574356000
e = 2574356000
f = 2574356000

print(f"ID d: {id(d)}") 
print(f"ID e: {id(e)}")
print(f"ID f: {id(f)}") 

# Python znów wyświetlił to samo ID dla wszystkich zmiennych z 257, spróbuję wiekszą liczbę.
# Za każdym razem dla zmiennych z wiekszą liczbą, Python tworzy nowe ID.
# Python nie zapisuje w pamięci większych zmiennych aby zaoszczędzić pamięć. 