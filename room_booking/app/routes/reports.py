from collections import defaultdict
from datetime import datetime
from io import BytesIO

import matplotlib

# Matplotlib nie będzie próbował otwierać osobnego okna
matplotlib.use("Agg")

import matplotlib.pyplot as plt

from flask import Blueprint, jsonify, request, send_file

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from app.models import Booking


# ==================================================
# Font obsługujący polskie znaki
# ==================================================

pdfmetrics.registerFont(
    TTFont(
        "DejaVuSans",
        "C:/Windows/Fonts/DejaVuSans.ttf"
    )
)

pdfmetrics.registerFont(
    TTFont(
        "DejaVuSans-Bold",
        "C:/Windows/Fonts/DejaVuSans-Bold.ttf"
    )
)


# ==================================================
# Blueprint
# ==================================================

reports_bp = Blueprint(
    "reports",
    __name__
)


# ==================================================
# GET /api/reports/monthly?month=2026-09
# ==================================================

@reports_bp.route(
    "/api/reports/monthly",
    methods=["GET"]
)
def monthly_report():

    # ----------------------------------------------
    # 1. Pobranie miesiąca z adresu URL
    # ----------------------------------------------

    month_param = request.args.get("month")

    if not month_param:
        return jsonify({
            "error": (
                "Podaj miesiąc w formacie YYYY-MM, "
                "np. ?month=2026-09"
            )
        }), 400

    try:
        month_start = datetime.strptime(
            month_param,
            "%Y-%m"
        )

    except ValueError:
        return jsonify({
            "error": (
                "Nieprawidłowy format miesiąca. "
                "Użyj YYYY-MM."
            )
        }), 400


    # ----------------------------------------------
    # 2. Obliczenie początku kolejnego miesiąca
    # ----------------------------------------------

    if month_start.month == 12:

        next_month = datetime(
            month_start.year + 1,
            1,
            1
        )

    else:

        next_month = datetime(
            month_start.year,
            month_start.month + 1,
            1
        )


    # ----------------------------------------------
    # 3. Pobranie rezerwacji z wybranego miesiąca
    # ----------------------------------------------

    bookings = Booking.query.filter(
        Booking.start_time >= month_start,
        Booking.start_time < next_month,
        Booking.status != "cancelled"
    ).all()


    # ----------------------------------------------
    # 4. Podsumowanie
    # ----------------------------------------------

    total_bookings = len(bookings)

    total_hours = sum(
        booking.duration_hours
        for booking in bookings
    )

    total_revenue = sum(
        booking.total_cost
        for booking in bookings
    )


    # ----------------------------------------------
    # 5. TOP 10 SAL
    # ----------------------------------------------

    room_stats = defaultdict(
        lambda: {
            "bookings": 0,
            "hours": 0
        }
    )

    for booking in bookings:

        room_name = getattr(
            booking.room,
            "name",
            f"Sala {booking.room_id}"
        )

        room_stats[
            room_name
        ]["bookings"] += 1

        room_stats[
            room_name
        ]["hours"] += booking.duration_hours


    top_rooms = sorted(
        room_stats.items(),
        key=lambda item: item[1]["bookings"],
        reverse=True
    )[:10]


    # ----------------------------------------------
    # 6. TOP 10 UŻYTKOWNIKÓW
    # ----------------------------------------------

    user_stats = defaultdict(
        lambda: {
            "bookings": 0,
            "hours": 0
        }
    )

    for booking in bookings:

        user_name = getattr(
            booking.user,
            "name",
            f"Użytkownik {booking.user_id}"
        )

        user_stats[
            user_name
        ]["bookings"] += 1

        user_stats[
            user_name
        ]["hours"] += booking.duration_hours


    top_users = sorted(
        user_stats.items(),
        key=lambda item: item[1]["bookings"],
        reverse=True
    )[:10]


    # ----------------------------------------------
    # 7. WYKRES WYKORZYSTANIA SAL
    # ----------------------------------------------

    chart_buffer = BytesIO()

    if top_rooms:

        room_names = [
            room[0]
            for room in top_rooms
        ]

        room_hours = [
            room[1]["hours"]
            for room in top_rooms
        ]

        plt.figure(
            figsize=(8, 4.5)
        )

        plt.bar(
            room_names,
            room_hours
        )

        plt.title(
            "Wykorzystanie sal"
        )

        plt.xlabel(
            "Sala"
        )

        plt.ylabel(
            "Liczba godzin"
        )

        plt.xticks(
            rotation=35,
            ha="right"
        )

        plt.tight_layout()

        plt.savefig(
            chart_buffer,
            format="png",
            dpi=150
        )

        plt.close()

        chart_buffer.seek(0)


    # ----------------------------------------------
    # 8. GENEROWANIE PDF
    # ----------------------------------------------

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm
    )


    # ----------------------------------------------
    # Style tekstu
    # ----------------------------------------------

    styles = getSampleStyleSheet()

    styles[
        "Title"
    ].fontName = "DejaVuSans-Bold"

    styles[
        "Heading2"
    ].fontName = "DejaVuSans-Bold"

    styles[
        "Normal"
    ].fontName = "DejaVuSans"


    elements = []


    # ----------------------------------------------
    # Tytuł raportu
    # ----------------------------------------------

    elements.append(
        Paragraph(
            f"Raport miesięczny – {month_param}",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(
            1,
            0.5 * cm
        )
    )


    # ----------------------------------------------
    # Podsumowanie
    # ----------------------------------------------

    elements.append(
        Paragraph(
            "Podsumowanie",
            styles["Heading2"]
        )
    )


    summary_data = [
        [
            "Liczba rezerwacji",
            str(total_bookings)
        ],
        [
            "Łączny czas",
            f"{total_hours:.2f} h"
        ],
        [
            "Łączny przychód",
            f"{total_revenue:.2f} zł"
        ]
    ]


    summary_table = Table(
        summary_data,
        colWidths=[
            7 * cm,
            7 * cm
        ]
    )


    summary_table.setStyle(
        TableStyle([

            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "DejaVuSans"
            ),

            (
                "FONTNAME",
                (0, 0),
                (0, -1),
                "DejaVuSans-Bold"
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.lightgrey
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            )

        ])
    )


    elements.append(
        summary_table
    )

    elements.append(
        Spacer(
            1,
            0.6 * cm
        )
    )


    # ----------------------------------------------
    # TOP 10 SAL
    # ----------------------------------------------

    elements.append(
        Paragraph(
            "Top 10 sal",
            styles["Heading2"]
        )
    )


    rooms_data = [
        [
            "Sala",
            "Rezerwacje",
            "Godziny"
        ]
    ]


    for room_name, stats in top_rooms:

        rooms_data.append([
            room_name,
            str(
                stats["bookings"]
            ),
            f'{stats["hours"]:.2f}'
        ])


    rooms_table = Table(
        rooms_data,
        colWidths=[
            8 * cm,
            3 * cm,
            3 * cm
        ]
    )


    rooms_table.setStyle(
        TableStyle([

            # Cała tabela używa fontu
            # obsługującego polskie znaki
            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "DejaVuSans"
            ),

            # Pierwszy wiersz jest pogrubiony
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "DejaVuSans-Bold"
            ),

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                5
            )

        ])
    )


    elements.append(
        rooms_table
    )

    elements.append(
        Spacer(
            1,
            0.6 * cm
        )
    )


    # ----------------------------------------------
    # TOP 10 UŻYTKOWNIKÓW
    # ----------------------------------------------

    elements.append(
        Paragraph(
            "Top 10 użytkowników",
            styles["Heading2"]
        )
    )


    users_data = [
        [
            "Użytkownik",
            "Rezerwacje",
            "Godziny"
        ]
    ]


    for user_name, stats in top_users:

        users_data.append([
            user_name,
            str(
                stats["bookings"]
            ),
            f'{stats["hours"]:.2f}'
        ])


    users_table = Table(
        users_data,
        colWidths=[
            8 * cm,
            3 * cm,
            3 * cm
        ]
    )


    users_table.setStyle(
        TableStyle([

            # WAŻNE:
            # font ustawiony dla CAŁEJ tabeli
            (
                "FONTNAME",
                (0, 0),
                (-1, -1),
                "DejaVuSans"
            ),

            # Nagłówek tabeli
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "DejaVuSans-Bold"
            ),

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                5
            )

        ])
    )


    elements.append(
        users_table
    )

    elements.append(
        Spacer(
            1,
            0.6 * cm
        )
    )


    # ----------------------------------------------
    # WYKRES
    # ----------------------------------------------

    elements.append(
        Paragraph(
            "Wykres wykorzystania sal",
            styles["Heading2"]
        )
    )


    if top_rooms:

        chart = Image(
            chart_buffer,
            width=17 * cm,
            height=9.5 * cm
        )

        elements.append(
            chart
        )

    else:

        elements.append(
            Paragraph(
                "Brak danych do wygenerowania wykresu.",
                styles["Normal"]
            )
        )


    # ----------------------------------------------
    # Budowanie PDF
    # ----------------------------------------------

    doc.build(
        elements
    )

    pdf_buffer.seek(0)


    # ----------------------------------------------
    # Zwrócenie PDF
    # ----------------------------------------------

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=(
            f"raport_{month_param}.pdf"
        )
    )