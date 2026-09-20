Zadanie 5 – Dodanie daty utworzenia (SQLAlchemy)
W pliku sqlalchemy_app/models.py, do klasy Zadanie dodaj nową kolumnę:
data_utworzenia = Column(DateTime, default=datetime.datetime.utcnow). Nie zapomnij o
imporcie from sqlalchemy import DateTime i import datetime. Następnie wygeneruj i
zastosuj nową migrację Alembic


Dodanie daty utworzenia (SQLAlchemy)

Do modelu `Zadanie` została dodana nowa kolumna `data_utworzenia`.

Kolumna przechowuje datę i czas utworzenia zadania.

W `models.py` wykorzystano:

- `DateTime` – typ kolumny przechowującej datę i czas,
- `datetime.datetime` – typ używany po stronie Pythona,
- `default=datetime.datetime.utcnow` – automatycznie ustawia czas podczas tworzenia nowego zadania.

Model zawiera:

`data_utworzenia: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)`

Następnie skonfigurowano Alembic tak, aby korzystał z modeli SQLAlchemy:

`target_metadata = Base.metadata`

Dzięki temu Alembic może porównywać modele z aktualną strukturą bazy danych.

Wygenerowano migrację poleceniem:

`.\.venv\Scripts\python.exe -m alembic revision --autogenerate -m "dodanie daty utworzenia"`

Następnie migracja została zastosowana:

`.\.venv\Scripts\python.exe -m alembic upgrade head`

Po wykonaniu migracji tabela `zadania` zawiera kolumny:

- `id`
- `opis`
- `zrobione`
- `data_utworzenia`

Alembic służy do kontrolowanego zmieniania struktury istniejącej bazy danych bez konieczności ręcznego usuwania i ponownego tworzenia tabel.