from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Zadanie, Tag


DATABASE_URL = "sqlite:///todo_orm.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)


def init_db():
    """Tworzy tabelę zadania, jeśli jeszcze nie istnieje."""
    Base.metadata.create_all(bind=engine)

def dodaj_zadanie(opis: str):
    """Dodaje nowe zadanie do bazy danych."""

    with SessionLocal() as db:
        zadanie = Zadanie(
            opis=opis,
            zrobione=False
        )

        db.add(zadanie)
        db.commit()


def pobierz_zadania():
    """Pobiera wszystkie zadania z bazy danych."""

    with SessionLocal() as db:
        return db.query(Zadanie).all()


def oznacz_jako_zrobione(id_zadania: int):
    """Oznacza zadanie o podanym ID jako zrobione."""

    with SessionLocal() as db:
        # Najpierw znajdujemy obiekt Zadanie o podanym ID.
        zadanie = db.query(Zadanie).filter(
            Zadanie.id == id_zadania
        ).first()

        if zadanie:
            # Zmieniamy wartość atrybutu obiektu.
            zadanie.zrobione = True

            # Zapisujemy zmianę w bazie.
            db.commit()

            return True

    return False

# Zadanie 2 – Usuwanie zadań (SQLAlchemy)
def usun_zadanie(id_zadania: int):
    """Usuwa zadanie o podanym ID."""

    with SessionLocal() as db:
        zadanie = db.query(Zadanie).filter(
            Zadanie.id == id_zadania
        ).first()

        if zadanie:
            db.delete(zadanie)
            db.commit()
            return True

    return False

def wyszukaj_zadania(fraza: str):
    """Wyszukuje zadania, których opis zawiera podaną frazę."""

    # Otwieramy sesję SQLAlchemy.
    with SessionLocal() as db:

        # Zadanie.opis wskazuje na kolumnę "opis" z modelu Zadanie.
        #
        # .contains(fraza) oznacza:
        # opis ma zawierać podaną frazę.
        #
        # Jest to odpowiednik Raw SQL:
        # WHERE opis LIKE '%fraza%'
        #
        # .all() pobiera wszystkie pasujące obiekty Zadanie.
        zadania = (
            db.query(Zadanie)
            .filter(Zadanie.opis.contains(fraza))
            .all()
        )

        return zadania

def dodaj_tag_do_zadania(id_zadania: int, nazwa_tagu: str):
    """Dodaje tag do zadania."""

    with SessionLocal() as db:
        # Szukamy zadania po ID.
        zadanie = (
            db.query(Zadanie)
            .filter(Zadanie.id == id_zadania)
            .first()
        )

        if not zadanie:
            return False

        # Sprawdzamy, czy tag o takiej nazwie już istnieje.
        tag = (
            db.query(Tag)
            .filter(Tag.nazwa == nazwa_tagu)
            .first()
        )

        # Jeśli tag nie istnieje, tworzymy go.
        if not tag:
            tag = Tag(nazwa=nazwa_tagu)
            db.add(tag)

        # Nie dodajemy tego samego taga drugi raz do tego samego zadania.
        if tag not in zadanie.tagi:
            zadanie.tagi.append(tag)

        db.commit()

        return True

def edytuj_zadanie(id_zadania: int, nowy_opis: str):
    """Zmienia opis zadania o podanym ID."""

    with SessionLocal() as db:
        # Szukamy zadania o podanym ID.
        zadanie = (
            db.query(Zadanie)
            .filter(Zadanie.id == id_zadania)
            .first()
        )

        # Jeśli zadanie istnieje, zmieniamy jego opis.
        if zadanie:
            zadanie.opis = nowy_opis

            # Zapisujemy zmianę w bazie.
            db.commit()

            return True

        # Jeśli nie znaleziono zadania o takim ID.
        return False