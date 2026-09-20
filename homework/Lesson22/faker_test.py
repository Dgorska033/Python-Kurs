from faker import Faker


# Tworzymy generator danych w języku polskim
fake = Faker('pl_PL')  # pl_PL ustawia polską lokalizację danych


# 10 losowych polskich imion i nazwisk
print("=== LOSOWE IMIONA I NAZWISKA ===")

for i in range(10):   # wykonaj poniższy kod 10 razy.
    print(fake.name()) # fake.name() - losowe nazwisko


# 10 losowych zdań
print("\n=== LOSOWE ZDANIA ===")

for i in range(10):
    print(fake.sentence()) # fake.sentence() losowe zdanie