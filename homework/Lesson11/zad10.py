# Zadanie 10 – Eksploracja MRO
# Stwórz następującą, złożoną hierarchię dziedziczenia:
# class A
# class B(A)
# class C(A)
# class D(B)
# class E(C)
# class F(D, E) Narysuj schemat tej hierarchii w mermaid. Następnie, nie uruchamiając
# kodu, spróbuj przewidzieć, jakie będzie MRO dla klasy F. Na koniec sprawdź swoją
# odpowiedź, używając print(F.mro()).


import subprocess

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C):
    pass

class F(D, E):
    pass

mermaid_code = """
classDiagram
    A <|-- B
    A <|-- C
    B <|-- D
    C <|-- E
    D <|-- F
    E <|-- F

"""

with open("diagram.mmd", "w", encoding="utf-8") as f:
    f.write(mermaid_code)

print(F.mro())

# odp według MRO klasę F Python znajdzie kolejno w F > D > B > E > C > A \

# Python : [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>,
#  <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]