"""
Dashboard ze statystykami.
"""

from flask import Blueprint, render_template, jsonify
from datetime import datetime, timedelta
from sqlalchemy import func, desc
from sqlalchemy.orm import joinedload

from app.models import (
    db,
    Room,
    Booking,
    User,
    get_booking_statistics
)


dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
def dashboard():
    """Strona główna dashboardu."""

    # ==================================================
    # STATYSTYKI OGÓLNE
    # ==================================================

    stats = {
        'total_rooms': Room.query.filter_by(
            is_active=True
        ).count(),

        'total_users': User.query.count(),

        'total_bookings': Booking.query.filter_by(
            status='confirmed'
        ).count(),

        'bookings_today': Booking.query.filter(
            func.date(Booking.start_time)
            == datetime.today().date(),

            Booking.status == 'confirmed'
        ).count()
    }

    # ==================================================
    # NAJBLIŻSZE REZERWACJE - 24H
    # ==================================================

    now = datetime.now()

    upcoming = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).filter(
        Booking.start_time >= now,
        Booking.start_time <= now + timedelta(hours=24),
        Booking.status == 'confirmed'
    ).order_by(
        Booking.start_time
    ).limit(
        10
    ).all()

    # ==================================================
    # TOP UŻYTKOWNICY
    # ==================================================

    top_users = db.session.query(
        User.name,
        func.count(
            Booking.id
        ).label(
            'booking_count'
        )
    ).join(
        Booking
    ).filter(
        Booking.status != 'cancelled'
    ).group_by(
        User.id
    ).order_by(
        desc('booking_count')
    ).limit(
        5
    ).all()

    # ==================================================
    # WYKORZYSTANIE SAL
    # ==================================================

    month_ago = now - timedelta(days=30)

    room_utilization = []

    active_rooms = Room.query.filter_by(
        is_active=True
    ).all()

    for room in active_rooms:

        total_hours = db.session.query(
            func.sum(
                func.extract(
                    'epoch',
                    Booking.end_time
                    - Booking.start_time
                ) / 3600
            )
        ).filter(
            Booking.room_id == room.id,
            Booking.start_time >= month_ago,
            Booking.status != 'cancelled'
        ).scalar() or 0

        # 8h dziennie * 22 dni robocze
        max_hours = 176

        utilization = (
            total_hours / max_hours
        ) * 100

        room_utilization.append({
            'room': room.name,
            'hours': round(
                float(total_hours),
                1
            ),
            'utilization': round(
                float(utilization),
                1
            )
        })

    room_utilization.sort(
        key=lambda x: x['utilization'],
        reverse=True
    )

    # ==================================================
    # ZADANIE 3
    # 1. REZERWACJE WG DEPARTAMENTU
    # ==================================================

    department_stats = db.session.query(
        User.department,
        func.count(
            Booking.id
        ).label(
            'booking_count'
        )
    ).join(
        Booking,
        Booking.user_id == User.id
    ).filter(
        Booking.status != 'cancelled'
    ).group_by(
        User.department
    ).order_by(
        desc('booking_count')
    ).all()

    department_data = [
        {
            'department': department or 'Brak departamentu',
            'count': booking_count
        }
        for department, booking_count
        in department_stats
    ]

    # ==================================================
    # ZADANIE 3
    # 2. HEATMAPA - DZIEŃ TYGODNIA × GODZINA
    # ==================================================

    heatmap_stats = db.session.query(

        func.extract(
            'dow',
            Booking.start_time
        ).label(
            'weekday'
        ),

        func.extract(
            'hour',
            Booking.start_time
        ).label(
            'hour'
        ),

        func.count(
            Booking.id
        ).label(
            'booking_count'
        )

    ).filter(
        Booking.status != 'cancelled'
    ).group_by(
        'weekday',
        'hour'
    ).order_by(
        'weekday',
        'hour'
    ).all()

    # PostgreSQL:
    # 0 = niedziela
    # 1 = poniedziałek
    # ...
    # 6 = sobota

    weekdays = [
        'Nd',
        'Pn',
        'Wt',
        'Śr',
        'Cz',
        'Pt',
        'Sb'
    ]

    heatmap_data = [
        {
            'weekday_number': int(row.weekday),
            'weekday': weekdays[
                int(row.weekday)
            ],
            'hour': int(row.hour),
            'count': row.booking_count
        }
        for row in heatmap_stats
    ]

    # ==================================================
    # ZADANIE 3
    # 3. TREND - OSTATNIE 30 DNI
    # ==================================================

    thirty_days_ago = (
        datetime.now().date()
        - timedelta(days=29)
    )

    trend_stats = db.session.query(

        func.date(
            Booking.start_time
        ).label(
            'booking_date'
        ),

        func.count(
            Booking.id
        ).label(
            'booking_count'
        )

    ).filter(
        func.date(
            Booking.start_time
        ) >= thirty_days_ago,

        Booking.status != 'cancelled'
    ).group_by(
        func.date(
            Booking.start_time
        )
    ).order_by(
        func.date(
            Booking.start_time
        )
    ).all()

    # Tworzymy słownik:
    # data -> liczba rezerwacji
    trend_lookup = {
        row.booking_date: row.booking_count
        for row in trend_stats
    }

    # Tworzymy wszystkie 30 dni,
    # również te, w których było 0 rezerwacji.
    trend_data = []

    for day_offset in range(30):

        current_date = (
            thirty_days_ago
            + timedelta(
                days=day_offset
            )
        )

        trend_data.append({
            'date': current_date.strftime(
                '%Y-%m-%d'
            ),
            'count': trend_lookup.get(
                current_date,
                0
            )
        })

    # ==================================================
    # RENDEROWANIE DASHBOARDU
    # ==================================================

    return render_template(
        'dashboard.html',

        stats=stats,
        upcoming=upcoming,
        top_users=top_users,
        room_utilization=room_utilization,

        # Zadanie 3
        department_data=department_data,
        heatmap_data=heatmap_data,
        trend_data=trend_data
    )


@dashboard_bp.route('/api/dashboard/stats')
def api_stats():
    """API endpoint dla statystyk."""

    stats = get_booking_statistics()

    return jsonify(stats)
