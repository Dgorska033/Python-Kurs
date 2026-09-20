import uuid
from datetime import datetime
from dateutil.rrule import rrule, WEEKLY
from dateutil.relativedelta import relativedelta

from flask import Blueprint, jsonify, request

from app import db
from app.models import Booking


recurring_bookings_bp = Blueprint(
    'recurring_bookings',
    __name__
)


# ==================================================
# FUNKCJA SPRAWDZAJĄCA KONFLIKT
# ==================================================

def has_booking_conflict(
    room_id,
    start_time,
    end_time
):
    """
    Sprawdza, czy sala jest już zajęta
    w podanym przedziale czasu.
    """

    conflict = Booking.query.filter(
        Booking.room_id == room_id,

        Booking.status != 'cancelled',

        Booking.start_time < end_time,

        Booking.end_time > start_time
    ).first()

    return conflict


# ==================================================
# POST /api/bookings/series
# ==================================================

@recurring_bookings_bp.route(
    '/api/bookings/series',
    methods=['POST']
)
def create_booking_series():
    """
    Tworzy serię cyklicznych rezerwacji.
    """

    data = request.get_json()

    if not data:
        return jsonify({
            'error': 'Brak danych JSON'
        }), 400

    # ----------------------------------------------
    # Wymagane pola
    # ----------------------------------------------

    required_fields = [
        'room_id',
        'user_id',
        'title',
        'start_time',
        'end_time',
        'recurrence_rule',
        'months'
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                'error': f'Brak pola: {field}'
            }), 400

    # ----------------------------------------------
    # Daty
    # ----------------------------------------------

    try:
        start_time = datetime.fromisoformat(
            data['start_time']
        )

        end_time = datetime.fromisoformat(
            data['end_time']
        )

    except ValueError:
        return jsonify({
            'error': 'Nieprawidłowy format daty'
        }), 400

    if end_time <= start_time:
        return jsonify({
            'error': (
                'end_time musi być późniejsze '
                'niż start_time'
            )
        }), 400

    # ----------------------------------------------
    # Reguła cykliczności
    # ----------------------------------------------

    recurrence_rule = (
        data['recurrence_rule']
        .upper()
    )

    if recurrence_rule == 'WEEKLY':
        interval = 1

    elif recurrence_rule == 'BIWEEKLY':
        interval = 2

    else:
        return jsonify({
            'error': (
                'Dozwolone recurrence_rule: '
                'WEEKLY lub BIWEEKLY'
            )
        }), 400

    # ----------------------------------------------
    # Liczba miesięcy
    # ----------------------------------------------

    try:
        months = int(data['months'])

    except (TypeError, ValueError):
        return jsonify({
            'error': 'months musi być liczbą'
        }), 400

    if months <= 0:
        return jsonify({
            'error': 'months musi być większe od 0'
        }), 400

    # ----------------------------------------------
    # Koniec serii
    # ----------------------------------------------

    series_end = (
        start_time
        + relativedelta(months=months)
    )

    # ----------------------------------------------
    # Generowanie terminów przez rrule
    # ----------------------------------------------

    occurrence_starts = list(
        rrule(
            WEEKLY,
            interval=interval,
            dtstart=start_time,
            until=series_end
        )
    )

    duration = end_time - start_time

    # ----------------------------------------------
    # Najpierw sprawdzamy WSZYSTKIE konflikty
    # ----------------------------------------------

    conflicts = []

    for occurrence_start in occurrence_starts:

        occurrence_end = (
            occurrence_start
            + duration
        )

        conflict = has_booking_conflict(
            data['room_id'],
            occurrence_start,
            occurrence_end
        )

        if conflict:
            conflicts.append({
                'start_time':
                    occurrence_start.isoformat(),

                'end_time':
                    occurrence_end.isoformat(),

                'conflicting_booking_id':
                    conflict.id
            })

    # ----------------------------------------------
    # Jeśli chociaż jeden konflikt →
    # nie tworzymy żadnej rezerwacji
    # ----------------------------------------------

    if conflicts:
        return jsonify({
            'error': (
                'Nie można utworzyć serii. '
                'Występują konflikty terminów.'
            ),
            'conflicts': conflicts
        }), 409

    # ----------------------------------------------
    # UUID całej serii
    # ----------------------------------------------

    series_id = str(
        uuid.uuid4()
    )

    created_bookings = []

    # ----------------------------------------------
    # Tworzenie wszystkich rezerwacji
    # ----------------------------------------------

    for occurrence_start in occurrence_starts:

        occurrence_end = (
            occurrence_start
            + duration
        )

        booking = Booking(
            room_id=data['room_id'],
            user_id=data['user_id'],
            title=data['title'],
            description=data.get(
                'description'
            ),
            start_time=occurrence_start,
            end_time=occurrence_end,
            status='confirmed',
            attendees_count=data.get(
                'attendees_count',
                1
            ),
            recurrence_rule=recurrence_rule,
            series_id=series_id
        )

        db.session.add(
            booking
        )

        created_bookings.append(
            booking
        )

    db.session.commit()

    # ----------------------------------------------
    # Odpowiedź
    # ----------------------------------------------

    return jsonify({
        'message': (
            'Seria rezerwacji została utworzona'
        ),

        'series_id': series_id,

        'recurrence_rule':
            recurrence_rule,

        'count':
            len(created_bookings),

        'bookings': [
            {
                'id': booking.id,
                'start_time':
                    booking.start_time.isoformat(),
                'end_time':
                    booking.end_time.isoformat()
            }
            for booking in created_bookings
        ]
    }), 201


# ==================================================
# POST /api/bookings/<id>/cancel
# Anulowanie pojedynczej rezerwacji
# ==================================================

@recurring_bookings_bp.route(
    '/api/bookings/<int:booking_id>/cancel',
    methods=['POST']
)
def cancel_single_booking(
    booking_id
):

    booking = db.session.get(
        Booking,
        booking_id
    )

    if booking is None:
        return jsonify({
            'error': (
                'Nie znaleziono rezerwacji'
            )
        }), 404

    booking.status = 'cancelled'

    db.session.commit()

    return jsonify({
        'message': (
            'Rezerwacja została anulowana'
        ),
        'booking_id': booking.id,
        'series_id': booking.series_id
    })


# ==================================================
# POST /api/bookings/series/<series_id>/cancel
# Anulowanie całej serii
# ==================================================

@recurring_bookings_bp.route(
    '/api/bookings/series/<string:series_id>/cancel',
    methods=['POST']
)
def cancel_booking_series(
    series_id
):

    bookings = Booking.query.filter_by(
        series_id=series_id
    ).all()

    if not bookings:
        return jsonify({
            'error': (
                'Nie znaleziono serii rezerwacji'
            )
        }), 404

    cancelled_count = 0

    for booking in bookings:

        if booking.status != 'cancelled':

            booking.status = 'cancelled'

            cancelled_count += 1

    db.session.commit()

    return jsonify({
        'message': (
            'Seria rezerwacji została anulowana'
        ),

        'series_id':
            series_id,

        'cancelled_count':
            cancelled_count
    })