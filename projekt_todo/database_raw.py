# database_raw.py
import sqlite3


class TaskManagerRaw:
    """Zarządza zadaniami zapisanymi w bazie SQLite."""

    def __init__(self, database_name="todo_raw.db"):
        # Zapamiętujemy nazwę bazy jako atrybut obiektu.
        self.database_name = database_name

        # Przy utworzeniu obiektu TaskManagerRaw
        # baza zostanie automatycznie zainicjalizowana.
        self.init_db()


    def init_db(self):
        """Tworzy tabelę zadania, jeśli jeszcze nie istnieje."""

        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS zadania (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    opis TEXT NOT NULL,
                    zrobione BOOLEAN NOT NULL
                        CHECK (zrobione IN (0, 1)),
                    priorytet INTEGER DEFAULT 1
                )
            """)

            conn.commit()


    def dodaj_zadanie(self, opis: str, priorytet: int):
        """Dodaje nowe zadanie do bazy danych."""

        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO zadania (opis, zrobione, priorytet)
                VALUES (?, ?, ?)
                """,
                (opis, False, priorytet)
            )

            conn.commit()


    def pobierz_zadania(self):
        """Pobiera wszystkie zadania z bazy danych."""

        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT id, opis, zrobione, priorytet FROM zadania"
            )

            return cursor.fetchall()


    def oznacz_jako_zrobione(self, id_zadania: int):
        """Oznacza zadanie o podanym ID jako zrobione."""

        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE zadania SET zrobione = ? WHERE id = ?",
                (True, id_zadania)
            )

            conn.commit()


    def usun_zadanie(self, id_zadania: int):
        """Usuwa zadanie o podanym ID."""

        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM zadania WHERE id = ?",
                (id_zadania,)
            )

            conn.commit()


    def wyszukaj_zadania(self, fraza: str):
        """Wyszukuje zadania zawierające podaną frazę."""

        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()

            # % oznacza dowolny tekst przed i po frazie.
            wzorzec = f"%{fraza}%"

            cursor.execute(
                "SELECT * FROM zadania WHERE opis LIKE ?",
                (wzorzec,)
            )

            return cursor.fetchall()