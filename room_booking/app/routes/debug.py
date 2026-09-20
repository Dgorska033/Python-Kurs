"""
Endpoint diagnostyczny pokazujący problem N+1
oraz porównanie z optymalizacją joinedload().
"""

from time import perf_counter

from flask import Blueprint, jsonify
from sqlalchemy import event
from sqlalchemy.orm import joinedload

from app import db
from app.models import Booking


debug_bp = Blueprint("debug", __name__)


@debug_bp.route("/debug/n-plus-1")
def debug_n_plus_1():
    """
    Porównuje liczbę zapytań i czas wykonania:

    1. Bez optymalizacji - klasyczny problem N+1.
    2. Z joinedload() - pobranie relacji w jednym zapytaniu.
    """

    # --------------------------------------------------
    # LICZNIK ZAPYTAŃ SQL
    # --------------------------------------------------

    query_counter = {
        "count": 0
    }

    def count_query(
        conn,
        cursor,
        statement,
        parameters,
        context,
        executemany
    ):
        """
        Funkcja wykonywana przed każdym zapytaniem SQL.

        Zwiększa licznik zapytań o 1.
        """
        query_counter["count"] += 1

    # Pobieramy silnik SQLAlchemy
    engine = db.engine

    # Podpinamy listener do silnika
    event.listen(
        engine,
        "before_cursor_execute",
        count_query
    )

    try:

        # ==================================================
        # TEST 1 - BEZ OPTYMALIZACJI
        # ==================================================

        query_counter["count"] = 0

        start = perf_counter()

        # Pobieramy tylko rezerwacje.
        # Relacje room i user NIE są pobierane od razu.
        bookings = Booking.query.all()

        without_optimization_data = []

        for booking in bookings:

            # Dostęp do:
            # booking.room
            # booking.user
            #
            # może powodować dodatkowe zapytania SQL.
            #
            # To właśnie jest problem N+1.

            without_optimization_data.append({
                "title": booking.title,
                "room": booking.room.name,
                "user": booking.user.name
            })

        end = perf_counter()

        without_optimization_time = end - start
        without_optimization_queries = query_counter["count"]

        # --------------------------------------------------
        # Czyścimy sesję przed drugim testem.
        #
        # Jest to ważne, ponieważ SQLAlchemy przechowuje
        # wcześniej pobrane obiekty w swojej sesji.
        #
        # Bez wyczyszczenia sesji drugi test mógłby korzystać
        # z danych znajdujących się już w pamięci.
        # --------------------------------------------------

        db.session.remove()

        # ==================================================
        # TEST 2 - Z OPTYMALIZACJĄ joinedload()
        # ==================================================

        query_counter["count"] = 0

        start = perf_counter()

        bookings_optimized = Booking.query.options(

            # Pobieramy salę razem z rezerwacją
            joinedload(
                Booking.room
            ),

            # Pobieramy użytkownika razem z rezerwacją
            joinedload(
                Booking.user
            )

        ).all()

        with_optimization_data = []

        for booking in bookings_optimized:

            with_optimization_data.append({
                "title": booking.title,
                "room": booking.room.name,
                "user": booking.user.name
            })

        end = perf_counter()

        with_optimization_time = end - start
        with_optimization_queries = query_counter["count"]

        # ==================================================
        # PORÓWNANIE
        # ==================================================

        queries_saved = (
            without_optimization_queries
            - with_optimization_queries
        )

        # Wynik zwracamy jako JSON
        return jsonify({

            "without_optimization": {
                "query_count": without_optimization_queries,
                "execution_time_ms": round(
                    without_optimization_time * 1000,
                    3
                ),
                "bookings": without_optimization_data
            },

            "with_joinedload": {
                "query_count": with_optimization_queries,
                "execution_time_ms": round(
                    with_optimization_time * 1000,
                    3
                ),
                "bookings": with_optimization_data
            },

            "comparison": {
                "queries_saved": queries_saved,
                "booking_count": len(
                    without_optimization_data
                )
            }

        })

    finally:

        # Listener musi zostać usunięty.
        #
        # Gdyby tego nie zrobić, każde kolejne wejście
        # na endpoint dodawałoby następny licznik.
        event.remove(
            engine,
            "before_cursor_execute",
            count_query
        )