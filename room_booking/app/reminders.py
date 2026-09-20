from datetime import datetime, timedelta

from app import db
from app.models import Booking, Notification


def create_upcoming_booking_notifications(app):
    """
    Tworzy przypomnienia dla użytkowników,
    których rezerwacja zaczyna się za około godzinę.
    """

    with app.app_context():

        now = datetime.now()

        # Szukamy rezerwacji zaczynających się
        # za około 1 godzinę
        start_range = now + timedelta(minutes=55)
        end_range = now + timedelta(minutes=65)

        bookings = Booking.query.filter(
            Booking.start_time >= start_range,
            Booking.start_time <= end_range,
            Booking.status != 'cancelled'
        ).all()

        for booking in bookings:

            message = (
                f'Przypomnienie: rezerwacja '
                f'"{booking.title}" rozpoczyna się '
                f'o {booking.start_time.strftime("%H:%M")} '
                f'(ID rezerwacji: {booking.id})'
            )

            # Sprawdzamy, czy takie przypomnienie
            # nie zostało już utworzone
            existing_notification = (
                Notification.query
                .filter_by(
                    user_id=booking.user_id,
                    message=message
                )
                .first()
            )

            if existing_notification:
                continue

            notification = Notification(
                user_id=booking.user_id,
                message=message
            )

            db.session.add(notification)

        db.session.commit()